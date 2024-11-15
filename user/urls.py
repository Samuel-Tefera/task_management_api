from django.urls import include, path

from . import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUSerView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
