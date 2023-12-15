# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import FeedbackForm
from .models import Activity, CustomUser

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feedback')
    return render(request, 'registration/login.html')

@login_required
def feedback(request):
    user = request.user
    custom_user = CustomUser.objects.get(email=user.email)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.instance.name = custom_user.username
            form.instance.email = custom_user.email
            form.save()

            Activity.objects.create(user=custom_user, activity_type='Feedback Submitted')

            return redirect('thank_you')
    else:
        form = FeedbackForm(initial={'name': custom_user.username, 'email': custom_user.email})

    return render(request, 'feedback_form.html', {'form': form})

@login_required
def activity_history(request):
    user = request.user
    activities = Activity.objects.filter(user=user)
    return render(request, 'activity_history.html', {'activities': activities})
