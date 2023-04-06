from dataclasses import dataclass
from typing import Optional
from enum import Enum




@dataclass
class GameParameters:
    game_id: str
    week: int
    season: int
    team: str

    def to_params(self) -> dict[str,str]:
        return {
            "GameId": (self.game_id),
            "Week": (self.week),
            "Season": (self.season),
            "Team": (self.team)
        }
    
@dataclass
class ScheduleParameters:
    week: Optional[int]
    season: Optional[int]
    team: Optional[str]   

    def to_params(self) -> dict[str,str]:
        return {
            "Week": (self.week),
            "Season": (self.season),
            "Team": (self.team)
        }
    
@dataclass
class ResultsParameters:
    team: str
    opposition: str
    game_offset: int
    game_type: str

    def to_params(self) -> dict[str,str]:
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

