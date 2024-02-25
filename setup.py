

from setuptools import setup , find_packages

with open('README.MD', 'r', encoding='utf-8') as f:
    long_description = f.read()



setup(
    name='PalmerPenguinClassification',
    version='0.0.0.0',
    author='augustin',
    author_email='augustin7766@gmail.com',
    description='End-end ANN project with mlflow',
    long_description=long_description,
    url='https://github.com/MadanuAugustin/PalmerArchipelagoPenguinClassification_with_MLflow_ANN.git',
    packages = find_packages()
)