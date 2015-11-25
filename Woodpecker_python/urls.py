from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Woodpecker_python.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$','index.views.login'),
    url(r'^register/$','index.views.register'),

    url(r'^main/$','main.views.main'),
    url(r'^left/$','main.views.left'),
    url(r'^welcome/$','main.views.welcome'),

    url(r'^extractor/$','extractor.views.extract'),
    url(r'^upload/$','extractor.views.input'),
    #url(r'^download/$','extractor.views.download'),

    url(r'^evaluation/$','evaluation.views.evaluate'),

    url(r'^history/$','history.views.showhistory'),
    #url(r'','log','history.views.log'),
    #url(r'^add/$','history.views.add',name='add'),
    #url(r'^ajax_list/$','history.views.ajax_list',name='ajax_list'),
    #url(r'^ajax_dict/$','history.views.ajax_dict',name='ajax_dict'),
    
    #url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS, 'show_indexes': True}),     
    #url(r'^staticfiles/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS, 'show_indexes': True}),     
    url(r'^staticfiles/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT, 'show_indexes': True}),     
    url(r'^download/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.DOWNLOAD_DIR, 'show_indexes': True}),     
)
