---

# 🧠 SHL Assessment Recommendation Engine

An **AI-powered semantic recommendation system** that suggests suitable SHL-style assessments based on a given **job description or required skills**.
The system uses **embedding-based similarity search** instead of rule-based filtering to provide intelligent, scalable recommendations.

---

## 📌 Table of Contents

1. Project Overview
2. Problem Statement
3. Solution Approach
4. Tech Stack
5. Project Architecture
6. Dataset Strategy
7. Why Web Scraping Failed (Important)
8. Custom Dataset Creation
9. Installation & Setup
10. How to Run the Project
11. File & Folder Structure
12. Use Cases
13. Design Decisions
14. Evaluation Strategy
15. API Endpoint (Backend)
16. Limitations
17. Future Improvements

---

🔗 **Live Demo:** [https://shl-internship-task-qo8cearcp2tq2dnxquqvsl.streamlit.app/](https://shl-internship-task-qo8cearcp2tq2dnxquqvsl.streamlit.app/)

---

## 1️⃣ Project Overview

Hiring teams often struggle to decide **which assessments best match a role**.
This project solves that problem by building a **semantic recommendation engine** that:

* Understands job descriptions
* Matches them with assessment metadata
* Returns the most relevant assessments using vector similarity

The focus is on **system design and recommendation logic**, not UI-heavy features.

---

## 2️⃣ Problem Statement

> Given a job description or required skills, recommend the most suitable SHL assessments.

Constraints:

* No official public SHL API
* Assessment pages are dynamically rendered
* Data availability is limited

---

## 3️⃣ Solution Approach

Instead of traditional rule-based matching, this system uses:

* **Sentence embeddings** to represent text semantically
* **FAISS** for fast similarity search
* **Streamlit** for interactive UI

### High-level flow:

```
Job Description → Embedding → FAISS Search → Ranked Assessments
```

---

## 4️⃣ Tech Stack

| Layer         | Technology                     |
| ------------- | ------------------------------ |
| Language      | Python                         |
| Data Handling | Pandas                         |
| NLP           | Sentence-Transformers (MiniLM) |
| Vector DB     | FAISS                          |
| UI            | Streamlit                      |
| Backend API   | FastAPI + Uvicorn              |
| Chunking      | LangChain Text Splitters       |
| Evaluation    | Precision@K, Hit Rate@K        |

---

## 5️⃣ Project Architecture

```
SHL/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── shl_assessments.csv
│
├── preprocessing/
│   ├── text_builder.py
│   └── chunker.py
│
├── embeddings/
│   ├── embedder.py
│   ├── vector_store.py
│   └── build_index.py
│
├── retrieval/
│   ├── retriever.py
│   └── ranker.py
│
├── evaluation/
│   ├── evaluation.py
│   └── evaluation_queries.json
│
├── utils/
│   ├── config.py
│   └── parser.py
│
├── faiss_index/
│   └── shl.index
│
├── app.py              # Streamlit UI
├── api.py              # FastAPI backend
└── README.md
```

---

## 6️⃣ Dataset Strategy

### Why data is required

The recommendation engine needs **assessment metadata** such as:

* Assessment name
* Skills measured
* Job roles
* Description
* Duration

This data is converted into **semantic embeddings**.

---

## 7️⃣ Why Web Scraping Failed (IMPORTANT)

We initially attempted to scrape assessment data using **BeautifulSoup**.

### Issues encountered:

* ❌ No stable public SHL API
* ❌ Assessment pages are **JavaScript-rendered**
* ❌ URLs frequently return **404**
* ❌ Dynamic content not accessible via Requests
* ❌ Legal & ethical concerns for scraping proprietary data

### Engineering decision:

> Stop fighting unstable scraping and focus on the **core recommendation system**.

📌 This is a **real-world engineering choice**, not a shortcut.

---

## 8️⃣ Custom Dataset Creation (Why & How)

To proceed safely and reliably, we created a **curated dataset** inspired by the **SHL Product Catalogue**.

### Why this approach is valid:

* Demonstrates full pipeline functionality
* Avoids legal and scraping issues
* Keeps system **scalable**
* Aligns with real-world engineering constraints

### Dataset format:

`data/processed/shl_assessments.csv`

```csv
assessment_name,assessment_type,skills_measured,job_roles,description,duration
Numerical Reasoning Test,Cognitive,"Numerical ability,Data interpretation","Data Analyst","Analyzes numerical data",25 minutes
```

---

## 9️⃣ Installation & Setup

### 🔹 Create virtual environment

```bash
conda create -n shl python=3.13
conda activate shl
```

### 🔹 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔟 How to Run the Project

### Step 1: Build FAISS Index

```bash
python -m embeddings.build_index
```

### Step 2: Run Streamlit App (Frontend)

```bash
streamlit run app.py
```

### Step 3: Run FastAPI Backend

```bash
uvicorn api:app --reload
```

Swagger UI available at:

```
http://127.0.0.1:8000/docs
```

---

## 1️⃣1️⃣ File Responsibilities

| File              | Purpose                                |
| ----------------- | -------------------------------------- |
| `text_builder.py` | Converts CSV rows to rich text         |
| `chunker.py`      | Splits text into overlapping chunks    |
| `embedder.py`     | Loads embedding model                  |
| `build_index.py`  | Builds FAISS index                     |
| `retriever.py`    | Performs semantic search               |
| `ranker.py`       | Removes duplicates                     |
| `parser.py`       | Converts raw text to structured output |
| `evaluation.py`   | Precision@K & Hit Rate@K evaluation    |
| `api.py`          | REST API backend                       |
| `app.py`          | UI + pipeline integration              |

---

## 1️⃣2️⃣ Use Cases

* HR teams selecting assessments
* Recruiters screening roles
* Talent analytics platforms
* Internal HR tooling
* AI-driven hiring assistants

---

## 1️⃣3️⃣ Key Design Decisions

* **Embedding-based retrieval** instead of keyword matching
* **FAISS** for scalable similarity search
* **Curated dataset** over unstable scraping
* **Decoupled UI and API layers**
* **Minimal UI** to highlight core logic

---

## 1️⃣4️⃣ Evaluation Strategy

Since no labeled dataset was provided, **classification accuracy was not suitable**.

### Metrics used:

* **Precision@K** – relevance of top-K recommendations
* **Hit Rate@K** – presence of at least one relevant assessment

A small curated evaluation set was used, and results are displayed directly in the UI for transparency.

---

## 1️⃣5️⃣ API Endpoint (Backend)

A REST API was implemented using **FastAPI** to expose the recommendation logic.

### Endpoint:

```
POST /recommend
```

### Input:

```json
{
  "query": "Data analyst with strong numerical skills",
  "top_k": 5
}
```

### Output:

```json
{
  "query": "...",
  "recommendations": [
    {
      "name": "...",
      "type": "...",
      "skills": "...",
      "roles": "...",
      "duration": "...",
      "description": "..."
    }
  ]
}
```

The API enables programmatic access and external system integration while keeping the UI independent.

---

## 1️⃣6️⃣ Limitations

* Dataset size is limited
* No real-time SHL API integration
* Recommendations are unsupervised and semantic

---

## 1️⃣7️⃣ Future Improvements

* Expand dataset coverage
* Add similarity score explanations
* Introduce feedback-based re-ranking
* Integrate LLM-based explanation layer
* Fully connect UI with backend API

---

## ✅ Final Note

This project focuses on **core system design, semantic relevance, proper evaluation, and clean deployment practices**, aligned with real-world constraints.

---


