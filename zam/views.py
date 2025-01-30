from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import PastWork
from django.contrib import messages
from .forms import ContactMessageForm
from .models import ContactMessage
from django.contrib.auth.decorators import user_passes_test

def home(request):
    return render(request, 'home.html')

def past_work(request):
    works = PastWork.objects.all()
    return render(request, 'past_work.html', {'works': works})

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    if request.method == 'POST':
        print("Form submission detected!")  # Debug statement
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            print("Form is valid. Saving message...")  # Debug statement
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            print("Form is invalid. Errors:", form.errors)  # Debug statement
            messages.error(request, 'There was an error with your submission.')
    else:
        form = ContactMessageForm()

    return render(request, 'contact.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)  # Restrict to staff users

def message_list(request):
    messages = ContactMessage.objects.all().order_by('-created_at')  # Fetch all messages, newest first
    return render(request, 'message_list.html', {'messages': messages})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('home')
