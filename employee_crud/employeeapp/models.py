from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    bank_account_no = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    projects_done_in_year = models.IntegerField()
    salary = models.FloatField()
    term_in_company = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.surname}"
