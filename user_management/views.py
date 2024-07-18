from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)

        # Authenticate user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            print("Authorized User")
            
            # Redirect to a success page
            return HttpResponse('Authorized User')
        else:
            return HttpResponse('Email or Password Incorrect')

    return render(request, 'index.html')
