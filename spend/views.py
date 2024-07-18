from django.shortcuts import render,redirect
from .models import Spend


def spend(request):
    spend=Spend.objects.all()
    return render(request,'spend/spend.html',{'spend':spend})