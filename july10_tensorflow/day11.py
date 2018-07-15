import tensorflow as tf
import numpy as np
#下面部分有错误
##Save
W = tf.Variable([[1,2,3],[4,4,4]],dtype=tf.float32,name='weight')
b   = tf.Variable([[1,2,3]],dtype=tf.float32,name='bias')

init = tf.global_variables_initializer()

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run (init)
    save_path = saver.save(sess,"my_saver/save_net.ckpt")
    print("save to path:",save_path)

#
# W = tf.Variable(np.arange(6).reshape((2,3)),dtype=tf.float32,name="weight")
# b = tf.Variable(np.arange(3).reshape((1,3)),dtype=tf.float32,name="bias")
#
# saver = tf.train.Saver()
# with tf.Session() as sess:
#     saver.restore(sess,"my_saver/save_net.ckpt")
#     print("weight",sess.run(W))
#     print("bias",sess.run(b))
# 先建立 W, b 的容器
W = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name="weights")
b = tf.Variable(np.arange(3).reshape((1, 3)), dtype=tf.float32, name="biases")

# 这里不需要初始化步骤 init= tf.initialize_all_variables()

saver = tf.train.Saver()
with tf.Session() as sess:
    # 提取变量
    saver.restore(sess, "my_saver/save_net.ckpt")
    print("weights:", sess.run(W))
    print("biases:", sess.run(b))
