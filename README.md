# MoneyTrail

## About

**MoneyTrail** is a finance tracker application designed to help users manage their income and expenses. Users can track their financial activities, categorize their expenses, and have a clear view of their financial status.

## Socials
[Website](https://moneytrail-ty5a.onrender.com/)

## User Stories

- The user can sign up and login
- The user can add, edit, and delete their income or an expenses
- The user can view a list of their incomes and expenses
- The user can see the total amount of income and expenses


## Wireframe

![image](https://github.com/user-attachments/assets/e98116cf-71c9-406d-9e91-2584f74d2e3e)


## Getting started

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

## ERD

**User**
- username, email, and password

**Income**
- amount, source, and date

**Expense**
- amount, description, category, and date

## Code Snippets

```python @login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = get_user(request)
            income.save()
            return redirect('income_list')
    else:
        form = IncomeForm()
    return render(request, 'money_app/incomes/add_income.html', {'form': form})

```

## Final Product


<img src="https://github.com/user-attachments/assets/485ad219-1d95-4105-a003-5f0f9ad9bbb6" alt="image" width="700"/>
<img src="https://github.com/user-attachments/assets/a9ae3c29-3f9b-40ae-ba04-8af02aba289a" alt="image" width="500"/>
<img src="https://github.com/user-attachments/assets/5be3aead-ed59-4f0a-98c1-eaf0ba2237ba" alt="image" width="400"/>


## Future Updates

- Add a Profile section
- Create payment reminders/subscription plans
- Fix User authentication

## Credits

I would like to thank my GA instructors [Rome Bell ](https://github.com/romebell) and [Alo](https://github.com/DigitalPhoneme)
