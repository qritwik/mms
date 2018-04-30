from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index , name = 'index'),
    url(r'^internal/', views.upload_file , name = 'internal'),
    #url(r'^templates/internal.html', views.internal , name = 'internal'),
    url(r'^templates/external.html', views.external , name = 'external'),
    url(r'^templates/individual.html', views.individual , name = 'individual'),
    url(r'^pass_fail/', views.pass_fail_view , name = 'pass_fail'),
    url(r'^range_marks/', views.range_marks_view , name = 'range_marks'),
    url(r'^list/', views.list_view , name = 'list'),
    
]
