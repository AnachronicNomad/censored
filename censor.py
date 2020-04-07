#!/usr/bin/python3
import subprocess

times = []

full_time = 18

with open("censor_times") as f:
	for line in f.readlines():
		start = 0
		end = 0
		x = line.split(",")
		y = x[0].split(":")
		z = x[1].split(":")
		start = (3600 * int(y[0])) + (60 * int(y[1])) + int(y[2])
		print(start)
		end = (3600 * int(z[0])) + (60 * int(z[1])) + int(z[2])
		print(end)
		times.append((start, end))


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
	proc = subprocess.Popen(["mv",
		 					 "out1.mkv",
		 					 "whatever.mkv"])
	proc.wait()


