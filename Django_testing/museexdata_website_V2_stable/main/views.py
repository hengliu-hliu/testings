from django.shortcuts import render
from django.http import HttpResponse
from .models import Exhibit_data, Institution_data
from .forms import NewExhibitEntry, NewInstitutionEntry, NewURLEntry

# Create your views here.


def home(response):
    return render(response, "main/home.html", {})

def institution_entry(response):

    if response.method == "POST":

        form_institution = NewInstitutionEntry(response.POST)

        if form_institution.is_valid():
            name = form_institution.cleaned_data["name_institution"]
            url = form_institution.cleaned_data["url_institution"]
            category = form_institution.cleaned_data["category_institution"]

            address = form_institution.cleaned_data["address_institution"]

            contact_phone = form_institution.cleaned_data["contact_phone_institution"]

            contact_email = form_institution.cleaned_data["contact_email_institution"]

            newEntry = Institution_data(
                name_institution=name,
                url_institution=url,
                category_institution=category,
                address_institution=address,
                contact_phone_institution=contact_phone,
                contact_email_institution=contact_email
            )
            newEntry.save()

    else:

        form_institution = NewInstitutionEntry()

    return render(response, "main/Institution_entry.html", {"form": form_institution})


def exhibit_entry(response):
    if response.method == "POST":
        form_exhibit = NewExhibitEntry(response.POST)

        if form_exhibit.is_valid():
            name = form_exhibit.cleaned_data["name_exhibit"]
            author = form_exhibit.cleaned_data["author_exhibit"]
            url = form_exhibit.cleaned_data["url_exhibit"]
            startdate = form_exhibit.cleaned_data["startdate_exhibit"]
            enddate = form_exhibit.cleaned_data["enddate_exhibit"]
            description = form_exhibit.cleaned_data["description_exhibit"]

            newEntry = Exhibit_data(
                name_exhibit=name,
                author_exhibit=author,
                url_exhibit=url,
                startdate_exhibit=startdate,
                enddate_exhibit=enddate,
                description_exhibit=description)

            newEntry.save()

    else:

        form_exhibit = NewExhibitEntry()

    return render(response, "main/Exhibit_entry.html", {"form": form_exhibit})


def url_entry(response):
    if response.method == "POST":
        url = NewURLEntry()
    else:

        url = NewURLEntry()
    return render(response, "main/Url_entry.html", {"form": url})


def entries(response):
    exhibits = Exhibit_data.objects.all()
    institutions = Institution_data.objects.all()

    return render(response, "main/Entries.html", {"exhibits": exhibits, "institutions": institutions})
