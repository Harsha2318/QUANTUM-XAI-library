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
from quantum_xai import QuantumNeuralNetwork, QuantumSHAPExplainer

# Load data and create model
# Train model
# Generate explanations
```

## Documentation

Detailed documentation is available in the `docs/` directory, including:

- API reference
- Tutorials and examples
- Limitations and known issues

## Testing and CI

Unit and integration tests are included in the `tests/` directory. Continuous integration is set up with GitHub Actions to run tests on every push and pull request.

Run tests locally with:

```bash
pytest
```

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Developed by Quantum-XAI Contributors.

## Contact

For questions or support, please open an issue on GitHub.
