from django.shortcuts import render

def showHome(request):
   return render(request,'homepage.html')
