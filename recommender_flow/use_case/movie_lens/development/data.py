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
    MOVIE_LENS_DATASET_PATH,
)
from recommender_flow.util.logger import logger


class MovieLensRawData(RawData):
    pass


class MovieLensTrustedData(TrustedData):
    pass


class MovieLensRefinedData(RefinedData):
    pass


class MovieLensToRaw(ToRaw):
    def process(self) -> MovieLensRawData:
        df = pd.read_csv(MOVIE_LENS_DATASET_PATH)
        return MovieLensRawData(df)


class MovieLensToTrusted(ToTrusted):
    def process(self, raw_data: MovieLensRawData) -> MovieLensTrustedData:
        return MovieLensTrustedData(raw_data.content, [raw_data])


class MovieLensToRefined(ToRefined):
    def process(self, trusted_data: MovieLensTrustedData) -> MovieLensRefinedData:
        return MovieLensRefinedData(
            trusted_data.content[["userId", "movieId", "rating"]], [trusted_data]
        )


class MovieLensDataProcessManager(DataProcessManager):
    def __init__(self, to_raw: ToRaw, to_trusted: ToTrusted, to_refined: ToRefined):
        self._to_raw = to_raw
        self._to_trusted = to_trusted
        self._to_refined = to_refined

    def process(self) -> ProcessedData:
        logger.info("Data Processing starting")
        raw_data = self._to_raw.process()
        trusted_data = self._to_trusted.process(raw_data)
        refined_data = self._to_refined.process(trusted_data)
        logger.info("Data Processing finished")
        return ProcessedData(refined_data)
