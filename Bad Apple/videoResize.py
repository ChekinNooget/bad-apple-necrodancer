#i just stole this code from online, i had to rename resize to resized though
#this is so that i don't have to do complicated things in order to choose which pixel is white or black
#python does it for me B)

from moviepy import VideoFileClip as mp
clip = mp("bad_apple trimmed.mp4")
clip_resized = clip.resized(height=16)
clip_resized.write_videofile("bad_apple trimmed resized.mp4")