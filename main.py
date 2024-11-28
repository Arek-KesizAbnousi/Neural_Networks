# main.py

import numpy as np
import pandas as pd
from utils.data_preprocessing import load_and_preprocess_data
from utils.evaluation import evaluate_models
from models.neural_networks import get_neural_network_models
from models.classification_methods import get_classification_models

def main():
    # Load and preprocess data
    X, y = load_and_preprocess_data('data/sonar_data.csv')
    
    # Define models
    nn_models = get_neural_network_models(input_dim=X.shape[1])
    classification_models = get_classification_models()
    
    # Combine all models
    all_models = {**nn_models, **classification_models}
    
    # Evaluate models
    results = evaluate_models(all_models, X, y, n_splits=100, test_size=50)
    
    # Save results
    results.to_csv('results/accuracy_table.csv', index=False)
    print(results)

if __name__ == "__main__":
    main()
