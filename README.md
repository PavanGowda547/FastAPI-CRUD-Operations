# 📘 User Management System

*A FastAPI CRUD Web Application using SQLAlchemy, SQLite, and Jinja2*

---

# 📌 Project Overview

This project is a **User Management System** built using **FastAPI** as the backend framework, **SQLAlchemy ORM** for database interaction, **SQLite** as the database, and **Jinja2 templates** for server-side HTML rendering.

The application allows users to:

* Create new users
* View all users
* Update user details
* Delete users

It demonstrates a clean **Layered Architecture**, follows **MVC principles**, and uses **Dependency Injection** for database session management.

---
# 📸 Screenshots

 🏠 User List Page
![Users List](./images/User%20List.PNG)

➕ Create User Page
![Create users](./images/Create%20users.PNG)

✏️ Update User Page
![Update users](./images/Update%20users%20list.PNG)

---

# 🛠 Tech Stack

| Technology     | Purpose                         |
| -------------- | ------------------------------- |
| **FastAPI**    | Web framework                   |
| **SQLAlchemy** | ORM for database operations     |
| **SQLite**     | Lightweight relational database |
| **Jinja2**     | Server-side templating engine   |
| **Uvicorn**    | ASGI server                     |

---

# 🏗 Architecture Overview

The project follows a **Layered Architecture with MVC principles**.

```
Client (Browser)
        ↓
Presentation Layer (Jinja2 Templates)
        ↓
Application Layer (FastAPI Routers)
        ↓
Data Access Layer (SQLAlchemy ORM)
        ↓
Database (SQLite)
```

---

## 🔹 Architectural Patterns Used

* ✅ Layered Architecture
* ✅ MVC (Model–View–Controller)
* ✅ Dependency Injection
* ✅ ORM-based Data Mapping

---

# 📂 Project Structure

```
project/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│   └── users.py
├── templates/
│   ├── index.html
│   ├── create.html
│   └── update.html
└── test.db
```

---

# 📁 File-by-File Explanation


## 🔹 1. `main.py` – Application Entry Point

### Responsibilities:

* Create FastAPI app instance
* Initialize database tables
* Include user router
* Redirect root URL

```python
app = FastAPI()
app.include_router(users.router, prefix="/users", tags=["users"])
```

### Root Route:

```python
@app.get("/")
def root():
    return RedirectResponse(url="/users")
```

### Database Initialization:

```python
Base.metadata.create_all(bind=engine)
```

This automatically creates database tables based on defined models.

---

## 🔹 2. `database.py` – Database Configuration

### Responsibilities:

* Create database engine
* Configure session factory
* Provide dependency injection for DB session

### Engine Setup:

```python
engine = create_engine(
    "sqlite:///./test.db",
    connect_args={"check_same_thread": False}
)
```

### Dependency Injection:

```python
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
```

This ensures:

* A new session per request
* Automatic session cleanup
* No memory leaks

---

## 🔹 3. `models.py` – Database Models (Model Layer)

Defines database schema using SQLAlchemy ORM.

```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
```

### Database Table Structure

| Column | Type    | Constraint       |
| ------ | ------- | ---------------- |
| id     | Integer | Primary Key      |
| name   | String  | Indexed          |
| email  | String  | Unique + Indexed |

---

## 🔹 4. `schemas.py` – Data Validation Layer

Defines Pydantic models for validation and serialization.

```python
class UserBase(BaseModel):
    name: str
    email: str
```

```python
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
```

`orm_mode = True` allows returning SQLAlchemy objects directly.

---

## 🔹 5. `routers/users.py` – Application Layer (Controller)

Handles all CRUD operations.

---

# 🚀 API Endpoints

## 1️⃣ View All Users

```
GET /users
```

* Fetches all users
* Renders `index.html`

---

## 2️⃣ Create User

### Display Form

```
GET /users/create
```

### Submit Form

```
POST /users/create
```

Process:

1. Receive form data
2. Create User object
3. Add to session
4. Commit transaction
5. Redirect to `/users`

---

## 3️⃣ Update User

### Display Form

```
GET /users/update/{user_id}
```

### Submit Update

```
POST /users/update/{user_id}
```

Process:

1. Fetch user by ID
2. Update attributes
3. Commit changes

---

## 4️⃣ Delete User

```
POST /users/delete/{user_id}
```

Process:

1. Fetch user
2. Delete record
3. Commit transaction

---

# 🔄 Request Lifecycle

Example: Creating a User

```
Browser submits form
        ↓
FastAPI route receives request
        ↓
Dependency Injection creates DB session
        ↓
SQLAlchemy executes INSERT
        ↓
Database saves record
        ↓
Redirect to /users
        ↓
Updated list rendered
```

---

# 🧠 How the Architecture Works

---

## 🟢 Presentation Layer (View)

Located in `/templates`

* Renders dynamic data using Jinja2
* Displays forms
* Sends POST requests

Example:

```html
{{ user.name }}
```

---

## 🟢 Application Layer (Controller)

Located in `routers/users.py`

* Handles HTTP requests
* Contains CRUD logic
* Connects View and Model

---

## 🟢 Data Access Layer (Model)

Located in:

* `models.py`
* `database.py`

Responsible for:

* Defining tables
* Managing DB sessions
* Executing queries

---

# 🔌 Dependency Injection

Used via:

```python
db: Session = Depends(get_db)
```

FastAPI:

1. Calls `get_db()`
2. Injects DB session
3. Closes session after request

Benefits:

* Clean resource management
* Loose coupling
* Better testability

---

# 📊 Database Schema

SQLite Database: `test.db`

Equivalent SQL:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    email VARCHAR UNIQUE
);
```

---

# ✅ Features

* Clean modular architecture
* Dependency injection
* ORM abstraction
* Server-side rendering
* Unique email constraint
* Redirect handling
* Full CRUD operations

---

# ⚠️ Current Limitations

* No authentication system
* No password hashing
* No CSRF protection
* No pagination
* No logging system
* SQLite not ideal for high concurrency

---

# 🔮 Possible Improvements

* Add JWT authentication
* Use PostgreSQL
* Add Alembic migrations
* Add service layer
* Add repository layer
* Add Docker support
* Add pagination & search
* Add frontend framework (React/Vue)
* Convert to REST API

---

# 🎯 Learning Outcomes

By building this project, you practiced:

* FastAPI routing
* SQLAlchemy ORM
* Database session management
* Template rendering
* Dependency injection
* MVC architecture
* CRUD operations
* Application structuring

---

# 🧩 Architectural Strengths

* Clear separation of concerns
* Clean layered design
* Scalable structure
* Maintainable codebase
* Proper DB session lifecycle

---

# 🚀 Running the Project

### 1️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy jinja2
```

### 2️⃣ Start Server

```bash
uvicorn main:app --reload
```

### 3️⃣ Open in Browser

```
http://127.0.0.1:8000
```

---

# 🏁 Conclusion

This project demonstrates a complete **CRUD web application** built with modern Python backend technologies.

It follows clean architectural principles, uses dependency injection correctly, and implements full database persistence using ORM.

It serves as:

* A beginner-to-intermediate backend project
* A strong portfolio demonstration
* A foundation for scaling into production-level systems
