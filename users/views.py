from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegistrationForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        register_form=CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Account Created"))
            return redirect('todolist')
        else:
            messages.success(request,("Invalid Details"))
    else:
        register_form=CustomRegistrationForm()
    context={
        'form':register_form
    }
    return render(request,'register.html',context)
