from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyObtainTokenPairView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('getlist/', views.WatchListViewSet.get_object),
    path('add/', views.WatchListViewSet.add_symbol),
    path('delete/', views.WatchListViewSet.del_symbol),
    path('depth/', views.PriceDepth.as_view(),)
]