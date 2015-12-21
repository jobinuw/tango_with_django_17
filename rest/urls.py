from django.conf.urls import url, include
from rest import views


# Serializers define the API representation.


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^snip/$', views.snippet_list),
    url(r'^snip/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]