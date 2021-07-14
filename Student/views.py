from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from Student.models import Student, University
from Student.serializers import UniversitySerializer, StudentSerializer
from rest_framework import status


# Create your views here.
@api_view(['GET', 'PUT'])
@csrf_exempt
def universities(request):
    if request.method == 'GET':
        university = University.objects.all()
        serializer = UniversitySerializer(university, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
@csrf_exempt
def students(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def university_detail(request, id):
    try:
        university = University.objects.get(id=id)

    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UniversitySerializer(university)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(university)
        serializer = UniversitySerializer(university, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        university.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def student_detail(request, id):
    try:
        student = Student.objects.get(id=id)

    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = JSONParser().parse(student)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

