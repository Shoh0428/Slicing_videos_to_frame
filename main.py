import cv2
import imageio
import os

def slice_videos(input_folder, output_folder, gif_duration_sec=10):
    video_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp4'))]

    for video_file in video_files:
        video_path = os.path.join(input_folder, video_file)
        video_name = os.path.splitext(video_file)[0]
        output_video_folder = os.path.join(output_folder, video_name)
      
        os.makedirs(output_video_folder, exist_ok=True)

        cap = cv2.VideoCapture(video_path)
        frame_rate = int(cap.get(5))
        frame_count = int(cap.get(7))

        
        num_partitions = int(frame_count / (frame_rate * gif_duration_sec))

        for i in range(num_partitions):
            start_frame = int(i * frame_rate * gif_duration_sec)
            end_frame = int((i + 1) * frame_rate * gif_duration_sec)

            
            cap.set(1, start_frame)

            frames = []
            for _ in range(start_frame, end_frame):
                ret, frame = cap.read()
                if not ret:
                    break
                frames.append(frame)

            output_gif_path = os.path.join(output_video_folder, f"part_{i}.gif")
            imageio.mimsave(output_gif_path, frames, duration=1 / frame_rate)

        cap.release()
      
input_folder = "input_path"
output_folder = "output_path"
clip_duration_sec = 10

slice_videos(input_folder, output_folder, gif_duration_sec)
