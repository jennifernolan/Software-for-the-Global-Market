from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from .models import Comment
from .forms import NewCommentForm

# Create your views here.
def cities(request):
	comments = Comment.objects.all()
	return render(request, 'cities.html', {'comments': comments})

@login_required
def comment(request):
	if request.method == 'POST':
		form = NewCommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			Comment.objects.create(
				message=form.cleaned_data.get('message'),
				created_by=request.user
			)
			return redirect('cities')
	else:
		form = NewCommentForm()
	return render(request, 'new_comment.html', {'form': form})