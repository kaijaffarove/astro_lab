import numpy as np
def load_file(filename):
    with np.load(filename) as d:
        arr = d["arr_0"].astype(float)
    return arr
