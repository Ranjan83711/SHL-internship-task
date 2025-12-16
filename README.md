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
14. Limitations
15. Future Improvements

---

🔗 **Live Demo:** https://shl-internship-task-qo8cearcp2tq2dnxquqvsl.streamlit.app/


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

| Layer                | Technology                     |
| -------------------- | ------------------------------ |
| Language             | Python                         |
| Data Handling        | Pandas                         |
| NLP                  | Sentence-Transformers (MiniLM) |
| Vector DB            | FAISS                          |
| UI                   | Streamlit                      |
| Scraping (Attempted) | Requests + BeautifulSoup       |
| Chunking             | LangChain Text Splitters       |

---

## 5️⃣ Project Architecture

```
SHL/
│
├── data/
│   ├── raw/               # (empty / unused due to scraping restrictions)
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
├── utils/
│   ├── config.py
│   └── parser.py
│
├── faiss_index/
│   └── shl.index
│
├── app.py
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

To proceed safely and reliably, we created a **curated dataset** inspired by **publicly described SHL assessments**.

### Why this approach is valid:

* Demonstrates full pipeline functionality
* Avoids legal and scraping issues
* Keeps system **scalable**
* Aligns with interview expectations

### Dataset format:

`data/processed/shl_assessments.csv`

Example fields:

```csv
assessment_name,assessment_type,skills_measured,job_roles,description,duration
Numerical Reasoning Test,Cognitive,"Numerical ability,Data interpretation","Data Analyst","Analyzes numerical data",25
```

📌 Adding more assessments only requires **updating the CSV**, no code changes.

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

### Step 2: Run Streamlit App

```bash
streamlit run app.py
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
* **FAISS** for scalability
* **Curated dataset** over unstable scraping
* **Minimal UI** for clarity
* **Modular architecture** for easy extension

---

## 1️⃣4️⃣ Limitations

* Dataset is limited in size
* No real-time SHL API integration
* Recommendations are semantic, not supervised predictions

---

## 1️⃣5️⃣ Future Improvements

* Add similarity score explanation
* Filter by assessment type
* Add user feedback loop
* Expand dataset
* Add export/download feature
* Integrate LLM for explanation layer

---


---



---

