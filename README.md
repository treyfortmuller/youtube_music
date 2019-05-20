# YouTube Music Downloader

_not for illegal stuff_

A script to download music associated with videos from youtube for local playback. Prompts the user for artist and song title, then saves a file `[song]-[artist].mp3` to my `~/Music` directory (filepaths are hardcoded because that's where all my local music is).

I set up an aliases for my terminal environment to run the script from anywhere, anytime I need a song downloaded. Super convenient.

```bash
# youtube music download script
alias yt_music="python ~/Dev/youtube_music/yt_music.py"
```

### References

* [Will Drevo](https://willdrevo.com/downloading-youtube-and-soundcloud-audio-with-python-and-pandas)

* [youtube-dl](https://ytdl-org.github.io/youtube-dl/index.html)

