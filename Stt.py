from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from sys import argv
script, filename = argv

IDkey = 'GKoPAKPsXPAnRBEwLcNalKLdTExUlavDO-RfgtrosYNi'  # API密钥
URL = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/89716e51-0ee4-489e-88a1-4cb4c776634a'

# Music = 'data/audio-file2.flac'  # 要转换的音频存放的路径
Music = input("please input filename: ")

authenticator = IAMAuthenticator(IDkey)
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url(URL)

with open(Music, 'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        # content_type='audio/flac',  # 指定转换的音频是.flac音频格式
        # content_type='audio/wav',  # 指定转换的音频是.wav音频格式
        content_type='audio/mp3', # 指定转换的音频是.mp3音频格式
        model='zh-CN_BroadbandModel'# 表示识别中文语音，不指定则默认识别英文
        # timestamps=True  # 识别内容对应的时间轴（作字幕很重要的一个属性，但是我还不知道具体怎么使用）
    ).get_result()
result = speech_recognition_results

list = result['results']
list2 = []
for dic in list:
    print (">>>dic=",dic)
    list2.append(dic)

print ("I'm going to write these to the file.")
txt = str(list2)
target = open(filename, 'w')
target.write(txt)
target.close()
