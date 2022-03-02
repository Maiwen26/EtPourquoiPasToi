from django.shortcuts import render
from django.utils import timezone
from .models import Temoignage

# Create your views here.
def temoignages_list(request):
    temoignages = Temoignage.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'eppt/temoignages_list.html', {'temoignages':temoignages})