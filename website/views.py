from django.shortcuts import render
from joblib import load
model = load('./savedModels/model.joblib')

# Create your views here.
def index(request):
    return render(request, 'Form/home.html')

def login(request):
    return render(request, 'Form/login.html')

def register(request):
    return render(request, 'Form/register.html')

def result(request):
    text = request.GET['text']
    
    result, model_output =  model.predict([text])

    return render(request, 'Form/result.html', {'result': result})