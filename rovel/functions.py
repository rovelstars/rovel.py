import requests

BASE_URL = "https://rovelapi.glitch.me"

def post_guild_stats(bot_id, token, guild):
    return requests.post(f"https://bots.rovelstars.ga/api/v1/bots/{bot_id}/stats", headers={
        "Authorization": token,
        "Content-Type": "application/json"
    })

def chat(user_id, message):
    return requests.get(BASE_URL + f"/chat?user={user_id}&msg={message}").text

def base():
    return requests.get(BASE_URL).text

def download(url, dest):
    resp = requests.get(url)
    if resp.ok:
        with open(dest, "x") as f:
            f.write(resp.text)
    else:
        raise Exception(f"Server responded with {resp.status_code}: {resp.content}")
