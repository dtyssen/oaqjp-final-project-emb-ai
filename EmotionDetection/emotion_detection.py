import requests
import json  
def emotion_detector(text_to_analyze): 

    if not text_to_analyze or text_to_analyze.strip() == "":
        response = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        response["status_code"] = 400
        return response

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj =  { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header) 
   
    formatted_response = json.loads(response.text)   
    prediction = formatted_response['emotionPredictions'][0]['emotion']

    emotions = {}

    for emotion_name, score in prediction.items():
        emotions[emotion_name] = score

    emotions['dominant_emotion'] =  max(emotions, key=emotions.get)
       
    return emotions
    
    
    
  