# 🚀 Complaint & Defect Management System

A full-stack backend-driven system designed to manage customer complaints and associated defects with intelligent prioritization, workflow control, and optimized database handling.

---

## 📌 Overview

This project simulates an enterprise-grade complaint tracking platform used in production environments. It enables teams to create, track, update, and analyze complaints along with related defects.

The system is built with a focus on scalability, maintainability, and real-world backend practices such as layered architecture, query optimization, and business rule enforcement.

---

## 🛠️ Tech Stack

### Backend

* **FastAPI** – High-performance REST API framework
* **SQLAlchemy** – ORM for database interaction
* **SQLite** (can be upgraded to MySQL/PostgreSQL)

### Frontend

* **React.js** – Interactive UI
* **Fetch API** – API communication

### Deployment

* Backend → Render
* Frontend → Netlify

---

## ✨ Features

### 🔹 Core Functionality

* Create, Read, Update, Delete (CRUD) operations for complaints
* Manage defects linked to complaints (One-to-Many relationship)

### 🔹 Advanced Backend Features

* 🔍 **Search API** (keyword-based filtering)
* 🎯 **Status Filtering**
* 📄 **Pagination support** for scalability
* ⚡ **Optimized queries** using eager loading (`joinedload`)

### 🔹 Business Logic

* 🔄 **Status Workflow Validation**

  * OPEN → IN_PROGRESS → RESOLVED → CLOSED
* 🧠 **Priority Classification Engine**

  * HIGH → crash/failure
  * MEDIUM → slow/delay
  * LOW → minor issues

### 🔹 System Design

* Layered architecture:

  * `routes/` → API layer
  * `services/` → business logic
  * `models/` → database schema
  * `db/` → database setup

---

## 📁 Project Structure

```
complaint_system/
│
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── db/
│
├── frontend/
│   └── React UI
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔧 Backend Setup

```bash
git clone https://github.com/YOUR_USERNAME/complaint-system.git
cd complaint-system

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

👉 API Docs:
http://127.0.0.1:8000/docs

---

### 💻 Frontend Setup (React)

```bash
cd complaint-ui
npm install
npm start
```

👉 Runs on:
http://localhost:3000

---

## 🌐 Deployment

### Backend (Render)

* Build: `pip install -r requirements.txt`
* Start:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

### Frontend (Netlify)

```bash
npm run build
```

Upload `build/` folder to Netlify.

---

## 🧠 Key Learnings

* REST API design using FastAPI
* ORM-based database modeling
* Query optimization (avoiding N+1 problem)
* Implementing business rules in backend systems
* Full-stack integration (React + FastAPI)
* Deployment and CORS handling

---

## 🚀 Future Improvements

* 🔐 JWT Authentication & Role-based access
* 🐳 Docker containerization
* 🔁 CI/CD pipeline (GitHub Actions)
* 🗄️ Migration to MySQL/PostgreSQL
* 📊 Analytics dashboard

---

## 📌 Resume Highlight

> Built a scalable Complaint & Defect Management System using FastAPI and SQLAlchemy, implementing optimized database queries, workflow validation, and rule-based prioritization with a React frontend and deployed full-stack architecture.

---

## 🤝 Contribution

Feel free to fork and improve this project. Suggestions and improvements are welcome!

---

## 📧 Contact

**Sundar Eshwar**
GitHub: https://github.com/SUNDARESHWARL-07
LinkedIn: https://linkedin.com/in/sundareshwar-lakshminarayanan

---
