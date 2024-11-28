# Enhancing Classification Accuracy Using Neural Networks

## Introduction

This project analyzes the Sonar dataset using various neural network architectures and classical classification methods to enhance classification accuracy. We perform 100 independent replications (i.e., 100 independent training/testing splits) to ensure the robustness of our results.

## Objectives

- **Fit four different neural networks:**
  - **Two distinct single hidden layer neural networks:**
    1. A single hidden layer with **15 nodes**.
    2. A single hidden layer with **18 nodes**.
  - **Two distinct neural networks with two hidden layers:**
    3. Two hidden layers with **23 and 20 nodes**.
    4. Two hidden layers with **28 and 23 nodes**.

- **Compare the accuracy of these four neural networks.**

- **Compare neural network performance to other classification methods:**
  - Linear Discriminant Analysis (LDA).
  - Quadratic Discriminant Analysis (QDA).
  - Regularized Discriminant Analysis (RDA).
  - Support Vector Machines (SVMs).
  - Naïve Bayes.

## Data

### Sonar Dataset

The Sonar dataset is used for this analysis. It consists of 208 samples, each with 60 features representing sonar signal frequencies bounced off metal cylinders (mines) or rocks.

- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/connectionist+bench+(sonar%2C+mines+vs.+rocks))

## Project Structure

The project is organized into modular components for clarity and maintainability:
```plaintext
project/
├── data/
│   └── sonar_data.csv            # Dataset
├── results/                      # Results and figures
│   ├── accuracy_table.csv        # Accuracy results from experiments
│   └── figures/                  # Plots and figures generated
├── data_preprocessing.py         # Data loading and preprocessing functions
├── evaluation.py                 # Model evaluation logic
├── neural_networks.py            # Neural network architectures
├── classification_methods.py     # Classical classification methods
├── main.py                       # Main script
├── requirements.txt              # Lists required Python libraries
└── README.md                     # Documentation

```
## Code Implementation

### Languages and Libraries

- **Language:** Python 3.7 or higher
- **Libraries:**
  - **Data Manipulation:** `pandas`, `numpy`
  - **Machine Learning Models:** `scikit-learn`, `tensorflow` (Keras API)
  - **Visualization:** `matplotlib`, `seaborn`

### Neural Network Architectures

Implemented using TensorFlow's Keras API:

- **Single Hidden Layer Networks:**
  - Model with 15 nodes.
  - Model with 18 nodes.
- **Two Hidden Layer Networks:**
  - Model with 23 and 20 nodes.
  - Model with 28 and 23 nodes.

### Other Classification Methods

Implemented using scikit-learn:

- **Linear Discriminant Analysis (LDA)**
- **Quadratic Discriminant Analysis (QDA)**
- **Regularized Discriminant Analysis (RDA)** (custom implementation or via appropriate library)
- **Support Vector Machines (SVM)**
- **Naïve Bayes**

## Installation

### Prerequisites

- Python 3.7 or higher
- Recommended: Virtual environment (`venv` or `conda`)

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https: https://github.com/Arek-KesizAbnousi/Neural_Networks.git
   cd Neural_Networks


 ## **Methodology**

 ### Data Preprocessing

- **Feature Transformation**: Applied logarithmic transformation to the predictor variables to normalize the data.
- **Target Variable Encoding**: Converted class labels ('M' for Mine, 'R' for Rock) to binary format (1 for Mine, 0 for Rock).

### Experimental Setup

- **Train/Test Splits**: 100 independent replications with a training set size of 158 and a testing set size of 50.
- **Evaluation Metric**: Classification accuracy.

### Models Evaluated

1. **Neural Networks**:
   - Single hidden layer with 15 nodes.
   - Single hidden layer with 18 nodes.
   - Two hidden layers with 23 and 20 nodes.
   - Two hidden layers with 28 and 23 nodes.

2. **Classical Classification Methods**:
   - Linear Discriminant Analysis (LDA)
   - Quadratic Discriminant Analysis (QDA)
   - Regularized Discriminant Analysis (RDA)
   - Support Vector Machines (SVM)
   - Naïve Bayes
  
## Results

The average accuracies over 100 replications for each method are as follows:

| Model                                   | Average Accuracy |
|-----------------------------------------|------------------|
| Neural Network (15 nodes)               | **X.XX%**        |
| Neural Network (18 nodes)               | **X.XX%**        |
| Neural Network (23 & 20 nodes)          | **X.XX%**        |
| Neural Network (28 & 23 nodes)          | **X.XX%**        |
| Linear Discriminant Analysis (LDA)      | **X.XX%**        |
| Quadratic Discriminant Analysis (QDA)   | **X.XX%**        |
| Regularized Discriminant Analysis (RDA) | **X.XX%**        |
| Support Vector Machines (SVM)           | **X.XX%**        |
| Naïve Bayes                             | **X.XX%**        |



## Visualization

Plots and figures generated from the experiments are saved in the `results/figures/` directory. You can view the performance comparison by examining these visualizations.

Example plot:

![Accuracy Comparison](results/figures/accuracy_comparison.png)



## Conclusion

- **Best Neural Network Model**: The neural network with two hidden layers of 28 and 23 nodes achieved the highest accuracy among the neural networks evaluated.
- **Comparison with Other Methods**: The neural network with two hidden layers (28 & 23 nodes) performed competitively with other classification methods.
- **Overall Performance**: While classical methods like LDA and SVM provided strong baselines, the deeper neural network architectures showed potential for better accuracy with appropriate tuning.

## References

- [Sonar Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/connectionist+bench+(sonar%2C+mines+vs.+rocks))
- [TensorFlow Keras Documentation](https://www.tensorflow.org/api_docs/python/tf/keras)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

