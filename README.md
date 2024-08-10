# MoneyTrail

## About

**MoneyTrail** is a finance tracker application designed to help users manage their income and expenses. Users can track their financial activities, categorize their expenses, and have a clear view of their financial status.

## User Stories

- The user can sign up and login
- The user can add, edit, and delete their income or an expenses
- The user can view a list of their incomes and expenses
- The user can see the total amount of income and expenses


## Wireframe

![image](https://github.com/user-attachments/assets/e98116cf-71c9-406d-9e91-2584f74d2e3e)


## Installation Guide

1. **Clone the repository:**
   
`git clone https://github.com/Anwar-Abdel/MoneyTrail.git`

 `cd moneytrail`


2. **Create a virtual environment:**
   
`python3 -m venv moneytrail`

3. **Install the dependencies:**
   
`pip install -r requirements.txt`


4. **Set up the database:**
   
`python manage.py makemigrations`

`python manage.py migrate`


5. **Run the development server:**
   
`python manage.py runserver`


## Technologies used

### Frontend
- HTML
- CSS

### Backend
- Python
- Django
- PostgreSQL
- Plotly
- Pandas


## ERD

**User**
- username, email, and password

**Income**
- amount, source, and date

**Expense**
- amount, description, category, and date









