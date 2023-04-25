from django.urls import path
from appEx import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("stock/", views.stock, name="stock"),
    path("contact/", views.contact, name="contact"),
    path("home/", views.home, name="home"),
    path("", views.login, name='login'),
    path("signup/", views.signup, name="signup"),
    path("stock/<str:name>/", views.stock_info, name="stock_info")
]
urlpatterns += staticfiles_urlpatterns()
