import os
import subprocess

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=VUV7BBOn6Q8")

vids = yt.streams.all()

# 영상 형식 리스트 확인
for i in range(len(vids)):
    print(i, '. ', vids[i])

vnum = int(input("다운받을 화질은? : "))

parent_dir = "C:\youtube-music"  # 다운받을 경로
vids[vnum].download(parent_dir) # 다운로드 하기

new_filename = input("mp3 파일명을 입력하세요 : ")

default_filename = vids[vnum].default_filename
subprocess.call(['ffmpeg', '-i', os.path.join(parent_dir, default_filename), os.path.join(parent_dir, new_filename)])

print("os.path.join(parent_dir, default_filename) : " + os.path.join(parent_dir, default_filename))
print("os.path.join(parent_dir, new_filename) : " + os.path.join(parent_dir, new_filename))
print('동영상 다운로드 && mp3변환완료!!!')