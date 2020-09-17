import speech_recognition as vr
import binascii

p = vr.Recognizer()

file_audio = vr.AudioFile('audio_file.wav')

with file_audio as mainfile:
   audio_text = p.record(mainfile)

A = p.recognize_google(audio_text)
print("Audio To Text :",A)

binary = ''.join(format(ord(i), 'b') for i in A)

print("binary conversion : " + str(binary))