import numpy as np

def topsis(data, weights, impacts):
    # Normalize the decision matrix
    norm_data = data / np.sqrt((data ** 2).sum(axis=0))

    # Apply weights to the normalized matrix
    weighted_data = norm_data * weights

    # Determine the positive ideal and negative ideal solutions
    ideal_best = np.amax(weighted_data * impacts, axis=0)
    ideal_worst = np.amin(weighted_data * impacts, axis=0)

    # Calculate the separation measures
    separation_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    separation_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    # Calculate the relative closeness to the ideal solution
    score = separation_worst / (separation_best + separation_worst)

    return score
