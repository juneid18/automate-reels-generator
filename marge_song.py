from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

def marge(song_name):
    # Open the video and audio
    video_clip = VideoFileClip("output_video.avi")  # Update file format to MP4
    audio_clip = AudioFileClip(song_name)

    # Ensure that the audio duration matches the video duration exactly
    if audio_clip.duration != video_clip.duration:
        # Trim the audio to match the video duration
        audio_clip = audio_clip.subclip(0, video_clip.duration)

    # Concatenate the video clip with the trimmed audio clip
    final_clip = video_clip.set_audio(audio_clip)

    # Export the final video with audio
    final_clip.write_videofile("final.mp4")
    print("------------------------------------------------------------")
    print("Song Merge Successfully to the Video !! ")
    print("------------------------------------------------------------")
