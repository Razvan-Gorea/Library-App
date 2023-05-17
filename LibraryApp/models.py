from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    number_in_inventory = models.IntegerField()
    year = models.SmallIntegerField()
    author = models.TextField()
    title = models.TextField()
    genre = models.TextField()

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.TextField()

class Borrow(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_returned = models.BooleanField()