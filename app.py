from sys import argv
import moviepy.editor as mp
import os

link = argv[2]
path = argv[3] 
flag=0

if '-o' in argv[1]:
    flag=0
if '-m' in argv[1]:
    flag=1

def convert(name='',link=link):
    clip = mp.VideoFileClip(link)
    clip.audio.write_audiofile((path+'\\'+name+'.mp3'))

if flag==0:
    temp=path.split('/')[-1].split('.')[0]
    convert(temp)
    pass
else:
    for i in os.listdir(link):
        convert(i,link+'\\'+i,)