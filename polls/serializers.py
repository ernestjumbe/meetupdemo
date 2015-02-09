from swampdragon.serializers.model_serializer import ModelSerializer
#from .models import Question, Choice

class QuestionSerializer(ModelSerializer):
    choice_set = 'ChoiceSerializer'
    class Meta:
        model = 'polls.Question'
        # Fields you want to publish via the router
        publish_fields = ('question_text', )
        #  Any fields you have added that you would ike to update via the router
        update_fields = ('bar', )


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = 'polls.Choice'
        # Fields you want to publish via the router
        publish_fields = ('question_text', )
        # Any fields you have added that you would ike to update via the router
        update_fields = ('bar', )