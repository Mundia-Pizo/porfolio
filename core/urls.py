from django.urls import path
from.views import about,Work,home,contact, WorkDetailView, ProjectView

app_name='core'
urlpatterns = [
	path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('list/', Work.as_view(), name='list'),
    path('<slug>/', WorkDetailView.as_view(), name='project'),
]
