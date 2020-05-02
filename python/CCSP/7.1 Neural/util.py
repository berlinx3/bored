from math import exp
from random import random
from functools import reduce


def dot_product(xs, ys):
    return sum(x * y
               for x, y in zip(xs, ys))


def sigmoid(x):
    return 1.0 / (1.0 + exp(-x))


def derivative_sigmoid(x):
    sig = sigmoid(x)
    return sig * (1 - sig)

def normalize_by_feature_scaling(dataset):
    for col_num in range(len(dataset[0])):
        column = [row[col_num] for row in dataset]
        maximum = max(column)
        minimum = min(column)
        for row_num in range(len(dataset)):
            dataset[row_num][col_num] = (dataset[row_num][col_num] - minimum) / (maximum / minimum)
        


class Neuron:
    def __init__(self, weights, learning_rate, activation_function, derivative_activation_function):
        self.weights = weights
        self.activation_function = activation_function 
        self.derivative_activation_function = derivative_activation_function
        self.learning_rate = learning_rate
        self.output_cache = 0.0
        self.delta = 0.0

    def output(self, inputs):
        self.output_cache = dot_product(inputs, self.weights)
        return self.activation_function(self.output_cache)


class Layer:
    def __init__(self, previous_layer, num_neurons, learning_rate, activation_function, derivative_activation_function):
        self.previous_layer = previous_layer
        self.neurons = []

        for _ in range(num_neurons):
            if previous_layer is None:
                random_weights = []
            else:
                random_weights = [random() for _ in range(len(previous_layer.neurons))]
            
            neuron = Neuron(random_weights, learning_rate, activation_function, derivative_activation_function)
            self.neurons.append(neuron)

        self.output_cache = [0.0 for _ in range(num_neurons)]

    def outputs(self,inputs):
        if self.previous_layer is None:
            self.output_cache = inputs
        else:
            self.output_cache = [n.output(inputs) for n in self.neurons]

        return self.output_cache

    def calculate_deltas_for_output_layer(self, expected):
        for n in range(len(self.neurons)):
            self.neurons[n].delta = self.neurons[n].derivative_activation_function(self.neurons[n].output_cache) * (expected[n] - self.output_cache[n])

    def calculate_deltas_for_hidden_layer(self, next_layer):
        for index, neuron in enumerate(self.neurons):
            next_weights = [n.weights[index] for n in next_layer.neurons]
            next_deltas = [n.delta for n in next_layer.neurons]
            sum_weights_and_deltas = dot_product(next_weights, next_deltas)
            neuron.delta = neuron.derivative_activation_function(neuron.output_cache) * sum_weights_and_deltas
        
    
class Network:
    def __init__(self, layer_structure, learning_rate, activation_function = sigmoid, derivative_activation_function = derivative_sigmoid):
        if len(layer_structure) < 3:
            raise ValueError("Error: Should be at least 3 layers (1 input, 1 hidden, 1 output)")

        self.layers = []
        input_layer = Layer(None, layer_structure[0], learning_rate, activation_function, derivative_activation_function)
        self.layers.append(input_layer)

        for previous, num_neurons in enumerate(layer_structure[1::]):
            next_layer = Layer(self.layers[previous], num_neurons, learning_rate, activation_function, derivative_activation_function)
            self.layers.append(next_layer)

        
    def output(self, input):
        return reduce(lambda inputs, layer: layer.outputs(inputs), self.layers, input)

    def backpropagate(self, expected):
        last_layer = len(self.layers) - 1
        self.layers[last_layer].calculate_deltas_for_output_layer(expected)

        for l in range(last_layer - 1, 0 , -1):
            self.layers[l].calculate_deltas_for_hidden_layer(self.layers[l + 1])

    def update_weights(self):
        for layer in self.layers[1:]:
            for neuron in layer.neurons:
                for w in range(len(neuron.weights)):
                    neuron.weights[w] = neuron.weights[w] + (neuron.learning_rate * (layer.previous_layer.output_cache[w]) * neuron.delta)

    def train(self, inputs, expecteds):
        for location, xs in enumerate(inputs):
            ys = expecteds[location]
            self.output(xs)
            self.backpropagate(ys)
            self.update_weights()

    def validate(self, inputs, expecteds, interpret_output):
        correct = 0
        for input, expected in zip(inputs, expecteds):
            result = interpret_output(self.output(input))
            if result == expected:
                correct += 1

        percentage = correct / len(inputs)
        return correct, len(inputs), percentage