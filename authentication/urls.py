# urls.py

from django.urls import path

from .views import (
    GetUserDataView,
    LoginView,
    RegisterView,
    TaskListCreateView,
    TaskRetrieveUpdateDeleteView,
    UpdateUserDataView,
    update_password,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("get_user_data/", GetUserDataView.as_view(), name="get_user_data"),
    path("update_user_data/", UpdateUserDataView.as_view(), name="update_user_data"),
    path("update_password/", update_password, name="update_password"),
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path(
        "tasks/<int:pk>/",
        TaskRetrieveUpdateDeleteView.as_view(),
        name="task-retrieve-update-delete",
    ),
]
