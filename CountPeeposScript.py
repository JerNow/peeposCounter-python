import urllib.request, re, json
url = "https://tmi.twitch.tv/group/user/trynet123/chatters"
with urllib.request.urlopen(url) as response:
   html = response.read()
   myJson = json.loads(html)
   myString = json.dumps(myJson)
   peepoList = re.findall("peepo", myString)

print(len(peepoList))