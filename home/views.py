from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """A simple home view for the project."""
    return HttpResponse("Welcome to the OCR text app.")
