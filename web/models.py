from django.db import models

# Create your models here.

class College(models.Model):
    cname = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    code = models.IntegerField()
    contact_no = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.cname

class Student(models.Model):
    clg = models.ForeignKey(College,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField()
    branch = models.CharField(max_length=100)
    address = models.TextField()
    image = models.FileField(null=True)


    def __str__(self):
        return self.name






