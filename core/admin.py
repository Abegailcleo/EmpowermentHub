from django.contrib import admin

# Register your models here with the django admin.

from .models import JobListing, EducationalResource, FinancialAssistance, CommunitySupport, TechEducationalResource

admin.site.register(JobListing)
admin.site.register(EducationalResource)
admin.site.register(FinancialAssistance)
admin.site.register(CommunitySupport)
admin.site.register(TechEducationalResource)
