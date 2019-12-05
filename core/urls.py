from django.urls import path
from.views import about,Work,home,contact, ProjectView

app_name='core'
urlpatterns = [
	path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('work/', Work.as_view(), name='work'),
    path('project/<slug>/', ProjectView.as_view(), name='project'),

]
