import mlflow

from utils import Singleton

mlflow_flavors = {
    'sklearn': mlflow.sklearn
}


class MLFlowPredictor(metaclass=Singleton):
    def __init__(self, model_name, model_flavor, **kwargs):
        mlflow_flavor = mlflow_flavors.get(model_flavor)
        print(f'loading MLFlow model, flavor {model_flavor} from models:/{model_name}')
        self.model = mlflow_flavor.load_model(model_uri=f'models:/{model_name}')

    def predict(self, data):
        return data, self.model.predict(data)
