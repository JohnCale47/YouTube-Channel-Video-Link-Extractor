
Extracts All video links from a YouTube Channel using YouTube Data API and Python ❤️
-----------------
## Installing Google API Python Client
 - Do `pip install google-api-python-client`
 ## Getting API from Google Cloud Console
 - Go to the Google Cloud Console ([console.cloud.google](https://console.cloud.google.com/)), create a new project or use existing one, and enable the YouTube Data API v3 for that project. Create and Copy the API key, which you'll use to authenticate your requests.
 ## Getting YT Channel ID
 
 - Go here [commentpicker.com/youtube-channel-id](https://commentpicker.com/youtube-channel-id.php)
 - Paste in the URL of the YT Channel and Click **Get YouTube Channel ID Button**
 - Copy the Channel ID
 ## Editing `extractor.py`
 
 - Open `extractor.py` using your favorite text editor and scroll down to `Line 38 and 39`
 - Replace `YOUR_API_KEY` with your own API Key which you acquired earlier.
 - Replace `THE_CHANNEL_ID` with the Channel ID you got from the Site.
 - and **SAVE!**
## Running `extractor.py`
 - Do `python extractor.py`
 - Copy all the Video IDs
 - Use [browserling.com/tools/prefix-suffix-lines](https://www.browserling.com/tools/prefix-suffix-lines) to add Prefix to the Video IDs [make sure to remove the `"` and `,` s from Video IDs
 - Prefix String: `https://www.youtube.com/watch?v=` and done there is your Links..

   OR **You can skip all the formating by using** `extractorv2.py` which gives you Video Links instead of Video IDs.
		 
Bei bei and Umma 😘
