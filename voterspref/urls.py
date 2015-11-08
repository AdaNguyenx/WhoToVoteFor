from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'voterspref.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'survey.views.home', name='home'),
    url(r'^results1/', 'survey.views.results1', name='results'),
    url(r'^results2/', 'survey.views.results2', name='results'),
    url(r'^marijuana/', 'survey.views.marijuana', name='facts'),
    url(r'^refugees/', 'survey.views.refugees', name='facts'),
    url(r'^abortions/', 'survey.views.abortions', name='facts'),
    url(r'^dealthpenalty/', 'survey.views.dealthpenalty', name='facts'),
    url(r'^healthcare/', 'survey.views.healthcare', name='facts'),
    url(r'^globalwarming/', 'survey.views.globalwarming', name='facts'),
    url(r'^gunsrights/', 'survey.views.gunsrights', name='facts'),
    url(r'^education/', 'survey.views.education', name='facts'),
    url(r'^veterans/', 'survey.views.veterans', name='facts'),
    url(r'^survey/', 'survey.views.some_view'),
    url(r'^admin/', include(admin.site.urls)),
]

