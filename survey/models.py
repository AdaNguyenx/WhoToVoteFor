from django.db import models

class SurveyResponse(models.Model):

	answer = models.CharField(max_length=2)


