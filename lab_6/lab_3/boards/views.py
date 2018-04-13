from django.shortcuts import render
from .models import Board
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

def home(request):
    boards = Board.objects.all()
#Return the page home.html 
    return render(request, 'home.html', {'boards': boards})
	
def testlang(request):
	return HttpResponse(_('Welcome to the discussion board!'))

