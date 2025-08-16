from django.shortcuts import render,redirect
from emailsapp.forms import Detail
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# def sndmail(request):
#     if request.method=='POST':
#         form=Detail(request.POST)
#         if form.is_valid(): 
#             form.save()
#             subject='application for python developer'
#             message='we have received your application'
#             recepient=form.cleaned_data.get('email')
#             send_mail(subject,message,settings.EMAIL_HOST_USER,[recepient])
#             return redirect('/')
#     return render(request,'page1.html')
def page1(request):
    form=Detail()
    return render(request,'page1.html',{'form':form})

def sndmail(request):
    if request.method == 'POST':
        form = Detail(request.POST)
        if form.is_valid():
            form.save()
            subject = 'application for python developer'
            message = 'we have received your application'
            recepient = form.cleaned_data.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recepient])
            return redirect('/')
    return render(request, 'page1.html')