from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

# Create your views here.
class Index(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'users/index.html')

class SignUpView(View):
	def get(self, request, *args, **kwargs):
		form = SignUpForm()
		return render(request, 'users/signup.html', {'form': form})

	def post(self, request, *args, **kwargs):
		print(request.POST)
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('index')
		return render(request, 'users/signup.html', {'form': form})

