from django.urls import path

from . import views

urlpatterns = [
    path("Exhibit_entry/", views.exhibit_entry, name="exhibit_entry"),

    path("Institution_entry/", views.institution_entry, name="institution_entry"),

    path("Url_entry/", views.url_entry, name="url_entry"),

    path("entries/", views.entries, name="entries"),

    path("", views.home, name="home"),


]
