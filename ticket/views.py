from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import SignupForm, LoginForm
from ticket.models import CustomUser, Tickets
from django.contrib.auth.decorators import login_required
from ticket.forms import TicketsForm


@login_required
def index(request):
	html = 'index.html'
	ticket_data = Tickets.objects.all()
	return render(request, html, {'ticket_data': ticket_data})


@login_required
def signup_view(request):
	html = 'signup.html'
	form = SignupForm()
	if request.method == 'POST':
		form = SignupForm(request.POST)
	if form.is_valid():
		data = form.cleaned_data
		new_user = CustomUser.objects.create_user(
			username=data['username'], display_name=data['display_name'],
			password=data['password1'], )
		new_user.save()
		login(request, new_user)
		return HttpResponseRedirect(reverse('home'))
	form = SignupForm()
	return render(request, html, {'form': form})


def loginview(request):
	html = 'login.html'
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(
				request, username=data['username'],
				password=data['password']
			)
			if user:
				login(request, user)
			return HttpResponseRedirect(
				request.GET.get('next', reverse('home'))
			)
	form = LoginForm()
	return render(request, html, {'form': form})


def logoutview(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))


def ticket_detail(request, id):
	ticket = Tickets.objects.get(id=id)
	return render(request, 'ticket_detail.html', {'ticket': ticket})


def create_ticket(request, user_id):
	html = 'create_ticket.html'
	if request.method == 'POST':
		form = TicketsForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = CustomUser.objects.get(id=user_id)
			ticket = Tickets.objects.create(
				title=data['title'],
				description=data['description'],
				valid_user=user
			)
			return HttpResponseRedirect(reverse('home'))
	form = TicketsForm()
	return render(request, html, {'form': form})


def edit_ticket(request, ticket_id):
	ticket = Tickets.objects.get(id=ticket_id)
	if request.method == 'POST':
		form = TicketsForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			ticket.title = data['title']
			ticket.description = data['description']
			ticket.save()
		return HttpResponseRedirect(reverse('ticket_detail', args=(ticket_id,)))
	form = TicketsForm(initial={
		'title': ticket.title,
		'description': ticket.description
	})
	return render(request, "create_ticket.html", {'form': form})


def in_progress(request, ticket_id):
	ticket = Tickets.objects.get(id=ticket_id)
	ticket.ticket_status = "in_progress"
	ticket.assigned_user = request.user
	ticket.assigned_user = None
	ticket.save()
	return HttpResponseRedirect(
		reverse('ticket_detail.html', args=ticket_id))


def completed_ticket(request, ticket_id):
	ticket = Tickets.objects.get(id=ticket_id)
	ticket.ticket_status = 'DONE'
	ticket.completed_user = request.user
	ticket.assigned_user = request.user
	ticket.save()
	assert isinstance({ticket_id:ticket_id ,user_detail: user_detail},)
	return HttpResponseRedirect(
		reverse('ticket_detail', args=ticket_id))


def invalid_ticket(request, ticket_id):
	ticket = Tickets.objects.get(id=ticket_id)
	ticket.ticket_status = "INVALID"
	ticket.assigned_user = None
	ticket.completed_user = None
	ticket.save()
	return HttpResponseRedirect(reverse('ticket_detail', args=(ticket_id,)))


def user_detail(request, user_id):
	html = 'user_detail.html'
	assigned_ticket = Tickets.objects.filter(assigned_user=user_id)
	complete_ticket = Tickets.objects.filter(complete_user=user_id)
	valid_ticket = Tickets.objects.filter(valid_user=user_id)
	return render(request, html, {
		'valid_ticket': valid_ticket,
		'assigned_ticket': assigned_ticket,
		'complete_ticket': complete_ticket})
