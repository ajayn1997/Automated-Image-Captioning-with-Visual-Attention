import tensorflow as tf
from sklearn.utils import shuffle

import numpy as np
import os
import json

def get_train_data(num_examples=3000):
    annotation_zip = tf.keras.utils.get_file('captions.zip',
                                             cache_subdir=os.path.abspath('.'),
                                             origin = 'http://images.cocodataset.org/annotations/annotations_trainval2014.zip',
                                             extract = True)
    annotation_file = os.path.dirname(annotation_zip)+'/annotations/captions_train2014.json'

    name_of_zip = 'train2014.zip'
    if os.path.exists(os.path.abspath('.') + '/' + name_of_zip) :
        image_zip = tf.keras.utils.get_file(name_of_zip, 
                                          cache_subdir=os.path.abspath('.'),
                                          origin = 'http://images.cocodataset.org/zips/train2014.zip',
                                          extract = True)
        PATH = os.path.dirname(image_zip)+'/train2014/'
    else:
      print ('Skipped')
      PATH = os.path.abspath('.')+'/train2014/'

    # read the json file
    with open(annotation_file,'r') as f:
        annotations = json.load(f)

    
    
