#!/bin/sh

export DATASET_PATH=$(realpath $DATASET_PATH)

if [ -f $DATASET_PATH ]; then \
        echo 'File exists. Skipping download'; \
    else \
        echo 'File does not exist. Downloading from kaggle'; \
        python3 download_data.py; \
fi

jupyter nbconvert --to notebook --execute /app/model_training/experiments.ipynb
