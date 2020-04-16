from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('employer/', views.employer_list, name='employer_list'),
    path('', HomeView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='searh'),
    # path('', views.employer_list, name='employer_list'),
    path('jobs/', JobListView.as_view(), name='jobs'),
    # path('jobs/', views.jobs_list, name='jobs_list'),
    path('employer/<int:pk>', views.employer_detail, name='employer_detail'),
    # path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    path('job/<int:pk>', views.job_detail, name='job_detail'),
    path('employer/new', views.employer_create, name='employer_create'),
    path('job/new', views.job_create, name='job_create'),
    path('employer/<int:pk>/edit', views.employer_edit, name='employer_edit'),
    path('job/<int:pk>/edit', views.job_edit, name='job_edit'),
    path('employer/<int:pk>/delete', views.employer_delete, name='employer_delete'),
    path('job/<int:pk>/delete', views.job_delete, name='job_delete')
      # path('', views.jobsearch_list, name='jobsearch_list'),
] 