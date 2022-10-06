import numpy as np

def calculate(l):
    if len(l) == 9:
        results = {}
        arr = np.array(l).reshape((3, 3))
        flatten_arr = np.matrix(arr).flatten()

        results["mean"] = [ list(np.mean(arr, axis=0)), list(np.mean(arr, axis=1)), flatten_arr.mean()]

        results["variance"] = [list(np.var(arr, axis=0)), list(np.var(arr, axis=1)), flatten_arr.var()]

        results["standard deviation"] = [list(np.std(arr, axis=0)), list(np.std(arr, axis=1)), flatten_arr.std()]

        results["max"] = [list(np.max(arr, axis=0)), list(np.max(arr, axis=1)), flatten_arr.max()]

        results["min"] = [list(np.min(arr, axis=0)), list(np.min(arr, axis=1)), flatten_arr.min()]

        results["sum"] = [list(np.sum(arr, axis=0)), list(np.sum(arr, axis=1)), flatten_arr.sum()]

        return results
    else:
        raise ValueError("List must contain nine numbers")
