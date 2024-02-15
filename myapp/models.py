from django.db import models

# Create your models here.
class userpass(models.Model):
    username=models.CharField(max_length=50,blank=False,null=False,verbose_name='username')
    password=models.IntegerField(null=False,blank=False ,unique=True,verbose_name='password')
    usertype=models.CharField(max_length=50,blank=False,null=False,verbose_name='usertype')
    class Meta:
        db_table='userpass'
class Student(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False,verbose_name='stdtname')
    phone=models.IntegerField(null=False,blank=False ,unique=True,verbose_name='phone')
    email=models.EmailField(max_length=50,blank=False,unique=True,verbose_name='email')
    departmant=models.CharField(max_length=50,blank=False,null=False,verbose_name='departmant')
    passid=models.ForeignKey(userpass,on_delete=models.CASCADE,verbose_name='passid')
    class Meta:
        db_table='Student'
class Teacher(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False,verbose_name='techname')
    phone=models.IntegerField(null=False,blank=False ,unique=True,verbose_name='phone')
    email=models.EmailField(max_length=50,blank=False,unique=True,verbose_name='email')
    departmant=models.CharField(max_length=50,blank=False,null=False,verbose_name='departmant')
    passid=models.ForeignKey(userpass,on_delete=models.CASCADE,verbose_name='passid')

    class Meta:
        db_table='Teacher'
