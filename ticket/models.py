from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
	display_name = models.CharField(max_length=40, unique=True)


class Tickets(models.Model):
	NEW = 'NEW'
	IN_PROG = 'IN_PROG'
	DONE = 'DONE'
	INVALID = 'INVALID'
	STATUS_CHOICES = [
		(NEW, 'NEW'),
		(IN_PROG, 'IN_PROG'),
		(DONE, 'DONE'),
		(INVALID, 'INVALID'),
	]

	title = models.CharField(max_length=30)
	date = models.DateTimeField(default=timezone.now)
	description = models.TextField()
	valid_user = models.ForeignKey(
		get_user_model(),
		related_name='valid_user',
		on_delete=models.CASCADE,
		null=True,
		blank=True, default=None, )
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW)
	complete_user = models.ForeignKey(
		get_user_model(),
		related_name='complete_user',
		null=True, blank=True,
		default=None,
		on_delete=models.CASCADE)
	assigned_user = models.ForeignKey(
		get_user_model(),
		related_name='assigned_user',
		null=True,
		blank=True,
		default=None,
		on_delete=models.CASCADE)

	def __str__(self):
		return self.title

