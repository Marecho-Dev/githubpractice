from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()

prediction=ImagePrediction()
prediction.setModelTypeAsSqueezeNet()#using squeeze net over ResNet because it's a smaller file size so easier to run
prediction.setModelPath(os.path.join(excution_path,mobilenet_v2.h5 ))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "giraffe.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)