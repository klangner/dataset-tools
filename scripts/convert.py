#
# Convert TensorFlow model into CoreML model
#

import sys
import tfcoreml as tf_converter


if __name__ == '__main__':
    input_model = sys.argv[1]
    output_model = sys.argv[2]
    print(input)
    tf_converter.convert(tf_model_path=input_model,
                         mlmodel_path=output_model,
                         class_labels='build/retrained_labels.txt',
                         image_input_names='input:0',
                         output_feature_names=['final_result:0'],
                         red_bias=-1,
                         green_bias=-1,
                         blue_bias=-1,
                         image_scale=2.0/255.0)
