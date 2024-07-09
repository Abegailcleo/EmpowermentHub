from rest_framework import serializers
from .models import JobListing, EducationalResource, FinancialAssistance, CommunitySupport
from django.contrib.auth.models import User


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



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user