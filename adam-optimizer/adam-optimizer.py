import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    m = np.array(m)
    v = np.array(v)
    grad = np.array(grad)
    param = np.array(param)
    
    m_t = beta1 * m + (1 - beta1) * grad
    v_t = beta2 * v + (1 - beta2) * grad**2

    mt_hat = m_t / (1 - beta1 ** t) 
    vt_hat = v_t / (1 - beta2 ** t)

    param_t = param - lr * mt_hat / np.sqrt(vt_hat + eps)
    
    return (param_t, m_t, v_t)
    