from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]

#eg: http://www.mysite.com/post/12345/
#^post/(\d+)/$
#(\d+) means that there will be a number (one or more digits) and that we want the number captured and extracted
#^ for beginning of the text
#$ for end of text
#\d for a digit
#+ to indicate that the previous item should be repeated at least once
#() to capture part of the pattern
