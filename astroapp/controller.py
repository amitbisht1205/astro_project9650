from django.urls import path
from django.views.generic import TemplateView
from .views import *
from . import views

# from .views import AddProfileNumerologyForm
app_name='astroapp'

urlpatterns=[
    path('show_kundli/', show_kundli, name='show_kundli'),
    path('get_history_data/', GetHistoryDataView.as_view(), name='get_history_data'),
    path('numerology_prediction/',views.numerology_prediction,name='numerology_prediction'),
    path('dreamnumber1/',views.dreamNumber1),
    path('calculate_balance_number/',views.calculate_balance_number),
    path('',views.home,name='home'),
    path('get_tarot/',views.get_tarot),
    path('signup/',views.signup.as_view(),name='signup'),
    path('logout',views.signout,name='logout'),
    path('signin/',views.signin.as_view(),name='signin'),
    path('signup',views.signup.as_view(),name='signup'),
    # path('tarot_prdediction/',views.tarot_prdediction,name='tarot_prdediction'),
    path('getSoulNumber/',views.getsoulNumber),
    path('calculate/',views.get_destiny_number),
    path('get_prediction/',views.getBhagyankPrediction),
    path('get_dream_number/<str:nameList>/',views.getDreamNumber),
    path('soulnumber/<str:nameList>/',views.soulNumber),
    path('card/',views.get_card_name),
    path('getimage/',views.get_card_image),
    path('card_prediction/',views.get_card_prediction),
    path('get_properties/',views.get_properties),
    path('calculate_challenge_number/',views.calculate_challenge_number),
    path('calculate_maturity_number/',views.calculate_maturity_number),
    path('karmic_number_view/',views.karmic_number_view),
    path('balance_number_view/',views.balance_number_view),
    path('pinnacle_number/',views.pinnacle_number_view),
    path('loshugrid_view/',views.loshugrid_view),
    path('find_pythagorean_numerology/',views.find_pythagorean_numerology),
    path('find_chaldean_numerology/',views.find_chaldean_numerology),
    path('calculate_moolank/<str:date_str>/',views.calculate_moolank,name='calculate_moolank'),
    path('click_to_get_card/',views.click_to_get_card,name='click_to_get_card'),
    path('test_numerology',views.test_numerology,name='test_numerology'),
    path('set_language/', views.set_language, name='set_language'),
    path('xyz',views.xyz),
    path('kundli/',views.kundli,name='kundli'),
    # path('api_view/',views.api_view),
    path('tarot_card_view/',views.tarot_card_view,name='tarot_card_view'),
    path('new_svg/', TemplateView.as_view(template_name='astro_app/new_svg.html'), name='new_svg'),
    path('choghadiya/',choghadiya,name='choghadiya'),
    path('register/', register, name='register'),
    path('verify-otp/', verify_otp, name='verify_otp'),
]