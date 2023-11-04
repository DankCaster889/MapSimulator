import tensorflow as tf

tensor_a = tf.constant(3.0)
tensor_b = tf.constant(2.0)

result = tensor_a * tensor_b

with tf.Session() as session:
    output = session.run(result)
    print("result: ", output)
