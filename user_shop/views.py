import datetime

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.template import context
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

from user_shop.forms import UserProfileForm, MyRegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from user_shop.models import UserProfiler
from django.template.context_processors import csrf


@csrf_exempt  # <------
def user_profile(request):
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

            if form.is_valid():
                user = request.user
                user.profile.image = form.cleaned_data['image']
                print(user.profile.image.url)
                user.profile.last_name = form.cleaned_data['last_name']
                user.profile.first_name = form.cleaned_data['first_name']
                user.profile.mid_name = form.cleaned_data['mid_name']
                user.profile.phone_number = form.cleaned_data['phone_number']
                user.profile.about = form.cleaned_data['about']

                form.save()
                return redirect('user_shop:myinformation')
                request.FILES['image'].temporary_file_path
        else:
            user = request.user
            form = UserProfileForm(instance=user.profile)
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('user_shop/profile.html', args)


def magic(request):
    current = auth.get_user(request)
    if request.GET.get('username'):
        name = request.GET['username']
        user = User.objects.get(username__iexact=name)
        id = user.id
        table = UserProfiler.objects.filter(user=id)
        test = current == user
    else:
        table = UserProfiler.objects.filter(user=current.id)
        test = True
    a = dict(posts=table, current=test)
    return render_to_response('user_shop/profile_information.html', a)


def home(request):
    # auth.logout(request)
    form = LoginForm()
    return render_to_response('user_shop/login.html', {'form': form})


def login(request):
    if request.GET.get('login'):
        login_user = request.GET['login']
    else:
        return render_to_response('user_shop/error.html', {
            'back': '/account/home',
            'error': 'Enter the login!'
        })
    if request.GET.get('passw'):
        passw = request.GET['passw']
    else:
        return render_to_response('user_shop/error.html', {
            'back': '/account/home',
            'error': 'Enter the password!'
        })
    uuser = auth.authenticate(username=login_user, password=passw)
    if uuser:
        auth.login(request, uuser)
        return render(request, 'user_shop/userlist.html')
    else:
        return render_to_response('user_shop/error.html', {
            'back': '/account/home',
            'error': 'Error! Incorrect login or password...'
        })


def usrlist(request):
    # if 'logout' in request.GET:
    #     auth.logout(request)
    # table = User.objects.all()
    # if request.user.is_authenticated():
    #     a = dict(users=table, where='Logout')
    # else:
    #     a = dict(users=table, where='Login')
    return render_to_response('user_shop/userlist.html')


@csrf_exempt  # <------
def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data['username'])
            print(user.id)
            print(user.pk)
            print(user.username)
            print(user.email)
            profile = UserProfiler.objects.get(user_id=user.id)
            profile.email = form.cleaned_data['email']
            profile.save()
            return HttpResponseRedirect('register_success')
    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
    return render_to_response('user_shop/registrating.html', args)


def register_success(request):
    return render_to_response('user_shop/registration_complete.html')


def logout_request(request):
    auth.logout(request)
    return render_to_response('user_shop/logout.html')
