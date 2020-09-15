from django import forms

class NewInstitutionEntry(forms.Form):

    # form entry institution name
    name_institution = forms.CharField(label="Name of Instituion :")

    # form entry instituion url
    url_institution = forms.CharField(label="Exhibit Website Link ",
                                      max_length=100, required=False)

    # form entry instituion category
    category_institution = forms.CharField(
        label="Category (museum, zoo, etc.) ")

    # form entry instituion address
    address_institution = forms.CharField(label="Address ")

    # institution phone number
    contact_phone_institution = forms.CharField(
        label="Contact Phone Number ")

    # institution email
    contact_email_institution = forms.CharField(label="Contact Email")


class NewExhibitEntry(forms.Form):

    # exhibit name
    name_exhibit = forms.CharField(
        label="Exhibit Name ", max_length=50, required=True)

    # exhibit author
    author_exhibit = forms.CharField(label="Author ",
                                     max_length=50, required=False)

    # url of exhibit page
    url_exhibit = forms.CharField(
        max_length=100)

    # exhibit start date
    startdate_exhibit = forms.CharField(label="Start Date ")

    # exhibit end date
    enddate_exhibit = forms.CharField(label="End Date ")

    # exhibit description
    description_exhibit = forms.CharField(label="Description ")


class NewURLEntry(forms.Form):
    name_exhibit = forms.CharField(
        label="URL ", max_length=50, required=True)
