from django.urls import path

from .views import IndexView, AboutView, ContactView

app_name = "website"
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about-us/', AboutView.as_view(), name="about"),
    path('contact-us/', ContactView.as_view(), name="contact"),

    ]