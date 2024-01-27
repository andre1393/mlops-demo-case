import mlflow

from settings import settings
from data_flavors.flavors import data_source_flavors, data_target_flavors
from pipeline.flavors import model_flavors


def run_batch(settings):
    predictor = model_flavors[settings.model_config['type']](            
        **settings.model_config['params']
    )
    
    dfs = data_source_flavors[settings.data_config['source']['type']](
        **settings.data_config['source']['load_params']
    ).load()

    save_method = data_target_flavors[settings.data_config['target']['type']](
        **settings.data_config['target']['save_params']
    )

    for df, metadata in dfs:
        predictions = predictor.predict(df)[1]
        save_method.save(df, predictions, metadata)

if __name__ == '__main__':
    run_batch(settings)
