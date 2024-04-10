# -*- coding: utf-8 -*-
# @Time : 2024/4/8 21:03
# @Author : 18083
# @Email : wayne_lau@aliyun.com
# @File : dmx.py
# @Project : djangoProject1
from zhipuai import ZhipuAI

import speech_recognition as sr
import logging

def audio_record():
    logging.basicConfig(level=logging.DEBUG)
    count = 0
    while count < 1:
        r = sr.Recognizer()
        # Mic1
        mic = sr.Microphone()
        logging.info('message enter')
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            logging.info('message end and recognize')
            test = r.recognize_google(audio, language='cmn-Hans-CN', show_all=True)
            logging.info('end')
            transcript = test['alternative'][0]['transcript']
            count += 1
            print(f"Transcript {count}: {transcript}")
            return transcript
        except sr.UnknownValueError:
            logging.error("Could not understand audio")
            break




# Call the function to start audio recording and speech recognition
result = audio_record()
print("Final Transcript:", result)
def get_completion( messages1,gogle_result):
    client = ZhipuAI(api_key="a49e70e2979d6eb986e2ace35fc0ca2d.1SvVd0KoQNUG52Xd") # 请填写您自己的APIKey

    messages1.append({"role": "user", "content": gogle_result})
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages1,
        stream=True,
)

    result =""
    for chunk in response:
        result+=chunk.choices[0].delta.content
    return result
import sys
import json

# # 保证兼容python2以及python3
def make_mp3(zp_result):
    IS_PY3 = sys.version_info.major == 3
    if IS_PY3:
        from urllib.request import urlopen
        from urllib.request import Request
        from urllib.error import URLError
        from urllib.parse import urlencode
        from urllib.parse import quote_plus
    # else:
    #     import urllib2
    #     from urllib import quote_plus
    #     from urllib2 import urlopen
    #     from urllib2 import Request
    #     from urllib2 import URLError
    #     from urllib import urlencode
    API_KEY = 'eTX9TD5qiKf6FlK4iPe4hpGp'
    SECRET_KEY = 'qi0uOijWVOIugXyT40PAm4tccaAvPOBC'
    TEXT = zp_result

    TTS_URL = 'http://tsn.baidu.com/text2audio'
    TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
    def fetch_token():
        params = {'grant_type': 'client_credentials',
                  'client_id': API_KEY,
                  'client_secret': SECRET_KEY}
        post_data = urlencode(params)
        if (IS_PY3):
            post_data = post_data.encode('utf-8')
        req = Request(TOKEN_URL, post_data)
        try:
            f = urlopen(req, timeout=5)
            result_str = f.read()
        except URLError as err:
            print('token http response http code : ' + str(err.code))
            result_str = err.read()
        if (IS_PY3):
            result_str = result_str.decode()


        result = json.loads(result_str)

        if ('access_token' in result.keys() and 'scope' in result.keys()):
            if not 'audio_tts_post' in result['scope'].split(' '):
                print ('please ensure has check the tts ability')
                exit()
            return result['access_token']
        else:
            print ('please overwrite the correct API_KEY and SECRET_KEY')
            exit()


    """  TOKEN end """

    if __name__ == '__main__':

        token = fetch_token()

        tex = quote_plus(TEXT)  # 此处TEXT需要两次urlencode

        params = {'tok': token, 'tex': tex, 'cuid': "quickstart",
                  'lan': 'zh', 'ctp': 1,'per':3,'spd':10,}  # lan ctp 固定参数

        data = urlencode(params)

        req = Request(TTS_URL, data.encode('utf-8'))
        has_error = False
        try:
            f = urlopen(req)
            result_str = f.read()

            headers = dict((name.lower(), value) for name, value in f.headers.items())

            has_error = ('content-type' not in headers.keys() or headers['content-type'].find('audio/') < 0)
        except  URLError as err:
            print('http response http code : ' + str(err.code))
            result_str = err.read()
            has_error = True

        save_file = "error.txt" if has_error else u'大姚的订单信息.mp3'

        with open(save_file, 'wb') as of:
            of.write(result_str)

        if has_error:
            if (IS_PY3):
                result_str = str(result_str, 'utf-8')
            print("tts api  error:" + result_str)

        print("file saved as : " + save_file)


import pygame

def play_mp3(mp3_file):
    """
    :param mp3_file:需要播放的录音文件地址
    :return:无
    """
    pygame.init()  # 初始化pygame
    pygame.mixer.init()  # 初始化音频混合器
    pygame.mixer.music.load(mp3_file)  # 加载指定MP3文件
    pygame.mixer.music.play()  # 播放
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():  # 使用一个循环来等待音频播放完毕，保证程序不会在播放结束前退出
        clock.tick(3)
messages1 = [
               {"role": "system",
               "content": "你是一个心理健康助手，你的任务是为用户提供心理健康方面的专业咨询服务，引导用户心理健康向积极方向发展。字数少于50字。"},
        ]
def main():
    global messages1
    while True:
            # 1. 提示用户发言
        print('你好')
        # 2. 进行语音识别
        speechRecognition=audio_record()
        print(speechRecognition)

        # 3.调用大语言模型进行文本生成
        zp_result = get_completion(messages1,speechRecognition)
        print('zpdmx recognition result:',zp_result)
        print(messages1)

        # 4. 生成语音
        make_mp3(zp_result)

        # 8. 播放
        mp3_file="D:\Project\Pycharm_Proj\djangoProject1\djangoProject1\大姚的订单信息.mp3"
        play_mp3(mp3_file)
        user_input = input('是否继续对话')
        if user_input == '是':
            continue
        if user_input == '否':
            break

if __name__ == "__main__":
    main()



