import tensorflow as tf


state = tf.Variable(0,name ='counter')#变量
one = tf.constant(1)#常量
# print(state.name)
new_value = tf.add(state, one)
update = tf.assign(state,new_value)#将后边的赋值到前面的

init = tf.initialize_all_variables()#初始化 必须有
with  tf.Session() as sess:
    sess.run(init)#必须有
    for _ in range(3):
        # sess.run(update)
        print(sess.run(update))

