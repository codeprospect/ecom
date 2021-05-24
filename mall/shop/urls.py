from django.urls import path
from . import views

from django.conf.urls.static import static

urlpatterns = [
    # path('', views.homepage, name="homepage"),
    path('', views.homepage, name='shop-home'),
]
