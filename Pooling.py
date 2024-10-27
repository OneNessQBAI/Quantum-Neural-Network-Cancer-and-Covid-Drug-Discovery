import numpy as np

# Piece 1: Pooling Forward Calculations

def pool_layer(X, f, stride, mode):
    (n_C, n_H_prev, n_W_prev) = X.shape
    
    n_H = int(1 + (n_H_prev - f) / stride)
    n_W = int(1 + (n_W_prev - f) / stride)
    
    X_pool = np.zeros((n_C, n_H, n_W))
    
    for h in range(n_H):
        for w in range(n_W):
            for c in range(n_C):
                vert_start = h * stride
                vert_end = vert_start + f
                horiz_start = w * stride
                horiz_end = horiz_start + f
                
                if mode == 'max':
                    X_pool[c, h, w] = np.max(X[c, vert_start:vert_end, horiz_start:horiz_end])
                elif mode == 'average':
                    X_pool[c, h, w] = np.mean(X[c, vert_start:vert_end, horiz_start:horiz_end])
    
    return X_pool

# Piece 2: Pooling Forward (Wrapper Function)

def pool_forward(X, f=2, stride=2, mode='max'):
    return pool_layer(X, f, stride, mode)

# Piece 3: Pooling Backward Calculations

def pool_gradients(dX_pool, X, f, stride, mode):
    (n_C, n_H_prev, n_W_prev) = X.shape
    
    n_H = int(1 + (n_H_prev - f) / stride)
    n_W = int(1 + (n_W_prev - f) / stride)
    
    dX = np.zeros(X.shape)
    
    for h in range(n_H):
        for w in range(n_W):
            for c in range(n_C):
                vert_start = h * stride
                vert_end = vert_start + f
                horiz_start = w * stride
                horiz_end = horiz_start + f
                
                if mode == 'max':
                    X_slice = X[c, vert_start:vert_end, horiz_start:horiz_end]
                    mask = (X_slice == np.max(X_slice))
                    dX[c, vert_start:vert_end, horiz_start:horiz_end] += mask * dX_pool[c, h, w]
                elif mode == 'average':
                    da = dX_pool[c, h, w]
                    shape = (f, f)
                    dX[c, vert_start:vert_end, horiz_start:horiz_end] += np.ones(shape) * da / (f * f)
    
    return dX

# Piece 4: Pooling Backward (Wrapper Function)

def pool_backward(dX_pool, X, f=2, stride=2, mode='max'):
    return pool_gradients(dX_pool, X, f, stride, mode)

# Test function to combine and verify

def test_pooling(X, dX_pool, f=2, stride=2, mode='max'):
    X_pool = pool_forward(X, f, stride, mode)
    dX = pool_backward(dX_pool, X, f, stride, mode)
    
    return X_pool, dX

# Example usage
if __name__ == "__main__":
    X = np.random.rand(3, 10, 10)  # Example input of shape (n_C, n_H_prev, n_W_prev)
    dX_pool = np.random.rand(3, 5, 5)  # Example gradient w.r.t. output
    X_pool, dX = test_pooling(X, dX_pool, f=2, stride=2, mode='max')
    print(f"Pooled Output (X_pool): {X_pool}")
    print(f"Gradient w.r.t. input (dX): {dX}")
