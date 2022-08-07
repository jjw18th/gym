from django.db import models

# Create your models here.\
class Products(models.Model):
      ProductName=models.CharField(max_length=200);
      Pic=models.ImageField(upload_to='pictures');
      Price=models.IntegerField();
      def __str__(self):
          return self.ProductName;
class Recipe(models.Model):
      MealName=models.CharField(max_length=200);
      Pic=models.ImageField(upload_to='pictures');
      Recipe=models.CharField(max_length=200);
      def __str__(self):
          return self.MealName;
class Diet(models.Model):
    Meal=models.CharField(max_length=200);
    Time=models.CharField(max_length=100);
    WhatToEat=models.CharField(max_length=500);
    def __str__(self):
        return self.Meal;
class Batches(models.Model):
    BatchName=models.CharField(max_length=200);
    BatchTiming=models.CharField(max_length=100);
    def __str__(self):
        return self.BatchName;

class Message(models.Model):
    name=models.CharField(max_length=100)
    msg=models.CharField(max_length=500)
    def __str__(self):
     return self.name;
class Faq(models.Model):
    Query=models.CharField(max_length=300)
    Response=models.CharField(max_length=300)
def __str__(self):
    return self.Query;
