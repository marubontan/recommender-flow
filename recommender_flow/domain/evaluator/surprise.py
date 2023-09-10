from typing import Dict, Generator, List, Tuple
from uuid import uuid4

import pandas as pd
from surprise import Dataset, Reader
from surprise.dataset import DatasetAutoFolds
from surprise.model_selection import LeaveOneOut, train_test_split
from surprise.trainset import Trainset

from recommender_flow.domain.data.processor import ProcessedData
from recommender_flow.domain.evaluator import Evaluation, Evaluator, ModelName
from recommender_flow.domain.metrics.surprise import (
    SurpriseHitRateMetrics,
    SurpriseMaeMetrics,
)
from recommender_flow.domain.model.surprise import SurpriseBaseModel
from recommender_flow.domain.util.type import TestDataSchema


class SurpriseEvaluator(Evaluator):
    def __init__(self, models: List[SurpriseBaseModel]):
        Evaluator.__init__(self, models)
        self._mae_metrics = SurpriseMaeMetrics()
        self._hit_rate_metrics = SurpriseHitRateMetrics()

    def execute(
        self, processed_data: ProcessedData
    ) -> Dict[ModelName, List[Evaluation]]:
        surprise_data = self._load_to_surprise(processed_data.refined_data.content)

        train_set, test_set = self._train_test_split(
            surprise_data, test_size=0.25, random_state=42
        )
        leave_one_out_train_set, leave_one_out_test_set = self._leave_one_out(
            surprise_data
        )

        evaluations = self._evaluate_models(
            train_set, test_set, leave_one_out_train_set, leave_one_out_test_set
        )
        return evaluations

    @staticmethod
    def _load_to_surprise(data: pd.DataFrame) -> DatasetAutoFolds:
        reader = Reader(sep=",", skip_lines=1)
        return Dataset.load_from_df(data, reader)

    @staticmethod
    def _train_test_split(
        data: DatasetAutoFolds, test_size: float, random_state: int = 42
    ) -> Tuple[Trainset, List[TestDataSchema]]:
        return train_test_split(data, test_size=test_size, random_state=random_state)

    @staticmethod
    def _leave_one_out(
        data: DatasetAutoFolds,
    ) -> Tuple[Trainset, List[TestDataSchema]]:
        leave_one_out = LeaveOneOut(n_splits=1, random_state=42)
        leave_one_out_set = next(leave_one_out.split(data))
        return leave_one_out_set

    def _evaluate_models(
        self,
        train_set: Trainset,
        test_set: List[TestDataSchema],
        leave_one_out_train_set: Trainset,
        leave_one_out_test_set: List[TestDataSchema],
    ) -> Dict[ModelName, List[Evaluation]]:
        return {
            model.__class__.__name__: self._evaluate(
                model,
                train_set,
                test_set,
                leave_one_out_train_set,
                leave_one_out_test_set,
            )
            for model in self._models
        }

    def _evaluate(
        self,
        model: SurpriseBaseModel,
        train_set: Trainset,
        test_set: List[TestDataSchema],
        leave_one_out_train_set: Trainset,
        leave_one_out_test_set: List[TestDataSchema],
    ) -> List[Evaluation]:
        model.fit(train_set)
        predictions = model.test(test_set)
        mae = self._mae_metrics.calculate(predictions)

        model.fit(leave_one_out_train_set)
        leave_one_out_predictions = model.test(leave_one_out_test_set)
        leave_one_out_anti_test_set = leave_one_out_train_set.build_anti_testset()
        leave_one_out_all_predictions = model.test(leave_one_out_anti_test_set)
        leave_one_out_hit_rate = self._hit_rate_metrics.calculate(
            leave_one_out_all_predictions, leave_one_out_predictions
        )

        return [
            Evaluation(uuid4(), model.id, model.name, "MAE", mae),
            Evaluation(
                uuid4(),
                model.id,
                model.name,
                "Hit Rate",
                leave_one_out_hit_rate,
            ),
        ]
