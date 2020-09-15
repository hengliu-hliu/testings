from django.urls import path

from . import views

urlpatterns = [
    path("entry/", views.Exhibit_entry, name="entry"),
    path("", views.home, name="home"),

]
