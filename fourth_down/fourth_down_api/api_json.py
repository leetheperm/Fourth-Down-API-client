from .fourth_down_api_base import FourthDownApiBase
from .parameters import (
    GameParameters, ScheduleParameters
)

class ForthDownApiJson(FourthDownApiBase):
    def game_plays(self, parameters: GameParameters, verbose: bool = False):
        return self._get(self._game_plays_request(parameters, verbose))

    def game_drives(self, parameters: GameParameters, verbose: bool = False):
        return self._get(self._game_drives_request(parameters, verbose))

    def game_scores(self, parameters: GameParameters, verbose: bool = False):
        return self._get(self._game_scores_request(parameters, verbose))
    
    def all_teams(self, verbose: bool = False):
        return self._get_without_params(self._all_teams_request(verbose))
    
    def schedule(self, parameters: ScheduleParameters = {}, verbose: bool = False):
        return self._get(self._schedule_request(parameters,verbose))
    
    def schedule_results(self, parameters: ScheduleParameters = {}, verbose: bool = False):
        return self._get(self._schedule_results_request(parameters,verbose))
    
    # def play_by_play(self, parameters, verbose: bool = False):
    #     return self._get(self.)