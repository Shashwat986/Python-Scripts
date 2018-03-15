import requests
import datetime
import time
import json
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.cfg')

API_KEY = config.get('API_KEY', 'key')


URL_HASH = {
  "NA": "https://na.api.pvp.net",
  "EUW": "https://euw.api.pvp.net",
  "EUNE": "https://eune.api.pvp.net"
}

URL = URL_HASH["NA"]

def query(url, params = None):
  if params is None:
    params = {}
  params["api_key"] = API_KEY
  resp = requests.get(URL + url, params)

  if resp.status_code == 200:
    return json.loads(resp.text)
  elif resp.status_code == 429:
    print "Rate limit exceeded. Waiting 10s"
    time.sleep(10)
    query(url)
  else:
    print "Query Failed: ", url
    print "Error code:", resp.status_code
    return None


#summoner_name = "".join("ShashMan".lower().split())
#summoner = query("/api/lol/na/v1.4/summoner/by-name/" + summoner_name)
#summoner_id = summoner[summoner_name]["id"]
#print summoner_id

summoner_id = str(35053467)

match_list = query('/api/lol/na/v2.2/matchlist/by-summoner/' + summoner_id)

print len(match_list["matches"])

duration = {}
for match_obj in match_list["matches"]:
  try:
    match_id = str(match_obj["matchId"])
    match = query('/api/lol/na/v2.2/match/' + match_id, {"includeTimeline": True})

    if match is None: continue

    print match["matchId"], "...",

    total_duration = match["matchDuration"]

    team_ids = None
    team1 = []
    team2 = []
    for p in match["participants"]:
      if team_ids is None:
        team_ids = p["teamId"]

      if p["teamId"] == team_ids:
        team1.append(p["participantId"])
      else:
        team2.append(p["participantId"])

    for frame in match["timeline"]["frames"]:
      gold_team_1 = 0
      gold_team_2 = 0
      for p_id in frame["participantFrames"]:
        if int(p_id) in team1:
          gold_team_1 += frame["participantFrames"][p_id]["totalGold"]
        else:
          gold_team_2 += frame["participantFrames"][p_id]["totalGold"]

      gold_diff = abs(gold_team_1 - gold_team_2)

      time_frame = frame["timestamp"]/1000
      game_duration_since = total_duration - time_frame
      if game_duration_since < 0:
        game_duration_since = 0

      duration[int(gold_diff / 1000)] = duration.get(int(gold_diff / 1000), []) + [game_duration_since]

    print "Done"
  except (KeyError, TypeError):
    print "failed"
    continue

for k in duration:
  avg = int(1.0 * sum(duration[k])/len(duration[k]))
  print "Gold diff of {}k gold takes {} time.".format(k, datetime.timedelta(seconds=avg))
