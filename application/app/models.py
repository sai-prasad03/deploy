from django.db import models

# Create your models here.
class Applicant(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    job_role = models.CharField(max_length = 50)
    address = models.CharField(max_length = 120)
    city = models.CharField(max_length = 40)
    pincode = models.IntegerField()
    date = models.DateField(auto_now_add =True)
    file = models.FileField(upload_to='rdocs', blank=True)