from django.conf.urls import url
from . import views           # This line is new!

print("I M IN LOGREG APP URLS.PY")
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$',views.success),
    url(r'^regProcess$',views.regProcess),
    url(r'^valLogin$',views.valLogin),
    url(r'^logout$',views.logout)

]
