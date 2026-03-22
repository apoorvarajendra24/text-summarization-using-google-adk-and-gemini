# 🧠 Text Summarization AI Agent (ADK + Gemini + Cloud Run)

## 📌 Overview

This project implements a **Text Summarization AI Agent** using the **Agent Development Kit (ADK)** and **Gemini model**.
The agent is deployed on **Google Cloud Run** and can be accessed via an **HTTP endpoint**.

The agent takes a block of text as input and returns a concise 3-line summary.

---

## 🚀 Features

* ✅ Built using **Google ADK (Agent Development Kit)**
* ✅ Uses **Gemini (Google Generative AI)** for inference
* ✅ Implements a **multi-agent workflow**
* ✅ Deployed on **Cloud Run**
* ✅ Accessible via **HTTP API**
* ✅ Clean and modular agent architecture

---

## 🧠 Architecture

The system follows a **multi-agent workflow**:

```
Root Agent
   ↓
Text Summarization Workflow (SequentialAgent)
   ↓
Text Summarizer Agent → Response Formatter Agent
```

### 🔹 Components

* **Root Agent**

  * Entry point of the system
  * Accepts user input
  * Stores input in state
  * Transfers control to workflow

* **Text Summarizer Agent**

  * Uses Gemini model
  * Generates concise summary

* **Response Formatter Agent**

  * Formats output for readability

---

## 📁 Project Structure

```
project-root/
│── agents/
│   └── text-summarization/
│       ├── agent.py
│       ├── __init__.py
│── requirements.txt
│── README.md
```

---

## 🎯 Key Concepts Used

* Agent Development Kit (ADK)
* Sequential Agent Workflow
* Prompt-based summarization
* Cloud Run deployment
* Containerization using Docker

---

## 📌 Conclusion

This project demonstrates how to build, structure, and deploy a **production-ready AI agent** using modern tools like ADK, Gemini, and Cloud Run.
It highlights modular agent design and real-world deployment practices.

---

## 📄 License

This project is for educational purposes.
