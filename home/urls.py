from django.urls import path

from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("application-create/", views.applicationCreate, name="application-create"),
    path("application-list/", views.applicationList, name="application-list"),
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
]
