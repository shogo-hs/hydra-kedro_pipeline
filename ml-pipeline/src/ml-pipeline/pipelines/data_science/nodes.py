import logging

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

def select_columns(data: pd.DataFrame, features: list) -> pd.DataFrame:
    """
    Selects only the necessary columns from the dataset.

    Args:
        data: Data containing all columns.
        parameters: Parameters defined in parameters/data_science.yml.

    Returns:
        Data containing only the selected columns.
    """
    required_columns = features + ["price"]
    return data[required_columns]

def split_data(data: pd.DataFrame, preprocess_parameters: dict, features: list) -> tuple:
    """
    Splits data into features and targets training and test sets.

    Args:
        data: Data containing selected features and target.
        parameters: Parameters defined in parameters/data_science.yml.

    Returns:
        Split data (X_train, X_test, y_train, y_test).
    """
    X = data[features]
    y = data["price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=preprocess_parameters["test_size"], random_state=preprocess_parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test



def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """Trains the linear regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor


def evaluate_model(
    regressor: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series
):
    """Calculates and logs the coefficient of determination.

    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    y_pred = regressor.predict(X_test)
    score = r2_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient R^2 of %.3f on test data.", score)
