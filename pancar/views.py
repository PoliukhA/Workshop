from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import MessageForm
from .models import Klient, Car, Process, Category


class ProcessView(View):
    form_class = MessageForm
    def get(self, request):
        form = self.form_class()
        category_basic = Category.objects.get(name='Główne roboty')
        basic_proc = category_basic.processes.all().order_by('name')
        front_suspension = Category.objects.get(name='Zawieszenie przednie')
        front_susp_proc = front_suspension.processes.all().order_by('name')[:10]
        rear_suspension = Category.objects.get(name='Zawieszenie tylne')
        rear_susp_proc = rear_suspension.processes.all().order_by('name')
        braking_system = Category.objects.get(name='Układ hamulcowy')
        brak_sys_proc = braking_system.processes.all().order_by('name')[:7]
        fuel_system = Category.objects.get(name='Układ paliwowy')
        fuel_sys_proc = fuel_system.processes.all().order_by('name')
        silencer = Category.objects.get(name='Układ wydechowy')
        silencer_proc = silencer.processes.all().order_by('name')
        sterring_system = Category.objects.get(name='Układ kierownicy')
        sterring_sys_proc = sterring_system.processes.all().order_by('name')
        engine = Category.objects.get(name='Naprawa silnika')
        engine_proc = engine.processes.all().order_by('name')[:10]
        transmission = Category.objects.get(name='Skrzynia biegów')
        trans_proc = transmission.processes.all().order_by('name')[:10]
        context = {
            'form': form,
            'basic_proc': basic_proc,
            'front_susp_proc': front_susp_proc,
            'rear_susp_proc': rear_susp_proc,
            'brak_sys_proc': brak_sys_proc,
            'fuel_sys_proc': fuel_sys_proc,
            'silencer_proc': silencer_proc,
            'sterring_sys_proc': sterring_sys_proc,
            'engine_proc': engine_proc,
            'trans_proc': trans_proc,
        }
        return render(request, 'base.html', context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            info = form.cleaned_data['info']
            context['name'] = name
            context['phone'] = phone
            context['email'] = email
            context['info'] = info
        return render(request, 'pancar/forma.html', context)