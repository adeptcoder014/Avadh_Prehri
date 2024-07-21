from django.urls import path
from . import views
urlpatterns = [
    path('create-subscription', views.create_subscription),
    path('get-subscribers', views.Get_subscribers),

]


