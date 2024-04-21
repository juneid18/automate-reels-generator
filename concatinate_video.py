import cv2

def concatinate(selected):
    # List of video file paths to combine
    video_paths = selected

    #print(video_paths)

    # Initialize an empty list to store video frames
    frames = []

    # Get frame size and frame rate from the first video
    cap = cv2.VideoCapture(video_paths[0])
    frame_size = (int(cap.get(3)), int(cap.get(4)))
    fps = int(cap.get(5))
    cap.release()

    # Initialize VideoWriter for the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
    out = cv2.VideoWriter('concatinated_video.mp4', fourcc, fps, frame_size)

    # Read and write frames from each video
    for video_path in video_paths:
        cap = cv2.VideoCapture(video_path)

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)

        cap.release()

    # Release the output video
    out.release()
    print("------------------------------------------------------------")
    print("Videos successfully concatinated to 'concatinated_video.mp4'")
    print("------------------------------------------------------------")
