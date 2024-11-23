from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model, split_data, train_model, select_columns


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=select_columns,
                inputs=["model_input_table", "params:features"],
                outputs="pdf_selected",
                name="select_columns_node",
            ),
            node(
                func=split_data,
                inputs=["pdf_selected", "params:preprocessing", "params:features"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="regressor",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["regressor", "X_test", "y_test"],
                outputs=None,
                name="evaluate_model_node",
            ),
        ]
    )
