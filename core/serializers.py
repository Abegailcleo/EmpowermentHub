from rest_framework import serializers
from .models import JobListing, EducationalResource, FinancialAssistance, CommunitySupport

class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = '__all__'

class EducationalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalResource
        fields = '__all__'

class FinancialAssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialAssistance
        fields = '__all__'

class CommunitySupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunitySupport
        fields = '__all__'
