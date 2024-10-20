from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from Financial.models import FinancialRecord


class Project(models.Model):
    COLOR_CHOICES = (
        ('red', 'red'),
        ('black', 'black'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('gray', 'gray'),
        ('pink', 'pink'),
        ('yellow', 'yellow'),
    )
    title = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    color = models.CharField(max_length=6, choices=COLOR_CHOICES)
    image = models.ImageField(upload_to='projects/project/',
                              default='projects/default/project_d.png')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)
    budget = models.PositiveBigIntegerField(null=True, blank=True)
    financial_object_type = GenericRelation(FinancialRecord, related_name='project')

    def __str__(self):
        return self.title

    @property
    def content_id(self):
        c = ContentType.objects.get_for_model(self)
        return c.id


class Task(models.Model):
    COLOR_CHOICES = (
        ('red', 'red'),
        ('black', 'black'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('gray', 'gray'),
        ('pink', 'pink'),
        ('yellow', 'yellow'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    color = models.CharField(max_length=6, choices=COLOR_CHOICES)
    image = models.ImageField(upload_to='projects/task/',
                              default='projects/default/project_d.png')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)
    budget = models.PositiveBigIntegerField(null=True, blank=True)
    financial_object_type = GenericRelation(FinancialRecord, related_name='task')

    def __str__(self):
        return self.title

    @property
    def content_id(self):
        c = ContentType.objects.get_for_model(self)
        return c.id


class SubTask(models.Model):
    COLOR_CHOICES = (
        ('red', 'red'),
        ('black', 'black'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('gray', 'gray'),
        ('pink', 'pink'),
        ('yellow', 'yellow'),
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    color = models.CharField(max_length=6, choices=COLOR_CHOICES)
    image = models.ImageField(upload_to='projects/subtask/',
                              default='projects/default/project_d.png')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)
    budget = models.PositiveBigIntegerField(null=True, blank=True)
    financial_object_type = GenericRelation(FinancialRecord, related_name='subtask')

    def __str__(self):
        return self.title

    @property
    def content_id(self):
        c = ContentType.objects.get_for_model(self)
        return c.id
