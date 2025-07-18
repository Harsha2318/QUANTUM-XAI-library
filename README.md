# Quantum-XAI Library

Quantum-XAI is a comprehensive explainable quantum machine learning library designed to provide interpretability and transparency for quantum neural network models. Inspired by classical explainability tools like SHAP and LIME, Quantum-XAI adapts these concepts to the quantum domain, enabling users to understand and trust quantum model predictions.

## Features

- Variational Quantum Classifier (VQC) implementation with flexible encoding schemes.
- Multiple quantum explainability methods including Quantum SHAP, Gradient, LIME, and Perturbation explainers.
- Visualization tools for feature importance and quantum circuit explanations.
- Dataset loaders for popular datasets prepared for quantum machine learning.
- Benchmarking and evaluation utilities for explanation quality and consistency.
- Comprehensive documentation, examples, and community standards.

## Installation

Install via pip from PyPI:

```bash
pip install quantum_xai
```

Or clone the repository and install dependencies:

```bash
git clone https://github.com/Harsha2318/QUANTUM-XAI-library.git
cd QUANTUM-XAI-library
pip install -r requirements.txt
```

## Usage

### Quick Start Example

```python
from quantum_xai import QuantumXAIDemo

demo = QuantumXAIDemo()
results = demo.run_complete_demo(dataset='iris', n_samples=80)
```

### Custom Model Training

```python
from quantum_xai import QuantumNeuralNetwork, QuantumSHAPExplainer, QuantumGradientExplainer, QuantumXAIVisualizer
from sklearn.model_selection import train_test_split
from quantum_xai import QuantumDatasetLoader

# Load data
X, y, feature_names = QuantumDatasetLoader.load_iris_quantum(n_samples=100)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train model
model = QuantumNeuralNetwork(n_features=X.shape[1], n_qubits=4, n_layers=2)
model.train(X_train, y_train, epochs=100, lr=0.1)

# Create explainers
shap_explainer = QuantumSHAPExplainer(model, X_train)
gradient_explainer = QuantumGradientExplainer(model)

# Generate explanation for a sample
explanation = shap_explainer.explain(X_test, 0)

# Visualize explanation
visualizer = QuantumXAIVisualizer()
fig = visualizer.plot_feature_importance(explanation, feature_names)
fig.show()
```

---

## Research Applications

- Benchmark quantum vs classical explainability methods
- Analyze quantum Fisher information and entanglement effects
- Extend to other quantum platforms (Qiskit, Cirq)
- Develop advanced quantum-specific explanation metrics
- Apply to real quantum datasets in chemistry, finance, and more

---

## Project Structure

- `QuantumNeuralNetwork`: Variational quantum classifier model
- `QuantumExplainer` and subclasses: Explainability methods (SHAP, Gradient, LIME, Perturbation)
- `QuantumXAIVisualizer`: Visualization utilities
- `QuantumDatasetLoader`: Dataset loading and preprocessing
- `QuantumXAIBenchmark`: Benchmarking and evaluation tools
- `QuantumXAIDemo`: Complete demo and example workflows
- `save_model_and_explanations` / `load_model_and_explanations`: Persistence utilities
- `QuantumXAIResearch`: Advanced research features

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Developed by Quantum-XAI Contributors.

## Contact

For questions or support, please open an issue on GitHub.
