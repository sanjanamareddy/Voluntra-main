from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,   auth
from django.contrib.auth.decorators import login_required
from voluntra.models import PostEvent

# Create your views here.

def main(request):
    return render(request, 'main.html')
 
def login(request):
    return render(request, 'login.html')

def aboutUs(request):
    return render(request, 'aboutus.html')

def myEvents(request):
    current_user = request.user.username

    user_events = PostEvent.objects.filter(username=current_user)

    context = {
        'user_events': user_events,
    }

    return render(request, 'myevents.html', context)

    # return render(request, 'myevents.html', context)
    # return render(request, 'myevents.html')

def eventDetails(request):
    return render(request, 'eventdetails.html')

def home(request):
    return render(request, 'main.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('/login1')
    else:
        return render(request, 'login1.html')

# def signUp(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         username = request.POST['username']
#         # phoneNumber = request.POST['phoneNumber']
#         email = request.POST['email']
#         password = request.POST['password']

#         user = User.objects.create_user(first_name = first_name, username = username, email = email, password = password)
#         user.save()
#         print('user created')
#         return redirect('/home')
#     else:
#         return render(request, 'signup.html')

def signUp(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        username = request.POST['username']
        # phone_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']


        if User.objects.filter(username=username).exists():
            print('Username taken')
            messages.error(request, 'Username already taken.Choose another.')
            return redirect('/signUp')
        elif User.objects.filter(email=email).exists():
            print('Email taken')
            messages.error(request, 'Email is already taken. Please use a different one.')
            return redirect('/signUp')
        else:
            try:
                user = User.objects.create_user(first_name=first_name, username=username, email=email, password=password)
                print('User created successfully')
                return redirect('/login1')
            except Exception as e:
                print(f'Error creating user: {e}')
                messages.error(request, 'Error creating user. Please try again.')
                return redirect('/signUp')
    else:
        return render(request, 'signup.html')


def loginOrg(request):
    if request.method == 'POST':
        form = request.POST
        picture = request.FILES.get('picture')

        try:
            event = PostEvent.objects.create(
                username=request.user.username,
                nameOfEvent=form['nameOfEvent'],
                descOfEvent=form['descOfEvent'],
                placeOfEvent=form['placeOfEvent'],
                dateOfEvent=form['dateOfEvent'],
                numOfVol=form['numOfVol'],
                minAge=form['minAge'],
                eventPoster=picture
            )
            event.save()
            print('Event created successfully')
            # Redirect to the home view after saving the event
            return redirect('/home')
        except Exception as e:
            print(f'Error creating Event: {e}')
            messages.error(request, 'Error creating Event. Please try again.')
            return redirect('/loginOrg')
    else:
        # If it's not a POST request, render the loginorg2.html template
        current_user = request.user
        return render(request, "loginorg2.html", {'context': current_user.username})

    
def loginVol(request):
    if request.method == 'POST':
        name = request.POST['name']
        Phone_number = request.POST['Phone_number']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(name = name, Phone_number = Phone_number, email = email, password = password)
        user.save()
        print('user created')
        return redirect('/home')
        
    else:
        return render(request, 'loginvol.html')

def joinEvent_1(request):
    events = PostEvent.objects.all()
    return render(request, 'joinEventPage1.html', {'events': events})
    # return render(request, 'joinEventPage1.html')

def joinEvent_2(request):
    # event_id = PostEvent.objects.get(id)
    # event = get_object_or_404(PostEvent, id=event_id)
    return render(request, 'joinEventPage2.html')
    # return render(request, 'joinEventPage2.html')

def joinEvent_3(request):
    if request.method == 'POST':
        return render(request, 'joinEventPage4.html')
    else:
        return render(request, 'joinEventPage3.html')

def joinEvent_4(request):

    return render(request, 'joinEventPage4.html')


def logout(request):
    auth.logout(request)
    return redirect('/home')