# -*- coding: utf-8 -*-
# @Time : 2024/4/9 21:52
# @Author : 18083
# @Email : wayne_lau@aliyun.com
# @File : aa.py
# @Project : djangoProject1
import logging
import speech_recognition as sr


def audio_record():
    logging.basicConfig(level=logging.DEBUG)
    count = 0
    while count < 3:
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
        except sr.UnknownValueError:
            logging.error("Could not understand audio")
            break

    return transcript


# Call the function to start audio recording and speech recognition
result = audio_record()
print("Final Transcript:", result)

