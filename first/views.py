from django.http import HttpResponse

def showHome(request):
   return HttpResponse('Hello World')
