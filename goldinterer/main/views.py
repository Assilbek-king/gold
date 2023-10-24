from django.shortcuts import render
from main.models import *
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render

from main.models import Feedback




# Create your views here.

def indexHandler(request):
    tovars = Tovar.objects.order_by('status')
    photos = Photo.objects.all()
    feeds = Feedback.objects.all()
    # otzivs = Otziv.objects.all()
    # services = Service.objects.all()
    # partners = Partner.objects.all()

    if request.method == 'POST':
        BOT_TOKEN = "6229480873:AAH4-YF9xLEkpJRQiXAzFDadMG4o0KSVkEc"
        TELEGRAM_CHAT_ID = "604469732"
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        feedback = Feedback(name=name, phone=phone, comment=comment)
        feedback.save()
        if comment:
            message = f"Новый клиент\nИмя: {name}\nНомер: {phone}\nТовар: {comment}"
        else:
            message = f"Новый клиент\nИмя: {name}\nНомер: {phone}"
        response = requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}")
        from django.shortcuts import redirect
        return redirect('/')

    return render(request, 'index.htm', {
        'tovars': tovars,
        'photos': photos,
        'feeds': feeds,
        # 'otzivs': otzivs,
        # 'services': services,
        # 'partners': partners,
    })

