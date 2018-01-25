from django.shortcuts import render
from notify.forms import ApplicationForm
from django.http import HttpResponse

import json
import logging

import telepot
from django.template.loader import render_to_string
from django.http import HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings


TelegramBot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)

logger = logging.getLogger('telegram.bot')

def index(request):
    form = ApplicationForm()
    return render(request, 'notify/index.html', {'form':form})

def send_message(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data
            msg = 'Name: ' + x['name'] + '\n Phone Number: ' + x['phone_number']
            TelegramBot.sendMessage(441549627, msg)
            return HttpResponse('Thank you!')
        else:
            return HttpResponse('Something went wrong, try again!')
    else:
        return index(request)
