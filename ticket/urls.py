from django.urls import path

from ticket import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('ticket_detail/<int:id>', views.ticket_detail, name='ticket_detail'),
    path('create_ticket/<int:user_id>', views.create_ticket, name='create_ticket'),
    path('in_progress/edit/<int:ticket_id>', views.in_progress, name='in_progress'),
    path('completed/edit/<int:ticket_id>', views.completed_ticket, name='DONE'),
    path('invalid/edit/<int:ticket_id>', views.invalid_ticket, name='invalid'),
    path('edit_ticket/edit/<int:ticket_id>', views.edit_ticket, name='edit'),
    path('user_detail/<int:user_id>', views.user_detail, name='user_detail'),

]