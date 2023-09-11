from recommender_flow.domain.evaluator.surprise import SurpriseEvaluator
from recommender_flow.use_case.movie_lens.development import MovieLensDevelopmentUseCase
from recommender_flow.use_case.movie_lens.development.data import (
    MovieLensDataProcessManager,
)
from recommender_flow.use_case.movie_lens.development.model import SvdModel
from recommender_flow.util.type.status import Status

if __name__ == "__main__":
    data_processor = MovieLensDataProcessManager()
    svd_model = SvdModel(name="SVD")
    evaluator = SurpriseEvaluator(models=[svd_model])
    use_case = MovieLensDevelopmentUseCase(
        data_process_manager=data_processor, evaluator=evaluator
    )
    output_dto = use_case.execute()
    assert output_dto.status == Status.SUCCESS
    print(output_dto.evaluations)
