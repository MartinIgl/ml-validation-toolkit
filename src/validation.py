from metrics import (
    calculate_accuracy,
    calculate_precision,
    calculate_recall,
    calculate_f1,
)
def evaluate_model(y_pred:list, y_true:list)->dict:
"""
    Orquestrator that Calculate the classification metrics.

    Parameters
    ----------
    y_true : list
        Ground truth labels.

    y_pred : list
        Predicted labels.

    Returns
    -------
    dict
    Dictionary containing the evaluation metrics.
         Accuracy, precision, recall and f1 score between 0 and 1.

    """

    return {"accuracy": calculate_accuracy(y_true,y_pred),
            "precision": calculate_precision(y_true,y_pred),
            "recall":  calculate_recall(y_true,y_pred),
            "f1": calculate_f1(y_true,y_pred) }