import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def add_layer (inputs ,in_size,out_size, activation_function= None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))#变量矩阵
    biases = tf.Variable(tf.zeros([1,out_size])+0.1)#常量矩阵
    Weights_x_plus_bia= tf.matmul(inputs,Weights)+biases#矩阵相乘
    if activation_function== None:
        outputs = Weights_x_plus_bia
    else :
        outputs = activation_function(Weights_x_plus_bia)
    return outputs

x_data = np.linspace(-1,1,300)[:,np.newaxis]#增加列维度变成（300,1）矩阵
noise = np.random.normal(0,0.05,x_data.shape).astype(np.float32)#在正态分布中随机取得样本，平均值为0，方差0.05类型和x_data一样
y_data = np.square(x_data)-0.5 + noise#定义y = x2-0.5

xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])#占位符字典

# 隐藏层，激励函数为TensorFlow自带的tf.nn.relu
hidden_Weights = tf.Variable(tf.random_normal([1, 10]))#一维十个神经元
hidden_biases = tf.Variable(tf.zeros([1, 10]) + 0.1)
hidden_layer = tf.nn.relu(tf.matmul(xs, hidden_Weights) + hidden_biases)
# print(hidden_layer)

# 输出层，不需要激励函数
output_Weights = tf.Variable(tf.random_normal([10, 1]))
output_biases = tf.Variable(tf.zeros([1, 1]) + 0.1)
prediction = tf.matmul(hidden_layer, output_Weights) + output_biases

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

session = tf.Session()
init = tf.global_variables_initializer()
session.run(init)

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
ax = plt.subplot(111)
ax.scatter(x_data,y_data)
plt.ion()#连续输出



for i in range(1000):
    session.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i % 50 ==0 :
        # print(session.run(loss,feed_dict={xs: x_data, ys: y_data}))
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass#抹除上一条线
        prediction_value = session.run(prediction,feed_dict={xs:x_data})
        lines = ax.plot(x_data,prediction_value,'r-',lw =5)
        plt.pause(0.1)#暂停0.1s

