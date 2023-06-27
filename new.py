import pytube
import os
from time import sleep
import sy
#Checking the number of arguments to determine the functionalitys
if(len(sys.argv) > 1):
    print((sys.argv[1]))
    url = sys.argv[1]
    scan = sys.argv[2]
    print("The saved file will be named {0}".format(scan))
else:
    scan = input('Enter the query')
    array = pytube.Search(scan)
    url = array.results[0].watch_url
#retrieving the file and downloading it in current folder, then converting it
pytube.YouTube(url).streams.get_by_itag('140').download(filename=(scan+".mp4"))
name1 = str("\ ".join(scan.split(" ")) + ".mp4")
convert = "ffmpeg -i " + name1 + " " + name1[:-4] + ".mp3"  
os.system(convert)
os.system("rm " + name1)

if(os.system("mkdir music 2>>error.txt")):
    pass
else:
    print("music directory created")
os.system("open " + name1[:-4] + ".mp3")
sleep(5)
os.system("python3 organize.py")

