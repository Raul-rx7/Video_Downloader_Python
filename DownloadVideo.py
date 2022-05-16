from pytube import YouTube
import os

def DownloadVideo(mp3InLinux=False):
  YtLink = input('Enter the link: ')
  video = YouTube(YtLink)
  stream = video.streams.get_highest_resolution()
  downloadFile = stream.download()
  if mp3InLinux==True:
    base, ext = os.path.splitext(downloadFile)
    newFile = base + '.mp3'
    os.rename(downloadFile, newFile)
  else:
    pass
  print('Done.')

#Calling the function:
DownloadVideo(mp3InLinux=True)

