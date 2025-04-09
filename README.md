# 👥 Employee Management System (Django)
A comprehensive web application built using Django that allows you to manage employees, departments, projects, and tasks with full CRUD (Create, Read, Update, Delete) functionality.



---

## 🌟 Features

**Employee Management**

Add new employees with detailed information
Update existing employee profiles
View comprehensive employee lists with filtering and sorting
Delete employee records safely


**Department Management**

Create and organize departments
Assign employees to departments
Track department performance


**Project Tracking**

Create and assign projects
Track project status (Planning, In Progress, Completed)
Associate employees with multiple projects
Monitor project timelines


**Task Assignment**

Create tasks with priorities
Assign tasks to employees
Track task completion status
Set due dates and deadlines


## 📋 Database Schema
**Employee Model**

id: Auto-generated primary key
name: Employee first name
surname: Employee last name
email: Unique email address
bank_account_no: Bank account information
gender: Male, Female, or Other
address: Employee address
projects_done_in_year: Number of projects completed
salary: Employee salary
term_in_company: Employment duration in months
hire_date: Date of hiring
is_active: Employee current status

**Project Model**

name: Project name
description: Project details
start_date: Project commencement date
end_date: Project deadline (optional)
status: Planning, In Progress, or Completed
employees: Many-to-many relationship with Employee model

**Task Model**
title: Task name
description: Task details
project: Foreign key to Project model
assigned_to: Foreign key to Employee model
priority: Low, Medium, or High
due_date: Task deadline
completed: Task completion status

---

## 🏰️ Technologies Used

**Backend**

Python 3.x
Django 5.x
Django ORM for database operations


 **Frontend**
HTML/CSS
Bootstrap 5
Font Awesome icons
JavaScript


**Database**

MySQL (default)
Compatible with PostgreSQL, SQLite


 **Deployment**

Compatible with Heroku, AWS, DigitalOcean





---

## 📦 Setup Instructions

1. **Clone the Repository:**

```bash
git clone https://github.com/yourusername/employee_crud.git
cd employee_crud
```

2. **Create a Virtual Environment:**

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

3. **Install Dependencies:**

```bash
pip install django mysqlclient
```

4. **Run Migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Start the Development Server:**

```bash
python manage.py runserver
```

6. **Open in Browser:**

```
http://127.0.0.1:8000/
```

---





## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
Contribution Guidelines

Fork the repository
Create your feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add some amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

