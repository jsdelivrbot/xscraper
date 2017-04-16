from django.shortcuts import render
from django.http import HttpResponse
from .model import Article

# Create your views here.


def home_page(request):
    latest_question_list = Article.objects.order_by('-pub_date')[:5]
    template = loader.get_template('vegasliving.html')
    context = {
        'latest_property_list': latest_property_list,
    }
    return HttpResponse(template.render(context, request))
