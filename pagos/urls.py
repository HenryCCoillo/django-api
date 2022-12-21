from . import api
from rest_framework import routers
from apipagos.api import ServideViewSet,PaymentUserViewSet,ExproredPaumentViewSet
router = routers.DefaultRouter()
router.register(r'pagos', api.PagoViewSet, 'pagos')
router.register(r'service', ServideViewSet, 'service')
router.register(r'pago-user', PaymentUserViewSet, 'pago-user')
router.register(r'pago-exprored', ExproredPaumentViewSet, 'pago-exprored')

urlpatterns = router.urls