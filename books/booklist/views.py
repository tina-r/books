from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from booklist.models import BookList
from django.contrib.auth import authenticate, login
from django.template import Context, loader
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from .forms import RenewBookForm
from django.shortcuts import get_object_or_404
from .forms import DeleteBookForm
from .forms import EditBookForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout


def buecher(request):
    titel = BookList.objects.all().order_by('pub_date')
    ti = loader.get_template('buecher.html')
    ci = Context({'titel': titel})
    return HttpResponse(ti.render(ci))

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #user = User.objects.create_user(username=form.cleaned_data['username'])
            user = authenticate(username=username, password=password)
            #login(request, user)
            return redirect('/buecher')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def list_titles(request):
    titel_liste = BookList.objects.all().order_by('pub_date')
    t = loader.get_template('list_titles.html')
    c = Context({'titel_liste': titel_liste})
    return HttpResponse(t.render(c))


def list_delete_titles(request):
    if request.user.is_authenticated():
        delete_list = BookList.objects.all().order_by('pub_date')
        t = loader.get_template('deletion_list_title.html')
        c = Context({'delete_list': delete_list})
        return HttpResponse(t.render(c))
    else:
        return redirect('/buecher/log_in')
        

def list_infos(request,id):
    info_list = BookList.objects.get(pk=id)
    i = loader.get_template('list_infos.html')
    il = Context({'info_list': info_list})
    return HttpResponse(i.render(il))


def list_content(request):
    content_list = BookList.objects.all().order_by('pub_date')
    cl = loader.get_template('list_content.html')
    cc = Context({'content_list': content_list})
    return HttpResponse(cl.render(cc))


def renew_book(request):
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_inst = form.save(commit=False)
	    book_inst.save()
            return HttpResponseRedirect('/buecher/titel_liste')
    else:
        form = RenewBookForm()
    return render(request, 'book_renew.html', {'form': form})


def delete_book(request, pk):
    if request.method == 'POST':
        form = DeleteBookForm(request.POST)
        if form.is_valid():
 	    book_inst = BookList.objects.get(pk = pk)
	    book_inst.delete()
            return HttpResponseRedirect('/buecher/titel_liste')
    else:
        form = DeleteBookForm()
    return render(request, 'book_delete.html', {'form': form})


def edit_book(request,pk):
    if request.method == 'POST':
        form = EditBookForm(request.POST)
        if form.is_valid():
 	    book_inst = BookList.objects.get(pk = pk)
	    book_inst.title = request.POST.get('title')
	    book_inst.text = request.POST.get('text')
	    book_inst.author = request.POST.get('author')
            #book_inst = form.save()
	    book_inst.save()
            return HttpResponseRedirect('/buecher/titel_liste')
    else:
        form = EditBookForm()
    return render(request, 'book_edit.html', {'form': form})

