from django.db import models

# Create your models here. Creates database model

# Table for Exhibit_data


class Exhibit_data(models.Model):
    name = models.CharField(max_length=50)  # name of exhibit
    # author/contributors to site
    author = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=100, null=True)  # url of exhibit page
 #   startdate = models.DateField(auto_now_add=False)  # start date
 #   enddate = models.DateField(auto_now_add=False)  # end date
 #   description from website, for keywords
 #   description = models.TextField(max_length=None)


# Table for Institution data
'''class Institution_data(models.Model):
    category = models.CharField(max_length = 50) # type of institution, museum, zoo, etc.
    url = models.CharField(max_length=50) # url of main page of Instituion
    address = models.CharField(max_length=150) # address of museum
    contact_phone = models.
    '''
