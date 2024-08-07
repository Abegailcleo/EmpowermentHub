from django.db import models

# Create your models here.





class JobListing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

class EducationalResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()


# Educational Resources

class TechEducationalResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()


class LanguageEducationalResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()


class ArtsAndCraftsEducationalResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()


class FinancialAssistance(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class CommunitySupport(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.CharField(max_length=100)


# Community Support
class Mentorship(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.CharField(max_length=100)


class CommunityForum(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.CharField(max_length=100)


class MentalHealthResources(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.CharField(max_length=100)