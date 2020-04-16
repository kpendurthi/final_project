from django.db import models
from django.utils import timezone


JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

class Employer(models.Model):
    Company_Name= models.CharField(max_length=100)
    Company_Address=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)

    def __str__(self):
        return self.Company_Name

class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE,related_name='job')
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    category = models.CharField(max_length=100)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    website = models.CharField(max_length=100, default="")
    image_url = models.TextField(default='https://www.mydrdental.com/wp-content/uploads/2017/12/Prinicpal_Financial_Group.jpg')
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)
    salary = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title




