from django.shortcuts import render

from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class StudentApi(APIView):
    def get(self,request,pk=None,format=None):
        if pk is not None:
            stu = Student.objects.get(id = pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu , many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"data creted"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk,format=None):
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data update successfully'})
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


    def patch(self,request,pk,format=None):
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial update successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        stu = Student.objects.get(id = pk)
        stu.delete()
        return Response({'msg':'data delete'})





