from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from Projects.models import Project
import datetime


class FinancialRecord(models.Model):
    STATUS_CHOICES = (
        ('paid', 'paid'),
        ('in progress', 'in progress'),
        ('canceled', 'canceled'),
    )

    who_created = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    price = models.FloatField()
    description = models.TextField()
    status = models.CharField(max_length=11, choices=STATUS_CHOICES)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_at = self.updated_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        super().save(*args, **kwargs)


class FinancialProjectInput(models.Model):
    EXPENSE_CHOICES = [
        ('labor', 'Labor'),
        ('material', 'Material'),
        ('overhead', 'Overhead'),
        ('other', 'Other'),
    ]
    who_created = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='financial_inputs')
    financial_record = models.ForeignKey(FinancialRecord, on_delete=models.CASCADE, related_name='project_financials')
    expense_type = models.CharField(max_length=50, choices=EXPENSE_CHOICES)
    amount = models.FloatField()
    description = models.TextField(blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.project.title}: {self.expense_type} - {self.amount}"

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        super().save(*args, **kwargs)
