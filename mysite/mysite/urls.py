from django.contrib import admin
from django.urls import path
from app_blog import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Додаємо шлях до адміністративної панелі
    path('', views.HomePageView.as_view()),  # Ваша домашня сторінка
]
