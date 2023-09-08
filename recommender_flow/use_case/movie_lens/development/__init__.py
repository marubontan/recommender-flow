from recommender_flow.use_case.movie_lens.development.dto import OutputDto
from recommender_flow.util.logger import logger
from recommender_flow.util.type.status import Status

class MovieLensDevelopmentUseCase:
    def __init__(self):
        pass

    def execute(self):
        try:
            return OutputDto(status=Status.SUCCESS)
        except Exception as e:
            logger.exception(e)
            return OutputDto(status=Status.FAILURE, message=str(e))