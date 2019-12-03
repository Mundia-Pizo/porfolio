from django.urls import path
from.views import about,work,home,contact, ProjectView

app_name='core'
urlpatterns = [
	path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('work/', work, name='work'),
    path('project/', ProjectView.as_view(), name='project'),
]
