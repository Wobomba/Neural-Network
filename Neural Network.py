class NeuralNetwork:
    def __init__(self,x,y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1],4)
        self.weights2 = np.random.rand(4,1)
        self.y = y
        self.output = np.zeros(y.shape)
#for a two layer neural network, obtaining the result of the neural network(predicted output from the feedforward function below)
    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))
#obtaining the accuracy of the predictions made by the neural network
    def backprop(self):
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output)*sigmoid_derivation(self.output)))
        d_weights1 = np.dot(self.input.T, (np.dot(2*(self.y - self.output)*sigmoid_derivation(self.output), self.weights2.T)*sigmoid_derivation(self.layer1)))
#updating the weights
        self.weights1 += d_weights1
        self.weights2 +=d_weights2
