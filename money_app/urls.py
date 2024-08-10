from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='money_app/login.html'), name='login'),

    path('income_list/', views.income_list, name='income_list'),
    path('add_income/', views.add_income, name='add_income'),
    path('delete_income/<int:id>/', views.delete_income, name='delete_income'),
    path('edit_income/<int:id>/', views.edit_income, name='edit_income'),

    path('expense_list/', views.expense_list, name='expense_list'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('delete_expense<int:id>/', views.delete_expense, name='delete_expense'),
    path('edit_expense<int:id>/', views.edit_expense, name='edit_expense'),

]