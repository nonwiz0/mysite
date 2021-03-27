from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
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


class AccountView(generic.DetailView):
    model = User
    template_name = 'aiuts/account_dash.html'

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
          #  return HttpResponseRedirect(reverse('aiuts:getbalance'))
            return redirect(request.META['HTTP_REFERER'])
        if acc.acc_id == acc_id and acc.password != hash_pw:
            messages.info(request, 'Incorrect credential')
           # return HttpReponseRedirect(reverse('aiuts:getbalance'))
            return redirect(request.META['HTTP_REFERER'])


def check_accid(request):
    fullname = request.POST['fullname']
    password = request.POST['password']
    hash_acc = hashlib.md5(str.encode(fullname)).hexdigest()
    hash_pw = hashlib.md5(str.encode(password)).hexdigest()
    for acc in User.objects.all():
        if acc.acc_id == hash_acc and acc.password == hash_pw:
            messages.info(request, 'Acc ID: {}'.format(acc.acc_id))
            return redirect(request.META['HTTP_REFERER'])
        if acc.acc_id == hash_acc and acc.password != hash_pw:
            messages.info(request, 'Incorrect credential')
            return redirect(request.META['HTTP_REFERER'])

def check_account(request):
    acc_id = request.POST['acc_id']
    password = request.POST['password']
    hash_pw = hashlib.md5(str.encode(password)).hexdigest()
    for acc in User.objects.all():
        if acc.acc_id == acc_id and acc.password == hash_pw:
            messages.info(request, 'Login successfully')
            return HttpResponseRedirect(reverse('aiuts:account', args=[acc.acc_id]))
        if acc.acc_id == acc_id and acc.password != hash_pw:
            messages.info(request, 'Incorrect credential')
            return HttpResponseRedirect(reverse('aiuts:login'))


def send_money(request):
    acc_id = request.POST['source']
    recipient = request.POST['destination']
    amount = float(request.POST['amount'])
    password = request.POST['password']
    hash_pw = hashlib.md5(str.encode(password)).hexdigest()
    for acc in User.objects.all():
        if acc.acc_id == acc_id and acc.password == hash_pw:
            if amount < acc.balance and User.objects.filter(pk=recipient).exists():
                recipient_acc = User.objects.get(pk=recipient)
                acc.balance -= amount
                recipient_acc.balance += amount
                recipient_acc.save()
                acc.save()
                messages.info(request, "Money sent successfully, you have {} baht left".format(acc.balance))
                return redirect(request.META['HTTP_REFERER'])
            else:
                messages.info(request, "Failed to send, please make sure you have enough balance")
                return redirect(request.META['HTTP_REFERER'])
        if acc.acc_id == acc_id and acc.password != hash_pw:
            messages.info(request, 'Incorrect credential')
           # return HttpReponseRedirect(reverse('aiuts:getbalance'))
            return redirect(request.META['HTTP_REFERER'])



