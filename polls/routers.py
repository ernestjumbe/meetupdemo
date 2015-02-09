from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from .serializers import QuestionSerializer, ChoiceSerializer
from .models import Question, Choice

class QuestionRouter(ModelRouter):
    route_name = 'questions-list'
    serializer_class = QuestionSerializer
    model = Question

    # return a single question by 'pk'
    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])

    # return all your questions
    def get_query_set(self, **kwargs):
        return self.model.objects.all()

class ChoiceRouter(ModelRouter):
    serializer_class = ChoiceSerializer
    route_name = 'choice-route'

    # get a single choice by 'pk'
    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])

    # return all your choices for a question
    def get_query_set(self, **kwargs):
        return self.model.objects.filter(question__id=kwargs['q_id'])

route_handler.register(QuestionRouter)
route_handler.register(ChoiceRouter)