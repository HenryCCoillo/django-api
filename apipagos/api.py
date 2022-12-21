from .models import Service,PaymentUser, ExproredPaument
from rest_framework import viewsets
from .serializers import ServiceSerializer, PaymentUserSerializer,ExproredPaumentSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission,SAFE_METHODS,AllowAny
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 

class ServideViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.get_queryset().order_by('id')
    serializer_class = ServiceSerializer

    pagination_class = StandardResultsSetPagination
    throttle_scope = 'service'

    def get_permissions(self):
        if self.action == "list" or self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class PaymentUserViewSet(viewsets.ModelViewSet):
    queryset = PaymentUser.objects.get_queryset().order_by('id')
    serializer_class = PaymentUserSerializer

    pagination_class = StandardResultsSetPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ['payment_date','expiration_date']
    throttle_scope = 'pagouser'

    def get_permissions(self):
        if self.action == "list" or self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class ExproredPaumentViewSet(viewsets.ModelViewSet):
    queryset = ExproredPaument.objects.get_queryset().order_by('id')
    serializer_class = ExproredPaumentSerializer
    pagination_class = StandardResultsSetPagination
    throttle_scope = 'service'

    def get_permissions(self):
        if self.action == "list" or self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated&ReadOnly]
        return [permission() for permission in permission_classes]

