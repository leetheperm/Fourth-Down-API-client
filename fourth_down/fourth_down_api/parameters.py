from dataclasses import dataclass
from typing import Optional
from enum import Enum


@dataclass
class GameParameters:
    game_id: Optional[str] = "2023_01_DAL_LA"
    week: Optional[int] = 1
    season: Optional[int] = 2022
    team: Optional[str] = "LA"

    def to_params(self) -> dict[str, str]:
        return {
            "GameId": (self.game_id),
            "Week": (self.week),
            "Season": (self.season),
            "Team": (self.team)
        }


@dataclass
class ScheduleParameters:
    week: Optional[int] = None
    season: Optional[int] = None
    team: Optional[str] = None

    def to_params(self) -> dict[str, str]:
        return {
            **({"week": self.week} if self.week is not None else {}),
            **({"Season": self.season} if self.season is not None else {}),
            **({"Team": self.team} if self.team is not None else {})
        }


@dataclass
class ResultsParameters:
    team: Optional[str] = "NYJ"
    opposition: Optional[str] = "LA"
    game_offset: Optional[int] = 1
    game_type: Optional[str] = "REG"

    def to_params(self) -> dict[str, str]:
        return {
            "Team": (self.team),
            "Opposition": (self.opposition),
            "gameOffset": (self.game_offset),
            "gameType": (self.game_type)
        }


class GameType(Enum):
    regular = "Reg"
    post = "Post"
    all = "All"