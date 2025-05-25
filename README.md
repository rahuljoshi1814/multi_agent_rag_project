#  Multi-Agent RAG System for Natural Language Querying of a Relational Database

###  Objective
This project implements a **Multi-Agent Retrieval-Augmented Generation (RAG)** system that allows users to ask **natural language questions**, translates them to **PostgreSQL SQL queries**, and returns human-readable answers via a web interface and API.

---

##  Features
-  Natural language query interface
-  Modular multi-agent architecture:
  - **Schema Agent**: Finds relevant tables
  - **SQL Generator Agent**: Creates SQL query
  - **Retriever Agent**: Executes query on PostgreSQL
  - **Synthesizer Agent**: Converts results to human-like answer
-  `/ask` API endpoint (FastAPI)
-  Web frontend (HTML+JS)
-  Error handling for schema, SQL, empty results

---

##  System Architecture
User → Web/API → Schema Agent → SQL Agent → Retriever → Synthesizer → Final Answer


---

## 🗃️ Database Schema

PostgreSQL schema includes 5 interrelated tables:
- `customers(id, name, email, created_at)`
- `products(id, name, category, price)`
- `employees(id, name, role, department, hire_date)`
- `projects(id, name, description, start_date, end_date)`
- `sales(id, customer_id, product_id, employee_id, amount, sale_date)`

---

## 📦 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/multi-agent-rag.git
cd multi-agent-rag


