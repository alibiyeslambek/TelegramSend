from django.conf.urls import url

#from .views import CommandReceiveView
from .views import index, send_message

urlpatterns = [
    #url(r'^bot/(?P<bot_token>.+)/$', CommandReceiveView.as_view(), name='command'),
    url(r'^send_message$', send_message, name='send_message'),
    url(r'^$', index, name='index'),
]
