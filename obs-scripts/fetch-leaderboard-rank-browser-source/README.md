# Leaderboard Profiles - OBS Browser Source

![Leaderboard-rank-obs-browser-source](https://user-images.githubusercontent.com/6104940/90958560-2f1a5d00-e48d-11ea-889a-40c546a65ecc.png)


## 🚀 Quick start

- Open OBS, under your "Sources", add a "Browser source"
- Configure your C&C Community API webview settings and copy the URL 
- Paste the URL into OBS browser source and hit save. 
- Your Leaderboard profile will update every 15 minutes.

![image](https://user-images.githubusercontent.com/6104940/90894626-d37e9f80-e3b8-11ea-88ec-4af55fc919db.png)


## Finding your API URL 

1. First find your leaderboard profile for [Red Alert](https://cnc.community/command-and-conquer-remastered/leaderboard/red-alert) or [Tiberian Dawn](https://cnc.community/command-and-conquer-remastered/leaderboard/tiberian-dawn).

2. Click into your profile and look for the ID on the end of the url. 
E.g `https://cnc.community/command-and-conquer-remastered/leaderboard/red-alert/player/3951` the id would be `3951`.

3. For Red Alert: Now go to `https://cnc.community/api/leaderboard/red-alert/player/(ID_HERE)/webview/config`.
For Tiberian Dawn: Go here: `https://cnc.community/api/leaderboard/tiberian-dawn/player/(ID_HERE)/webview/config`.

4. Your URL should look like: `https://cnc.community/api/leaderboard/red-alert/player/3951/webview/config`.

5. Once you have your API url, enter it into the URL property in the script.



## License
[GPL-2.0 License](https://github.com/cnc-community/api/blob/master/LICENSE)
