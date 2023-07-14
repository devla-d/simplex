from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("about-us/", views.about, name="about"),
    path("contact-us", views.contact, name="contact"),
    path("faqs/", views.faq, name="faq"),
    path("plans/", views.plan, name="plans"),
    path("privacy-policies/", views.privacy, name="privacy"),
    path("terms-conditions/", views.terms, name="terms"),
    path("testimonies/", views.testimonies, name="testimonies"),
]
