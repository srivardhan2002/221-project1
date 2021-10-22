from django.db import models

class librarian(models.Model):
    name = models.CharField(max_length=64)
    phone_number = models.IntegerField(blank=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email_id = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} Ph.no:{self.phone_number}"
    
class student(models.Model):
    name = models.CharField(max_length=64)
    phone_number = models.IntegerField(blank = True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email_id = models.CharField(max_length=64, blank = True)

    def __str__(self):
        return f"{self.name} Ph.no:{self.phone_number}"


