from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from booklist.models import BookList
from django.contrib.auth import authenticate, login

def buecher(request):
    return render_to_response('buecher.html')


def list_titles(request):
    titel_liste = BookList.objects.order_by('pub_date')
    return render_to_response('list_titles.html', {'titel_liste': titel_liste})
