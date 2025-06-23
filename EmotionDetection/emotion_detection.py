import requests, json, copy

def emotion_detector(text_to_analyse) -> dict:
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=input_json, headers=header)
    formatted_response = json.loads(response.text)

    # init default values `scores` (emotion: value)
    scores_ = {"anger": 0.0, "disgust": 0.0, "fear": 0.0, "joy": 0.0, "sadness": 0.0}
    # create a copy for the actual scores
    scores = scores_.copy()

    # capture the highest score encountered so far and the associated emotion
    max_score = 0.0
    dominant_emotion = ""
    # loop through data
    for emotion in scores_.keys():
        score = (
            formatted_response.get("emotionPredictions")[0].get("emotion").get(emotion)
        )
        scores[emotion] = score

        # determine the max score (dominant emotion)
        if score > max_score:
            # update max. score and dominant emotion
            max_score = score
            dominant_emotion = emotion

    output = {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
        "dominant_emotion": dominant_emotion,
    }

    return output
