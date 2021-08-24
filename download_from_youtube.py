from pytube import YouTube
video_url = input(str("enter the url : "))
while not len(video_url):
    video_url = input(str("enter the url : "))
    if len(video_url):
        break

try:
    video = YouTube(video_url).streams.filter(res="720p").first().download()
except:
    print("sorry, please try again later...")