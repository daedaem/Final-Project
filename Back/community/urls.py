from django.urls import path
from . import views

# from rest_framework_jwt.views import obtain_jwt_token


app_name = 'community'

urlpatterns = [
    
    # path('signup/', views.signup, name='signup'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
#     path('<username>/', views.profile, name='profile'),
#     path('<int:user_pk>/follow/', views.follow, name='follow'),
    # path('api-token-auth/', obtain_jwt_token),
]