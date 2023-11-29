from moviepy.editor import VideoFileClip
def extract_audio(video_path, audio_output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_output_path)

# Exemple d'utilisation
extract_audio("video/test.mp4", "audio/test.wav")