from django.shortcuts import render, HttpResponse, redirect
import requests
from django.utils import translation

def home(request):
    response=requests.get('http://127.0.0.1:5000/Objave').json()
    return render(request, "home.html", {'response':response}) 

def tekmovanja(request):
    response=requests.get('http://127.0.0.1:5000/tekmovanja').json()
    return render(request, "tekmovanja.html", {'response':response}) 

def porocila(request):
    name = request.GET.get('ironman_name')
    surname = request.GET.get('ironman_surname')
    return render(request, "porocila.html", {'name': name, 'surname': surname})

def generate_reports(request):
    if request.method == 'POST':
        ironman_name = request.POST.get('ironman_name')
        ironman_surname = request.POST.get('ironman_surname')
        report_type = request.POST.get('report_type')

        return redirect(report_type, ironman_name=ironman_name, ironman_surname=ironman_surname)

def get_runner_results(request, ironman_name, ironman_surname):
    api_url = f"http://127.0.0.1:5000/tekmovalec_run/{ironman_name}/{ironman_surname}"
    response = requests.get(api_url).json()
    return render(request, 'runners.html', {'response': response, 'runner_name': ironman_name})

def get_biker_results(request, ironman_name, ironman_surname):
    api_url = f"http://127.0.0.1:5000/tekmovalec_bike/{ironman_name}/{ironman_surname}"
    response = requests.get(api_url).json()
    return render(request, 'bikers.html', {'response': response, 'runner_name': ironman_name})

def get_swimmer_results(request, ironman_name, ironman_surname):
    api_url = f"http://127.0.0.1:5000/tekmovalec_swim/{ironman_name}/{ironman_surname}" 
    response = requests.get(api_url).json()
    return render(request, 'swimmers.html', {'response': response, 'runner_name': ironman_name})

def add_objava(request):
    title = request.POST.get('title')
    body = request.POST.get('body')
    author = request.POST.get('author')
    upvote = request.POST.get('upvote')
    downvote = request.POST.get('downvote')
    return render(request, 'add_objava.html', {'title': title, 'body': body, 'author': author, 'upvote': upvote, 'downvote': downvote})

def objava_added(request, title, body, author, upvote, downvote):
    data = {
        'title': title,
        'body': body,
        'author': author,
        'upvote': upvote,
        'downvote': downvote
    }
    api_url = "http://127.0.0.1:5000/objavapost"
    response = requests.post(api_url, json=data).json()
    return render(request, 'objava_added.html', {'response': response})
    
from django.shortcuts import redirect

def translate(request, lang_code):
    request.session['django_language'] = lang_code
    return redirect(request.META.get('HTTP_REFERER', '/'))
