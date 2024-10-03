from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('task', views.TaskAPIViewSets)

app_name = 'task'

urlpatterns = [
    path('', include(router.urls)),
    path('statistic', views.TaskStatisticAPIView.as_view(), name='statistic')
]
