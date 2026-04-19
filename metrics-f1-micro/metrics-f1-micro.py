import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    # precision = so du doan positive dung / tong so du doan positive => muon model du doan cang ki cang tot, khong duoc du doan postive bua bai
    # recall = so du doan postive dung / (so du doan positive dung + so du doan negative sai) => muon so luon case predict postitive dung cang nhieu cang tot (dua tren so luong case postive thuc te), 
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    pre = np.where(y_true == y_pred, 1, 0)
    tp = pre.sum()
    fn = fp = y_pred.size - tp
    return 2 * tp / (2 * tp + fp + fn)
    