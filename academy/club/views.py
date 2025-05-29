from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class CRUD_Students(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class ListStudents(APIView):
    def get(self, request):
        student = Students.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def list_stu(request):
    if request.method == 'GET':
        student = Students.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)


def info(request, sname):
    a = Students.objects.filter(name=sname).values()
    return HttpResponse(a)

def members(request):
    return HttpResponse("Hello bache ha!!")