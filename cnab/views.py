from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse


from .forms import UploadForm

from .models import Upload
# Create your views here.

class IndexView(TemplateView):
    template_name = 'form-upload.html'

class UploadView(ListView):
    model = Upload
    template_name = 'transactions.html'

def index(request):
    form = None
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            print('Form is not valid')
            return HttpResponse('thanks')
        else:
            form = UploadForm()
        return render(request, 'transactions.html', {'form': form} )