import hashlib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as BS
import re
import datetime


reg_url = input("Enter Twitch Tracker URL: ").strip()
parsedUrl = re.split('https://twitchtracker.com/(\w+)/streams/(\w+)', reg_url)
name = parsedUrl[1]
vod = parsedUrl[2]

headers = {'User-Agent': "Magic Browser"}
req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()


soupHtml = BS(html, "html.parser")
timeString = (soupHtml.find("meta", {"name":"description"})['content'])

timeTemp = re.compile(name, re.IGNORECASE)
timeTemp = timeTemp.sub("", timeString)
timeTemp = re.findall(r'\d+', timeTemp)

timeList = list(map(str, timeTemp))
myDate = timeList[0] + '/' + timeList[1] + '/' + timeList[2] + " " + timeList[3]+ ':' + timeList[4] + ':' + timeList[5]
dateTime = (datetime.datetime.strptime(myDate, "%Y/%m/%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc))
timestamp = int(dateTime.timestamp())


formattedEnding = name + "_" + vod + "_" + str(timestamp)

hash = str(hashlib.sha1(formattedEnding.encode('utf-8')).hexdigest())

urlHash = hash[:20]

finalString = urlHash + '_' +  formattedEnding

urlFinal = "https://d2vjef5jvl6bfs.cloudfront.net/" + finalString + "/chunked/index-dvr.m3u8"

try:
    print(urlopen(urlFinal).getcode())
    print(urlFinal)
except:
    print("VOD not found.")
