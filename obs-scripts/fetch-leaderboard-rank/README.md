# Show your Rank for C&C Remasters in an OBS stream


![image](https://user-images.githubusercontent.com/6104940/90895778-8dc2d680-e3ba-11ea-997c-51bd78b80c6e.png)


## Prerequisites 
- Python version 3.6.8 installed and configured in OBS settings. Read how to check you have Python installed below.

## 🚀 Quick start

- Download `leaderboard-rank.py` to your PC. 
- Open OBS, go to Tools > Scripts.
- Click + and point to `leaderboard-rank.py`
- You should then see the properties below. 
- Enter your URL to your API profile.
- Select your OBS text sources from the dropdowns. If they don't appear, click the refresh ICON bottom left, not refresh button.
- Click the "Refresh" button to fetch the latest data for your text sources. Note this will likely be cached for 15 minutes. 


![image](https://user-images.githubusercontent.com/6104940/90894626-d37e9f80-e3b8-11ea-88ec-4af55fc919db.png)


## Finding your API URL 

1. First find your leaderboard profile for [Red Alert](https://cnc.community/command-and-conquer-remastered/leaderboard/red-alert) or [Tiberian Dawn](https://cnc.community/command-and-conquer-remastered/leaderboard/tiberian-dawn).

2. Click into your profile and look for the ID on the end of the url. 
E.g `https://cnc.community/command-and-conquer-remastered/leaderboard/tiberian-dawn/player/2902` the id would be `2902`.

3. For Red Alert: Now go to `https://cnc.community/api/leaderboard/red-alert/player/(ID_HERE)`.
For Tiberian Dawn: Go here: `https://cnc.community/api/leaderboard/tiberian-dawn/player/(ID_HERE)`.

4. Your URL should look like: `https://cnc.community/api/leaderboard/red-alert/player/2902`.

5. Once you have your API url, enter it into the URL property in the script.


## Update Text source from your leaderboard profile
- All sources look for text fields in OBS.

    ![image](https://user-images.githubusercontent.com/6104940/90895109-88b15780-e3b9-11ea-8041-a44a4b7d1358.png)

- Add a new Text (GDI+) source
- Go to Tools > Scripts > Click the refresh icon

    ![image](https://user-images.githubusercontent.com/6104940/90895180-a979ad00-e3b9-11ea-9926-e8387d377f64.png)

- Now to go to the dropdown and select your new text source.
    ![image](https://user-images.githubusercontent.com/6104940/90895257-c910d580-e3b9-11ea-8a72-3aa48b28827a.png)



## Checking you have Python configured
OBS Scripts require Python version 3.6.8 to be installed. 

First - check you already have this configured. If you do, you can skip everything around configuring python.


1. Go to OBS > Tools > Scripts
2. Click "Python Settings"
3. If you have Python listed in this box like below, you should be fine to skip this step.

![image](https://user-images.githubusercontent.com/6104940/90896059-eeeaaa00-e3ba-11ea-9973-3d7f6c4ed084.png)

4. If you don't have it listed, note the "Python Install Path (64bit). If yours says "64Bit) it means you need Python 64 bit installed. 
[Find the download here](https://www.python.org/downloads/release/python-368/)

5. Follow the Python instructions to install noting where it installs.
6. Once installed, set the path to Python in the OBS dialogue above. 