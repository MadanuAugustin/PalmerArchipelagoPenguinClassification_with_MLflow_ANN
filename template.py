


import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s : %(message)s : ]')


project_name = 'PalmerArchipelagoPenguinClassification'



list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'DockerFile',
    'requirements.txt',
    'setup.py',
    'research/trails.ipynb',
    'templates/index.html',
    'templates/results.html'
]



for file_paths in list_of_files:

    file_paths = Path(file_paths)

    filedir, filename = os.path.split(file_paths)

    if filedir != "" : 
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'creating directory {filedir} for the filename {filename}...!')


    if (not os.path.exists(file_paths)) or (os.path.getsize(file_paths) ==0):
        with open(file_paths, 'w') as f:
            pass
            logging.info(f'creating empty files : {file_paths}')

    else:
        logging.info(f'{filename} already exists...!')
        


