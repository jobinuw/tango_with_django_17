from django.conf.urls import url, include
from rest import views
from rest_framework.urlpatterns import format_suffix_patterns


# Serializers define the API representation.


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^snip/$', views.snippet_list),
    url(r'^snip/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^cat/$', views.SnippetList.as_view()),
    url(r'^cat/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]