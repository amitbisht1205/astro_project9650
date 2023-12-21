from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import NumerologyHistory,CustomUser
# from .models import UserProfile


LANG_CHOICES = [
    ('eng', 'English'),
    ('hin', 'Hindi'),
    # Add more language choices if needed
]
class Registerform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    Retype_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=CustomUser
        fields = ('email', 'first_name', 'last_name','phone_number')
    def clean(self):
        super().clean()
        p=self.cleaned_data.get('password')
        p1=self.cleaned_data.get('Retype_password')
        if p!=p1:
            raise forms.ValidationError("both passwords did not match")    

class logform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
class ValueForm(forms.Form):
    namelist=forms.CharField(label='Name List', max_length=50)
    
  
class ChacterForm(forms.Form):
    ch=forms.CharField(max_length=5)


class NumberForm(forms.Form):
    number=forms.IntegerField()   



class BhagyankPredictionForm(forms.Form):
    bhagyank=forms.IntegerField()
    lang=forms.CharField(max_length=3)

class CardPredictionForm(forms.Form):
    tarot_num=forms.IntegerField()
    bin_num=forms.IntegerField()
    lang=forms.ChoiceField(choices=LANG_CHOICES,label='language')

class BirthDateForm(forms.Form):
    birth_date=forms.DateField(label='birth_date',widget=forms.DateInput(attrs={'type':'date'}))  
    

class MaturityNumberForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    dob = forms.DateField(label='Date of Birth (YYYY-MM-DD)', required=True, input_formats=['%Y-%m-%d'])

class KarmicNumberForm(forms.Form):
    date_str = forms.CharField(label='Date (YYYY-MM-DD)', max_length=10)

class BalanceNumberForm(forms.Form):
    name = forms.CharField(label='Enter Name', max_length=100)    

class NameForm(forms.Form):
    name = forms.CharField(label='Enter Name', max_length=100)    

class DateForm(forms.Form):
    date = forms.DateField(label='Enter Date (YYYY-MM-DD)')


class TarotForm(forms.Form):
    rand_num = forms.IntegerField()
    bin_num = forms.IntegerField()
    




class NumerologyForm(forms.ModelForm):
    class Meta:
        model = NumerologyHistory
        fields = ['Name', 'Gender', 'DOB', 'TOB', 'POB']
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date'}),
            'TOB': forms.TimeInput(attrs={'type': 'time'}),
            'POB':forms.TextInput(attrs={'id':'place_of_birth'}),
        }


class AstrologyForm(forms.Form):
    Name = forms.CharField(label='Name')
    gender = forms.CharField(label='Gender')
    DOB= forms.CharField(label='Date')
    TOB = forms.CharField(label='Time')
    POB = forms.CharField(label='Place')         



class ChoghadiyaForm(forms.Form):
    dateSelect = forms.ChoiceField(choices=[('today', 'Today'), ('tomorrow', 'Tomorrow'), ('yesterday', 'Yesterday')])
    currentDate = forms.DateField()
    currentTime = forms.TimeField()
    place = forms.CharField()
    dayOfWeek = forms.IntegerField(min_value=1, max_value=7)

class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(max_length=15)