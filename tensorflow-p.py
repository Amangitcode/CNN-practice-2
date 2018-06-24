import tensorflow as tf

x = tf.constant([1,2,3,4], shape=[4,1])
y = tf.constant([2,2,2,3], shape=[1,4])

R = tf.matmul(x,y)

with tf.Session() as sess:
    print(sess.run(R))