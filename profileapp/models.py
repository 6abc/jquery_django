from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    agree = models.BooleanField(default=False)

    def __str__(self):
        return self.name