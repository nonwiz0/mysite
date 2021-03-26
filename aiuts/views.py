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

class GetaccidView(generic.TemplateView):
    template_name = 'aiuts/get_acc_id.html'

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
    messages.info(request, '{} has been created!'.format(new_acc.acc_id))
    return HttpResponseRedirect(reverse('aiuts:index'))

def check_balance(request):
    acc_id = request.POST['acc_id']
    password = request.POST['password']
    hash_pw = hashlib.md5(str.encode(password)).hexdigest()
    for acc in User.objects.all():
        if acc.acc_id == acc_id and acc.password == hash_pw:
            messages.info(request, 'Your account has {:.2f} Baht'.format(acc.balance))
            return HttpResponseRedirect(reverse('aiuts:getbalance'))
        if acc.acc_id == acc_id and acc.password != hash_pw:
            messages.info(request, 'Incorrect credential')
            return HttpReponseRedirect(reverse('aiuts:getbalance'))


def check_accid(request):
    fullname = request.POST['fullname']
    password = request.POST['password']
    hash_acc = hashlib.md5(str.encode(fullname)).hexdigest()
    hash_pw = hashlib.md5(str.encode(password)).hexdigest()
    for acc in User.objects.all():
        if acc.acc_id == hash_acc and acc.password == hash_pw:
            messages.info(request, 'Acc ID: {}'.format(acc.acc_id))
            return HttpResponseRedirect(reverse('aiuts:getaccid'))
        if acc.acc_id == hash_acc and acc.password != has_pw:
            messages.info(request, 'Incorrect credential')
            return HttpReponseRedirect(reverse('aiuts:getaccid'))


