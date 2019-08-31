from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False)
    phone = models.TextField(blank=True)
    recording = models.FileField(upload_to='registration')
    submit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
