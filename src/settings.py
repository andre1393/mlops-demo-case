import yaml


class Settings:
    def __init__(self, model_config, data_config):
        self.model_config = model_config
        self.data_config = data_config

    @classmethod
    def from_yaml(self, file_path):
        with open(file_path, 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)

            model_config = data.get('model', {})
            data_config = data.get('data', {})

            return self(model_config, data_config)

# Exemplo de uso
settings = Settings.from_yaml('config.yaml')