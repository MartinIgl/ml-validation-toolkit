# ML Validation Toolkit

A lightweight Python toolkit to evaluate, compare and document Machine Learning classification models.

## Objectives

- Evaluate classification models
- Compare experiments
- Generate reports
- Visualize metrics
- Improve reproducibility

## Status

ml-validation-toolkit
│
├── src
│   └──ml_validation
│       ├── __init__.py
│       ├── metrics.py
│       ├── plots.py
│       ├── reports.py
│       └── validation.py
│
└── tests
    └── test_metrics.py
    
✔ Accuracy
✔ Precision
✔ Recall
✔ F1 Score
✔ ROC AUC
✔ Confusion Matrix
✔ HTML Reports

Status

# Validation.py
## Ejemplo de uso directo si se ejecuta como script
if __name__ == "__main__":
    y_t = [1, 0, 1, 1]
    y_p = [1, 0, 0, 1]
    
    resultados = evaluate_model(y_t, y_p)
    
    print("Resultados de la evaluación:")
    for metrica, valor in resultados.items():
        print(f"{metrica.capitalize()}: {valor:.4f}")   