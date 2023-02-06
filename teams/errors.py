from rest_framework.views import status
import ipdb
from .models import Team

class NegativeTitlesError(Exception):

    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

    def valid_title(title):
        if title < 0:
            raise NegativeTitlesError({"error": "titles cannot be negative"}, status.HTTP_400_BAD_REQUEST)


class InvalidYearCupError(Exception):

    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        
    def valid_year(year):
        if year < 1930 or ((year - 1930) % 4) != 0: 
            raise InvalidYearCupError({"error": "there was no world cup this year"}, status.HTTP_400_BAD_REQUEST)

class ImpossibleTitlesError(Exception):

    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
    
    
    def valid_title(number_title, first_year, this_year):
        if number_title > ((this_year - first_year) / 4):
            raise ImpossibleTitlesError({"error": "impossible to have more titles than disputed cups"}, status.HTTP_400_BAD_REQUEST)

class NotfoundId(Exception):

    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

    def check_id(team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            raise NotfoundId({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        return team