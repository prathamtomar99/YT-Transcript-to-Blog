# from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
youtbe_video="https://www.youtube.com/watch?v=csWluHwfsB8"
video_id= youtbe_video.split("=")[1]
from IPython.display import YouTubeVideo
print(YouTubeTranscriptApi.get_transcript(video_id))