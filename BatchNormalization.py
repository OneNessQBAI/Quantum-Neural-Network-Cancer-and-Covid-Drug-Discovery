import numpy as np

# Batch Normalization Forward Pass Calculations

def calculate_mean_variance(X, eps=1e-5):
    mean = np.mean(X, axis=0)
    variance = np.var(X, axis=0)
    return mean, variance


def normalize_input(X, mean, variance, eps=1e-5):
    return (X - mean) / np.sqrt(variance + eps)


def scale_and_shift(X_normalized, gamma, beta):
    return gamma * X_normalized + beta


def batch_normalization_forward(X, gamma, beta, eps=1e-5):
    mean, variance = calculate_mean_variance(X, eps)
    X_normalized = normalize_input(X, mean, variance, eps)
    out = scale_and_shift(X_normalized, gamma, beta)
    return out, X_normalized, mean, variance

# Batch Normalization Backward Pass Calculations

def calculate_gradients(dout, X_normalized, mean, variance, gamma, beta, eps=1e-5):
    N, D = dout.shape
    
    X_mu = X_normalized * np.sqrt(variance + eps)
    dbeta = np.sum(dout, axis=0)
    dgamma = np.sum(dout * X_normalized, axis=0)
    
    dX_normalized = dout * gamma
    dvariance = np.sum(dX_normalized * (X_normalized - mean), axis=0) * -0.5 * np.power(variance + eps, -1.5)
    dmean = np.sum(dX_normalized * -1 / np.sqrt(variance + eps), axis=0) + dvariance * np.sum(-2 * (X_normalized - mean), axis=0) / N
    
    dX = (dX_normalized / np.sqrt(variance + eps)) + (dvariance * 2 * (X_normalized - mean) / N) + (dmean / N)
    
    return dX, dgamma, dbeta


def batch_normalization_backward(dout, X_normalized, mean, variance, gamma, beta, eps=1e-5):
    return calculate_gradients(dout, X_normalized, mean, variance, gamma, beta, eps)

# Test function to combine and verify

def test_batch_normalization(X, gamma, beta, dout, eps=1e-5):
    mean, variance = calculate_mean_variance(X, eps)
    X_normalized = normalize_input(X, mean, variance, eps)
    output = scale_and_shift(X_normalized, gamma, beta)
    
    dX, dgamma, dbeta = calculate_gradients(dout, X_normalized, mean, variance, gamma, beta, eps)
    
    return output, dX, dgamma, dbeta

# Example usage
if __name__ == "__main__":
    X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Example input
    gamma = np.array([1, 1, 1])  # Example scale parameter
    beta = np.array([0, 0, 0])  # Example shift parameter
    dout = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])  # Example upstream gradient
    output, dX, dgamma, dbeta = test_batch_normalization(X, gamma, beta, dout)
    print(f"Output: {output}")
    print(f"dX: {dX}")
    print(f"dgamma: {dgamma}")
    print(f"dbeta: {dbeta}")
