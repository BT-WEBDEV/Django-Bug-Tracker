from django.db import models
from django.utils.timezone import timezone
from datetime import datetime
# Create your models here.

#Priority
class Priority(models.Model):
    name = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name #or self.title for blog posts

#Category
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name #or self.title for blog posts


#TICKET
class Ticket(models.Model):
    #BugID
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    reporter = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    #BugOverview
    summary = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)

    #BugEnvironment
    platform = models.CharField(max_length=20, blank=True, null=True)
    operating_system = models.CharField(max_length=20, blank=True, null=True)
    browser = models.CharField(max_length=20, blank=True, null=True)
    categories = models.ManyToManyField('Category', related_name='posts')
 
    #BugDetails
    steps_to_reproduce = models.TextField(blank=True, null=True)
    expected_result = models.CharField(max_length=100, blank=True, null=True)
    actual_result = models.CharField(max_length=100, blank=True, null=True)
    
    #BugTracking
    priorities = models.ManyToManyField('Priority', related_name='tickets')
    assigned_to = models.CharField(max_length=100, blank=True, null=True)
    completed = models.BooleanField(db_column='Completed', default=False)
    datecompletion = models.DateTimeField(db_column='DateCompletion', blank=True, null=True)

    def set_completion(self):
        self.completed = True
        self.datecompletion = datetime.now()
        self.save()
    
    def __str__(self):
        return self.title

#TICKET COMMENT
class Comment(models.Model):
    author = models.CharField(max_length=60,)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Ticket', on_delete=models.CASCADE)