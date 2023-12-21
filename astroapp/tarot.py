from django.shortcuts import get_object_or_404
from .models import TarotCardPrediction
def get_card_name(rand_num):
    try:
        card = get_object_or_404(TarotCardPrediction, card_num=rand_num)
        card_name = card.card_name
        return card_name
    except TarotCardPrediction.DoesNotExist:
        return "Card not found"



def get_card_image(rand_num):
    try:
        card = TarotCardPrediction.objects.get(card_num=rand_num)
        print(rand_num)
        card_image = card.card_image
    except TarotCardPrediction.DoesNotExist:
        card_image = None

    return card_image


# utils.py (or any relevant file)

def get_properties(rand_num):
    properties = []
    if 0 <= rand_num <= 21:
        properties = ["Major Events", "Universal Human Experiences like:", "Challenging Authorities", "Fall in love", "Unexpected bad news"]
    elif 22 <= rand_num <= 36:
        if 22 <= rand_num <= 31:
            properties = ["Minor Events", "Emotions & Relationship", "Represent Water Element", "90% positive"]
        elif rand_num == 33:
            properties = ["Minor Events", "Emotions & Relationship", "Represent Water Element", "90% positive", "Immaturity", "Energetic", "Youth", "Indecisive"]
        elif rand_num == 34:
            properties = ["Minor Events", "Emotions & Relationship", "Represent Water Element", "90% positive", "Maturity", "Discipline", "Decision Making"]
        elif rand_num == 35:
            properties = ["Minor Events", "Emotions & Relationship", "Represent Water Element", "90% positive", "Emotions", "Indecisive", "Power to Influence Decision"]
        elif rand_num == 36:
            properties = ["Minor Events", "Emotions & Relationship", "Represent Water Element", "90% positive", "Authority", "Decision Making"]
    elif 37 <= rand_num <= 50:
        if 37 <= rand_num <= 46:
            properties = ["Minor Events", "Thoughts", "Represent Air Element", "90% negative"]
        elif rand_num == 47:
            properties = ["Minor Events", "Thoughts", "Represent Air Element", "90% negative", "Immaturity", "Energetic", "Youth", "Indecisive"]
        elif rand_num == 48:
            properties = ["Minor Events", "Thoughts", "Represent Air Element", "90% negative", "Maturity", "Discipline", "Decision Making"]
        elif rand_num == 49:
            properties = ["Minor Events", "Thoughts", "Represent Air Element", "90% negative", "Emotions", "Indecisive", "Power to Influence Decision"]
        elif rand_num == 50:
            properties = ["Minor Events", "Thoughts", "Represent Air Element", "90% negative", "Authority", "Decision Making"]
    elif 51 <= rand_num <= 64:
        if 51 <= rand_num <= 60:
            properties = ["Minor Events", "Karma/Action", "Represent Fire Element", "50% positive"]
        elif rand_num == 61:
            properties = ["Minor Events", "Karma/Action", "Represent Fire Element", "50% positive", "Immaturity", "Energetic", "Youth", "Indecisive"]
        elif rand_num == 62:
            properties = ["Minor Events", "Karma/Action", "Represent Fire Element", "50% positive", "Maturity", "Discipline", "Decision Making"]
        elif rand_num == 63:
            properties = ["Minor Events", "Karma/Action", "Represent Fire Element", "50% positive", "Emotions", "Indecisive", "Power to Influence Decision"]
        elif rand_num == 64:
            properties = ["Minor Events", "Karma/Action", "Represent Fire Element", "50% positive", "Authority", "Decision Making"]
    else:
        if 65 <= rand_num <= 74:
            properties = ["Minor Events", "Materialistic-Money", "Represent Earth Element", "90% positive"]
        elif rand_num == 75:
            properties = ["Minor Events", "Materialistic-Money", "Represent Earth Element", "90% positive", "Immaturity", "Energetic", "Youth", "Indecisive"]
        elif rand_num == 76:
            properties = ["Minor Events", "Materialistic-Money", "Represent Earth Element", "90% positive", "Maturity", "Discipline", "Decision Making"]
        elif rand_num == 77:
            properties = ["Minor Events", "Materialistic-Money", "Represent Earth Element", "90% positive", "Emotions", "Indecisive", "Power to Influence Decision"]
        elif rand_num == 78:
            properties = ["Minor Events", "Materialistic-Money", "Represent Earth Element", "90% positive", "Authority", "Decision Making"]
    
    return properties

def get_card_prediction(rand_num, bin_num, lang):
    if bin_num == 0:
        if lang == "eng":
            prediction_col = "Prediction_Down_eng"
        else:
            prediction_col = "Prediction_Down_hin"
    elif bin_num == 1:
        if lang == "eng":
            prediction_col = "Prediction_Up_eng"
        else:
            prediction_col = "Prediction_Up_hin"
    else:
        return "Invalid bin_num value. It should be 0 or 1."

    try:
        tarot_card = TarotCardPrediction.objects.get(card_num=rand_num)
        prediction = getattr(tarot_card, prediction_col)
        return prediction
    except TarotCardPrediction.DoesNotExist:
        return "Prediction not found."
