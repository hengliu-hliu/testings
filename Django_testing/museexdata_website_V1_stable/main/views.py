from django.shortcuts import render
from django.http import HttpResponse
from .models import Exhibit_data
from .forms import CreateNewEntry

# Create your views here.


def home(response):
    return render(response, "main/home.html", {})


def Exhibit_entry(response):
    if response.method == "POST":
        form = CreateNewEntry(response.POST)

        if form.is_valid():
            a = form.cleaned_data["name"]
            b = form.cleaned_data["author"]
            c = form.cleaned_data["url"]

            f = Exhibit_data(name=a, author=b, url=c)
            f.save()

    else:

        form = CreateNewEntry()

    return render(response, "main/Exhibit_entry.html", {"form": form})
