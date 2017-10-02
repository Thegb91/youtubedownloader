#!/usr/bin/env python
from __future__ import unicode_literals

"""ydownloader.py: download  and convert video songs to mp3 directly."""

__author__      = "Thegb91"
__copyright__   = "Copyright 2017"

import youtube_dl, sys

ydl_opts = {
    'format': 'bestaudio/best', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3 
    'outtmpl': '%(title)s.mp3',
    'noplaylist' : True,}
for i in range(1, len(sys.argv)):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([sys.argv[i]])
