import tensorflow as tf

v = tf.constant("Hello Wold!", dtype=None, shape=None, name='Const')
a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b

sess = tf.Session()
print(sess.run(v))
sess.close()