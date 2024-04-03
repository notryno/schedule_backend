from django.urls import path

from .views import ClassroomViewList

urlpatterns = [
    path("class/", ClassroomViewList.as_view(), name="class-list"),
]
