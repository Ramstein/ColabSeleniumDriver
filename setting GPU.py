import tensorflow as tf

device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
    tf.test.is_gpu_available
    raise SystemError('GPU device not found')
