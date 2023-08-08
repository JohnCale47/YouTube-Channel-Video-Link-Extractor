import os
import json
import googleapiclient.discovery

CHANNEL_ID = input("enter channel id: ")
def get_channel_videos(api_key, channel_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    # Get the playlist ID of the channel's uploads
    response = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()
    
    playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    # Get all video IDs from the channel's uploads playlist
    videos = []
    next_page_token = None

    while True:
        response = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        videos.extend([item["snippet"]["resourceId"]["videoId"] for item in response["items"]])

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return videos

if __name__ == "__main__":
    API_KEY = "AIzaSyDpu-yw-E-y0ZJAGI-A4RPmC4SPxr_lxiY" # Replace it with YouTube Data API 
    #CHANNEL_ID = "UC4x_BWvr5oDg3s6kELprCGw"  # Replace with the ID of the YouTube channel you want to extract videos from

    videos = get_channel_videos(API_KEY, CHANNEL_ID)
    
    video_links = [f"https://www.youtube.com/watch?v={video_id}" for video_id in videos]
    
    for link in video_links:
        print(link)
