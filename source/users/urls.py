from django.urls import path

from users.views import LoginView, logout_view, RegisterView, ProfileView

urlpatterns =[
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    # path('profile/<int:pk>/change', UserChangeView.as_view(), name='change')
]