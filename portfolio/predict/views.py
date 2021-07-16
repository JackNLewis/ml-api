from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .apps import PredictConfig

# Create your views here.
def Cnn(request):
    res = PredictConfig.cnn.predict()
    dic = {"result" : res}
    return JsonResponse(dic)