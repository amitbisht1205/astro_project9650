from .models import MoolankPrediction,BhagyankPrediction
def calculate_single_digit(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
        return num
    


def getMoolankPrediction(moolank, lang):
    try:
        prediction = MoolankPrediction.objects.get(Moolank=moolank)
        if lang == "eng":
            return prediction.Moolank_Prediction_eng
        else:
            return prediction.Moolank_Prediction_hin
    except MoolankPrediction.DoesNotExist:
        return None
def getBhagyankPrediction(bhagyank, lang):
    try:
        prediction = BhagyankPrediction.objects.get(Bhagyank=bhagyank)
        if lang == "eng":
            return prediction.Bhagyank_Prediction_eng
        else:
            return prediction.Bhagyank_Prediction_hin
    except BhagyankPrediction.DoesNotExist:
        return None    