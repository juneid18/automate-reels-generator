import random

def select_video(num, selected_category):
    # List of 10 video filenames
    videos = [f"video/{selected_category}/video1.mp4", f"video/{selected_category}/video2.mp4", f"video/{selected_category}/video3.mp4", f"video/{selected_category}/video4.mp4", f"video/{selected_category}/video5.mp4", f"video/{selected_category}/video6.mp4", f"video/{selected_category}/video7.mp4", f"video/{selected_category}/video8.mp4", f"video/{selected_category}/video9.mp4"]

    # List of 10 song filenames
    songs = [f"songs/{selected_category}/song1.mp3", f"songs/{selected_category}/song2.mp3", f"songs/{selected_category}/song3.mp3", f"songs/{selected_category}/song4.mp3", f"songs/{selected_category}/song5.mp3", f"songs/{selected_category}/song6.mp3", f"songs/{selected_category}/song7.mp3", f"songs/{selected_category}/song8.mp3", f"songs/{selected_category}/song9.mp3", f"songs/{selected_category}/song10.mp3"]

    # Randomly select one video and one song
    selected_videos = random.sample(videos, num)
    selected_song = random.choice(songs)

    # print("Selected Video: ", selected_videos)
    # print("Selected Song: ", selected_song)

    return selected_videos, selected_song
