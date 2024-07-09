from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobListingViewSet, EducationalResourceViewSet, FinancialAssistanceViewSet, CommunitySupportViewSet,UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
 

router = DefaultRouter()
router.register(r'job-listings', JobListingViewSet)
router.register(r'educational-resources', EducationalResourceViewSet)
router.register(r'financial-assistance', FinancialAssistanceViewSet)
router.register(r'community-support', CommunitySupportViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
