from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    path('', views.BirthdayCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/',
         views.BirthdayDeleteView.as_view(),
         name='delete'),
    path('list/', views.BirthdatListView.as_view(), name='list'),
]
