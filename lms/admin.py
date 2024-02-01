from django.contrib import admin
from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display=('userid','name','email','membership_date')

class BookAdmin(admin.ModelAdmin):
    list_display=('bookid','isbn','title','genre')

class BookDetailsAdmin(admin.ModelAdmin):
    list_display=('publisher','language')

class BorrowedBooksAdmin(admin.ModelAdmin):
    list_display=('borrowed_date','return_date')

admin.site.register(UserModel,UserAdmin)  
admin.site.register(BookModel,BookAdmin)    
admin.site.register(BookDetailsModel,BookDetailsAdmin)    
admin.site.register(BorrowedBooksModel,BorrowedBooksAdmin)    


