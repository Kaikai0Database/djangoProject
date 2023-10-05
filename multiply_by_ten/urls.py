from django.urls import path
from . import views

urlpatterns = [
    path('', views.multiply_by_ten), #path中的''空下來是因為在html中已經有執行輸入網址不必再額外設立
]