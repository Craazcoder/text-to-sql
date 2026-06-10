from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from agent.retriever import retrieve_relevant_schema
from agent.hitl_guard import is_safe_sql
from model.database import SessionLocal
from sqlalchemy import text
import os
import yaml

llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL"))

with open("agent/few_shot_examples.yaml") as f:
    examples = yaml.safe_load(f)["examples"]
few_shot_text = "\n".join([f"Q: {e['question']}\nSQL: {e['sql']}" for e in examples])

def run_pipeline(question: str):
    schema_context = retrieve_relevant_schema(question)
    prompt = ChatPromptTemplate.from_template("""
You are a SQL expert. Use MySQL syntax.
Relevant schema:
{schema}

Few-shot examples:
{examples}

Write only the SQL query for: {question}
""")
    chain = prompt | llm
    sql = chain.invoke({"schema": schema_context, "examples": few_shot_text, "question": question})
    sql_text = sql.content.strip().strip("```sql").strip("```").strip()

    if not is_safe_sql(sql_text):
        return {"sql": sql_text, "results": [], "blocked": True}

    with SessionLocal() as session:
        result = session.execute(text(sql_text))
        rows = [dict(r._mapping) for r in result]

    return {"sql": sql_text, "results": rows, "blocked": False}