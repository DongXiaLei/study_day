import tensorflow as tf
import numpy as np

matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix2,matrix1)

result = tf.Session().run(product)
print(result)
tf.Session().close()

with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)