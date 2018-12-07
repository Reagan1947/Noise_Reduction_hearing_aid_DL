# coding = utf-8
import wave
import struct
from scipy import *
from pylab import *

# 读取wav文件，我这儿读了个自己用python写的音阶的wav
wavefile = wave.open('D:/Noise_Reduction_hearing_aid_DL/wav_file/zted170919_4626690iTb.wav', 'r')  # open for writing

# 读取wav文件的四种信息的函数。期中numframes表示一共读取了几个frames，在后面要用到滴。
nchannels = wavefile.getnchannels()
sample_width = wavefile.getsampwidth()
framerate = wavefile.getframerate()
numframes = wavefile.getnframes()

# ------------绘图部分-------------- #
# 参数Print
# print("channel", nchannels)
# print("sample_width", sample_width)
# print("framerate", framerate)
# print("numframes", numframes)

# 建一个y的数列，用来保存后面读的每个frame的amplitude。
y = zeros(numframes)

# for循环，readframe(1)每次读一个frame，取其前两位，是左声道的信息。右声道就是后两位啦。
# unpack是struct里的一个函数，用法详见http://docs.python.org/library/struct.html。简单说来就是把＃packed的string转换成原来的数据，无论是什么样的数据都返回一个tuple。这里返回的是长度为一的一个
# tuple，所以我们取它的第零位。
for i in range(numframes):
    val = wavefile.readframes(1)
    left = val[0:2]
    # right = val[2:4]
    v = struct.unpack('h', left)[0]
    y[i] = v

# framerate就是44100，文件初读取的值。然后本程序最关键的一步！specgram！实在太简单了。。。
Fs = framerate
specgram(y, NFFT=1024, Fs=Fs, noverlap=900)
show()
# 参数介绍 https://blog.csdn.net/shenziheng1/article/details/53868684
# ---------------绘图部分结束------------------ #

# ---------------特征提取---------------------- #
