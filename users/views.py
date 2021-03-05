from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from .models import Profile


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, "users/register.html", context)

@login_required
def profile(request):
    profile = Profile.objects.get(user = request.user)
    points = 0
    for i in profile.awards.all():
        points += i.points
    context = {
        'profile': profile,
        'awards': profile.awards.all(),
        'points': points
    }
    return render(request, "users/profile.html", context)

@login_required
def profile_update(request):
    
    if request.method == 'POST':
        print("Inside POST")
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            print("FORM SAVED")
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {
        'form':form
    }
    return render(request, "users/profile_update.html", context)