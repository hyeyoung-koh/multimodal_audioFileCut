import pandas as pd
import librosa.segment
import math
import soundfile as sf

def librosa_apply(file_path):
    for i in range(1, 100):
        clip=pd.read_csv('D:\json_file_list\clip_'+str(i)+'.csv', encoding='utf-8-sig')
        print(len(clip))
        for j in range(len(clip)):
            startsec=clip.loc[j, 'text_script_start']*1/29.97
            endsec=clip.loc[j, 'text_script_end']*1/29.97
            print('startsec:', startsec)
            print('endsec:', endsec)
            y, sr=librosa.load(clip, sr=None)
            ny=y[math.floor(sr*(startsec)):math.ceil(sr*(endsec))]
            print(ny)
            sf.write('D:\json_file_list\clip'+str(i)+'_cut'+str(j)+'.wav', ny, sr)
            j+=1
        i+=1