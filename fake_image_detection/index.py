import os
from efficientnet.tfkeras import EfficientNetB0
from tensorflow.keras.models import load_model
best_model = './fake_image_detection/best_model_EB0_7_classification.h5'
model = load_model(best_model)
input_size=128

def predict(file_path):
    print('in function', file_path)

    #Making Single new prediction
    import numpy as np
    from tensorflow.keras.utils import load_img, img_to_array
    test_image = load_img(file_path, target_size = (input_size, input_size))
    test_image = img_to_array(test_image)
    test_image = test_image /255.
    #use this function to change the image from 2dimension(64, 64) to 3dimension(64, 64, 3)
    test_image = np.expand_dims(test_image, axis=0)
    #add one more dimension before predicting because the predict method expects a batch
    images = np.vstack([test_image])
    result = model.predict(images, batch_size=10)

    prediction = ''
    if np.argmax(result) == 0:
        prediction = 'celeba'
        # print('fake')
    elif np.argmax(result) == 1:
        # print('real')
        prediction = 'celeba_hq'
    elif np.argmax(result) == 2:
        prediction = 'deepfakes'
    elif np.argmax(result) == 3:
        prediction = 'face2face'
    elif np.argmax(result) == 4:
        prediction = 'faceswap'
    elif np.argmax(result) == 5:
        prediction = 'neuraltextures'
    elif np.argmax(result) == 6:
        prediction = 'youtube'
    print(prediction)
    
    # remove file from uploads folder
    os.remove(file_path)


        

    return prediction
