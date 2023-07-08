import os
from huggingface_hub import from_pretrained_keras

model = from_pretrained_keras("kampkelly/fakeimagedetection")

input_size=128

def predict(file_path):
    print('in function', file_path)
    print('>>>>1')

    #Making Single new prediction
    import numpy as np
    from tensorflow.keras.utils import load_img, img_to_array
    test_image = load_img(file_path, target_size = (input_size, input_size))
    print('>>>>2')
    test_image = img_to_array(test_image)
    print('>>>>3')
    test_image = test_image /255.
    print('>>>>4')
    #use this function to change the image from 2dimension(64, 64) to 3dimension(64, 64, 3)
    test_image = np.expand_dims(test_image, axis=0)
    print('>>>>5')
    #add one more dimension before predicting because the predict method expects a batch
    images = np.vstack([test_image])
    print('>>>>6')
    result = model.predict(images, batch_size=10, verbose=2)
    print('>>>>7')

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
    print('>>>>8')
    
    # remove file from uploads folder
    os.remove(file_path)
    print('>>>>9')

    return prediction
