#!/usr/bin/python3
import subprocess

times = [(7,8), (13,14)]

full_time = 18

for time in times:
	start = time[0]
	end = time[1]
	proc = subprocess.Popen(["ffmpeg",
						   "-i",
						   "whatever.mkv",
						   "-af",
						   f"volume=enable='between(t,{start},{end})':volume=0, volume=enable='between(t,{end},{full_time})':volume=1",
						   "-vcodec",
						   "copy", 
						   "out1.mkv"])
	proc.wait()


