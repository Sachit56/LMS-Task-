import datetime
from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *



#■ Create a New User, List All Users...................

class UserView(APIView):

    def get(self,request):
        users=UserModel.objects.all()
        serializer=UserSerializer(users,many=True)

        return Response({'status':200,'users':serializer.data})
    
    
    def post(self,request):
        try:
            serializer=UserSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                return Response({'status':200,'users':serializer.data})
            else:
                return Response({'status':400,'message':serializer.errors})
        
        except Exception as e:
            return Response({'status': 500, 'message': f'Internal Server Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#■ Get User by ID.......................

class UserIdView(APIView):


    def get(self,request,id):
        try:
            user=UserModel.objects.get(id=id)
            serializer=UserSerializer(user)

            return Response({'status':200,'user':serializer.data})
        except:
            return Response({'status':400,'message':serializer.errors})

   
# ■ Add a New Book , ■ List All Books............

class BookView(APIView):

    def get(self,request):
        try:
            books=BookModel.objects.all()
            serializer=BookSerializer(books,many=True)

            return Response({'status':200,'users':serializer.data})
        except:
            return Response({'status':400,'message':serializer.errors})
    
    
    def post(self,request):
        try:
            serializer=BookSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()

                return Response({'status':200,'books':serializer.data})
            else:
                return Response({'status':400,'message':serializer.errors})
        except Exception as e:
            return Response({'status': 500, 'message': f'Internal Server Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
    
    
    def patch(self,request):

        try:    
            books=BookModel.objects.get(id=request.data['id'])
            serializer=BookSerializer(books,data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'books':serializer.data})
            else:
                return Response({'status':400,'message':serializer.errors})
        except Exception as e:
            return Response({'status': 500, 'message': f'Internal Server Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        

#■ Get Book by ID , ■ Assign/Update Book Details.............

class BookDetailsView(APIView):


    def get(self,request,id):
        try:
            book=BookDetailsModel.objects.get(book=id)
            serializer=BookDetailsSerializer(book)

            return Response({'status':200,'Details':serializer.data})
        except Exception as e:
            return Response({'status': 500, 'message': f'Internal Server Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
    
    
    def put(self,request,id):
        try:
            book=BookDetailsModel.objects.get(book=id)
            serializer=BookDetailsSerializer(book,data=request.data)

            if serializer.is_valid():
                serializer.save()

                return Response({'status':200,'Details':serializer.data})
            else:
                return Response({'status':400,'message':serializer.errors}) 
        except Exception as e:
            return Response({'status': 500, 'message': f'Internal Server Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

#■ Borrow a Book , ■ Return a Book , ■ List All Borrowed Books...........................

class BorrowedBooksView(APIView):


    def get(self,request):
        try:
            books=BorrowedBooksModel.objects.all()
            serializer=BorrowedBooksSerializer(books,many=True)

            return Response({'status':200,'borrowed_books':serializer.data})
        except:
            return Response({'status':400,'message':serializer.errors})

    
    
    def post(self,request):
        try:
            serializer=BorrowedBooksSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response({'status':200,'borrowedbooks_by_user':serializer.data['userid']})
            else:
                return Response({'status':400,'message':serializer.errors})
        except Exception as e:
            return Response({'status': 500, 'message': f'Internal Server Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
    
    
    def put(self,request):
        try:
            book=BorrowedBooksModel.objects.get(return_date=request.data['return_date'])
            book.delete()

            return Response({'status':200,'message':'Book returned successfully'})
        except:
            return Response({'status':400,'message':'cannot return'})    



