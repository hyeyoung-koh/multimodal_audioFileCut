#  mfcc 자르기 코드
import pandas as pd
import librosa.segment
import math
import soundfile as sf
clip_1_csv=pd.read_csv('clip_1.csv',encoding='cp949')
print(len(clip_1_csv)) #10

i=1
for i in range(len(clip_1_csv)):
    startsec=clip_1_csv.loc[i, 'start']
    endsec=clip_1_csv.loc[i, 'end']
    print('startsec:', startsec)
    print('endsec:', endsec)
    y, sr=librosa.load('clip_1.wav', sr=None)
    #  ny=y[round(sr*(startsec)):round(sr*(endsec))] #  시작은 내림으로 하고 끝은 올림으로 하자.
    ny=y[math.floor(sr * (startsec)):math.ceil(sr * (endsec))]
    #  librosa.output.write_wav(i+'.wav',ny,sr)
    #  sf.write(str(i)+'_cut.wav',np.random.randn(10,2),44100)
    sf.write('clip1_'+str(i)+'_cut.wav', ny, sr)
    i+=1