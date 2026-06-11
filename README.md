# 🧠 Text-to-SQL — Natural Language Database Query System

> Ask your database anything in plain English. Get SQL queries and results instantly using AI.

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-green?style=flat-square&logo=fastapi)
![React](https://img.shields.io/badge/React-TypeScript-61DAFB?style=flat-square&logo=react)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=flat-square&logo=mysql)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-purple?style=flat-square)
![ChromaDB](https://img.shields.io/badge/ChromaDB-RAG-red?style=flat-square)

---

## 🚀 Overview

Text-to-SQL is a full-stack AI-powered application that converts natural language questions into SQL queries and executes them on a MySQL database.

Users can ask questions in plain English and receive accurate database results without writing SQL.

### Key Features

- Natural Language → SQL conversion
- RAG-based schema retrieval using ChromaDB
- GPT-4o powered query generation
- Automatic SQL execution
- FastAPI REST backend
- React + TypeScript frontend
- Query safety protection
- MySQL database integration

---

## 📌 Example

### User Question

```text
What are the top 5 product categories by revenue?
```

### Generated SQL

```sql
SELECT p.category_name,
       SUM(o.order_total_usd) AS revenue
FROM fact_orders o
JOIN dim_products p
ON o.product_id = p.product_id
WHERE o.order_status = 'delivered'
GROUP BY p.category_name
ORDER BY revenue DESC
LIMIT 5;
```

---

## 🏗️ System Architecture

```text
User Question
      │
      ▼
React Frontend
      │
      ▼
FastAPI Backend
      │
      ▼
RAG Pipeline
├── OpenAI Embeddings
├── ChromaDB Retrieval
├── Prompt Construction
├── GPT-4o SQL Generation
├── Safety Validation
└── SQL Execution
      │
      ▼
MySQL Database
      │
      ▼
Results Returned to User
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---------|-----------|
| Frontend | React + TypeScript |
| Backend | FastAPI |
| Database | MySQL 8.0 |
| ORM | SQLAlchemy |
| AI Model | GPT-4o |
| Framework | LangChain (LCEL) |
| Vector Database | ChromaDB |
| Embeddings | text-embedding-3-small |
| Build Tool | Vite |

---

## 📁 Project Structure

```text
text-to-sql/
│
├── agent/
│   ├── sql_chain.py
│   ├── retriever.py
│   ├── semantic_layer.py
│   ├── build_index.py
│   ├── hitl_guard.py
│   └── few_shot_examples.yaml
│
├── api/
│   ├── main.py
│   └── routes/
│       ├── query.py
│       ├── schema.py
│       └── health.py
│
├── model/
│   ├── database.py
│   └── schema.py
│
├── frontend/
│   └── src/
│       └── App.tsx
│
├── data/
│   ├── raw/
│   └── seed.py
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/vivekKumar3674/text-to-sql.git
cd text-to-sql
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-4o
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/olist_db
CHROMA_PERSIST_DIR=./chroma_store
EMBEDDING_MODEL=text-embedding-3-small
```

---

## 🗄️ Database Setup

```sql
CREATE DATABASE olist_db;
```

Import the Olist E-Commerce Dataset into MySQL.

Dataset:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

## ▶️ Run Backend

```bash
uvicorn api.main:app --reload --port 8000
```

Backend:

```text
http://localhost:8000
```

---

## ▶️ Run Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | /query | Generate and execute SQL |
| GET | /schema | View schema metadata |
| GET | /health | Health check |

---

## 🛡️ Safety Features

Dangerous SQL commands are automatically blocked:

```python
BLOCKED_KEYWORDS = [
    "drop",
    "delete",
    "truncate",
    "update",
    "insert",
    "alter"
]
```

This prevents accidental modification of production data.

---

## 📊 Sample Questions

```text
What are the top 5 product categories by revenue?
```

```text
Which city has the most customers?
```

```text
Average review score by seller state?
```

```text
Top 10 sellers by total sales?
```

```text
How many orders were delivered last month?
```

---

## 🎯 Skills Demonstrated

- Generative AI
- Retrieval Augmented Generation (RAG)
- Prompt Engineering
- Vector Databases
- FastAPI Development
- REST APIs
- SQL & Database Design
- React Frontend Development
- Full Stack Development

---

## 👨‍💻 Author

### Vivek Kumar

B.Tech CSE | Full Stack Developer | AI/ML Enthusiast

GitHub: https://github.com/vivekKumar3674

---

## ⭐ Star this repository if you found it useful!
