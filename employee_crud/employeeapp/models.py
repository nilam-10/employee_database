from django.db import models
from decimal import Decimal

class Employee(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    bank_account_no = models.CharField(max_length=30, verbose_name="Bank Account Number")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    projects_done_in_year = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_joined = models.DateField()

    @property
    def term_in_company(self):
        from datetime import date
        return date.today().year - self.date_joined.year

    def __str__(self):
        return f"{self.name} {self.surname}"
