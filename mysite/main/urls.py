from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name='index'),
    path("<int:id>", views.List, name="list"),
    path("create/", views.Create, name="create")
]
