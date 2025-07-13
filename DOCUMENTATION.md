# Quantum-XAI Library Documentation

## Overview

Quantum-XAI is a comprehensive library designed to provide explainability for quantum machine learning models, specifically quantum neural networks (QNNs). It offers multiple explanation methods inspired by classical ML explainability techniques, adapted for quantum models. The library also includes quantum data encodings, a variational quantum classifier implementation, visualization tools, benchmarking utilities, and advanced research features.

---

## Core Components

### ExplanationResult

A data container class that holds the results of an explanation, including feature importance scores, sample index, prediction values, explanation method, and metadata.

### QuantumExplainer (Abstract Base Class)

Defines the interface for all quantum explainers. Requires implementation of the `explain` method for single sample explanation and provides a batch explanation method.

---

## Quantum Data Encodings

- **Angle Encoding:** Encodes classical features as rotation angles on qubits.
- **Amplitude Encoding:** Encodes classical data into quantum state amplitudes.
- **IQP Encoding:** Instantaneous Quantum Polynomial encoding with layers of rotations and entangling gates.

---

## Quantum Neural Network (QuantumNeuralNetwork)

A variational quantum classifier implemented using PennyLane. Key features:

- Configurable number of qubits, layers, and encoding type.
- Parameter initialization and quantum circuit definition.
- Forward pass, prediction, and probability estimation.
- Training using Adam optimizer with hinge loss.

---

## Explainability Methods

### QuantumSHAPExplainer

SHAP-like explainer using sampling of feature coalitions to estimate marginal contributions.

### QuantumGradientExplainer

Gradient-based explainer using parameter-shift rule to compute feature gradients.

### QuantumLIMEExplainer

LIME-like explainer generating perturbed samples and fitting a weighted linear regression.

### QuantumPerturbationExplainer

Perturbation-based explainer using feature occlusion to measure importance.

---

## Visualization Tools (QuantumXAIVisualizer)

- Plot feature importance as horizontal bar charts.
- Compare multiple explanation methods side-by-side.
- Visualize quantum circuit structure with explanation overlays.
- Radar charts for quantum feature importance.

---

## Dataset Utilities (QuantumDatasetLoader)

Load and preprocess popular datasets (Iris, Wine, Breast Cancer) for quantum ML, including normalization and binary classification options.

---

## Benchmarking and Evaluation (QuantumXAIBenchmark)

- Compare multiple explainers on test samples.
- Compute explanation consistency via correlation.
- Evaluate explanation quality metrics such as faithfulness, sparsity, and stability.

---

## Complete Demo (QuantumXAIDemo)

An end-to-end demonstration of the library including data loading, model training, explanation generation, visualization, benchmarking, and reporting.

---

## Save and Load Utilities

- `save_model_and_explanations`: Save model parameters and explanations to JSON.
- `load_model_and_explanations`: Load model and explanations from JSON.

---

## Research Extensions (QuantumXAIResearch)

- Compute quantum Fisher information matrix.
- Analyze quantum entanglement contribution to predictions.
- Analyze quantum feature interactions beyond classical correlations.

---

## Usage

1. Import the desired components.
2. Load and preprocess data using `QuantumDatasetLoader`.
3. Create and train a `QuantumNeuralNetwork`.
4. Instantiate explainers (e.g., `QuantumSHAPExplainer`) with the trained model.
5. Generate explanations for samples.
6. Visualize explanations using `QuantumXAIVisualizer`.
7. Benchmark and evaluate explanations with `QuantumXAIBenchmark`.
8. Save and load models and explanations as needed.

---

## Requirements

- Python 3.7+
- PennyLane
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- pandas

---

## License and Contribution

This library is open-source and welcomes contributions. Please follow standard open-source contribution guidelines.

---

## Contact and Support

For questions, issues, or contributions, please use the GitHub repository issue tracker or contact the maintainers.
