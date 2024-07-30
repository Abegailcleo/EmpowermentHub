from django.urls import path, include

from . import admin
from . import views
from rest_framework.routers import DefaultRouter
from .views import JobListingViewSet, EducationalResourceViewSet, FinancialAssistanceViewSet, CommunitySupportViewSet,UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
 

urlpatterns = [
    path('', views.home, name='index'),  # Root URL of the core app is handled by 'home' view.
    path('',views.homey, name ='home'),
    path('about/', views.about, name='about'),
    path('job_listing/',views.job_listing,name = 'job_listing'),
    path('educational_resource/',views.educational_resource,name = 'educational_resource'),
    path('financial_assistance/',views.financial_assistance,name = 'financial_assistance'),
    path('login/',views.login,name = 'login'),
    path('user-reasearch/',views.user_research,name = 'user_research'),
    path('community_support/',views.community_support,name = 'community_support'),
    path('sign-up/', views.sign_up, name='sign_up'), 
    path('share_opportunities/', views.share_opportunities, name='share_opportunities'),
    
    


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
]
