

from src.PalmerArchipelagoPenguinClassification.entity.config_entity import DataTransformationConfig
import pandas as pd
from loggerFile.logger import logger
from sklearn.model_selection import train_test_split
import os
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import OneHotEncoder
from exceptionFile.exception import CustomException
import sys
from sklearn.preprocessing import LabelEncoder
import numpy as np

class DataTransformation:
    def __init__(self, config : DataTransformationConfig):
        self.config = config


    def preprocessor_fun(self):
        try:
            logger.info(f'starting the construction of numeric and categoric pipelines...!')

            numeric_columns = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']

            categoric_columns = ['island', 'sex']

            

            numeric_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', RobustScaler(with_centering=False))
                ]
            )


            categoric_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehot', OneHotEncoder(drop='first')),
                    ('robustscaler', RobustScaler(with_centering=False))
                    
                ]
            )

            




            preprocessor = ColumnTransformer(
                [
                    ('numeric_pipeline', numeric_pipeline, numeric_columns),
                    ('categoroc_pipeline', categoric_pipeline, categoric_columns),
                ]
            )

            logger.info(f'completed the construction of numeric and categoric pipelines...!')

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)




    def transformation_fun(self):
        try:
            data = pd.read_csv(self.config.data_path)

            xx = data[data.sex == '.']

            data = data.drop(index = xx.index, axis = 0)

            logger.info(f'splitting the data into training and testing...!')

            train, test = train_test_split(data)

            train.to_csv(os.path.join(self.config.root_dir, 'train_raw.csv'), index = False, header = True)

            test.to_csv(os.path.join(self.config.root_dir, 'test_raw.csv'), index = False, header = True)

            train_X = train.drop(columns = 'species', axis = 1)

            train_Y = train[['species']]

            test_X = test.drop(columns = 'species', axis = 1)

            test_Y = test[['species']]

            preprocessor_obj = self.preprocessor_fun()

            train_X = preprocessor_obj.fit_transform(train_X)
            test_X = preprocessor_obj.transform(test_X)

            le = LabelEncoder()

            train_Y = le.fit_transform(train_Y)
            test_Y = le.transform(test_Y)


            transformed_train_df = pd.DataFrame(np.c_[train_X,train_Y])
            transformed_test_df = pd.DataFrame(np.c_[test_X,test_Y])

            transformed_train_df = transformed_train_df.rename(columns={7:'species'})
            transformed_test_df = transformed_test_df.rename(columns={7:'species'})

            transformed_train_df.to_csv(os.path.join(self.config.root_dir, 'transformed_train_df.csv'), index = False, header = True)
            transformed_test_df.to_csv(os.path.join(self.config.root_dir, 'transformed_test_df.csv'), index=False, header=True)

            logger.info(f'completed splitting the data into training and testing...!')
            
        except Exception as e:
            raise CustomException(e, sys)



        

        


