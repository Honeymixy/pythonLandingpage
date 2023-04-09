from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm



# Create your views here.
# login function

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.add_message(request, messages.SUCCESS, 'Acc created successfully,kindly login to continue.')
            return redirect(reverse('login'))

    context = {'form': form}     
                            
    return render(request, 'register.html',context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('login')


