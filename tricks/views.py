from django.shortcuts import render,  get_object_or_404
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import Trick
from .forms import TrickForm

# Create your views here.
def index(request):
  tricks = Trick.objects.all()
  return render(request, 'tricks/view_all_tricks.html', {'tricks': tricks})

def about(request):
  return render(request, 'tricks/about.html', {})

def register(request):
  return render(request, 'tricks/register.html', {})

def loggin(request):
  return render(request, 'tricks/login.html', {})

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect("/")

def trick_detail(request, trick_slug):
  trick = get_object_or_404(Trick, slug=trick_slug)
  return render(request, 'tricks/trick_detail.html', {'trick': trick})

def trick_new(request):
  if request.method == "POST":
      form = TrickForm(request.POST)
      if form.is_valid():
        trick = form.save(commit=False)
        trick.user = request.user
        trick.save()
        return redirect('tricks.views.trick_detail', trick_slug=trick.slug)
  else:
    form = TrickForm()
  return render(request, 'tricks/trick_edit.html', {'form': form})

def trick_edit(request, trick_slug):
  trick = get_object_or_404(Trick, slug=trick_slug)
  if request.method == "POST":
      form = TrickForm(request.POST, instance=trick)
      if form.is_valid():
        trick = form.save(commit=False)
        trick.user = request.user
        trick.save()
        return redirect('tricks.views.trick_detail', trick_slug=trick.slug)
  else:
    form = TrickForm(instance=trick)
  return render(request, 'tricks/trick_edit.html', {'form': form})
