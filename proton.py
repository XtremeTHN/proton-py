import requests, json, re
from random import randrange

def DefaultFormater(title):
    print(title)

class ProtonDB():
    def __init__(self):
        self.games = json.loads(requests.get("https://protondb.max-p.me/games/").content.decode())
    
    def get_games(self, formater=DefaultFormater) -> None:
        for x in self.games:
            DefaultFormater(x["title"])

    def get_game_id(self, game_title: str) -> int | None:
        for x in self.games:
            if re.search(game_title, x["title"], re.IGNORECASE):
                return x["appId"], x["title"]
            else:
                continue
        return None, None
    def get_game_reports(self, game_id: int) -> tuple:
        obj = json.loads(requests.get(f"https://protondb.max-p.me/games/{game_id}/reports").content.decode())
        rates_count = {"Borked":0,"Bronze":0,"Silver":0,"Gold":0,"Platinum":0}
        if obj:
            for x in obj:
                rates_count[x["rating"]] += 1
            return max(rates_count, key=lambda k: rates_count[k]), obj[randrange(0, len(obj))]["notes"]
