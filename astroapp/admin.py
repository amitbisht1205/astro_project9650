from django.contrib import admin
from .models import BhagyankPrediction,TarotCardPrediction,CardPrediction,MoolankPrediction,NumerologyHistory,KundliData,OTP
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from astroapp.models import CustomUser  # Import the correct custom user model


class CardPredictionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...
class MoolankPredictionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...


class TarotCardPredictionAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    ...
class BhagyankPredictionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...


admin.site.register(CardPrediction,CardPredictionAdmin)    
admin.site.register(BhagyankPrediction,BhagyankPredictionAdmin)
admin.site.register(TarotCardPrediction,TarotCardPredictionAdmin)
admin.site.register(MoolankPrediction,MoolankPredictionAdmin)
admin.site.register(NumerologyHistory)
admin.site.register(CustomUser)
admin.site.register(KundliData)
admin.site.register(OTP)