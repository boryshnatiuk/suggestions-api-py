from django.conf.urls import url
from corrections import views

urlpatterns = [
    url(r'^suggest', views.Suggestions.as_view())
]
