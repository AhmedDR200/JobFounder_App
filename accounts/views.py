from django.contrib.auth import authenticate , login
from django.shortcuts import render , redirect
from .forms import SignupForm
# Create your views here.


def signup(request):
    if request.method == "POST":
        form =SignupForm(request.POST)
        if  form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user )
            return redirect('/accounts/profile/')
        
    else:
        form=SignupForm()

    return render(request, 'registration/signup.html', {'form':form})