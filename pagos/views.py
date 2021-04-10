from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import PayForm


def pay(request):
    pay_form = PayForm()

    if request.method == "POST":
        pay_form = PayForm(data=request.POST)
        if pay_form.is_valid():
            name = request.POST.get('name', '')
            content = request.POST.get('content', '')
            amount = request.POST.get('amount', '')
            grant = request.POST.get('grant', '')
            created = request.POST.get('created', '')
            classification = request.POST.get('classification', '')

            return redirect(reverse('pay')+"?ok")

    return render(request, "pagos/registro_pago.html",{'form':pay_form})
