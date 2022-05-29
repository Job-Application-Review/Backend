from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from . import views
from .views import UserList, current_user

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("application-create/", views.applicationCreate, name="application-create"),
    path("application-list/", views.applicationList, name="application-list"),
    path(
        "application-list-admin/",
        views.applicationListAdmin,
        name="application-list-admin",
    ),
    path(
        "application-detail/<str:pk>/",
        views.applicationDetail,
        name="application-detail",
    ),
    path(
        "application-update/<str:pk>/",
        views.applicationUpdate,
        name="application-update",
    ),
    path(
        "application-delete/<str:pk>/",
        views.applicationDelete,
        name="application-delete",
    ),
    path("token-auth/", obtain_jwt_token),
    path("current_user/", current_user),
    path("users/", UserList.as_view()),
    path(
        "all-users",
        views.allUser,
        name="allUser",
    ),
]
