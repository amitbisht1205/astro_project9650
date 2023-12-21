from django.shortcuts import render,redirect
from datetime import datetime
from .models import CustomUser
from .backends import PhoneNumberBackend
from django.contrib.auth.backends import ModelBackend   
from django.http import HttpResponseServerError
from requests.exceptions import RequestException
from django.shortcuts import get_object_or_404
from .tarot import *
from .models import KundliData 
import requests
from django.http import JsonResponse
from .moolank import *
import time
from datetime import datetime
from datetime import timedelta
from django.utils.translation import activate
import re
import json
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View,CreateView
from .forms import logform,Registerform,ValueForm,ChacterForm,NumberForm,BhagyankPredictionForm,CardPredictionForm,BirthDateForm,MaturityNumberForm,KarmicNumberForm,NameForm,DateForm,TarotForm,NumerologyForm,ChoghadiyaForm
from django.db.models import Max
import random
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import BhagyankPrediction,TarotCardPrediction,CardPrediction,MoolankPrediction,NumerologyHistory
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import PhoneNumberForm
from django.contrib import messages
# Create your views here.
@login_required(login_url='astroapp:signin')
def home(request):
    return render(request,'astro_app/index.html')

# def numerology(request):
#     if request.method == 'POST':
#         form = NumerologyForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the form data to the database
#             return redirect('astroapp:calculate_moolank')  # Change to the appropriate URL

#     else:
#         form = NumerologyForm()
#         return render(request, 'astro_app/numerology_template.html', {'form': form})
def numerology_prediction(request):

    return render(request,'astro_app/numerology_prediction.html')
def tarot_prdediction(request):
    return render(request,'astro_app/tarot_predict.html')
def get_tarot(request):
    return render (request,'astro_app/tarot.html')
def calculate_balance_number(request):
    if request.method == 'POST':
        form = ChacterForm(request.POST)
        if form.is_valid():
            ch = form.cleaned_data.get('ch')
            mappings = {
                'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
                'I': 9, 'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7,
                'Q': 8, 'R': 9, 'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6,
                'Y': 7, 'Z': 8
            }
            if len(ch) != 1 or not ch.isalpha():
                error_message = 'Invalid input'
            else:
                ch = ch.upper()
                if ch not in mappings:
                    error_message = 'Character not found in mappings'
                else:
                    balance_number = mappings[ch]
                    return render(request, 'astro_app/balance_result.html', {'ch': ch, 'balance_number': balance_number})
        else:
            error_message = 'Form is not valid'
        return render(request, 'astro_app/calculate_balance.html', {'form': form, 'error_message': error_message})
    else:
        form = ChacterForm(None)
    
    return render(request, 'astro_app/calculate_balance.html', {'form': form})


    

   

   



def dreamNumber1(request):
    if request.method == 'POST':
        form = ValueForm(request.POST)
        if form.is_valid():
            namelist = form.cleaned_data.get('namelist')
            hn = 0
            vowels = ['A', 'E', 'I', 'O', 'U']
            consonants = {
                'J': 1, 'Q': 1, 'Y': 1,
                'B': 2, 'K': 2, 'R': 2,
                'C': 3, 'G': 3, 'L': 3, 'S': 3,
                'D': 4, 'M': 4, 'T': 4,
                'H': 5, 'N': 5, 'X': 5,
                'V': 6, 'W': 6,
                'Z': 7
            }
            for ch in namelist:
                if ch.upper() in vowels:
                    continue
                hn += consonants.get(ch.upper(), 8)
            
            if hn == 11 or hn == 22:
                result = hn
            else:
                num1 = hn % 10
                num2 = hn // 10
                hn = num1 + num2
                result = hn
            
            return render(request, 'astro_app/result.html', {'result': result})
    else:
        form = ValueForm(None)
        
    return render(request, 'astro_app/result_form.html', {'form': form})



    
    

# def dreamNumber(request, nameList):
#     hn = 0
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     consonants = {
#         'J': 1, 'Q': 1, 'Y': 1,
#         'B': 2, 'K': 2, 'R': 2,
#         'C': 3, 'G': 3, 'L': 3, 'S': 3,
#         'D': 4, 'M': 4, 'T': 4,
#         'H': 5, 'N': 5, 'X': 5,
#         'V': 6, 'W': 6,
#         'Z': 7
#     }
    
#     for ch in nameList:
#         if ch in vowels:
#             continue
#         hn += consonants.get(ch, 8)
    
#     if hn == 11 or hn == 22:
#         return HttpResponse(hn)
    
#     num1 = hn % 10
#     num2 = hn // 10
#     hn = num1 + num2
#     return HttpResponse(hn)

def getsoulNumber(request):
    if request.method=='POST':
        form=ValueForm(request.POST)
        if form.is_valid():
            namelist=form.cleaned_data.get('namelist')
            sn =0
            for ch in namelist:
                if (ch == 'A' or ch == 'I'):
                    sn += 1
                if (ch == 'E'):
                    sn += 5
                if (ch == 'U'):
                    sn += 6
                if (ch == 'O'):
                    sn += 7
                if(sn == 11 or sn ==22):
                    result=sn
                num1 = sn % 10
                num2 = (int( sn/10))
                sn = num1+num2
                result=sn
                return render(request, 'astro_app/result1.html', {'result': result})
    
    else:
        form = ValueForm(None)
        
    return render(request, 'astro_app/result_form1.html', {'form': form})


def get_destiny_number(request):
    if request.method=='POST':
        form=ValueForm(request.POST)
        if form.is_valid():
            namelist=form.cleaned_data.get('namelist')
            dn =0
            for ch in namelist:
                if( ch == 'A' or ch == 'I' or ch == 'J' or ch == 'Q' or ch == 'Y'):
                    dn += 1
                elif(ch == 'B' or ch == 'K' or ch == 'R'):
                    dn +=2
                elif( ch == 'C' or ch == 'G' or ch == 'L' or ch == 'S'):
                    dn += 3
                elif( ch == 'D' or ch == 'M' or ch == 'T'):
                    dn += 4
                elif( ch == 'E' or ch == 'H' or ch == 'N' or ch == 'X'):
                    dn += 5
                elif( ch == 'U' or ch == 'V' or ch == 'W'):
                    dn += 6
                elif( ch == 'O' or ch == 'Z'):
                    dn += 7
                else:
                    dn+=8
            if(dn == 11 or dn ==22):
                result=dn
            num1 = dn%10
            num2 = (int( dn/10))
            dn = num1+num2
            result=dn
        return render(request, 'astro_app/destinyresult.html', {'result': result})

    else:
        form = ValueForm()
        return render(request, 'astro_app/destiny_result.html', {'form': form})

     
    
   
    



# def reduce_to_single_digit(request):
#     if request.method=='POST':
#         form=NumberForm(request.POST)
#         if form.is_valid():
#             number=form.cleaned_data.get('number')
#             while number > 9:
#                 number = sum(int(digit) for digit in str(number))
#             return render(request,'astro_app/number.html',{'number':number})
#     else:
#         form = NumberForm()
#         return render(request, 'astro_app/number_display.html', {'form': form})       
    
      

# def get_bhagyank_prediction(request):
#     if request.method=='POST':
#         form=BhagyankPredictionForm(request.POST)
#         if form.is_valid():
#             bhagyank=form.cleaned_data.get('bhagyank')
#             lang=form.cleaned_data.get('lang')
#             if lang=="eng":
#                 lang_col="Bhagyank_prediction_eng"
#             else:
#                 lang_col="Bhagyank_prediction_hin"
#             prediction=BhagyankPrediction.objects.filter(Bhagyank=bhagyank).values(lang_col).first()
#             if prediction:
#                 prediction_text=prediction[lang_col]
#             else:
#                 prediction_text="prediction not found"
#             return render(request, 'astro_app/bhagyank_prediction_result.html', {'prediction': prediction_text})
#     else:
#         form=BhagyankPredictionForm()
#         return render(request,'astro_app/bhagyank_prediction_form.html',{'form':form})   










   



def getDreamNumber(request,nameList):

    hn =0
    for ch in nameList:
        if(ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
            print("")
        else:
            if( ch == 'J' or ch == 'S'):
                hn += 1
            elif( ch == 'B' or ch == 'K' or ch == 'T'):
                hn +=2
            elif( ch == 'C' or ch == 'L'):
                hn += 3
            elif( ch == 'D' or ch == 'M' or ch == 'V'):
                hn += 4
            elif( ch == 'N' or ch == 'W'):
                hn += 5
            elif( ch == 'F' or ch == 'X'):
                hn += 6
            elif( ch == 'G' or ch == 'P' or ch == 'Y'):
                hn += 7
            elif( ch == 'H' or ch == 'Q' or ch == 'Z'):
                hn += 8
            else:
                hn+=8
    if(hn == 11 or hn ==22):
        return HttpResponse(hn)
    num1 = hn%10
    num2 = (int( hn/10))
    hn = num1+num2
    return HttpResponse(hn)


def soulNumber(request,nameList):
    sn =0
    for ch in nameList:
        if (ch == 'A' or ch == 'I'):
            sn += 1
        if (ch == 'E'):
            sn += 5
        if (ch == 'U'):
            sn += 6
        if (ch == 'O'):
            sn += 7
    if(sn == 11 or sn ==22):
        return HttpResponse(sn)
    num1 = sn%10
    num2 = (int( sn/10))
    sn = num1+num2
    return HttpResponse(sn)



def getDestinyNumber(nameList):

    dn =0
    for ch in nameList:
        if( ch == 'A' or ch == 'J' or ch == 'S'):
            dn += 1
        elif(ch == 'B' or ch == 'K' or ch == 'T'):
            dn +=2
        elif( ch == 'C' or ch == 'L' or ch == 'U'):
            dn += 3
        elif( ch == 'D' or ch == 'M' or ch == 'V'):
            dn += 4
        elif( ch == 'E' or ch == 'N' or ch == 'W'):
            dn += 5
        elif( ch == 'F' or ch == 'O' or ch == 'X'):
            dn += 6
        elif( ch == 'G' or ch == 'P' or ch == 'Y'):
            dn += 7
        elif( ch == 'H' or ch == 'Q' or ch == 'Z'):
            dn += 8
        else:
            dn+=9
    if(dn == 11 or dn ==22):
        return HttpResponse(dn)
    num1 = dn%10
    num2 = int( dn/10)
    dn = num1+num2
    return HttpResponse(dn)




# def get_card_name(request):
#     if request.method=='POST':
#         form=NumberForm(request.POST)
#         if form.is_valid():
#             rand_num=form.cleaned_data.get('number')
#             try:
#                 card = get_object_or_404(TarotCardPrediction,card_num=rand_num)
#                 card_name = card.card_name
#                 return render(request,'astro_app/card_name_result.html',{'card_name':card_name})
    
#             except TarotCardPrediction.DoesNotExist:
#                 card_name = "Card not found"
#                 return render(request,'astro_app/card_name_result.html',{'card_name':card_name})
#     else:
#         form=NumberForm()
#         return render(request,'astro_app/card_name.html',{'form':form})
# def get_card_image(request):
#     max_card_num = TarotCardPrediction.objects.aggregate(max_card=Max('card_num'))['max_card']
#     rand_num = random.randint(1, max_card_num)

#     try:
#         card = TarotCardPrediction.objects.get(card_num=rand_num)
#         card_image = card.card_image
#     except TarotCardPrediction.DoesNotExist:
#         card_image = None

#     return render(request, 'astro_app/card_image.html', {'card_image': card_image})



# def get_card_prediction(request):
#     prediction=None
#     if request.method=='POST':
#         form=CardPredictionForm(request.POST)
#         if form.is_valid():
#             rand_num=form.cleaned_data.get('rand_num')
#             bin_num=int(form.cleaned_data.get('bin_num'))
#             lang=form.cleaned_data.get('lang')
#             card_prediction = get_object_or_404(CardPrediction, Card_Num=rand_num)
#             if bin_num == 0:
#                 prediction_col = f"Prediction_Down_{lang}"
#             else:
#                 prediction_col = f"Prediction_Up_{lang}"
#                 prediction = getattr(card_prediction, prediction_col, "No prediction available")
#                 return render(request, 'astro_app/prediction_result_template.html', {'prediction': prediction})
#     else:
#         form=CardPredictionForm()
#         return render(request, 'astro_app/prediction_template.html', {'form': form})


# def get_properties(request):
#     properties=[]
#     if request.method=='POST':
#         form=NumberForm(request.POST)
#         if form.is_valid():
#             rand_num=form.cleaned_data.get('number')
#             if 0 <= rand_num <= 21:
#                 properties= [
#                     "Major Events",
#                     "Universal Human Experiences like:",
#                     "Challenging Authorities",
#                     "Fall in love",
#                     "Unexpected bad news"
            
#                        ]
#             elif 22 <= rand_num <= 31:
#                 properties= [
#             "Minor Events",
#             "Emotions & Relationship",
#             "Represent Water Element",
#             "90% positive"
#                        ]
#             elif rand_num == 33:
#                 properties= [
#             "Minor Events",
#             "Emotions & Relationship",
#             "Represent Water Element",
#             "90% positive",
#             "Immaturity",
#             "Energetic",
#             "Youth",
#             "Indecisive"
#                        ]
#             elif rand_num == 34:
#                 properties= [
#             "Minor Events",
#             "Emotions & Relationship",
#             "Represent Water Element",
#             "90% positive",
#             "Maturity",
#             "Discipline",
#             "Decision Making"
#                        ]
#             elif rand_num == 35:
#                 properties= [
#             "Minor Events",
#             "Emotions & Relationship",
#             "Represent Water Element",
#             "90% positive",
#             "Emotions",
#             "Indecisive",
#             "Power to Influence Decision"
#                        ]
#             elif rand_num == 36:
#                 properties= [
#             "Minor Events",
#             "Emotions & Relationship",
#             "Represent Water Element",
#             "90% positive",
#             "Authority",
#             "Decision Making"
#                        ]
#             elif 37 <= rand_num <= 46:
#                 properties= [
#             "Minor Events",
#             "Thoughts",
#             "Represent Air Element",
#             "90% negative"
#                        ]
#             elif rand_num == 47:
#                 properties= [
#             "Minor Events",
#             "Thoughts",
#             "Represent Air Element",
#             "90% negative",
#             "Immaturity",
#             "Energetic",
#             "Youth",
#             "Indecisive"
#                        ]
#             else:
#                 properties= ["Unknown Property"]
#         return render(request, 'astro_app/property.html', {'properties': properties})

#     else:
#         form=NumberForm()
#         return render(request, 'astro_app/property_template.html', {'form': form})
 
    


   



class signup(View):
    def get(self,request):
        f=Registerform(None)
        return render(request,'astro_app/signup.html',{"data":f})
    def post(self,request):
        f=Registerform(request.POST)
        if f.is_valid():
            data=f.save(commit=False)
            p=f.cleaned_data.get('password')
            data.set_password(p)
            data.save()
            return redirect('astroapp:signin')
        return render(request,'astro_app/signup.html',{"data":f})
    
class signin(View):
    def get(self, request):
        f = logform(None)
        return render(request, "astro_app/login.html", {'data': f})

    def post(self, request):
        f = logform(request.POST)
        if f.is_valid():
            e = f.cleaned_data.get('email')
            p = f.cleaned_data.get('password')

            user = authenticate(request,email=e, password=p)
            nxt = request.GET.get('next')
            print(nxt)
            if user:
                login(request, user)
                if nxt:
                    return redirect(nxt)
                return redirect('astroapp:home')  # Redirect on successful login

        # If form is invalid or authentication fails, return to the login page with errors
        return render(request, "astro_app/login.html", {'data': f})
def signout(request):
    logout(request)
    return redirect('astroapp:signin')
    

def reduce_to_single_digit1(number):
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    return number

def calculate_challenge_number(request):
    if request.method == 'POST':
        form = BirthDateForm(request.POST)
        if form.is_valid():
            birth_date = form.cleaned_data['birth_date']
            birth_date_str = birth_date.strftime('%Y%m%d')
            birth_date_digits = [int(digit) for digit in birth_date_str]
            
            life_path_number = reduce_to_single_digit1(sum(birth_date_digits))

            first_challenge = reduce_to_single_digit1(life_path_number + 1)
            second_challenge = reduce_to_single_digit1(life_path_number + 2)
            third_challenge = reduce_to_single_digit1(life_path_number + 3)
            fourth_challenge = reduce_to_single_digit1(life_path_number + 4)

            challenges = {
                "first_challenge": first_challenge,
                "second_challenge": second_challenge,
                "third_challenge": third_challenge,
                "fourth_challenge": fourth_challenge,
            }
            return render(request, 'astro_app/challenges_result.html', {'challenges': challenges})
    else:
        form = BirthDateForm()

    return render(request, 'astro_app/calculate_challenges.html', {'form': form})


def get_numerology_number(name):
    
    numerology_map = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
    }

    name = name.upper()
    total = 0

    for letter in name:
        if letter in numerology_map:
            total += numerology_map[letter]

    while total > 9:
        total = sum(int(digit) for digit in str(total))
    return total    



def calculate_maturity_number(request):
    form = MaturityNumberForm()

    if request.method == 'POST':
        form = MaturityNumberForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']

            day = dob.day
            month = dob.month
            year = dob.year

            life_path_number = sum(int(digit) for digit in str(day + month + year))

            while life_path_number > 9:
                life_path_number = sum(int(digit) for digit in str(life_path_number))

            name = name.replace(" ", "")
            expression_number = get_numerology_number(name)

            maturity_number = life_path_number + expression_number

            while maturity_number > 9:
                maturity_number = sum(int(digit) for digit in str(maturity_number))

            return render(request, 'astro_app/maturity_number_result.html', { 'maturity_number': maturity_number})

    return render(request, 'astro_app/maturity_number.html', {'form': form})

def calculate_single_digit(num):
    print(f"Calculating for {num}")
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num

def karmic_number_view(request):
    karmic_number = None

    if request.method == 'POST':
        form = KarmicNumberForm(request.POST)
        if form.is_valid():
            date_str = form.cleaned_data['date_str']
            
            year, month, day = map(int, date_str.split('-'))
            
            if day <= 0 or month <= 0 or month > 12 or year <= 0:
                karmic_number = "Invalid Date"
            else:
                karmic_number = calculate_single_digit(day + month + year)
    else:
        form = KarmicNumberForm()
    
    return render(request, 'astro_app/karmic_number.html', {'form': form, 'karmic_number': karmic_number})

def calculate_balance_number(character):
    mappings = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
        'I': 9, 'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7,
        'Q': 8, 'R': 9, 'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6,
        'Y': 7, 'Z': 8
    }

    character = character.upper()
    if len(character) != 1 or not character.isalpha():
        return 'Invalid input'
    elif character not in mappings:
        return 'Character not found in mappings'
    else:
        balance_number = mappings[character]
        return balance_number
def calculate_balance_for_name(name):
    name = name.upper()
    name_list = name.split()
    number_list = [calculate_balance_number(part_name[0]) for part_name in name_list]
    
    balance_number = sum(number_list)
    if balance_number > 9:
        first_digit = balance_number % 10
        second_digit = int(balance_number / 10)
        balance_number = first_digit + second_digit
    
    return balance_number


def balance_number_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            balance_number = calculate_balance_for_name(name)
            return render(request, 'astro_app/balance_number_result.html', {'name': name, 'balance_number': balance_number})
    else:
        form = NameForm()
    
    return render(request, 'astro_app/balance_number_form.html', {'form': form})

def calculate_pinnacle_numbers(year, month, day):
    first_pinnacle = calculate_single_digit(day + month)
    second_pinnacle = calculate_single_digit(day + year)
    third_pinnacle = calculate_single_digit(first_pinnacle + second_pinnacle)
    fourth_pinnacle = calculate_single_digit(month + year)

    data = {
        "first_pinnacle": first_pinnacle,
        "second_pinnacle": second_pinnacle,
        "third_pinnacle": third_pinnacle,
        "fourth_pinnacle": fourth_pinnacle,
    }
    return data

def pinnacle_number_view(request):
    if request.method == 'POST':
        form=DateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            if date:
                year = date.year
                month = date.month
                day = date.day
                pinnacle_data = calculate_pinnacle_numbers(year, month, day)
                print(pinnacle_data)
                return render(request, 'astro_app/pinnacle_number_result.html', {'pinnacle_data':pinnacle_data})
            else:
                error_message = 'Invalid input'
                return render(request, 'astro_app/pinnacle_number_form.html',{'error_message':error_message})
                
    else:
        form=DateForm()
        return render(request, 'astro_app/pinnacle_number_form.html',{'form':form})
    


def find_loshugrid(date):
    day, month, year = map(int, date.split('-'))

    num = []
    dayList = list(map(int, str(day)))
    monthList = list(map(int, str(month)))
    yearList = list(map(int, str(year)))

    num.extend(dayList)
    num.extend(monthList)
    num.extend(yearList)

    freq = {}
    for item in num:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    for f in range(10):
        if f not in freq:
            freq[f] = 0

    if 0 in freq:
        del freq[0]

    return freq


def loshugrid_view(request):
    freq = None

    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            freq = find_loshugrid(date.strftime('%Y-%m-%d'))
            return render(request, 'astro_app/loshugrid_view_result.html',{'freq': freq})

    else:
        form = DateForm()
        return render(request, 'astro_app/loshugrid_view.html', {'form': form})



def calculate_destiny_number(namelist):
    dn = 0
    for ch in namelist:
        if ch in ['A', 'I', 'J', 'Q', 'Y']:
            dn += 1
        elif ch in ['B', 'K', 'R']:
            dn += 2
        elif ch in ['C', 'G', 'L', 'S']:
            dn += 3
        elif ch in ['D', 'M', 'T']:
            dn += 4
        elif ch in ['E', 'H', 'N', 'X']:
            dn += 5
        elif ch in ['U', 'V', 'W']:
            dn += 6
        elif ch in ['O', 'Z']:
            dn += 7
        else:
            dn += 8
    
    if dn in [11, 22]:
        return dn
    
    num1 = dn % 10
    num2 = int(dn / 10)
    dn = num1 + num2
    return dn

def calculate_soul_number(namelist):
    sn = 0
    for ch in namelist:
        if ch in ['A', 'I']:
            sn += 1
        if ch == 'E':
            sn += 5
        if ch == 'U':
            sn += 6
        if ch == 'O':
            sn += 7
            
    if sn in [11, 22]:
        return sn
    
    num1 = sn % 10
    num2 = int(sn / 10)
    sn = num1 + num2
    return sn


def calculate_dream_number(namelist):
    hn = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = {
        'J': 1, 'Q': 1, 'Y': 1,
        'B': 2, 'K': 2, 'R': 2,
        'C': 3, 'G': 3, 'L': 3, 'S': 3,
        'D': 4, 'M': 4, 'T': 4,
        'H': 5, 'N': 5, 'X': 5,
        'V': 6, 'W': 6,
        'Z': 7
    }
    for ch in namelist:
        if ch.upper() in vowels:
            continue
        hn += consonants.get(ch.upper(), 8)
        
    if hn == 11 or hn == 22:
        result = hn
    else:
        num1 = hn % 10
        num2 = hn // 10
        hn = num1 + num2
        result = hn
        
    return result


def find_pythagorean_numerology(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = name.upper().replace(" ", "")
            name_list = [x for x in name]
            destiny_number =calculate_destiny_number(name_list)
            soul_number = calculate_soul_number(name_list)
            dream_number =calculate_dream_number(name_list)

            data = {
                "destiny_number": destiny_number,
                "soul_number": soul_number,
                "dream_number": dream_number
            }
            return render(request, 'astro_app/calculate.html', {'data':data})
    else:
        form = NameForm()

    return render(request, 'astro_app/form12.html', {'form': form})

def getDreamNumber(name_list):
    hn = 0
    for ch in name_list:
        if ch in ['A', 'E', 'I', 'O', 'U']:
            pass
        else:
            if ch in ['J', 'Q', 'Y']:
                hn += 1
            elif ch in ['B', 'K', 'R']:
                hn += 2
            elif ch in ['C', 'G', 'L', 'S']:
                hn += 3
            elif ch in ['D', 'M', 'T']:
                hn += 4
            elif ch in ['H', 'N', 'X']:
                hn += 5
            elif ch in ['V', 'W']:
                hn += 6
            elif ch == 'Z':
                hn += 7
            else:
                hn += 8
    
    if hn == 11 or hn == 22:
        return hn
    
    num1 = hn % 10
    num2 = int(hn / 10)
    hn = num1 + num2
    return hn


def getSoulNumber(name_list):
    sn =0
    for ch in name_list:
        if (ch == 'A' or ch == 'I'):
            sn += 1
        if (ch == 'E'):
            sn += 5
        if (ch == 'U'):
            sn += 6
        if (ch == 'O'):
            sn += 7
    if(sn == 11 or sn ==22):
        return sn
    num1 = sn%10
    num2 = (int( sn/10))
    sn = num1+num2
    return sn



def getDestinyNumber(name_list):

    dn =0
    for ch in name_list:
        if( ch == 'A' or ch == 'I' or ch == 'J' or ch == 'Q' or ch == 'Y'):
            dn += 1
        elif(ch == 'B' or ch == 'K' or ch == 'R'):
            dn +=2
        elif( ch == 'C' or ch == 'G' or ch == 'L' or ch == 'S'):
            dn += 3
        elif( ch == 'D' or ch == 'M' or ch == 'T'):
            dn += 4
        elif( ch == 'E' or ch == 'H' or ch == 'N' or ch == 'X'):
            dn += 5
        elif( ch == 'U' or ch == 'V' or ch == 'W'):
            dn += 6
        elif( ch == 'O' or ch == 'Z'):
            dn += 7
        else:
            dn+=8
    if(dn == 11 or dn ==22):
        return dn
    num1 = dn%10
    num2 = (int( dn/10))
    dn = num1+num2
    return dn

def find_chaldean_numerology(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = name.upper().replace(" ", "")
            name_list = [x for x in name]
            destiny_number = getDestinyNumber(name_list)
            soul_number = getSoulNumber(name_list)
            dream_number = getDreamNumber(name_list)

            context = {
                "destiny_number": destiny_number,
                "soul_number": soul_number,
                "dream_number": dream_number
            }
            return render(request, 'astro_app/chaldean_result.html', context)
    else:
        form = NameForm()

    return render(request, 'astro_app/chaldean_form.html', {'form': form})




def calculate_moolank(request,date_str):
            selected_lang = request.session.get("selected_lang")
            print(selected_lang)
            try:
                year, month, day = map(int, date_str.split('-'))
                if day <= 0 or month <= 0 or month > 12 or year <= 0:
                    raise ValueError("Invalid date format")

                if day != 11 and day != 22:
                    moolank = calculate_single_digit(day)
                else:
                    moolank = day

                moolank_month = calculate_single_digit(month)
                moolank_year = calculate_single_digit(year)
                if day == 11 or day == 22:
                    moolank_t = calculate_single_digit(day)
                else:
                    moolank_t = moolank

                total = moolank_t + moolank_month + moolank_year
                if total in (11, 22, 33):
                    bhagyank = total
                else:
                    bhagyank = calculate_single_digit(moolank + moolank_month + moolank_year)

                Moolank_Prediction_eng = getMoolankPrediction(moolank, selected_lang)
                Moolank_Prediction_hin = getMoolankPrediction(moolank, selected_lang)

                Bhagyank_Prediction_eng = getBhagyankPrediction(bhagyank, selected_lang)
                Bhagyank_Prediction_hin = getBhagyankPrediction(bhagyank, selected_lang)

                context = {
                    'moolank': moolank,
                    'moolank_prediction_eng': Moolank_Prediction_eng,
                    'moolank_prediction_hin': Moolank_Prediction_hin,
                    'bhagyank': bhagyank,
                    'bhagyank_prediction_eng': Bhagyank_Prediction_eng,
                    'bhagyank_prediction_hin': Bhagyank_Prediction_hin,
                }

                # return render(request, 'astro_app/numerology_prediction.html', context)
                return render(request, 'astro_app/xyz.html', context)

            except ValueError as e:
                return render(request, 'astro_app/error.html', {'error_message': str(e)})

            except Exception as e:
                return render(request, 'astro_app/error.html', {'error_message': "Error: " + str(e)})
    




def tarot_card_view(request):
    selected_lang = request.session.get("selected_lang")
    print(selected_lang)
    rand_num = random.randint(0,78)
    bin_num = random.randint(0, 1)
    prediction_eng =get_card_prediction(rand_num, bin_num, selected_lang)
    prediction_hin =get_card_prediction(rand_num, bin_num,selected_lang)
    card_name = get_card_name(rand_num)
    card_image =get_card_image(rand_num)
    property = get_properties(rand_num)
    data = {
                'card_name': card_name,
                'card_image': card_image,
                'property': property,
                'prediction_eng': prediction_eng,
                'prediction_hin': prediction_hin,
            }
    return render(request, 'astro_app/tarot_predict.html', {'data': data})

            


@login_required(login_url='astroapp:signin')
def click_to_get_card(request):
    return render(request,'astro_app/click_to_get_card.html')



@login_required(login_url='astroapp:signin')
def test_numerology(request):
    form = NumerologyForm(request.POST or None)
    if request.method == 'POST':
        # form = NumerologyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Name']
            gender = form.cleaned_data['Gender']
            dob = form.cleaned_data['DOB']
            tob = form.cleaned_data['TOB']
            pob = form.cleaned_data['POB']
            form.save()
            dob_str = str(dob)
            return redirect('astroapp:calculate_moolank',date_str=dob_str)  # Change this to the actual URL name
    else:
        form = NumerologyForm()
        return render(request, 'astro_app/numerology_template.html', {'form': form})

def set_language(request):
    if request.method == "POST":
        lang = request.POST.get("lang",'hin')  # Default to Hindi if not provided
        request.session["selected_lang"] = lang
        activate(lang)
        next_url = request.POST.get("next", "/")  # Default to the home page if not provided
        return HttpResponseRedirect(next_url)
def xyz(request):
    return render(request,'astro_app/xyz.html')

url = "https://json.freeastrologyapi.com/planets"
url1 = "https://json.freeastrologyapi.com/navamsa-chart-info"

def make_api_request_with_retry(url, payload, headers, max_retries=3, retry_delay=5):
    for _ in range(max_retries):
        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {str(e)}")
            time.sleep(retry_delay)
    
    # If all retry attempts fail, return None
    return None

@login_required(login_url='astroapp:signin')
def kundli(request):
    if request.method == 'POST':
        form = NumerologyForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            gender = form.cleaned_data['Gender']
            date = form.cleaned_data['DOB']
            time = form.cleaned_data['TOB']
            place = form.cleaned_data['POB']
            latitude_Str= request.POST.get('latitude')
            longitude_str= request.POST.get('longitude')
            latitude=float(latitude_Str)
            longitude=float(longitude_str)
            day = date.day
            month = date.month
            year = date.year
            hours = time.hour
            minutes = time.minute
            kundli_data = KundliData(
                name=Name,
                gender=gender,
                date=date,
                time=time,
                place=place,
                latitude=latitude,
                longitude=longitude,
                # Add other fields as needed
            )
            kundli_data.save()

            payload = json.dumps({
                "year": year,
                "month": month,
                "date": day,
                "hours": hours,
                "minutes": minutes,
                "seconds": 0,
                "latitude": latitude,
                "longitude": longitude,
                "timezone": 5.5,
                "settings": {
                    "observation_point": "geocentric",
                    "ayanamsha": "lahiri"
                }
            })

            headers = {
                'Content-Type': 'application/json',
                'x-api-key': 'eEeX9Ldpxp28yUaNs4mk313CSGFEg7EO8uf5DViu'
            }
           
            # Use the make_api_request_with_retry function to make API requests
            response = make_api_request_with_retry(url, payload, headers)
            if response is not None:
                data = response.json()
                desired_data = {str(i): data["output"][0][str(i)] for i in range(13)}
                data = json.dumps(desired_data)

                navmasa_response = make_api_request_with_retry(url1, payload, headers)
                if navmasa_response is not None:
                    data2 = navmasa_response.json()
                    desired_data1 = {str(i): data2["output"].get(str(i), None) for i in range(13)}
                    data2 = json.dumps(desired_data1)

                    numbers = [2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 16, 20, 24, 27, 30, 40, 45, 60]
                    additional_data = {}
                    for num in numbers:
                        url_i = f"https://json.freeastrologyapi.com/d{num}-chart-info"
                        response_i = make_api_request_with_retry(url_i, payload, headers)
                        if response_i is not None:
                            data_i = response_i.json()
                            desired_data1 = {str(i): data_i["output"].get(str(i), None) for i in range(13)}
                            data_i = json.dumps(desired_data1)
                            additional_data[num] = data_i

                    context = {
                        'data_for_num1': additional_data.get(2),
                        'data_for_num2': additional_data.get(3),
                        'data_for_num3': additional_data.get(4),
                        'data_for_num4': additional_data.get(5),
                        'data_for_num5': additional_data.get(6),
                        'data_for_num6': additional_data.get(7),
                        'data_for_num7': additional_data.get(8),
                        'data_for_num8': additional_data.get(10),
                        'data_for_num9': additional_data.get(11),
                        'data_for_num10': additional_data.get(12),
                        'data_for_num11': additional_data.get(16),
                        'data_for_num12': additional_data.get(20),
                        'data_for_num13': additional_data.get(24),
                        'data_for_num14': additional_data.get(27),
                        'data_for_num15': additional_data.get(30),
                        'data_for_num16': additional_data.get(40),
                        'data_for_num17': additional_data.get(45),
                        'data_for_num18': additional_data.get(60),
                        'data': data,
                        'data2': data2
                    }
                    return render(request, 'astro_app/Kundlitable.html', context)

    else:
        form = NumerologyForm()

    return render(request, 'astro_app/test.html', {'form': form})

#     newApiResponse = request.GET.get('newApiResponse', '') 
#     print(newApiResponse)
#     return render(request, 'astro_app/new_svg.html', {'newApiResponse': newApiResponse})

class GetHistoryDataView(View):

    def get(self, request, *args, **kwargs):
        # Fetch Kundli history data for the logged-in user
        history_data = KundliData.objects.all()
        
        # Convert history_data to a JSON-compatible format
        serialized_data = [
            {
                'name': item.name,
                'gender': item.gender,
                'date_of_birth': item.date,
                'time_of_birth': item.time,
                'place_of_birth': item.place,
                'latitude': item.latitude,
                'longitude': item.longitude
            } for item in history_data
        ]
        
        return JsonResponse({'history_data': serialized_data})
    

url = "https://json.freeastrologyapi.com/planets"
url1 = "https://json.freeastrologyapi.com/navamsa-chart-info"

def make_api_request_with_retry(url, payload, headers, max_retries=3, retry_delay=5):
    for _ in range(max_retries):
        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {str(e)}")
            time.sleep(retry_delay)

def show_kundli(request):
    try:
        date_str = request.GET.get('date_of_birth')
        time_str = request.GET.get('time_of_birth')
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')

        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        time = datetime.strptime(time_str, '%H:%M:%S').time()

        day = date.day
        month = date.month
        year = date.year
        hours = time.hour
        minutes = time.minute
        payload = {
            "year": year,
            "month": month,
            "date": day,
            "hours": hours,
            "minutes": minutes,
            "seconds": 0,
            "latitude": float(latitude),
            "longitude": float(longitude),
            "timezone": 5.5,
            "settings": {
                "observation_point": "geocentric",
                "ayanamsha": "lahiri"
            }
        }

        headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'eEeX9Ldpxp28yUaNs4mk313CSGFEg7EO8uf5DViu'
        }

        response = make_api_request_with_retry(url, json.dumps(payload), headers)
        if response is not None:
            data = response.json()
            desired_data = {str(i): data["output"][0][str(i)] for i in range(13)}
            data = json.dumps(desired_data)

            navmasa_response = make_api_request_with_retry(url1, json.dumps(payload), headers)
            if navmasa_response is not None:
                data2 = navmasa_response.json()
                desired_data1 = {str(i): data2["output"].get(str(i), None) for i in range(13)}
                data2 = json.dumps(desired_data1)

                numbers = [2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 16, 20, 24, 27, 30, 40, 45, 60]
                additional_data = {}
                for num in numbers:
                    url_i = f"https://json.freeastrologyapi.com/d{num}-chart-info"
                    response_i = make_api_request_with_retry(url_i, json.dumps(payload), headers)
                    if response_i is not None:
                        data_i = response_i.json()
                        desired_data1 = {str(i): data_i["output"].get(str(i), None) for i in range(13)}
                        data_i = json.dumps(desired_data1)
                        additional_data[num] = data_i

                context = {
                    'data_for_num1': additional_data.get(2),
                    'data_for_num2': additional_data.get(3),
                    'data_for_num3': additional_data.get(4),
                    'data_for_num4': additional_data.get(5),
                    'data_for_num5': additional_data.get(6),
                    'data_for_num6': additional_data.get(7),
                    'data_for_num7': additional_data.get(8),
                    'data_for_num8': additional_data.get(10),
                    'data_for_num9': additional_data.get(11),
                    'data_for_num10': additional_data.get(12),
                    'data_for_num11': additional_data.get(16),
                    'data_for_num12': additional_data.get(20),
                    'data_for_num13': additional_data.get(24),
                    'data_for_num14': additional_data.get(27),
                    'data_for_num15': additional_data.get(30),
                    'data_for_num16': additional_data.get(40),
                    'data_for_num17': additional_data.get(45),
                    'data_for_num18': additional_data.get(60),
                    'data': data,
                    'data2': data2
                }
                return render(request, 'astro_app/Kundlitable.html', context)

        else:
            print("Error processing the API request.")
            return HttpResponseServerError("Error processing the API request.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return HttpResponseServerError(f"An error occurred: {str(e)}")




def get_sunrise_sunset(latitude, longitude, current_date, timezone='UTC', date='today'):
    url = f'https://api.sunrisesunset.io/json?lat={latitude}&lng={longitude}&timezone={timezone}&date={date}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        sunrise_time = datetime.strptime(data['results']['sunrise'], '%I:%M:%S %p').time()
        sunset_time = datetime.strptime(data['results']['sunset'], '%I:%M:%S %p').time()

        current_date_object = datetime.strptime(current_date, '%Y-%m-%d').date()

        sunrise_datetime = datetime.combine(current_date_object, sunrise_time)
        sunset_datetime = datetime.combine(current_date_object, sunset_time)

        return sunrise_datetime, sunset_datetime
    else:
        print(f"Error: {response.status_code}")
        return None, None


@login_required(login_url='astroapp:signin')

def choghadiya(request):
    if request.method == 'POST':
        date = request.POST.get('selectedDateOption')
        current_date = request.POST.get('currentDate')
        current_time = request.POST.get('currentTime')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        now=datetime.now()
        Today= now.weekday()+1
        Tomorrow = (Today + 1) % 7
        day = Today if date == 'today' else Tomorrow
        print(Today)
        print(Tomorrow)
        sunrise, sunset = get_sunrise_sunset(latitude, longitude,current_date,current_time,date)
        print(sunrise,sunset)
        duration_day = sunset - sunrise
        each_chaughadiya_duration_day = duration_day / 8

        choghadiya_names_day = {
            0: ["Udveg", "Char", "Labh", "Amrit", "Kaal","Shubh", "Rog","Udveg"],
            1: ["Amrit", "Kaal", "Shubh", "Rog", "Udveg", "Char","Labh", "Amrit"],
            2: ["Rog", "Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog"],
            3: ["Labh", "Amrit", "Kaal", "Shubh", "Rog", "Udveg", "Char", "Labh"],
            4: ["Shubh", "Rog", "Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh"],
            5: ["Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog", "Udveg", "Char"],
            6: [ "Kaal", "Shubh", "Rog", "Udveg", "Char","Labh", "Amrit","Kaal"],
        
            # Add mappings for other days as needed
        }

        # Get Choghadiya names based on the current day
        choghadiya_names_for_today = choghadiya_names_day.get(day)
        
        # Calculate choghadiya timings for the day
        choghadiya_timings_day = []
        for i, choghadiya_name in enumerate(choghadiya_names_for_today):
            start_time = sunrise + i * each_chaughadiya_duration_day
            end_time = start_time + each_chaughadiya_duration_day

            choghadiya_timings_day.append({
                "name": f"{choghadiya_name} (Day Choghadiya {i + 1})",
                "start_time": start_time.strftime("%I:%M %p"),
                "end_time": end_time.strftime("%I:%M %p")
            })

        # Calculate choghadiya duration for the night (assuming it starts after sunset)
        duration_night = timedelta(hours=24) - duration_day
        each_chaughadiya_duration_night = duration_night / 8

        # Map day of the week to Choghadiya names for the night
        choghadiya_names_night = {
            0: [ "Shubh", "Amrit", "Char","Rog", "Kaal","Labh", "Udveg","Shubh"],
            1: ["Char","Rog", "Kaal","Labh", "Udveg","Shubh", "Amrit", "Char"],
            2: ["Kaal", "Labh", "Udveg", "Shubh", "Amrit", "Char","Rog", "Kaal"],
            3: ["Udveg", "Shubh", "Amrit", "Char", "Rog", "Kaal",  "Labh", "Udveg"],
            4: ["Amrit", "Char", "Rog", "Kaal", "Labh", "Udveg", "Shubh", "Amrit"],
            5: ["Rog", "Kaal", "Labh", "Udveg", "Shubh", "Amrit", "Char", "Rog"],
            6: [ "Labh", "Udveg", "Shubh", "Amrit", "Char","Rog", "Kaal", "Labh"],
        
        }

        # Get Choghadiya names based on the current day
        choghadiya_names_current_night = choghadiya_names_night.get(day)
        
        # Calculate choghadiya timings for the night
        choghadiya_timings_night = []
        for i, choghadiya_name in enumerate(choghadiya_names_current_night):
            start_time = sunset + i * each_chaughadiya_duration_night
            end_time = start_time + each_chaughadiya_duration_night

            choghadiya_timings_night.append({
                "name": f"{choghadiya_name} (Night Choghadiya {i + 1})",
                "start_time": start_time.strftime("%I:%M %p"),
                "end_time": end_time.strftime("%I:%M %p")
            })
            response_data = {
            'choghadiya_timings_day': choghadiya_timings_day,
            'choghadiya_timings_night': choghadiya_timings_night,
        }
        # Render the HTML template with choghadiya details
        return JsonResponse(response_data)

    return render(request, 'astro_app/choghadiya.html')

def send_otp(phone_number):
    otp = str(random.randint(100000, 999999))
    api_url = f'https://api.textlocal.in/send/?apiKey=MzMzNzU0NGM3Mjc0NDg0ODM3NDQ2NzUwNjgzNzYxMzI=&sender=ASTCLL&numbers=91{phone_number}&message=Dear%20User%2C%20%0AYour%20OTP%20for%20login%20to%20Call-Astro%20is%20{otp}.%20Valid%20for%2030%20minutes.%20Please%20do%20not%20share%20this%20OTP.%20%0ARegards%20%0ACall-Astro%20Team%20%0AVAS%20Ventures%20Pvt.%20Ltd.'
    
    try:
        response = requests.post(api_url)
        if response.status_code == 200:
            return otp
        else:
            print(f'Failed to send OTP. API error: {response.text}')
            return None
    except requests.RequestException as e:
        print(f'Failed to send OTP. Request exception: {e}')
        return None
def register(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            user_exists = CustomUser.objects.filter(phone_number=phone_number).exists()
            if user_exists:
                otp = send_otp(phone_number)
                print(otp)
                if otp:
                    request.session['otp'] = otp
                    request.session['phone_number'] = phone_number

                    return JsonResponse({'success': True, 'message': 'OTP sent successfully'})
                else:
                    return JsonResponse({'success': False, 'message': 'Failed to send OTP. Please try again.'})
            else:
                return JsonResponse({'success': False, 'message': 'User not registered. Please sign up.'})
                
        else:
            return JsonResponse({'success': False, 'message': 'Invalid form submission. Please try again.'})
    else:
        form = PhoneNumberForm()

    return render(request, 'astro_app/registration.html', {'form': form})



def verify_otp(request):
    if request.method == 'POST':
        user_input_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        phone_number = request.session.get('phone_number')

        if user_input_otp and stored_otp and phone_number:
            if user_input_otp == stored_otp:
                try:
                    user = CustomUser.objects.get(phone_number=phone_number)
                    print(user)
                except CustomUser.DoesNotExist:
                    user = None

                if user is not None:
                    login(request, user, backend='astroapp.backends.PhoneNumberBackend')
                    request.session.pop('otp')
                    request.session.pop('phone_number')
                    return JsonResponse({'success': True, 'message': 'User authenticated successfully.'})
                else:
                    print("Authentication failed. User is None.")
                    return JsonResponse({'success': False, 'message': 'Invalid OTP. Authentication failed.'})
            else:
                print("Invalid OTP. user_input_otp:", user_input_otp, "stored_otp:", stored_otp)
                return JsonResponse({'success': False, 'message': 'Invalid OTP. Please try again.'})
        else:
            print("Incomplete data for OTP verification.")
            return JsonResponse({'success': False, 'message': 'Incomplete data for OTP verification'})
    else:
        print("Invalid request method for OTP verification.")
        return JsonResponse({'success': False, 'message': 'Invalid request method for OTP verification'})
