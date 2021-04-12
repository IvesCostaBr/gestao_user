from django.urls import path
from .views import CreateUserData
urlpatterns = [
    path('adicionar_cadastro/', CreateUserData.as_view(), name='create_user'),
]
