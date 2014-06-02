from django.contrib import admin
from rango.models import Topic, Site

class SiteAdmin(admin.ModelAdmin):
	"""docstring for TopicAdmin"""
	list_display=('topic', 'title', 'url', 'views')

class TopicAdmin(admin.ModelAdmin):
	"""docstring for TopicAdmin"""
	list_display=('name', 'views', 'likes')
		

admin.site.register(Topic,TopicAdmin)
admin.site.register(Site, SiteAdmin)