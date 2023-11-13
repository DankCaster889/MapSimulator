import numpy as np

#these are both pretty self explanatory, neccesary nonetheless
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

#input should be organized where each interger = checking a specific state
#0; was_hit = false, 1; enemy_alive = True
#alterations are probably neccesary
binary_input = np.array([
        [0, 0], [1, 1], [1, 0], [0, 1]
])

binary_output = np.array([[0], [0], [1], [0]])
#the values here we can assign pretty much however we need
#but we have to keep in mind how exactly we want to process
#the information via binary

#have now realized bigger issue,
#this is one data set, we need thousands
#to train it properly

class NeuralNet:
    def __init__(self, x, y):
        self.input = x #input                   #1 = num of features
        self.weights1 = np.random.rand(self.input.shape[1], 16) #3 = num of outputs
        #line above assigns number of features and output layers
        self.weights2 = np.random.rand(16, 8) # 16 input layers to 8 hidden layers
        self.weights3 = np.random.rand(8, 3) # 8 hidden layers to 3 output layers
        self.y = y #output
        self.output = np.zeros((y.shape[0], 1)) #predicted output

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        self.layer3 = sigmoid(np.dot(self.layer2, self.weights3))
        self.output = self.layer3
        #I'm gonna be honest I'm not even sure if this code is doing anything

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
        pass
        #need to figure out what exactly is going on
        #so I can properly pass data through it

nn = NeuralNet(binary_input, binary_output)
nn.train(binary_input, binary_output, 10000)

nn.feedforward()
predictions = nn.output
print(predictions)
