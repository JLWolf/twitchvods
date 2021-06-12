# TwitchVODs

Watch Sub-only VODs, and deleted VODs from Twitch.

# how to use
1. Run the script
2. Enter a Twitch Tracker URL Ex. https://twitchtracker.com/gamesdonequick/streams/42312689085
3. A link to the vod will be generated! Ex. https://d2vjef5jvl6bfs.cloudfront.net/78a4379902f6dc60c409_gamesdonequick_42312689085_1623365391/360p30/index-dvr.m3u8

# Notes
The domains that host these .m3u8 files change periodically. 
The current domain for this script is set to https://d2vjef5jvl6bfs.cloudfront.net and will not be automatically updated.
if the VOD is not found on that domain then the script will print "VOD not found".

Past domains have been:
https://vod-secure.twitch.tv
https://vod-metro.twitch.tv
https://dqrpb9wgowsf5.cloudfront.net
https://d2e2de1etea730.cloudfront.net
https://ds0h3roq6wcgc.cloudfront.net
https://dgeft87wbj63p.cloudfront.net
https://d3c27h4odz752x.cloudfront.net
https://d2aba1wr3818hz.cloudfront.net

to find future domains:
Check the request URL for the channel VOD's thumbnails. This will contain the domain for that channel's .m3u8 files.

