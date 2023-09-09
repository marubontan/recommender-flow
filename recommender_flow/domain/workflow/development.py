from datetime import datetime
from uuid import uuid4
from recommender_flow.domain.data.processor import DataProcessManager
from recommender_flow.domain.evaluator import Evaluator
from recommender_flow.domain.workflow.dto import WorkFlowDto

class DevelopmentWorkFlow:
    def __init__(self, data_process_manager: DataProcessManager,evaluator: Evaluator):
        self._id = uuid4()
        self._data_process_manager = data_process_manager
        self._evaluator = evaluator
    
    def execute(self) -> WorkFlowDto:
        processed_data = self._data_process_manager.process()
        evaluation = self._evaluator.execute(processed_data.refined_data)
        return WorkFlowDto(
            id=self._id,
            created_at=datetime.now(),
            evaluation = evaluation
        )

    