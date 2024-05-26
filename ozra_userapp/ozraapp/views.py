from django.shortcuts import render, HttpResponse, redirect
import requests
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

@login_required
def home(request):
    response=requests.get('http://127.0.0.1:5000/Objave').json()
    return render(request, "home.html", {'response':response}) 

def logout_view(request):
    logout(request)
    return redirect('login_view')

@login_required
def tekmovanja(request):
    response=requests.get('http://127.0.0.1:5000/tekmovanja').json()
    return render(request, "tekmovanja.html", {'response':response}) 

@login_required
def porocila(request):
    name = request.GET.get('ironman_name')
    surname = request.GET.get('ironman_surname')
    return render(request, "porocila.html", {'name': name, 'surname': surname})

@login_required
def generate_reports(request):
    if request.method == 'POST':
        ironman_name = request.POST.get('ironman_name')
        ironman_surname = request.POST.get('ironman_surname')
        report_type = request.POST.get('report_type')

        return redirect(report_type, ironman_name=ironman_name, ironman_surname=ironman_surname)

@login_required
def get_runner_results(request, ironman_name, ironman_surname):
    api_url = f"http://127.0.0.1:5000/tekmovalec_run/{ironman_name}/{ironman_surname}"
    response = requests.get(api_url).json()
    return render(request, 'runners.html', {'response': response, 'runner_name': ironman_name})

@login_required
def get_biker_results(request, ironman_name, ironman_surname):
    api_url = f"http://127.0.0.1:5000/tekmovalec_bike/{ironman_name}/{ironman_surname}"
    response = requests.get(api_url).json()
    return render(request, 'bikers.html', {'response': response, 'runner_name': ironman_name})

@login_required
def get_swimmer_results(request, ironman_name, ironman_surname):
    api_url = f"http://127.0.0.1:5000/tekmovalec_swim/{ironman_name}/{ironman_surname}" 
    response = requests.get(api_url).json()
    return render(request, 'swimmers.html', {'response': response, 'runner_name': ironman_name})

@login_required
def add_objava(request):
    title = request.POST.get('title')
    body = request.POST.get('body')
    author = request.POST.get('author')
    upvote = request.POST.get('upvote')
    downvote = request.POST.get('downvote')
    return render(request, 'add_objava.html', {'title': title, 'body': body, 'author': author, 'upvote': upvote, 'downvote': downvote})

@login_required
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
    
@login_required
def translate(request, lang_code):
    request.session['django_language'] = lang_code
    return redirect(request.META.get('HTTP_REFERER', '/'))

def login_view(request):
        name = request.POST.get('username')
        password = request.POST.get('password')
        return render(request, 'login.html', {'name': name, 'password': password})
        


def auth(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        uri = 'home'

        api_url = f"http://127.0.0.1:5000/uporabnik/{name}/{password}"

        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            response_data = response.json()

            if response_data.get('accessible'):
                # Check if the user exists in Django's user model
                user, created = User.objects.get_or_create(username=name)
                if created:
                    user.set_password(password)  # Set password for the new user
                    user.save()

                # Authenticate the user with Django's authentication system
                user = authenticate(request, username=name, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(uri)
                else:
                    return HttpResponse("Invalid credentials", status=401)
            else:
                return HttpResponse("Access denied", status=403)

        except requests.exceptions.RequestException as e:
            return HttpResponse(f"API request failed: {e}", status=500)

    return render(request, 'login.html')

