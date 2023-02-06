from django.urls import path
from .views import TeamView
from .views import TeamParamsView

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<team_id>/", TeamParamsView.as_view()),
]
