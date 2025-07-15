import argparse
from utils.backend_selector import get_device
from quantum_xai import QuantumNeuralNetwork, QuantumDatasetLoader, QuantumSHAPExplainer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", default="default", help="Backend to use (default, lightning, aer, ibmq)")
    args = parser.parse_args()

    device = get_device(args.backend, wires=4)

    # Load a dataset
    X, y, feature_names = QuantumDatasetLoader.load_iris_quantum(n_samples=20)

    # Create and train a quantum neural network
    model = QuantumNeuralNetwork(n_features=X.shape[1], n_qubits=4, n_layers=2, device=device)
    model.train(X, y, epochs=10, lr=0.1)

    # Use an explainer
    explainer = QuantumSHAPExplainer(model, X, n_samples=10)
    explanation = explainer.explain(X, 0)

    # Print the explanation
    print("Feature importances:", explanation.feature_importance)
    print("Prediction:", explanation.prediction)

if __name__ == "__main__":
    main()
