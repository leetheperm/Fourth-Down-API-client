from .api_base import ApiBase, ApiRequest
from .environment import FourthDownEnvironment
from .parameters import GameParameters, ScheduleParameters
from typing import Optional


class FourthDownApiBase(ApiBase):

    def __init__(self, endpoint: FourthDownEnvironment, headers: dict[str, str] = {}) -> None:
        super().__init__(endpoint, headers)

    def _game_plays_request(self, parameters: GameParameters, verbose: bool = False) -> ApiRequest:
        return ApiRequest(
            path="/api/game/plays",
            params=parameters.to_params(),
            headers={},
            verbose=verbose
        )

    def _game_drives_request(self, parameters: GameParameters, verbose: bool = False) -> ApiRequest:
        return ApiRequest(
            path="/api/game/drives",
            params=parameters.to_params(),
            headers={},
            verbose=verbose
        )

    def _game_scores_request(self, parameters: GameParameters, verbose: bool = False) -> ApiRequest:
        return ApiRequest(
            path="/api/game/scoringSummaries",
            params=parameters.to_params(),
            headers={},
            verbose=verbose
        )

    def _all_teams_request(self, verbose: bool = False) -> ApiRequest:
        return ApiRequest(
            path="/api/teams",
            headers={},
            verbose=verbose
        )

    def _schedule_request(self, parameters: Optional[ScheduleParameters], verbose: bool = False) -> ApiRequest:
        return ApiRequest(
            path="/api/schedule",
            params=parameters.to_params(),
            headers={},
            verbose=verbose
        )

    def _schedule_results_request(self, parameters: ScheduleParameters, verbose: bool = False) -> ApiRequest:
        return ApiRequest(
            path="/api/schedule/results",
            params=parameters.to_params(),
            headers={},
            verbose=verbose
        )

    def _play_by_play_request(self, parameters, verbose: bool = False) -> ApiRequest:
        return ApiRequest(
            path="/api/nflfastr",
            params=parameters.to_params(),
            headers={},
            verbose=verbose
        )
