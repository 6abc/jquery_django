from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

def profile_view(request):
    profile, _ = Profile.objects.get_or_create(pk=1)  # For demo, use pk=1
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profileapp/profile.html', {'form': form})

def home(request):
    return render(request, 'profileapp/home.html')