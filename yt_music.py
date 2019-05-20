'''
A script for downloading music from youtube videos, and saving them
to the Music directory with semantic filenames
'''

from __future__ import unicode_literals
import youtube_dl
import os
import traceback
import sys

# get video information for saved filename and downloader
artist = raw_input('Artist name: ')
title = raw_input('Song title: ')
link = raw_input('Video link: ')

# create directory
savedir = "/home/trey/Music"
if not os.path.exists(savedir):
    os.makedirs(savedir)

def make_savepath(title, artist, savedir=savedir):
    return os.path.join(savedir, "%s-%s.mp3" % (title, artist))

# create YouTube downloader
options = {
    'format': 'bestaudio/best', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3 
    'outtmpl': '%(id)s',        # name the file the ID of the video
    'noplaylist' : True,}       # only download single song, not playlist
ydl = youtube_dl.YoutubeDL(options)

with ydl:
    print "Downloading from %s..." % (link)
    
    # create saved filename
    savepath = make_savepath(title, artist)
    
    # check the file hasn't already been saved
    try:
        os.stat(savepath)
        print "%s already downloaded" % savepath

    except OSError:
        # download video
        try:
            result = ydl.extract_info(link, download=True)
            os.rename(result['id'], savepath)
            print "Downloaded and converted %s successfully!" % savepath

        except Exception as e:
            print "Can't download audio! %s\n" % traceback.format_exc()
