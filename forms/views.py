from django.shortcuts import render
from . import PhotosForms

# Create your views here.
def sharePhotos(request):
    return render(request,'forms/uploadfile.html')

def album(request):
    form = PhotosForms.PhotosForms()
    return render(request,'forms/photos.html',{'form':form })
