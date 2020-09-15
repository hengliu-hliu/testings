from django.db import models

# Create your models here. Creates database model


# Table for Institution data
class Institution_data(models.Model):

    # name of institution
    name_institution = models.CharField(max_length=50)

    # type of institution, museum, zoo, etc.
    category_institution = models.CharField(max_length=50)

    # url of main page of Instituion
    url_institution = models.CharField(max_length=50)

    # address of museum
    address_institution = models.CharField(max_length=150)

    # phone number contact
    contact_phone_institution = models.CharField(
        max_length=50, null=True)

    # phone email contact
    contact_email_institution = models.CharField(
        max_length=50, null=True)


# Table for Exhibit_data
class Exhibit_data(models.Model):

    # name of exhibit
    name_exhibit = models.CharField(max_length=50)

    # author/contributors to site
    author_exhibit = models.CharField(
        max_length=50, null=True)

    # url of exhibit page
    url_exhibit = models.CharField(
        max_length=100, null=True)

    # start date
    startdate_exhibit = models.CharField(
        max_length=50, null=True)

    # end date
    enddate_exhibit = models.CharField(
        max_length=50, null=True)

    # description from website, for keywords
    description_exhibit = models.CharField(max_length=50, null=True)

    # left join joining institution_data key to institution_museum column
    #instituion_museum = models.ForeignKey('Institution_data',on_delete=models.CASCADE,)
