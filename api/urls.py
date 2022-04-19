from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
# from tasks.models import Tasks
from . import views


urlpatterns = [
    path('', views.ViewAPIHome.as_view()),
    path('auth/', include('rest_framework.urls'), name="auth"),
    path('create/', views.TaskCreateAPIView.as_view(), name="create"),
    path('list/', views.TaskListAPIView.as_view(), name="list"),
    path('detail/<int:pk>/', views.TaskDetailAPIView.as_view(), name="detail"),
    path('update/<int:pk>/', views.TaskUpdateAPIView.as_view(), name="update"),
    path('delete/<int:pk>/', views.TaskDestroyAPIView.as_view(), name="delete"),
    path('status-update/<int:pk>/', views.TaskStatusUpdateAPIView.as_view(), name="status"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]