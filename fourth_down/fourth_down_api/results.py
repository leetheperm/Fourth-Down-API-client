from dataclasses import dataclass

@dataclass
class GameFields:
    game_id: dict
    home_team: dict
    visitor_team: dict
    plays: list[dict]

    @classmethod
    def from_dict(cls, d: dict):
        return(cls(
            game_id=d["game"],
            home_team=d["homeTeam"],
            visitor_team=d["visitorTeam"],
            plays=d["plays"]
        ))
    
@dataclass
class TeamFields:
    city : str
    name : str
    abbrevation: str
    conference: str
    division: str
    label: str
    team_name_label: str

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            city=d["city"],
            name=d["name"]
            abbrevation=d["abbrevation"]
            conference=d["conference"]
            division=d["division"]
            label=d["label"]
            team_name_label=d["teamNameLabel"])
    

@dataclass
class ScheduleFields:
    game_id: str
    season: int
    game_type: str
    week: int
    game_day: str
    week_day: str
    game_time: str
    away_team: str
    home_team: str
    home_score: int
    location: str
    result: int
    total: int
    over_time: bool
    old_game_id: str
    away_rest: int
    home_rest: int
    away_money_line: float
    home_money_line: float
    spread_line: float
    away_spread_odds: float
    home_spread_odds: float
    total_line: float
    under_odds: float
    over_odds: float
    div_game: bool
    roof: str
    surface: str
    temp: int
    wind: int
    away_coach: str
    home_coach: str
    referee: str
    stadium_id: str
    stadium: str


