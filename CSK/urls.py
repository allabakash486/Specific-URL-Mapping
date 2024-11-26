from django.urls import path
from CSK.views import *

urlpatterns = [
    path('Captain/',Captain,name='Captain')
]