import numpy as np
import tensorflow as tf

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

weights= tf.Variable(tf.random_uniform([1],-1.0,1.0))#生成一个-1到1之间
biases = tf.Variable(tf.zeros([1]))#置0

y = weights * x_data + biases
loss = tf.reduce_mean(tf.square(y-y_data))#真实值得差距
optimizer = tf.train.GradientDescentOptimizer(0.5)#使用这种方法训练数据
train = optimizer.minimize(loss)#减少差距

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for step in range(301):
    sess.run(train)
    if step % 20 ==0:
        print(step,sess.run(weights),sess.run(biases))