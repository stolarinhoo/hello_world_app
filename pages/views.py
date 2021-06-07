from django.shortcuts import render

from django.http import HttpResponse
def homePageView(request):
    return HttpResponse('Hello, World!\n \t \n \n \n \n  MOja pierwsza strona internetowa ;p')