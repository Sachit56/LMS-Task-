from django.db import models

# Create your models here.
class UserModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254,unique=True)
    membership_date=models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.id)

class BookModel(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField( max_length=50)
    isbn=models.CharField(unique=True,max_length=50)
    published_date=models.DateField(auto_now=False, auto_now_add=False)
    genre=models.CharField(max_length=50)


    def __str__(self):
        return str(self.id)
    
class BookDetailsModel(models.Model):
    id=models.AutoField(primary_key=True)
    number_of_pages=models.IntegerField()
    publisher=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    book=models.OneToOneField(BookModel, on_delete=models.CASCADE,default=True)

    def __str__(self):
        return str(self.id)
    
class BorrowedBooksModel(models.Model):
    userid=models.ForeignKey("UserModel", verbose_name=("User Id"), on_delete=models.CASCADE)  
    bookid=models.ForeignKey("BookModel", verbose_name=("Book Id"), on_delete=models.CASCADE) 
    borrowed_date=models.DateField(auto_now=False, auto_now_add=False)   
    return_date=models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.id)


    


        