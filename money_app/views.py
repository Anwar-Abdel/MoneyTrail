from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Expense, Income
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user
from .forms import SignUpForm, IncomeForm, ExpenseForm
from django.contrib.auth.decorators import login_required


#--------VIEWS----------#
def welcome(request):
    return render(request, 'money_app/welcome.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'money_app/signup.html', {'form': form})

def user_login(request):
    return render(request, 'money_app/login.html')

def home(request):
    return render(request, 'money_app/home.html')


#--------GET----------#
def income_list(request):
    incomes = Income.objects.all()
    return render(request, 'money_app/incomes/income_list.html', {'incomes': incomes})

def expense_list(request):
    expense = Expense.objects.all()
    return render(request, 'money_app/expense.html', {'expense': expense})


#--------POST----------#
@login_required
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

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = get_user(request)
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'money_app/expense/expense_list.html', {'form': form})


#--------POST----------#
def edit_income(request, id):
    income = get_object_or_404(Income, id=id)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'money_app/incomes/edit_income.html', {'form': form})

def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'money_app/expense/edit_expense.html', {'form': form})


#--------DELETE----------#
def delete_income(request, id):
    income = get_object_or_404(Income, id=id)
    if request.method == 'POST':
        income.delete()
        return redirect('income_list')
    return render(request, 'money_app/incomes/delete_income.html', {'income': income})

def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'money_app/expense/delete_expense.html', {'expense': expense})


