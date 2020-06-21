from django.urls import path
from berkeleyApp.api.views import visit_count

app_name = 'berkeleyapp'

urlpatterns = [
    path('', visit_count, name="visit_counter"),
]
