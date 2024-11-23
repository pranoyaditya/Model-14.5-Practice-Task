from django.shortcuts import render
from .forms import*
# Create your views here.
def formPractice(request):
    full_form = Froms
    return render(request, 'formApp/formPage.html', {'full_form' : full_form})