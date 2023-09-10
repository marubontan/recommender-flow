# recommender-flow
## Overview
This repo is the development and experiment pipeline for recommendation model.  
As default, scikit-surprise is wrapped and you can make use case for your development.  

## How to set up
First, update some libraries.  
```
pip install --upgrade setuptools wheel
```
On the top directory of this repo
```
pip install -e .
```

## Example
As example, development and experiment with MovieLens dataset is there.  
To run, you need to download the data, ml-latest-small.zip, from https://grouplens.org/datasets/movielens/ . There, you can find `ratings.csv`. On the `recommender_flow/use_case/movie_lens/development/setting.py`, you need to set the path to this `ratings.csv`.  
From the top of the repo, you can run
```
python recommender_flow/interface/script/development_movie_lens.py
```
It will run the SVD model and show simple evaluation.  
