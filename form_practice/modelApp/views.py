from django.shortcuts import render
from .forms import MyModelForm

# Create your views here.
def modelForm(request):
    model_form = MyModelForm
    return render(request, 'modelApp/modelFormPage.html', {'form' : model_form})
