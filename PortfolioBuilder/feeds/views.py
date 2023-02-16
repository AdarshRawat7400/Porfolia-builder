from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile

def home_page(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    context = {
        "info": profile.personal_info,
        "about": profile.about,
        "skills": profile.projects.all(),
        "know": profile.skills.all()
    }

    return render(request, 'home_page.html', context)
