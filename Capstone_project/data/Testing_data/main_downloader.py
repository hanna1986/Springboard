import yt_downloader
import csv
import time
with open('abuse_video_urls.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    counter = 0
    for line in csv_reader:
        counter += 1
        print(counter)
        yt_downloader.yt_download(line[0])
        time.sleep(5)
