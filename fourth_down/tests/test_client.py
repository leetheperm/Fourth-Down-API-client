from fourth_down_api.api_json import ForthDownApiJson
from fourth_down_api.parameters import ResultsParameters, ScheduleParameters
from fourth_down_api.fourth_down_api_base import FourthDownEnvironment, FourthDownApiBase
import pytest


@pytest.fixture
def get_teams_request():
    sut = ForthDownApiJson(endpoint=FourthDownEnvironment.production)
    base = FourthDownApiBase

    req = sut._all_teams_request(base._all_teams_request)

    return req


def test_params_are_empty_for_team_request(get_teams_request):
    assert get_teams_request.params == {}


def test_path_is_correct_for_team_request(get_teams_request):
    assert get_teams_request.path == "/api/teams"
