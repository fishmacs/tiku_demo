from django.conf.urls import patterns, url
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

#from django.contrib import admin

import demo.views as v
from tiku_demo import settings

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'tiku_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^questions', v.question_list),

    #url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL)
