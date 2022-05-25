from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Application
from .serializers import ApplicationSerializer

# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/application-list/",
        "Detail View": "/application-detail/<str:pk>/",
        "Create": "/application-create/",
        "Update": "/application-update/<str:pk>/",
        "Delete": "/application-delete/<str:pk>/",
    }

    return Response(api_urls)


@api_view(["POST"])
def applicationCreate(request):
    serializer = ApplicationSerializer(data=request.data)

    print(serializer)

    if serializer.is_valid():
        print("hello")
        serializer.save()
    else:
        print("Not valid")

    return Response(serializer.data)


@api_view(["GET"])
def applicationList(request):
    tasks = Application.objects.all().order_by("-id")
    serializer = ApplicationSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def applicationDetail(request, pk):
    tasks = Application.objects.get(id=pk)
    serializer = ApplicationSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def applicationUpdate(request, pk):
    task = Application.objects.get(id=pk)
    serializer = ApplicationSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def applicationDelete(request, pk):
    task = Application.objects.get(id=pk)
    task.delete()

    return Response("Item succsesfully delete!")
