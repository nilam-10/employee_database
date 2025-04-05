from django.db import models
from decimal import Decimal
from datetime import date

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default='example@example.com')

    phone_number = models.CharField(max_length=20, blank=True, null=True)

    gender = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    bank_account_no = models.CharField(max_length=30, verbose_name="Bank Account Number")
    address = models.TextField(verbose_name="Residential Address")

    position = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)

    projects_completed = models.PositiveIntegerField(default=0, verbose_name="Projects Completed This Year")
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Monthly Salary")


    date_joined = models.DateField(verbose_name="Date of Joining", blank=True, null=True)

    @property
    def term_in_company(self):
        if self.date_joined:
            return date.today().year - self.date_joined.year
        return 0

    def __str__(self):
        return f"{self.name} {self.surname}"
