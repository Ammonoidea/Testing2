import os



def add_stuff():
	python_topic = add_topic('Python', views=128,likes=64)
	add_site(top = python_topic, title='Official Python Tutorial',url='http://docs.python.org/2/tutorial/')
	add_site(top = python_topic, title='How to Think Like A Computer Scientist',url='http://www.greenteapress.com/thinkpython')
	add_site(top = python_topic, title='',url='http://www.korokithakis.net/tutorial/python')

	django_topic = add_topic('Django',views=64,likes=32)
	add_site(top = django_topic, title='Official Django Tutorial',url='http://docs.djangoproject.com/en/1.5/intro/tutorial01')
	add_site(top = django_topic, title='Django Rocks',url='http://www.djangorocks.com')
	add_site(top = django_topic, title='How To Tango With Django',url='http://www.tangowithdjango.com/')

	frame_topic = add_topic('Other Frameworks',views=32,likes=16)
	add_site(top = frame_topic, title='Bottle',url='http://bottlepy.org/docs/dev')
	add_site(top = frame_topic, title='Flask',url='flask.pocoo.org')

	for t in Topic.objects.all():
		for s in Site.objects.all():
			print '-{0}-{1}'.format(str(t),str(s))

def add_site(top, title, url, views=0):
	#wget_or_created will get or create a thing, 
	s = Site.objects.get_or_create(topic= top, title=title, url=url, views=views)[0]
	return s

def add_topic(name, views, likes):
	t = Topic.objects.get_or_create(name=name, views=views, likes=likes)[0]
	return t

if __name__ == '__main__':
	print 'Starting Rango Population Script'
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
	from rango.models import Topic, Site
	add_stuff()
