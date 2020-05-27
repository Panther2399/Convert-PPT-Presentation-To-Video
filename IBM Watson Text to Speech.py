from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
filee=open('blockchain.txt','r',encoding='utf-8')
file=filee.read()
api = IAMAuthenticator("8G50RTeG739GtNvD8bzgeUH8qMxfRO4ePeUfk3noy9iz")
text_2_speech = TextToSpeechV1(authenticator=api)
text_2_speech.set_service_url("https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/697c95fd-211f-43c2-98aa-a5788ca79c1a")
with open("blockchain.mp3","wb") as audiofile:
    audiofile.write(
    text_2_speech.synthesize(file, accept="audio/mp3").get_result().content
    )





