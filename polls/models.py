from django.db import models

# Publishes a new object as soon as it is created
from swampdragon.models import SelfPublishModel

from .serializers import QuestionSerializer, ChoiceSerializer

class Question(SelfPublishModel, models.Model):
	# Serializes the model
	serializer_class = QuestionSerializer
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')


class Choice(SelfPublishModel, models.Model):
	serializer_class = ChoiceSerializer
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)