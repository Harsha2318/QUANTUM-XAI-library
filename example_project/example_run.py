import pennylane as qml
import pennylane.numpy as pnp
import numpy as np
from sklearn.model_selection import train_test_split
from quantum_xai import QuantumNeuralNetwork, QuantumSHAPExplainer, QuantumGradientExplainer, QuantumXAIVisualizer, QuantumDatasetLoader

def main():
    # Load dataset
    X, y, feature_names = QuantumDatasetLoader.load_iris_quantum(n_samples=100)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Create and train quantum neural network with pnp parameters
    model = QuantumNeuralNetwork(n_features=X.shape[1], n_qubits=4, n_layers=2)

    # Update model params to use pnp array with requires_grad=True
    model.params = pnp.array(model.params, requires_grad=True)

    # Modified train method to print parameter values and loss for debugging
    def train_with_debug(self, X_train, y_train, epochs=50, lr=0.1):
        opt = qml.AdamOptimizer(stepsize=lr)

        def cost_fn(params):
            predictions = pnp.stack([self.qnode(x, params) for x in X_train])
            labels = 2 * y_train - 1
            loss = pnp.mean(pnp.clip(1 - labels * predictions, a_min=0, a_max=None))
            return loss

        for epoch in range(epochs):
            self.params = opt.step(cost_fn, self.params)
            if epoch % 10 == 0:
                loss = cost_fn(self.params)
                print(f"Epoch {epoch}: Loss = {loss:.4f}")
                print(f"Params sample: {pnp.ravel(self.params)[:5]}")

        self.is_trained = True
        print("Training completed!")

    # Replace train method with debug version
    model.train = train_with_debug.__get__(model)

    model.train(X_train, y_train, epochs=50, lr=0.1)

    # Create explainers
    shap_explainer = QuantumSHAPExplainer(model, X_train, n_samples=50)
    gradient_explainer = QuantumGradientExplainer(model)

    # Generate explanation for first test sample
    explanation_shap = shap_explainer.explain(X_test, 0)
    explanation_grad = gradient_explainer.explain(X_test, 0)

    # Visualize explanations
    visualizer = QuantumXAIVisualizer()
    fig_shap = visualizer.plot_feature_importance(explanation_shap, feature_names)
    fig_grad = visualizer.plot_feature_importance(explanation_grad, feature_names)

    fig_shap.show()
    fig_grad.show()

if __name__ == "__main__":
    main()
