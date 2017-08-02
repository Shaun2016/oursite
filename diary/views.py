from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from diary.models import User, UserForm


def to_login(request):
    return render(request, 'diary/login/index.html')


def login(request):
    user = User.objects.filter(nickname=request.POST['nickname'], password=request.POST['password'])
    # user 集合为空时 user == False
    if user:
        return HttpResponseRedirect(reverse('diary:index'));
    return render(request, 'diary/login/index.html', {'error': '用户名或密码错误'})


def index(request):
    return render(request, 'diary/index.html')