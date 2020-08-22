# Leaderboard Profiles - OBS Browser Source

![Leaderboard-rank-obs-browser-source](https://user-images.githubusercontent.com/6104940/90958560-2f1a5d00-e48d-11ea-889a-40c546a65ecc.png)


## 🚀 Quick start

- Open OBS, under your "Sources", add a "Browser source"
- Configure your C&C Community API webview settings and copy the URL 
- Paste the URL into OBS browser source and hit save. 

## Features
- Configure the colour, size and layout types of your leaderboard profile
- Turn on/off properties, like wins, losses, and just have what you require.
- Automatic Leaderboard profile update every 15 minutes.

## Finding your API URL and configure page

1. First find your leaderboard profile for [Red Alert](https://cnc.community/command-and-conquer-remastered/leaderboard/red-alert) or [Tiberian Dawn](https://cnc.community/command-and-conquer-remastered/leaderboard/tiberian-dawn).

2. Click into your profile and on the end of the url add `?showWebView=true`
E.g `https://cnc.community/command-and-conquer-remastered/leaderboard/red-alert/player/3951?showWebView=true`

3. This will enable a button that will take you to your configuration page for the webview. 
![image](https://user-images.githubusercontent.com/6104940/90959022-c2ed2880-e48f-11ea-9efe-d8e6219f3830.png)

4. Your URL should look like: `https://cnc.community/api/leaderboard/red-alert/player/3951/webview/config`.

5. You can now configure how you want to display your stats with the settings listed. 

6. Once complete take the URL at the bottom of the page and copy it into your OBS browser source. 

![configure](https://user-images.githubusercontent.com/6104940/90958679-d7c8bc80-e48d-11ea-8904-3ce7abf63e35.png)


## License
[GPL-2.0 License](https://github.com/cnc-community/api/blob/master/LICENSE)
