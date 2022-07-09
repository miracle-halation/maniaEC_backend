from rest_framework import routers
from .views import CompanyViewset

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewset)
