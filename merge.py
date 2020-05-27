from mhmovie.code import *
from pydub import AudioSegment
src = "blockchain.mp3"
dst = "test.wav"
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
m = movie("blockchain.mp4")
mu = music("test.wav")
mu.Aconvert()
final = m+mu
final.save("Final sample.mp4")
