from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestCase(unittest.TestCase):
    def test_joy(self):
        query = "I am glad this happened"
        dominant_emotion_ = "joy"

        response = emotion_detector(query)
        dominant_emotion = response["dominant_emotion"]
        self.assertEqual(dominant_emotion_, dominant_emotion)

    def test_anger(self):
        query = "I am really mad about this"
        dominant_emotion_ = "anger"

        response = emotion_detector(query)
        dominant_emotion = response["dominant_emotion"]
        self.assertEqual(dominant_emotion_, dominant_emotion)

    def test_disgust(self):
        query = "I feel disgusted just hearing about this"
        dominant_emotion_ = "disgust"

        response = emotion_detector(query)
        dominant_emotion = response["dominant_emotion"]
        self.assertEqual(dominant_emotion_, dominant_emotion)

    def test_sadness(self):
        query = "I am so sad about this"
        dominant_emotion_ = "sadness"

        response = emotion_detector(query)
        dominant_emotion = response["dominant_emotion"]
        self.assertEqual(dominant_emotion_, dominant_emotion)

    def test_fear(self):
        query = "I am really afraid that this will happen"
        dominant_emotion_ = "fear"

        response = emotion_detector(query)
        dominant_emotion = response["dominant_emotion"]
        self.assertEqual(dominant_emotion_, dominant_emotion)
