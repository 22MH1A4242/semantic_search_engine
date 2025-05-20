# 🔎 Distributed Semantic Search Engine with Semantic Understanding

A powerful semantic search system that goes beyond traditional keyword-based search by using **machine learning and embeddings** to understand **contextual meaning** behind queries and documents. This engine can semantically retrieve news articles that are most relevant, even when exact keywords do not match.

---

## 🧠 Project Overview

Traditional search engines rely heavily on keyword matching. While effective in many scenarios, they often miss documents that use synonyms or related terminology. This project solves that problem by implementing a **semantic search engine** — powered by **sentence embeddings** and **FAISS** — to retrieve documents based on their **contextual similarity**.

This engine is built using:
- **Transformer-based sentence encoders** (from Sentence Transformers)
- **FAISS** for scalable and fast approximate nearest neighbor (ANN) search
- A preprocessed version of the **News Category Dataset**, enabling exploration across thousands of headlines and descriptions.

---

## 🧩 Key Components

### 🔤 1. Sentence Embeddings
- Uses the `all-MiniLM-L6-v2` model from `sentence-transformers`, a lightweight transformer that converts sentences into high-dimensional vectors.
- These vectors capture **semantic meaning**, allowing similar sentences to be close in vector space.

### 📦 2. FAISS Index
- FAISS (Facebook AI Similarity Search) allows for **efficient vector similarity search** over thousands of document embeddings.
- It uses a flat index (can be changed to IVF or HNSW for large-scale deployments).

### 📚 3. JSON Dataset (News Articles)
- Preprocessed from Kaggle’s **News Category Dataset**.
- Fields used: `category`, `headline`, `short_description`.
- Combined and cleaned to create high-quality document representations.

---

## 📌 Features

- ✅ Semantic understanding of queries
- ✅ High-speed vector
