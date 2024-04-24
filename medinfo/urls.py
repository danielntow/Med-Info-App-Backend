# # urls.py

from . import views
from django.urls import path, include
from .views import DrugListView, DrugDetailView, DrugViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'drug-name', DrugViewSet)


# app_name = "medinfo"
# urlpatterns = [
#     path('', DrugListView.as_view(), name='drug-list'),
#     path('<int:pk>/', DrugDetailView.as_view(), name='drug-detail'),
#     path('', include(router.urls)),
# ]


router = DefaultRouter()
# router.register(r'drugs', views.DrugsViewSet)
# router.register(r'dosages', views.DosagesViewSet)
# Register other viewsets for related models here

app_name = "medinfo"
urlpatterns = [
    path('list', DrugListView.as_view(), name='drug-list'),
    path('<slug:name>/', DrugDetailView.as_view(), name='drug-detail'),
    path('', include(router.urls)),
]
