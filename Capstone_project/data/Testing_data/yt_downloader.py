def yt_download(video_url):
    from pytube import YouTube
    yt = YouTube(video_url)
    print(video_url)
    stream = yt.streams.filter(file_extension='mp4').first()
    stream.download()
