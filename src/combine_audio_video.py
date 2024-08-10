import tkinter as tk
import tkinter.filedialog as fd
import moviepy.editor as mp

def combine(video_path, audio_path, start_time=0):
    video = mp.VideoFileClip(video_path).set_start(start_time)
    audio = mp.AudioFileClip(audio_path)

    # Adjust the audio to match the video length if necessary
    if audio.duration > video.duration:
        audio = audio.subclip(0, video.duration)
    
    # Set the audio to the video
    combined = video.set_audio(audio)
    return combined

def browse_video():
    video_file = fd.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi")])
    video_file_entry.delete(0, tk.END)
    video_file_entry.insert(0, video_file)

def browse_audio():
    audio_file = fd.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    audio_file_entry.delete(0, tk.END)
    audio_file_entry.insert(0, audio_file)

def merge():
    video_file = video_file_entry.get()
    audio_file = audio_file_entry.get()
    start_time = int(start_time_entry.get())

    # Use the combine function to merge video and audio
    combined_clip = combine(video_file, audio_file, start_time)

    # Save the merged video
    save_file = fd.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 Video", "*.mp4")])
    combined_clip.write_videofile(save_file, codec="libx264")

    status_label.config(text="Video merged successfully.")

root = tk.Tk()
root.title("Merge Video and Audio")

video_file_label = tk.Label(root, text="Video file path:")
video_file_entry = tk.Entry(root)
video_file_browse_button = tk.Button(root, text="Browse", command=browse_video)

audio_file_label = tk.Label(root, text="Audio file path:")
audio_file_entry = tk.Entry(root)
audio_file_browse_button = tk.Button(root, text="Browse", command=browse_audio)

start_time_label = tk.Label(root, text="Start time (seconds):")
start_time_entry = tk.Entry(root)

merge_button = tk.Button(root, text="Merge", command=merge)

status_label = tk.Label(root, text="")

video_file_label.pack()
video_file_entry.pack()
video_file_browse_button.pack()

audio_file_label.pack()
audio_file_entry.pack()
audio_file_browse_button.pack()

start_time_label.pack()
start_time_entry.pack()

merge_button.pack()

status_label.pack()

root.mainloop()
