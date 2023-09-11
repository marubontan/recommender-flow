from typing import Dict

import pandas as pd

from recommender_flow.domain.data.layer import RawData, RefinedData, TrustedData
from recommender_flow.domain.data.processor import (
    DataProcessManager,
    ProcessedData,
    ToRaw,
    ToRefined,
    ToTrusted,
)
from recommender_flow.use_case.movie_lens.development.setting import (
    MOVIE_DATASET_PATH,
    RATING_DATASET_PATH,
)
from recommender_flow.util.logger import logger


class RatingsRawData(RawData):
    pass


class MoviesRawData(RawData):
    pass


class RatingsTrustedData(TrustedData):
    pass


class MoviesTrustedData(TrustedData):
    pass


class RatingsRefinedData(RefinedData):
    pass


class MoviesYearSimilarityRefinedData(RefinedData):
    pass


class RatingsToRaw(ToRaw):
    def process(self) -> RatingsRawData:
        df = pd.read_csv(RATING_DATASET_PATH)
        return RatingsRawData(df)


class MoviesToRaw(ToRaw):
    def process(self) -> MoviesRawData:
        df = pd.read_csv(MOVIE_DATASET_PATH)
        return MoviesRawData(df)


class RatingsToTrusted(ToTrusted):
    def process(self, raw_data: RatingsRawData) -> RatingsTrustedData:
        return RatingsTrustedData(raw_data.content, [raw_data])


class MoviesToTrusted(ToTrusted):
    def process(self, raw_data: MoviesRawData) -> MoviesTrustedData:
        return MoviesTrustedData(raw_data.content, [raw_data])


class RatingsToRefined(ToRefined):
    def process(self, trusted_data: RatingsTrustedData) -> RatingsRefinedData:
        return RatingsRefinedData(
            trusted_data.content[["userId", "movieId", "rating"]], [trusted_data]
        )


class MoviesYearSimilarityToRefined(ToRefined):
    def process(
        self, trusted_data: MoviesTrustedData
    ) -> MoviesYearSimilarityRefinedData:
        return MoviesYearSimilarityRefinedData(
            trusted_data.content[["movieId", "title"]], [trusted_data]
        )


class MovieLensDataProcessManager(DataProcessManager):
    def __init__(self):
        self._ratings_to_raw = RatingsToRaw()
        self._ratings_to_trusted = RatingsToTrusted()
        self._ratings_to_refined = RatingsToRefined()
        self._movies_to_raw = MoviesToRaw()
        self._movies_to_trusted = MoviesToTrusted()
        self.movie_year_similarity_to_refined = MoviesYearSimilarityToRefined()

    def process(self) -> Dict[str, ProcessedData]:
        logger.info("Data Processing starting")
        ratings_raw_data = self._ratings_to_raw.process()
        ratings_trusted_data = self._ratings_to_trusted.process(ratings_raw_data)
        ratings_refined_data = self._ratings_to_refined.process(ratings_trusted_data)
        movies_raw_data = self._movies_to_raw.process()
        movies_trusted_data = self._movies_to_trusted.process(movies_raw_data)
        movie_year_similarity_refined_data = (
            self.movie_year_similarity_to_refined.process(movies_trusted_data)
        )

        logger.info("Data Processing finished")
        return {
            "ratings": ProcessedData(ratings_refined_data),
            "year-similarity": ProcessedData(movie_year_similarity_refined_data),
        }
