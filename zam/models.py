from django.db import models
from datetime import datetime
# Create your models here.

class PastWork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ('Architecture', 'Architecture'),
        ('Structural', 'Structural'),
        ('Mechanical', 'Mechanical'),
        ('Electrical', 'Electrical'),
        ('Quantity Surveying', 'Quantity Surveying')
    ])
    image = models.ImageField(upload_to='past_work/')

    def __str__(self):
        return self.title

from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=255)  # Full name of the sender
    email = models.EmailField()             # Email address
    phone = models.CharField(max_length=20, blank=True, null=True)  # Phone number (optional)
    subject = models.CharField(max_length=255)  # Subject of the message
    message = models.TextField()           # Message content
    sent_at = models.DateTimeField(auto_now_add=True)  # Timestamp of submission

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)  # Full name of the sender
    email = models.EmailField()             # Email address
    phone = models.CharField(max_length=20, blank=True, null=True)  # Phone number (optional)
    subject = models.CharField(max_length=255)  # Subject of the message
    message = models.TextField()
    created_at = models.DateTimeField(default=datetime.now) 
    # Add more fields as necessary
