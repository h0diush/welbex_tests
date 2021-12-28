from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from main.models import BaseModel
from .serializers import BaseModelSerializer


class BaseModelListView(ReadOnlyModelViewSet):
    queryset = BaseModel.objects.all()
    permission_classes = [AllowAny]
    serializer_class = BaseModelSerializer
