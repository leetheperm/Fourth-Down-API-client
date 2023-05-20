from fourth_down_api.api_json import ForthDownApiJson
from fourth_down_api.parameters import ResultsParameters, ScheduleParameters
from fourth_down_api.fourth_down_api_base import FourthDownEnvironment, FourthDownApiBase
import pytest


@pytest.fixture
def get_teams_request():
    # Arrange
    sut = ForthDownApiJson(endpoint=FourthDownEnvironment.local)
    base = FourthDownApiBase

    # Act
    req = sut._all_teams_request(base._all_teams_request)

    return req


# Assert
def test_params_are_empty_for_team_request(get_teams_request):
    response = get_teams_request()
    assert response.params == {}


def test_path_is_correct_for_team_request(get_teams_request):
    response = get_teams_request()
    assert response.params == {}

