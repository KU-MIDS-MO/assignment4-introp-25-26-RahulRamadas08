import numpy as np

def mask_and_classify_scores(arr: np.ndarray):
    
    if type(arr) != np.ndarray:
        return None
    if (arr.ndim != 2) or (arr.shape[0] != arr.shape[1]):
        return None
    if arr.size < 16:
        return None
    
    cleaned = arr
    
    n = cleaned.shape[0]
    
    for i in range(n):
        for j in range(n):
            if cleaned[i][j] < 0:
                cleaned[i][j] = 0
            if cleaned[i][j] > 100:
                cleaned[i][j] = 100
    
    levels = np.zeros((n, n), dtype=int)
    
    for i in range(n):
        for j in range(n):
            if cleaned[i][j] < 40:
                levels[i][j] = 0
            if (cleaned[i][j] >= 40) and (cleaned[i][j] < 70):
                levels[i][j] = 1
            if cleaned[i][j] >= 70:
                levels[i][j] = 2
    
    row_pass_counts = np.zeros(n, dtype=int)
    
    for i in range(n):
        for j in range(n):
            if cleaned[i][j] >= 50:
                row_pass_counts[i] += 1
    
    return (cleaned, levels, row_pass_counts)
    

arr = np.array([
            [-10,  20,  50, 110],
            [ 40,  69,  70, 101],
            [  0,  39,  41,  80],
            [ 55,  60,  95, 200]
        ])

print(mask_and_classify_scores(arr))