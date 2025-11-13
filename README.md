# 🧩 FastAPI Starter — Products CRUD App

A simple **FastAPI** starter project demonstrating basic CRUD operations using **PostgreSQL** as the database and **SQLAlchemy** as the ORM.

---

## 🚀 Features

- ⚡ Built with **FastAPI** — modern, fast (high-performance) web framework for Python  
- 🗄️ Integrated with **PostgreSQL** for persistent data storage  
- 🔗 **SQLAlchemy ORM** for database interaction  
- 📚 **Swagger UI** (auto-generated) for easy API testing and documentation  
- 🧱 Basic CRUD endpoints for managing products

---

## 📦 Tech Stack

| Component | Description |
|------------|-------------|
| **Backend** | FastAPI |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Language** | Python 3.10+ |
| **Docs** | Built-in Swagger UI (`/docs`) |

---

## 🧩 Product Model

```python
class Product(BaseModel):
    id: int
    name: str
    desc: str
    price: float
    qty: int

```
This represents a simple products table to demonstrate CRUD operations.



## ⚙️ Setup Instructions
Follow these steps to get the application running locally.

### 1. Clone the Repository

```bash
git clone https://github.com/muhammedrafi-kp/fastapi-starter
cd fastapi-starter
```

### 2. Create and Activate Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv .venv
```

### 3. Activate the environment:

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 5. Configure Database Connection

You must update the PostgreSQL connection string in your `database.py` file (or equivalent config).

**Example URL format:**

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/mydb"
```

### 6. Run the Application

Start the FastAPI development server using Uvicorn with `--reload` for hot-reloading:

```bash
uvicorn main:app --reload
```

The server will be available at:

👉 **Local URL:** `http://127.0.0.1:8000`

---

## 🧭 API Documentation

Once the server is running, the documentation is automatically generated and available at:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

---

## 🧹 .gitignore

The following files and directories are ignored to ensure unnecessary or sensitive files aren’t tracked by Git:

```text
__pycache__/
.venv/
.env
*.pyc
```

