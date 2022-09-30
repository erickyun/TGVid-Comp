#    Copyright (c) 2021 
#    Improved By @

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 0
    OWNER = config("OWNER")
    ffmpegcode = ["-preset slower -c:v libx265 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By 9LifeCat' -pix_fmt yuv420p10 -crf 16 -c:a aac -b:a 128k -c:s copy"]
    THUMBNAIL = config("THUMBNAIL", default="https://trac.ffmpeg.org/ffmpeg-logo.png")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
