from sklearn.metrics import accuracy_score

def calculate_accuracy(
    y_true: list,
    y_pred: list,
    ) -> float:
    """
    Calculate the classification accuracy.

    Parameters
    ----------
    y_true : list
        Ground truth labels.

    y_pred : list
        Predicted labels.

    Returns
    -------
    float
        Accuracy score between 0 and 1.
    """
    raise ValueError(
    "y_true and y_pred must have the same length.")
    return accuracy_score(y_true, y_pred)