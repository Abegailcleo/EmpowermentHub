from django.shortcuts import render

from rest_framework import viewsets
from .models import JobListing, EducationalResource, TechEducationalResource, FinancialAssistance, CommunitySupport
from .serializers import JobListingSerializer, EducationalResourceSerializer, TechEducationalResourceSerializer, FinancialAssistanceSerializer, CommunitySupportSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

def home(request):
    return render(request, 'core/index.html')

def homey(request):
    return render(request,'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def resource_sections(request):
    return render(request, 'core/resource_sections.html')

def job_listing(request):
    return render(request, 'core/job_listing.html')

def educational_resource(request):
    return render(request, 'core/educational_resource.html')

def tech_educational_resources(request):
    return render(request, 'core/tech-educational-resources.html')

def some_view(request):
    # Some processing
    url = reverse('tech_educational_resources')
    return redirect(url)



def financial_assistance(request):
    return render(request, 'core/financial_assistance.html')

def community_support(request):
    return render(request, 'core/community_support.html')

def login(request):
    return render(request, 'core/login.html')

def user_research(request):
    return render(request, 'core/user_research.html')

def share_opportunities(request):
    return render(request, 'core/share_opportunities.html')

def sign_up(request):
    return render(request, 'core/sign_up.html')
    
class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['title']

class EducationalResourceViewSet(viewsets.ModelViewSet):
    queryset = EducationalResource.objects.all()
    serializer_class = EducationalResourceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['title']

class TechEducationalResourcesResourceViewSet(viewsets.ModelViewSet):
    queryset = TechEducationalResource.objects.all()
    serializer_class = TechEducationalResourceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['title']





class FinancialAssistanceViewSet(viewsets.ModelViewSet):
    queryset = FinancialAssistance.objects.all()
    serializer_class = FinancialAssistanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['title']

class CommunitySupportViewSet(viewsets.ModelViewSet):
    queryset = CommunitySupport.objects.all()
    serializer_class = CommunitySupportSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['title']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['title']
