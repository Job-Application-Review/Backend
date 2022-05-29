from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Application
from .serializers import ApplicationSerializer, UserSerializer, UserSerializerWithToken

# Create your views here.


@api_view(["GET"])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):

        print(request.data)
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    file_uploaded = request.FILES.get("cv")
    print(file_uploaded)
    # print(serializer)

    if serializer.is_valid():
        serializer.save()
    else:
        print("Not valid")

    return Response(serializer.data)


@api_view(["GET"])
def applicationList(request):

    current_username = request.user.username
    print(current_username)
    # try:
    #     tasks = Application.objects.get(username=current_username)
    # except Application.DoesNotExist:
    #     tasks = None
    tasks = Application.objects.filter(username=current_username).order_by("-id")

    serializer = ApplicationSerializer(tasks, many=True)
    # print(serializer.data)
    return Response(serializer.data)


@api_view(["GET"])
def applicationListAdmin(request):

    current_username = request.user.username
    print(current_username)
    # try:
    #     tasks = Application.objects.get(username=current_username)
    # except Application.DoesNotExist:
    #     tasks = None
    tasks = Application.objects.all().order_by("-id")

    serializer = ApplicationSerializer(tasks, many=True)
    # print(serializer.data)
    return Response(serializer.data)


@api_view(["GET"])
def applicationDetail(request, pk):
    tasks = Application.objects.get(id=pk)
    serializer = ApplicationSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def applicationUpdate(request, pk):
    task = Application.objects.get(id=pk)
    serializer = ApplicationSerializer(instance=task, data=request.data)

    mail_subject = "Job Application Mail"
    to_email = task.email

    if serializer.is_valid():
        serializer.save()

        print(serializer.data["status"])
        if serializer.data["status"] == "A":
            message = "Your application has been accepted"
        else:
            message = "Your application has been rejcted"

        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

    return Response(serializer.data)


@api_view(["DELETE"])
def applicationDelete(request, pk):
    task = Application.objects.get(id=pk)
    task.delete()

    return Response("Item succsesfully delete!")


@api_view(["GET"])
def allUser(request):

    user = User.objects.all()

    serializer = UserSerializer(user)
    return Response(serializer.data)


def sendMail(request):
    mail_subject = "Activate your blog account."
    # message = render_to_string("acc_active_email.html")
    message = "There are some changes made in your application"
    to_email = "shubhamofficial7413@gmail.com"
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
