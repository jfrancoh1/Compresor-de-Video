import subprocess
from Duracion import *
from compresion import *


videofile = "It.avi"
fp=1
segn=duration(videofile)
subprocess.call(["ffmpeg", "-i", str(videofile), "-r", str(fp)+"/1", "Vid%04d.jpg"])
subprocess.call(["ffmpeg", "-i", str(videofile), "Aud.mp3"])
for i in range (int(fp*segn)):
	j=i+1
	ent=("Vid%04d.jpg" %j)
	comprimir(ent, j)
subprocess.call(["ffmpeg","-y","-r",str(fp),"-i", "Vid%04d.jpg", "-vcodec", "mpeg4", "-qscale", str(fp), "Vid2.mpeg"])
subprocess.call(["ffmpeg", "-i", "Vid2.mpeg", "-i", "Aud.mp3", "-acodec", "copy", "-vcodec", "copy", "Vid3.avi"])
