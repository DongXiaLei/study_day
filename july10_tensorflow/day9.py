#卷积神经网络
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data',one_hot=True)
#测试准确度
def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})  # tf.equal返回A的张量型bool
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))#tf.argmax(input,axis=0/1)1为返回行最大元素索引
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))#tf.cast类型转换（A,B）A转为B返回张量
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result

def weight_variable(shape):
    initial = tf.truncated_normal(shape,stddev=.1)#产生随机变量
    return tf.Variable(initial)
def bias_variable(shape):
    return  tf.constant(0.1,shape= shape)
def conv2d(x,W):#定义y=Wx+b
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')#strides =[1,x_move,y_move,1]
def max_pool_2x2(x):#池化
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')


xs = tf.placeholder(tf.float32,[None,784])#28x28None表示不管输入多少样本
ys = tf.placeholder(tf.float32,[None,10])
keep_prob = tf.placeholder(tf.float32)#overfitting的占位符
x_images = tf.reshape(xs,[-1,28,28,1])#-1表示不管输入的维数，后一个1表示图片高1表示黑白3表示RGB
##conv1 layer1
W_conv1 = weight_variable([5,5,1,32])#patch 5x5 in_size =1高度（黑白）out_size =32
b_conv1 = bias_variable([32])
h_conv1 = tf.nn.relu(conv2d(x_images,W_conv1)+b_conv1)#out_size 28x28x32
h_pool1 = max_pool_2x2(h_conv1)# 14x14x32

##conv1 layer2
W_conv2 = weight_variable([5,5,32,64])#patch 5x5 in_size =32高度out_size =64
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2)#out_size 14x14x64
h_pool2 = max_pool_2x2(h_conv2)# 7x7x64

#function layer1
W_func1 = weight_variable([7*7*64,1024])
b_func1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64])
h_func1 = tf.nn.relu(tf.matmul(h_pool2_flat,W_func1)+b_func1)
h_funcl_drop = tf.nn.dropout(h_func1,keep_prob)

#function layer2
W_func2 = weight_variable([1024,10])
b_func2 = bias_variable([10])
prediction = tf.nn.softmax(tf.matmul(h_funcl_drop,W_func2)+b_func2)

#误差
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),reduction_indices=[1]))

train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

sess =tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys,keep_prob:0.5})
    if i % 50 == 0:
        print(compute_accuracy(mnist.test.images,mnist.test.labels))


