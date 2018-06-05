from __future__ import unicode_literals
from django.shortcuts import render
from .models import ProgrammingLanguages

def showProfile(request):
    langObjects=ProgrammingLanguages.objects.all().order_by('proficiency')
    return render(request,'myProfile/profilePage.html',{'langObjects':langObjects})
