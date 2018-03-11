from subprocess import call
from datetime import datetime

def capture():
    dt = str(datetime.now())
    dtime = dt[0:4]+dt[5:7]+dt[8:10]+dt[11:13]+dt[14:16]+dt[17:19]
    call(["fswebcam", "-d", "/dev/video0", "-r", "640x480", "--no-banner", "./images/%d.jpg" % int(dtime)])

capture()
