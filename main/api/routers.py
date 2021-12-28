from rest_framework.routers import DefaultRouter

from .views import BaseModelListView

router = DefaultRouter()

router.register('', BaseModelListView, basename='www')

urlpatterns = [] + router.urls
