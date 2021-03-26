from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import User
from django.utils import timezone
import hashlib
from random import random
from django.contrib import messages

class IndexView(generic.ListView):
    template_name = 'aiuts/index.html'
    context_object_name = 'all_user'

    def get_queryset(self):
        """Return the last five published questions."""
        return User.objects.all()[:]

class LoginView(generic.TemplateView):
    template_name = 'aiuts/login.html'

class SignupView(generic.TemplateView):
    template_name = 'aiuts/sign_up.html'

class GetbalanceView(generic.TemplateView):
    template_name = 'aiuts/get_balance.html'

def create_acc(request):
    fullname = request.POST['fullname']
    password = request.POST['password']
    acc_id = hashlib.md5(str.encode(fullname)).hexdigest()
    hash_pw = hashlib.md5(str.encode(password)).hexdigest()
    for acc in User.objects.all():
        if acc.acc_id == acc_id:
            messages.info(request, 'This name is already registered once!')
            return HttpResponseRedirect(reverse('aiuts:signup'))
    new_acc = User(acc_id, hash_pw, random() * 100)    
    new_acc.save()
    return HttpResponseRedirect(reverse('aiuts:index'))

def check_balance(request):
    fullname = request.POST['fullname']
    password = request.POST['password']
    acc_id = hashlib.md5(str.encode(fullname)).hexdigest()
    hash_pw = hashlib.md5(str.encode(password)).hexdigest()
    for acc in User.objects.all():
        if acc.acc_id == acc_id and acc.password == hash_pw:
            messages.info(request, 'Your account has {} Baht'.format(acc.balance))
            return HttpResponseRedirect(reverse('aiuts:getbalance'))
        else:
            messages.info(request, "Entered credential is incorrect")
            return HttpResponseRedirect(reverse('aiuts:getbalance'))