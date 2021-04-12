from django.urls import path, include
from user_data import urls as user_data_urls


urlpatterns = [
    path('painel_user/',include(user_data_urls),name='adicionar')
]
