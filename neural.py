import numpy as np

#these are both pretty self explanatory, neccesary nonetheless
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

#input should be organized where each interger = checking a specific state
#0; was_hit = false, 1; enemy_alive = True

default_input = np.array([
        [0, 0], [0, 0], [0, 0], [0, 0]
]) #default

binary_input1 = np.array([
        [0, 1], [1, 1], [1, 0], [0, 1]
]) #defend

binary_input2 = np.array([
        [0, 0], [1, 1], [1, 1], [1, 1]
]) #attack

binary_input3 = np.array([
        [1, 1], [1, 0], [1, 0], [0, 0]
]) #run

test_input = np.array([
        [0, 0], [0, 1], [0, 0], [1, 1]
])

default_output = np.array([[0], [0], [0], [0]]) #all are 0

binary_output1 = np.array([[0], [1], [0], [0]]) #defend is 1

binary_output2 = np.array([[1], [0], [0], [0]]) #attack is 1

binary_output3 = np.array([[0], [0], [1], [0]]) #run is 1

#fuck a training set, we will make do with 4 templates

class NeuralNet:
    def __init__(self, x, y):
        self.input = x #input
        self.weights1 = np.random.rand(self.input.shape[1], 16) #1 = num of features, 16 = num input layers
        self.weights2 = np.random.rand(16, 8) # 16 input layers to 8 hidden layers
        self.weights3 = np.random.rand(8, 1) # 8 hidden layers to 3 output layers
        self.y = y #output
        self.output = np.zeros((y.shape[0], 1)) #predicted output

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        self.layer3 = sigmoid(np.dot(self.layer2, self.weights3))
        self.output = self.layer3

    def backprop(self):
        d_weights3 = np.dot(self.layer2.T, (2 * (self.y - self.output) * sigmoid_deriv(self.output)))
        d_weights2 = np.dot(self.layer1.T, (np.dot(2 * (self.y - self.output) * sigmoid_deriv(self.output), self.weights3.T) * sigmoid_deriv(self.layer2)))
        d_weights1 = np.dot(self.input.T, (np.dot(np.dot(2 * (self.y - self.output) * sigmoid_deriv(self.output), self.weights3.T) * sigmoid_deriv(self.layer2), self.weights2.T) * sigmoid_deriv(self.layer1)))
        
        self.weights3 += d_weights3
        self.weights2 += d_weights2
        self.weights1 += d_weights1
    
    def train(self, X, y, epochs=10000): #executes all of the training
        self.input = X
        self.y = y
        for epoch in range(epochs):
            self.feedforward()
            self.backprop()

    def test(self, input):
        layer1 = sigmoid(np.dot(input, self.weights1))
        layer2 = sigmoid(np.dot(layer1, self.weights2))
        layer3 = sigmoid(np.dot(layer2, self.weights3))
        return layer3

#initializes, trains, reinforces the training, then provides output
nn = NeuralNet(default_input, default_output)
nn.train(binary_input1, binary_output1, 10000)
nn.feedforward()
nn.train(binary_input2, binary_output2, 10000)
nn.feedforward()
nn.train(binary_input3, binary_output3, 10000)
nn.feedforward()
print(test_input)
predictions = nn.test(test_input)
print(predictions)
