from django import forms


class CreateNewEntry(forms.Form):
    name = forms.CharField(
        label="What is the exhibit name?", max_length=50, required=True)
    author = forms.CharField(label="Who is the author? ",
                             max_length=50, required=False)
    url = forms.CharField(label="What is the website link?",
                          max_length=100, required=False)
    #enter_button = forms.BooleanField()
