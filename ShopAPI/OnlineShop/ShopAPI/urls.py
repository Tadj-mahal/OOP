from django.urls import path
from .views import GoodAPIView

urlpatterns=[
    path('<token>', GoodAPIView.get.as_view()),
    path('<token>', GoodAPIView.post.as_view()),
]