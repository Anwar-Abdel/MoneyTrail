from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Income, Expense, User


admin.site.register(User)
admin.site.register(Income)
admin.site.register(Expense)