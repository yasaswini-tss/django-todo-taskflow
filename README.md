# 🚀 TaskFlow – Django ToDo Web Application

TaskFlow is a web-based task management application developed using **Python and Django**. It helps users organize their daily activities by creating, editing, completing, and deleting tasks. The application includes user authentication and keeps each user's tasks separate.

## ✨ Features

- 🔐 User Registration, Login, and Logout
- ➕ Add new tasks
- ✏️ Edit existing tasks
- ✅ Mark tasks as completed
- 🗑️ Delete tasks
- 📊 Dashboard displaying total, pending, and completed task counts
- 👤 User-specific task management
- 📱 Responsive interface

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML | Page structure |
| CSS | Styling |
| Bootstrap | Responsive UI |
| SQLite | Database |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
django-todo-taskflow/
├── manage.py
├── todo/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── todo_main/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   ├── home.html
│   ├── edit.html
│   ├── register.html
│   └── registration/
│       └── login.html
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/yasaswini-tss/django-todo-taskflow.git
cd django-todo-taskflow
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Django

```bash
pip install django
```

If a `requirements.txt` file is available, install the dependencies with:

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open this URL in your browser:

http://127.0.0.1:8000/

## 🔒 Security and Authentication

- Users must log in to access their dashboard.
- Tasks are associated with their respective users.
- Task operations check ownership to prevent users from modifying other users' tasks.

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

- Django models, views, and URL routing
- Database operations and migrations
- User authentication and session management
- CRUD application development
- User-specific data access
- Git and GitHub workflows

## 🚀 Future Enhancements

- Task priorities and due dates
- Search and filtering
- Task reminders
- Deployment to a public hosting platform

## 👩‍💻 Developer

**Yasaswini Sai Sri Theerdhala**

GitHub: [yasaswini-tss](https://github.com/yasaswini-tss)

---

⭐ If you find this project useful, feel free to explore the repository!

## 📸 Project Screenshot

![TaskFlow Dashboard](C:\Users\yasas\OneDrive\Pictures\Screenshots\screenshot)
