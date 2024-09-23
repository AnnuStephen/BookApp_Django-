from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from . models import UserProfile,LoginTable
# Create your views here.

def userRegistration(request):

    login_table = LoginTable()
    userprofile = UserProfile()

    if request.method == 'POST':
        userprofile.username = request.POST['username']
        userprofile.password = request.POST['password']
        userprofile.password2 = request.POST['password1']

        login_table.username = request.POST['username']
        login_table.password = request.POST['password']
        login_table.password2 = request.POST['password1']
        login_table.type = 'user'

        if request.POST['password'] == request.POST['password1']:
            userprofile.save()
            login_table.save()

            messages.info(request,'Registration success')
            return redirect('login')
        else:
            messages.info(request,'Password not match')
            return redirect('register')

    return render(request,'accounts/register.html')


def loginPage(request):

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = LoginTable.objects.filter(username=username,password=password,type='user').exists()

        try:
            if user is not None:

                user_details = LoginTable.objects.get(username=username,password=password)
                user_name = user_details.username
                type = user_details.type

                if type == 'user':
                    request.session['username'] = user_name
                    return redirect('user_view')
                elif type == 'admin':
                    request.session['username'] = user_name
                    return redirect('admin_view')
                else:
                    messages.error(request,'invalid username or password')
        except:
            messages.error(request, 'invalid role')
    return render(request,'accounts/login.html')


def admin_view(request):
    user_name = request.session['username']
    return render(request,'accounts/admin_view.html',{'user_name':user_name})


def user_view(request):

    user_name = request.session['username']

    return render(request,'accounts/user_view.html',{'user_name':user_name})

def logout_view(request):
    logout(request)
    return redirect('login')





