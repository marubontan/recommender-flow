from typing import Dict, List
from uuid import uuid4

from recommender_flow.domain.data.processor import DataProcessManager, ProcessedData
from recommender_flow.domain.evaluator import Evaluation, Evaluator, ModelName
from recommender_flow.use_case.movie_lens.development.dto import OutputDto
from recommender_flow.util.logger import logger
from recommender_flow.util.type.status import Status


class MovieLensDevelopmentUseCase:
    def __init__(self, data_process_manager: DataProcessManager, evaluator: Evaluator):
        self._data_process_manager = data_process_manager
        self._evaluator = evaluator

    def execute(self) -> OutputDto:
        try:
            processed_data = self._get_processed_data()
            evaluations = self._evaluate(processed_data)
            return OutputDto(
                id=uuid4(), status=Status.SUCCESS, evaluations=evaluations, message=None
            )
        except Exception as e:
            logger.exception(e)
            return OutputDto(
                id=uuid4(), status=Status.FAILURE, evaluations=None, message=str(e)
            )

    def _get_processed_data(self) -> ProcessedData:
        return self._data_process_manager.process()

    def _evaluate(
        self, processed_data: ProcessedData
    ) -> Dict[ModelName, List[Evaluation]]:
        return self._evaluator.execute(processed_data)
