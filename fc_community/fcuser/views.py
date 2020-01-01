from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None) 
        password = request.POST.get('password', None)
        usermail = request.POST.get('usermail', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and usermail and password and re_password):
             res_data['error'] = '모든 값을 입력해야합니다.'
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username = username,
                password = make_password(password),
                usermail = usermail
            )

            fcuser.save()

        return render(request, 'register.html', res_data)

def home(request):
    user_id = request.session.get('user')
        
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser)
    else:
        return HttpResponse('I don\'t have user_id')
        
    return HttpResponse('Home!')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        else :
            # Is password right that?
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
                request.session['user'] = fcuser.id
                return redirect('/')
            else :
                res_data['error'] = '비밀번호를 틀렸습니다.'

        return render(request, 'login.html', res_data)
