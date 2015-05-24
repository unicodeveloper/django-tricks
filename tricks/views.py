from django.shortcuts import render,  get_object_or_404
from .models import Trick

# Create your views here.
def index(request):
  tricks = Trick.objects.all()
  return render(request, 'tricks/view_all_tricks.html', {'tricks': tricks})

def trick_detail(request, trick_slug):
  trick = get_object_or_404(Trick, slug=trick_slug)
  return render(request, 'tricks/trick_detail.html', {'trick': trick})