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
    # Educational Resources
    path('tech_educational_resources/', views.tech_educational_resources, name='tech_educational_resources'),
    path('language_educational_resources/', views.language_educational_resources, name='language_educational_resources'),
    path('arts_and_crafts_educational_resources/', views.arts_and_crafts_educational_resources, name='arts_and_crafts_educational_resources'),
    path('financial_assistance/',views.financial_assistance,name = 'financial_assistance'),
    path('login/',views.login,name = 'login'),
    path('user-reasearch/',views.user_research,name = 'user_research'),
    path('community_support/',views.community_support,name = 'community_support'),
    # Community Support
    path('mentorship/',views.mentorship,name = 'mentorship'),
    path('community-forum/',views.community_forum,name = 'community_forum'),
    path('mental-health-resources/',views.mental_health_resources,name = 'mental_health_resources'),
    path('sign_up/', views.sign_up, name='sign_up'), 
    path('share_opportunities/', views.share_opportunities, name='share_opportunities'),
    path('dashboard/',views.dashboard, name='dashboard'),
    
    


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
]
