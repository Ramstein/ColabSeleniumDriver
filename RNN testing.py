


import tensorflow as tf
import numpy as np

n_inputs = 3
n_neurons = 5

# 0th input
X0 = tf.placeholder(tf.float16, [None, n_inputs])

# 1st input
X1 = tf.placeholder(tf.float16, [None, n_inputs])

# Xt
Wx = tf.Variable(tf.random_normal(shape=[n_inputs, n_neurons], dtype=tf.float16))

# Yt-1
Wy = tf.Variable(tf.random_normal(shape=[n_neurons, n_neurons], dtype=tf.float16))

# bias
b = tf.Variable(tf.zeros([1, n_neurons], dtype=tf.float16))

# 0th output having the 0th input X0
Y0 = tf.tanh(tf.matmul(X0, Wx) + b)

# 1st output having
Y1 = tf.tanh(tf.matmul(X1, Wy) + tf.matmul(X1, Wx) + b)

init = tf.global_variables_initializer()

X0_batch = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 0, 1]])   # at t=0

X1_barch = np.array([[9, 8, 7], [0, 0, 0], [6, 5, 4], [3, 2, 1]])

with tf.Session() as sess:
    init.run()
    Y0_val, Y1_val = sess.run([Y0, Y1], feed_dict={X0: X0_batch, X1: X1_barch})