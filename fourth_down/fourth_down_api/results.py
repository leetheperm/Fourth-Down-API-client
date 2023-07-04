from dataclasses import dataclass


@dataclass
class GamePlayFields:
    game_id: dict
    home_team: dict
    visitor_team: dict
    plays: list[dict]

    @classmethod
    def from_dict(cls, d: dict):
        return (cls(
            game_id=d["game"],
            home_team=d["homeTeam"],
            visitor_team=d["visitorTeam"],
            plays=d["plays"]
        ))
    
@dataclass
class ScoringSummariesFields:
    game_id: dict
    home_team: dict
    visitor_team: dict
    scoring_summaries: list[dict]

    @classmethod 
    def from_dict(cls, d: dict):
        return (cls(
            game_id=d["game"],
            home_team=d["homeTeam"],
            visitor_team=d["visitorTeam"],
            scoring_summaries=d["scoringSummaries"]
        ))


@dataclass
class TeamFields:
    city: str
    name: str
    abbrevation: str
    conference: str
    division: str
    label: str
    team_name_label: str

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            city=d["city"],
            name=d["name"],
            abbrevation=d["abbrevation"],
            conference=d["conference"],
            division=d["division"],
            label=d["label"],
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

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
                game_id=d["game"],
                season=d["season"],
                game_type=d["gameType"],
                week=d["week"],
                game_day=d["gameday"],
                week_day=d["weekday"],
                game_time=d["gametime"],
                away_team=d["awayTeam"],
                home_team=d["homeTeam"],
                home_score=d["homeScore"],
                location=d["location"],
                result=d["result"],
                total=d["total"],
                over_time=d["overtime"],
                old_game_id=d["oldGameId"],
                away_rest=d["awayRest"],
                home_rest=d["homeRest"],
                away_money_line=d["awayMoneyLine"],
                home_money_line=d["homeMoneyLine"],
                spread_line=d["spreadLine"],
                away_spread_odds=d["awaySpreadOdds"],
                home_spread_odds=d["homeSpreadOdds"],
                total_line=d["totalLine"],
                under_odds=d["underOdds"],
                over_odds=d["overOdds"],
                div_game=d["divGame"],
                roof=d["roof"],
                surface=d["surface"],
                temp=d["temp"],
                wind=d["wind"],
                away_coach=d["awayCoach"],
                home_coach=d["homeCoach"],
                referee=d["refree"],
                stadium_id=d["stadiumId"],
                stadium=d["stadium"]
            )


@dataclass
class ErrorFields:
    title: str
    status_code: int
    errors: dict

    @classmethod
    def from_dict(cls, d: dict):
        return (cls(
            title=d["title"],
            status_code=d["status"],
            errors=d.get("errors")
        ))