from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
import pickle 
import pandas as pd

@api_view(['GET'])
def getFood(request):
    daily_time_spent_on_site = request.data.get("daily_time_spent_on_site")
    age = request.data.get("age")
    area_income = request.data.get("area_income")
    daily_internet_usage = request.data.get("daily_internet_usage")
    male = request.data.get("male")
    model = pickle.load(open('ad_model.sav', 'rb'))
    
    data = [[daily_time_spent_on_site, age, area_income, daily_internet_usage, male]]
    df = pd.DataFrame(data, columns=['daily_time_spent_on_site', 'age', 'area_income', 'daily_internet_usage', 'male'])
    prediction = model.predict(df)
    return Response(prediction)