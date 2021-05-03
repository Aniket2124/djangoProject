from django.urls import path
from.import views


urlpatterns = [
    path('<int:course_id>/', views.Details, name='detail'),
    path('', views.Courses, name='home-page'),
]