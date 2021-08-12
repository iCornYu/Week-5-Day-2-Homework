from django.conf import settings
from django.shortcuts import render, redirect
from .models import PhoneNumber
from .forms import PhoneForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def homePage(request):
    return render(request, 'blog/index.html')

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        print(user)
        print(username,password)
        if user is not None:
            login(request,user)
            print(f'{user} has logged in.')
            return redirect('blog-view_all')
        messages.info(request, "Incorrect username or password. Please try again.")
    return render(request, 'blog/login.html')

def registerPage(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        
        user = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')

        context = {'username' : user}

        template = render_to_string('blog/emailtemplate.html', context)

        email_message = EmailMessage(
            'Welcome to The Phone Book',
            template,
            settings.EMAIL_HOST_USER,
            [email]
        )

        email_message.fail_silently = False
        email_message.send()

        messages.success(request, "Successfully created account for " + user)

        return redirect('blog-login')

    context = {'form': form}
    return render(request, 'blog/register.html', context)

def view_allPage(request):
    phone_numbers = PhoneNumber.objects.all()
    context = {'phone_number' : phone_numbers, 'page-title': 'List of Phone Numbers'}
    return render(request, 'blog/view_all.html', context)

@login_required(login_url = 'blog-login')
def createPage(request):
    form = PhoneForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'blog/create.html', context)

@login_required(login_url = 'blog-login')
def logoutPage(request):
    logout(request)
    return redirect('blog-login')

