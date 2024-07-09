from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobListingViewSet, EducationalResourceViewSet, FinancialAssistanceViewSet, CommunitySupportViewSet

router = DefaultRouter()
router.register(r'job-listings', JobListingViewSet)
router.register(r'educational-resources', EducationalResourceViewSet)
router.register(r'financial-assistance', FinancialAssistanceViewSet)
router.register(r'community-support', CommunitySupportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
