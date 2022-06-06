from pickle import FALSE
from turtle import title
from pytube import YouTube



link = input("Indirilecek video linki: ")
yt =YouTube(link)


print("\nDetails for Video","\n")
print("Title of video:   ",yt.title)
print("Number of views:  ",yt.views)
print("Length of video:  ",yt.length,"seconds")
baslik=yt.title

ys = yt.streams.get_by_itag(140)
ys1 = yt.streams.get_by_itag(137)

print(ys)
print(ys1)

print("\nDownloading...")

ys.download( 'D:\YT video',None, "AUDIO  " )

ys1.download('D:\YT video',None,"VIDEO  " )

print("\nDownload completed!!")