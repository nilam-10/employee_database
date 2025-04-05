rom django.db import models
from django.utils import timezone

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default='example@example.com')
    bank_account_no = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    projects_done_in_year = models.IntegerField(default=0)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    term_in_company = models.IntegerField(help_text="Employment duration in months")
    hire_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} {self.surname}"

class Project(models.Model):
    STATUS_CHOICES = [
        ('P', 'Planning'),
        ('I', 'In Progress'),
        ('C', 'Completed'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    employees = models.ManyToManyField(Employee, related_name='projects')
    
    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='assigned_tasks')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title


