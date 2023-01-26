import pytube
import os
scan = input('Enter the query')
array = pytube.Search(scan)
pytube.YouTube(array.results[0].watch_url).streams.get_by_itag('140').download(filename=(scan+".mp4"))
name1 = str("\ ".join(scan.split(" ")) + ".mp4")
convert = "ffmpeg -i " + name1 + " " + name1[:-4] + ".mp3"  
os.system(convert)
os.system("rm " + name1)
os.system("python3 organize.py")
