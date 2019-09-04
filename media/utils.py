from imageai.Detection import ObjectDetection
import os
from django.conf import settings

execution_path = os.getcwd()
def detect(path):
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(settings.MODELS_PATH)
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(os.path.dirname(os.path.dirname(__file__))+'/media/' ,path), output_image_path=os.path.join(os.path.dirname(os.path.dirname(__file__))+'/media/' , "imagenew.jpg"))

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    
    return eachObject