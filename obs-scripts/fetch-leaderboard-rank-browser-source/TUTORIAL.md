# Tutorial for OBS Browser Source Leaderboard

## Step 1 - Create your webview

- Find your leaderboard profile for [Red Alert](https://cnc.community/command-and-conquer-remastered/leaderboard/red-alert) or [Tiberian Dawn](https://cnc.community/command-and-conquer-remastered/leaderboard/tiberian-dawn). 

- Click into your profile and on the end of the url add `?showWebView=true`
E.g `https://cnc.community/command-and-conquer-remastered/leaderboard/red-alert/player/3951?showWebView=true`

- This will enable a button that will take you to your configuration page for the webview. 
![image](https://user-images.githubusercontent.com/6104940/90959022-c2ed2880-e48f-11ea-9efe-d8e6219f3830.png)

- Your URL should look like: `https://cnc.community/api/leaderboard/red-alert/player/3951/webview/config`. On this page you can configure how you want to display your stats with the settings shown. 

- Once complete take the URL at the bottom of the page and copy it to your clipboard.

![configure](https://user-images.githubusercontent.com/6104940/90958679-d7c8bc80-e48d-11ea-8904-3ce7abf63e35.png)

## Step 2 - Create an OBS Browser Source
- Create a new OBS Browser Source

  ![image](https://user-images.githubusercontent.com/6104940/90976207-f5039680-e532-11ea-8d47-f664b49ea019.png)

- Configure your webview and paste the URL from step 1 into the URL field.
  ![image](https://user-images.githubusercontent.com/6104940/90976287-b02c2f80-e533-11ea-9536-c797db603440.png)

- Configure thw width and height for your needs. E.g if you've enabled all the fields to show in your webview, you'll need a bigger width.


## Step 3 - Save and position on screen

- You can now move the browser source around and scale accordingly. You can also crop if you wish by holding the alt key and dragging the corners.

![image](https://user-images.githubusercontent.com/6104940/90976330-ff726000-e533-11ea-996c-e54aa09d5be8.png)

