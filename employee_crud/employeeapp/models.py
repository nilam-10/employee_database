from django.db import models
from decimal import Decimal

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    bank_account_no = models.CharField(max_length=30, verbose_name="Bank Account Number")
    gender = models.CharField(max_length=20) 
    address = models.TextField(verbose_name="Residential Address")
    projects_completed = models.IntegerField(verbose_name="Projects Completed This Year")
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monthly Salary")
    date_joined = models.DateField(verbose_name="Date of Joining")

    @property
    def term_in_company(self):
        from datetime import date
        return date.today().year - self.date_joined.year

    def __str__(self):
        return f"{self.name} {self.surname}"
