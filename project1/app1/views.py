from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jampandu(request):
    return HttpResponse('<h1><marquee>JAMPANDU TO JIGELRAANI:HI. HLO HOW ARE YOU</marquee></h1>')
def jigelrani(request):
    return HttpResponse('<h1><marquee>REPLY:FINE.... WHAT ABOUT YOU ????</marquee></h1>')
