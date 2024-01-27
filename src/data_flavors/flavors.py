from data_flavors.local_file_source import LoadLocalFile
from data_flavors.local_file_target import SaveLocalFile

data_source_flavors = {
    'local_file_source': LoadLocalFile
}

data_target_flavors = {
    'local_file_target': SaveLocalFile
}
