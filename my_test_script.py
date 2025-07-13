# my_test_script.py

# Import classes from your local module
from quantum_xai import QuantumNeuralNetwork, QuantumDatasetLoader, QuantumSHAPExplainer

# Load a dataset
X, y, feature_names = QuantumDatasetLoader.load_iris_quantum(n_samples=20)

# Create and train a quantum neural network
model = QuantumNeuralNetwork(n_features=X.shape[1], n_qubits=4, n_layers=2)
model.train(X, y, epochs=10, lr=0.1)

# Use an explainer
explainer = QuantumSHAPExplainer(model, X, n_samples=10)
explanation = explainer.explain(X, 0)

# Print the explanation
print("Feature importances:", explanation.feature_importance)
print("Prediction:", explanation.prediction)
