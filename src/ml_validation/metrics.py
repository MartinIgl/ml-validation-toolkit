from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

def calcular_metricas(y_real, y_pred):
    tp = fp = tn = fn = 0
    
    # Contar TP, FP, TN, FN
    for real, pred in zip(y_real, y_pred):
        if real == 1 and pred == 1:
            tp += 1
        elif real == 0 and pred == 1:
            fp += 1
        elif real == 0 and pred == 0:
            tn += 1
        elif real == 1 and pred == 0:
            fn += 1
            
    # Total de elementos
    total = tp + tn + fp + fn
    
    # Accuracy (Exactitud)
    accuracy = (tp + tn) / total if total > 0 else 0
    
    # Precision (Precisión)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    
    # Recall (Exhaustividad)
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    
    # F1-Score
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }
    


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
    
    tp = fp = tn = fn = 0
    
    # Contar TP, FP, TN, FN
    for real, pred in zip(y_true, y_pred):
        if real == 1 and pred == 1:
            tp += 1
        elif real == 0 and pred == 1:
            fp += 1
        elif real == 0 and pred == 0:
            tn += 1
        elif real == 1 and pred == 0:
            fn += 1
            
    # Total de elementos
    total = tp + tn + fp + fn
    
    return (tp + tn) / total if total > 0 else 0


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
    tp = fp = tn = fn = 0
    
    # Contar TP, FP, TN, FN
    for real, pred in zip(y_true, y_pred):
        if real == 1 and pred == 1:
            tp += 1
        elif real == 0 and pred == 1:
            fp += 1
        elif real == 0 and pred == 0:
            tn += 1
        elif real == 1 and pred == 0:
            fn += 1
            
    # Total de elementos
    total = tp + tn + fp + fn
    
    return tp / (tp + fp) if (tp + fp) > 0 else 0

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
    tp = fp = tn = fn = 0
    
    # Contar TP, FP, TN, FN
    for real, pred in zip(y_true, y_pred):
        if real == 1 and pred == 1:
            tp += 1
        elif real == 0 and pred == 1:
            fp += 1
        elif real == 0 and pred == 0:
            tn += 1
        elif real == 1 and pred == 0:
            fn += 1
            
    # Total de elementos
    total = tp + tn + fp + fn    
    return  tp / (tp + fn) if (tp + fn) > 0 else 0



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
        # 1. Calcula y guarda los valores en variables locales
    prec = calculate_precision(y_true, y_pred)
    rec = calculate_recall(y_true, y_pred)
    
    # 2. Usa las variables locales para el cálculo y la condición
    if (prec + rec) > 0:
        return (2 * prec * rec) / (prec + rec)
    else:
        return 0.0