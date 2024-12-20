import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 200:
        #convertimos la respuesta a formato json
        formatted_response = json.loads(response.text)

        #extraemos las emociones de la respuesta
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        #extraemos los puntajes de cada emocion
        anger = emotions["anger"]
        disgust = emotions["disgust"]
        fear = emotions["fear"]
        joy = emotions["joy"]
        sadness = emotions["sadness"]

        #creamos 2 listas para saber el indice de la emocion mas alta
        emotions_scores = [anger, disgust, fear, joy, sadness]
        emotions_index = ["anger", "disgust", "fear", "joy", "sadness"]

        #obtenemos la calificacion mas alta y el indice de la emocion con la calificacion mas alta
        max_score = max(emotions_scores)
        max_score_index = emotions_scores.index(max_score)

    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None

    result = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': emotions_index[max_score_index]
    }

    return result