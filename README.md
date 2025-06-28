# 🧠 KB Inspector – A Semantic Benchmark & Stress Tester for MindsDB

![kb-inspector-demo](https://raw.githubusercontent.com/Akshama2003/KB-Inspector-A-Semantic-Benchmark-Stress-Tester-for-MindsDB/main/assets/kb-inspector-demo.gif)

**A Streamlit-based tool to evaluate, benchmark, and stress-test MindsDB’s Knowledge Bases (KBs)** for performance and query relevancy.

---

## 🚀 Features

✅ Upload large JSON datasets  
✅ Automatically create a MindsDB Knowledge Base  
✅ Insert data using `INSERT INTO` with `metadata_columns`  
✅ Run semantic search queries using `SELECT ... WHERE content LIKE "<query>"`  
✅ Filter with metadata columns (e.g., `WHERE category = 'POLITICS'`)  
✅ Measure ingestion & query latency  
✅ Evaluate performance using `EVALUATE KNOWLEDGE_BASE`  
✅ Streamlit UI for ease of use

---

## 📸 Demo Animation

> Below is a GIF showing dataset upload, KB creation, semantic query, and performance evaluation:

![Demo](https://raw.githubusercontent.com/Akshama2003/KB-Inspector-A-Semantic-Benchmark-Stress-Tester-for-MindsDB/main/assets/kb-inspector-demo.gif)

---

## 🧑‍💻 Getting Started

```bash
git clone https://github.com/Akshama2003/KB-Inspector-A-Semantic-Benchmark-Stress-Tester-for-MindsDB.git
cd KB-Inspector-A-Semantic-Benchmark-Stress-Tester-for-MindsDB
pip install -r requirements.txt
streamlit run MindsDB_KB_Inspector.py
