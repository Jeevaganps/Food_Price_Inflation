import random
from datetime import datetime, timedelta

# Function to generate a random video ID
def generate_video_id():
    return "V" + ''.join(random.choice('0123456789') for _ in range(10))

# Function to generate a random comment ID
def generate_comment_id():
    return "C" + ''.join(random.choice('0123456789') for _ in range(10))

# Function to generate a random date within a specified range
def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

# Generate channel data
channel_data = {
    "Channel_Name": {
        "Channel_Name": "Example Channel",
        "Channel_Id": "UC1234567890",
        "Subscription_Count": 10000,
        "Channel_Views": 1000000,
        "Channel_Description": "This is an example channel.",
        "Playlist_Id": "PL1234567890"
    }
}

# Generate video data for the channel
video_data = {}
for i in range(1, 11):
    video_id = generate_video_id()
    video_data[video_id] = {
        "Video_Id": video_id,
        "Video_Name": f"Example Video {i}",
        "Video_Description": f"This is an example video {i}.",
        "Tags": ["example", "video"],
        "PublishedAt": generate_random_date(datetime(2022, 1, 1), datetime(2022, 9, 1)).isoformat() + "Z",
        "View_Count": random.randint(1000, 10000),
        "Like_Count": random.randint(100, 1000),
        "Dislike_Count": random.randint(1, 100),
        "Favorite_Count": random.randint(0, 50),
        "Comment_Count": random.randint(0, 50),
        "Duration": "00:05:00",
        "Thumbnail": "https://example.com/thumbnail.jpg",
        "Caption_Status": random.choice(["Available", "Not Available"]),
        "Comments": {}
    }

    # Generate comments for each video
    for j in range(1, 6):
        comment_id = generate_comment_id()
        video_data[video_id]["Comments"][comment_id] = {
            "Comment_Id": comment_id,
            "Comment_Text": f"This is comment {j} for video {i}.",
            "Comment_Author": f"User{j}",
            "Comment_PublishedAt": generate_random_date(
                datetime(2022, 1, 1), datetime(2022, 9, 1)).isoformat() + "Z"
        }

# Combine channel and video data
channel_data.update(video_data)

# Print the JSON data
import json
print(json.dumps(channel_data, indent=4))