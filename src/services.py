from typing import Any, Dict, List
from src.config_local import ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET
import tweepy
from src.connections import trends_collecton
from src.constants import BRAZIL_WOE_ID

def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:
    trends = api.get_place_trends(woe_id)
    return trends[0]["trends"]

def get_trends() -> List[Dict[str, Any]]:
    trends = trends_collecton.find({})
    return list(trends)

def save_trends() -> None:
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    trends = _get_trends(woe_id=BRAZIL_WOE_ID, api=api)
    trends_collecton.insert_many(trends)
    