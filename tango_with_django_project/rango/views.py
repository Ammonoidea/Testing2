from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Topic, Site



def index(request):
	#Gets details about the user. How much can I get?
	context = RequestContext(request)

	#specifies what to pass through to the html page
	topic_list = Topic.objects.order_by('likes')[:5]

	context_dict = {'topics' : topic_list, 'comm' : 'does this work?'}

	for topic in topic_list:
		topic.url = topic.name.replace(' ', '_')

	#returns template with the stuff. Note sure why we have to give context. We already gave context_dic
	return render_to_response('rango/index.html', context_dict, context)

def frontPage(request):
	return HttpResponse('This is the frontpage, yo! <a href=\'http://127.0.0.1:8000/rango/\'>""rango""</a>')

def about(request):
	#Gets details about the user. How much can I get?
	context = RequestContext(request)

	#specifies what to pass through to the html page
	context_dict = {'boldmessage' : str(context)}

	#returns template with the stuff. Note sure why we have to give context. We already gave context_dic
	return render_to_response('rango/about.html', context_dict, context)

def topic(request, topic_name_url):
	context = RequestContext(request)

	topic_name = topic_name_url.replace('_', ' ')

	context_dict = {'topic_name' : topic_name}

	try:
		topic = Topic.objects.get(name=topic_name)
		sites = Site.objects.filter(topic=topic)
		context_dict['sites'] = sites
		context_dict['topic'] = topic
		pass
	except Topic.DoesNotExist:
		pass

	return render_to_response('rango/topic.html', context_dict, context)