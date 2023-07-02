import sounddevice as sd
import soundfile as sf
path = "./music/"
readFile = input("Enter name of file you want to trim:\t")
readFileFull = "./music/" + readFile
data,fs = sf.read(readFileFull)
start = input("Enter the value in seconds to start:\t")
start = int(start)
stop = input("Enter the value in seconds to stop:\t")
stop = int(stop)
#playRate = float(input("Enter the rate which you want to play, normalized to 1:\t"))
#playRate = int(fs*playRate)
sd.play(data[start*fs:stop*fs],fs)
saveName =  readFile[:-4]+"trimmed.mp3"
print("You file will be saved as:\t" + saveName)
sd.wait()
sf.write(path + saveName,data[start*fs:stop*fs],fs)



