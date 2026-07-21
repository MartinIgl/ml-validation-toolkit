from src.metrics import calculate_accuracy


def test_calculate_accuracy():

    y_true = [1, 0, 1, 1]
    y_pred = [1, 0, 0, 1]

    expected = 0.75

    result = calculate_accuracy(y_true, y_pred)

    assert result == expected


import pytest

from src.metrics import calculate_accuracy


def test_different_lengths():

    with pytest.raises(ValueError):

        calculate_accuracy(
            [1,0,1],
            [1,0]
        )