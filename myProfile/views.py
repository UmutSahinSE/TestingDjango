from __future__ import unicode_literals

from django.shortcuts import render

def showProfile(request):
    return render(request,'myProfile/profilePage.html')
