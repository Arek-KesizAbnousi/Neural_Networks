# models/neural_networks.py

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

def create_model(layers, input_dim):
    model = Sequential()
    # Input layer
    model.add(Dense(layers[0], input_dim=input_dim, activation='relu'))
    # Hidden layers
    for units in layers[1:]:
        model.add(Dense(units, activation='relu'))
    # Output layer
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    return model

def get_neural_network_models(input_dim):
    models = {}
    # Single Hidden Layer Networks
    models['NN_15_nodes'] = lambda: create_model([15], input_dim)
    models['NN_18_nodes'] = lambda: create_model([18], input_dim)
    # Two Hidden Layer Networks
    models['NN_23_20_nodes'] = lambda: create_model([23, 20], input_dim)
    models['NN_28_23_nodes'] = lambda: create_model([28, 23], input_dim)
    return models
