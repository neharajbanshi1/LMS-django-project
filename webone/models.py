from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Student(models.Model):
    name= models.CharField(max_length=100)
    student_id=models.CharField(max_length=50)
    phone_nummber= models.CharField(max_length=10)
    image=models.FileField(upload_to='students/')

class Books(models.Model):
    name =models.CharField(max_length=100)
    author_name= models.CharField(max_length=100)
    number_of_copies= models.IntegerField()
    category_id= models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Bookborrow(models.Model):
    student_Id= models.ForeignKey("Student", on_delete=models.CASCADE)
    book_id=models.ForeignKey("Books", on_delete=models.CASCADE)
    burrowed_at= models.DateField()
    returned_at= models.DateField()
    is_returned= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student_id.name} burrowed {self.book_id.name}"
    