from django.shortcuts import render
import pickle
from django.http import JsonResponse, HttpResponseRedirect
from phising_detection.settings import prediction_model
from detection.forms import dataForm


def predict(request):
    if request.method == "POST":
        form = dataForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["EmailData"]
            print(text)
            input_text = [text]
            pred=prediction_model.predict(input_text)
            form = dataForm()
            print(pred[0 ])
            if pred[0] == "Phishing Email":
               
                return render(request,"Phish3.html",{"form":form,"ispred":True,"pred":True})
            elif pred[0] == "Safe Email":
                
                return render(request,"Phish3.html",{"form":form,"ispred":True,"pred":False})
    else:
        form = dataForm()
        return render(request,"Phish3.html",{"form":form,"ispred":False,"pred":None})


# Create your views here.
