from sys import argv
import moviepy.editor as mp
import os

link = argv[2]
path = argv[3]
flag = 0

if '-o' in argv[1]:
    flag = 0
if '-m' in argv[1]:
    flag = 1


def convert(link=link):
    name = link.split('/')[-1].split('.')
    if name[1] != "mp3":

        clip = mp.VideoFileClip(link)
        clip.audio.write_audiofile((path+'/'+name[0]+'.mp3'))


if flag == 0:
    convert()
else:
    for i in os.listdir(link):
        convert(link + '/'+i)
