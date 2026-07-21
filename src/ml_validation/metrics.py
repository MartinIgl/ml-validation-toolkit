from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

def calculate_accuracy(y_true: list, y_pred: list) -> float:
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
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    
    return accuracy_score(y_true, y_pred)


def calculate_precision(
    y_true: list,
    y_pred: list,
    ) -> float:
    """
    Calculate the classification precision.

    Parameters
    ----------
    y_true : list
        Ground truth labels.

    y_pred : list
        Predicted labels.

    Returns
    -------
    float
        Precision score between 0 and 1.
    """
    return precision_score(y_true, y_pred)    


def calculate_recall(
    y_true: list,
    y_pred: list,
    ) -> float:
    """
    Calculate the classification recall.

    Parameters
    ----------
    y_true : list
        Ground truth labels.

    y_pred : list
        Predicted labels.

    Returns
    -------
    float
        recall score between 0 and 1.
    """
    return recall_score(y_true, y_pred)    


def calculate_f1(
    y_true: list,
    y_pred: list,
    ) -> float:
    """
    Calculate the classification f1.

    Parameters
    ----------
    y_true : list
        Ground truth labels.

    y_pred : list
        Predicted labels.

    Returns
    -------
    float
        f1 score between 0 and 1.
    """
    return f1_score(y_true, y_pred)    