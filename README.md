# 🧠 Text-to-SQL — Natural Language Database Query System

> Ask your database anything in plain English. Get SQL and results instantly.

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square&logo=fastapi)
![React](https://img.shields.io/badge/React-TypeScript-61DAFB?style=flat-square&logo=react)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=flat-square&logo=mysql)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-purple?style=flat-square)
![ChromaDB](https://img.shields.io/badge/ChromaDB-RAG-red?style=flat-square)

---

## 📌 What is This Project?

**Text-to-SQL** is a full-stack AI-powered system that lets non-technical users type a question in plain English and automatically:

1. 🗺️ **Finds** which database tables are relevant using RAG + ChromaDB
2. ✍️ **Generates** the correct SQL query using GPT-4o
3. ⚡ **Runs** that SQL against a real MySQL database
4. 📊 **Returns** the results in a clean table in the browser
5. 🛡️ **Blocks** dangerous queries (DROP, DELETE, UPDATE) automatically

### Example
```
User types:  "What are the top 5 product categories by revenue?"

System returns:
SELECT p.category_name, SUM(o.order_total_usd) AS revenue
FROM fact_orders o
JOIN dim_products p ON o.product_id = p.product_id
WHERE o.order_status = 'delivered'
GROUP BY p.category_name
ORDER BY revenue DESC
LIMIT 5;
```

---

## 🏗️ Architecture

```
User Question
     │
     ▼
React Frontend (localhost:5173)
     │  POST /query
     ▼
FastAPI Backend (localhost:8000)
     │
     ▼
RAG Pipeline
├── Embed question → OpenAI Embeddings
├── Query ChromaDB → Top 3 relevant tables
├── Build prompt → Schema + Few-shot examples
├── Call GPT-4o → Generate SQL
├── hitl_guard → Safety check
└── Execute SQL → MySQL Database
     │
     ▼
Results → JSON → Frontend Table
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| LLM | GPT-4o | Generates SQL from natural language |
| Embeddings | text-embedding-3-small | Embeds schema for RAG |
| AI Framework | LangChain (LCEL) | Orchestrates the AI pipeline |
| Vector DB | ChromaDB | Stores and retrieves schema embeddings |
| Backend | FastAPI | REST API server |
| ORM | SQLAlchemy + PyMySQL | Database connection |
| Database | MySQL 8.0 | Stores the Olist e-commerce data |
| Frontend | React + TypeScript | User interface |
| Build Tool | Vite | Frontend dev server |

---

## 📁 Project Structure

```
text-to-sql/
│
├── agent/                        # Core AI pipeline
│   ├── sql_chain.py              # Main pipeline: question → SQL → results
│   ├── retriever.py              # RAG: embed question, query ChromaDB
│   ├── semantic_layer.py         # Business descriptions for tables/columns
│   ├── build_index.py            # One-time: embed schema into ChromaDB
│   ├── hitl_guard.py             # Safety: block dangerous SQL
│   └── few_shot_examples.yaml    # Q→SQL examples for in-context learning
│
├── api/                          # FastAPI web server
│   ├── main.py                   # App factory + CORS
│   └── routes/
│       ├── query.py              # POST /query
│       ├── schema.py             # GET /schema
│       └── health.py             # GET /health
│
├── model/                        # SQLAlchemy ORM
│   ├── database.py               # Engine + session factory
│   └── schema.py                 # Table definitions
│
├── frontend/                     # React + TypeScript UI
│   └── src/
│       └── App.tsx               # Main UI component
│
├── data/
│   ├── raw/                      # Olist CSV files (not in git)
│   └── seed.py                   # Load CSVs → MySQL
│
├── requirements.txt
└── .env.example
```

---

## 🗄️ Database Schema (Star Schema)

```
                    ┌─────────────┐
                    │  dim_users  │
                    │  user_id PK │
                    └──────┬──────┘
                           │
┌──────────────┐    ┌──────▼────────────┐    ┌───────────────┐
│ dim_products │    │   fact_orders     │    │  dim_sellers  │
│ product_id PK│◄───│   order_id PK     │───►│  seller_id PK │
│ category_name│    │   user_id FK      │    │  seller_city  │
└──────────────┘    │   product_id FK   │    └───────────────┘
                    │   order_total_usd │
                    │   order_status    │    ┌───────────────┐
                    │   created_at      │───►│  dim_reviews  │
                    └───────────────────┘    │  review_score │
                                             └───────────────┘
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.11+
- Node.js 20+
- MySQL 8.0
- OpenAI API Key (with credits)

### 1. Clone the repository
```bash
git clone https://github.com/Craazcoder/text-to-sql.git
cd text-to-sql
```

### 2. Set up Python environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

```env
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-4o
DATABASE_URL=mysql+pymysql://olist_user:yourpassword@localhost:3306/olist_db
CHROMA_PERSIST_DIR=./chroma_store
EMBEDDING_MODEL=text-embedding-3-small
```

### 4. Set up MySQL
```sql
CREATE DATABASE olist_db CHARACTER SET utf8mb4;
CREATE USER 'olist_user'@'localhost' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON olist_db.* TO 'olist_user'@'localhost';
FLUSH PRIVILEGES;
```

### 5. Download the dataset
Download the [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) from Kaggle and place all CSV files in `data/raw/`

### 6. Seed the database (run once)
```bash
python data/seed.py
```

### 7. Build ChromaDB index (run once)
```bash
python -m agent.build_index
```

### 8. Install frontend dependencies
```bash
cd frontend
npm install
cd ..
```

---

## 🚀 Running the Project

Open **two terminals**:

**Terminal 1 — Backend:**
```bash
uvicorn api.main:app --reload --port 8000
```

**Terminal 2 — Frontend:**
```bash
cd frontend
npm run dev
```

Open your browser at **http://localhost:5173** 🎉

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/query` | Submit a natural language question |
| GET | `/schema` | Get all table descriptions |
| GET | `/health` | Check if backend is running |

### Example Request
```json
POST /query
{
  "question": "What are the top 5 product categories by revenue?"
}
```

### Example Response
```json
{
  "sql": "SELECT p.category_name, SUM(o.order_total_usd) AS revenue...",
  "results": [
    {"category_name": "bed_bath_table", "revenue": 1245678.90},
    ...
  ],
  "blocked": false
}
```

---

## 🛡️ Safety Features

The `hitl_guard.py` module blocks any SQL that contains dangerous keywords:

```python
BLOCKED_KEYWORDS = ["drop", "delete", "truncate", "update", "insert", "alter"]
```

Blocked queries return `{"blocked": true}` and are never executed.

---

## 💡 Why RAG Instead of Full Schema?

| Approach | Problem |
|---------|---------|
| Send full schema | Token limit exceeded, LLM gets confused |
| No schema | LLM hallucinates column/table names |
| **RAG (our approach)** | Only relevant tables sent, accurate SQL |

We embed table descriptions into ChromaDB. When a question arrives, we find the 3 most semantically similar tables and only send those to GPT-4o.

---

## 📊 Sample Questions to Try

- `What are the top 5 product categories by revenue?`
- `Average review score by seller state?`
- `How many orders were delivered last month?`
- `Which city has the most customers?`
- `Top 10 sellers by total sales?`

---

## 🎯 Use Cases & Job Profiles

This project demonstrates skills relevant for:

- **AI/ML Engineer** — LLM integration, RAG, embeddings
- **Backend Developer** — FastAPI, SQLAlchemy, REST APIs
- **Data Engineer** — Star schema, ETL, MySQL
- **Full-Stack Developer** — React, TypeScript, FastAPI

---

## 📝 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | required | OpenAI API key |
| `OPENAI_MODEL` | gpt-4o | Chat model for SQL generation |
| `DATABASE_URL` | mysql+pymysql://... | MySQL connection string |
| `CHROMA_PERSIST_DIR` | ./chroma_store | ChromaDB storage path |
| `EMBEDDING_MODEL` | text-embedding-3-small | Embedding model |

---

## 👤 Author

**Vivek** — [@Craazcoder](https://github.com/Craazcoder)

---

## ⭐ If you found this useful, give it a star!
