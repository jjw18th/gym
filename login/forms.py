from django import forms
class UserLogin(forms.Form):
    username=forms.CharField(label='username');
class NewTrainer(forms.Form):
    FullName=forms.CharField(label='Full Name',max_length=200);
    Pic=forms.FileField(label='Picture');
    Email=forms.EmailField(label='Email');
    Contact=forms.IntegerField(label='Contact');
    JoinDate=forms.DateField(label='JoinDate');
    BirthDate=forms.DateField(label='BirthDate');
    Status=forms.CharField(label='Status');
class SearchTrainer(forms.Form):
    FullName=forms.CharField(label='Full Name',max_length=200);
