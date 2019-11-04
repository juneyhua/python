from imageai.Detection import ObjectDetection
import os
execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path ,
"resnet50_coco_best_v2.0.l.h5"))
detector.loadModel()
detections =
detector.detectObj ectsFromImage(input_ image=os . path. join(execution_path ,
"image.jpg"), output_image_path=os.path.join(execution_path,
"imagenew.jpg"))
for each0bject in detections:
	print(each0bject["name"] + " : " + 
each0bject["percentage_ probability"] )