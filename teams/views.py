from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import Team
from .errors import *
import ipdb
from datetime import datetime

class TeamView(APIView):

    def post(self, request):
 
        teams_data = request.data

        date_world_cup = datetime.strptime(teams_data['first_cup'],  "%Y-%m-%d")
        year = int(date_world_cup.strftime("%Y"))
        datetime_atual = datetime.now()
        this_year = int(datetime_atual.strftime("%Y"))

        try:
            NegativeTitlesError.valid_title(teams_data['titles']), 
            InvalidYearCupError.valid_year(year), 
            ImpossibleTitlesError.valid_title(teams_data['titles'], year, this_year)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as err:
            return Response (err.message, err.status_code)

        team = Team.objects.create(
            name = teams_data['name'],
            titles = teams_data['titles'],
            top_scorer = teams_data['top_scorer'],
            fifa_code = teams_data['fifa_code'],
            first_cup = teams_data['first_cup'],
        )

        return Response(model_to_dict(team), 201)
        
    
    def get(self, request):

        teams = Team.objects.all()
        teams_list = []

        for team in teams:
            t = model_to_dict(team)
            teams_list.append(t)
            
        return Response(teams_list)

class TeamParamsView(APIView):
    
    def get(self, request, team_id):
        
        try: 
            NotfoundId.check_id(team_id)
        except NotfoundId as err:
            return Response (err.message, err.status_code)

        team = Team.objects.get(pk=team_id)

        return Response(model_to_dict(team))

    def patch(self, request, team_id):

        to_update = request.data

        try: 
            NotfoundId.check_id(team_id)
        except NotfoundId as err:
            return Response (err.message, err.status_code)

        team = Team.objects.get(pk=team_id)

        if 'name' in to_update:
            setattr(team, 'name', to_update['name'])
        if 'titles' in to_update:
            setattr(team, 'titles', to_update['titles'])
        if 'top_scorer' in to_update:
            setattr(team, 'top_scorer', to_update['top_scorer'])
        if 'fifa_code' in to_update:
            setattr(team, 'fifa_code', to_update['fifa_code'])
        if 'first_cup' in to_update:
            setattr(team, 'first_cup', to_update['first_cup'])
            
        team.save()

        return Response(model_to_dict(team))


    def delete(self, request, team_id):

        try: 
            NotfoundId.check_id(team_id)
        except NotfoundId as err:
            return Response (err.message, err.status_code)

        team = Team.objects.get(pk=team_id)
        team.delete()
        
        return Response(None, 204)

        
# Create your views here.
