import cv2 as cv
import numpy as np

class ObjectRecognitionAI():
    whT = 320
    confThreshold = 0.5
    nmsThreshold = 0.2

    #### LOAD MODEL
    ## Coco Names
    classesFile = "coco.names"
    classNames = []
    with open(classesFile, 'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')

    ## Model Files
    modelConfiguration = "yolov3.cfg"
    modelWeights = "yolov3-320.weights"
    net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

    def get_objects(self, image):
        blob = cv.dnn.blobFromImage(image, 1 / 255, (self.whT, self.whT), [0, 0, 0], 1, crop=False)
        self.net.setInput(blob)
        layersNames = self.net.getLayerNames()
        outputNames = [(layersNames[i[0] - 1]) for i in self.net.getUnconnectedOutLayers()]
        outputs = self.net.forward(outputNames)
        hT, wT, cT = image.shape
        results = []
        bbox = []
        classIds = []
        confs = []
        for output in outputs:
            for det in output:
                scores = det[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > self.confThreshold:
                    results.append(self.classNames[classId])

        return results
