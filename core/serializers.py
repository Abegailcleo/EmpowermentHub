from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = '__all__'

class EducationalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalResource
        fields = '__all__'

# Educational Resources Serializers
class TechEducationalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechEducationalResource
        fields = '__all__'


class LanguageEducationalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageEducationalResource
        fields = '__all__'


class ArtsAndCraftsEducationalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtsAndCraftsEducationalResource
        fields = '__all__'

class BusinessAndEconomicsResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAndEconomicsResources
        fields = '__all__'

class HealthAndWellnessResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthAndWellnessResources
        fields = '__all__'

class CareerDevelopmentResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerDevelopmentResources
        fields = '__all__'



# Community Support Serializers
class CommunitySupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunitySupport
        fields = '__all__'

class MentorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = '__all__'


class CommunityForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityForum
        fields = '__all__'


class MentalHealthResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalHealthResources
        fields = '__all__'


class FinancialAssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialAssistance
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