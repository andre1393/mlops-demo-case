import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('sufyant/brazilian-real-bank-dataset', path='data', unzip=True)
