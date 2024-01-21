import argparse
import yaml
import numpy as np 
import pandas as pd 
from typing import List,Dict


def read_yaml_config(config_path:str) -> Dict:
    """
    This function reads parameters from yaml config
    input: params.yaml location
    output: parameters as dictionary
    """
    with open(config_path) as yaml_file_ctx:
        config = yaml.safe_load(yaml_file_ctx)
        return config
    
def load_data(data_path:str, model_var:List)  -> pd.DataFrame:
    """
    This function loads the raw feed using data_path and returns pandas DataFrame
    input: csv path
    params: list of columns
    output: pandas DataFrame
    """
    df = pd.read_csv(data_path, sep=",", encoding="utf-8")
    df = df[model_var]
    return df

def load_raw_data(config_path:str) -> None:
    """
    load data from external location(data/external) to the raw folder(data/raw) with train and teting dataset 
    input: config_path 
    output: save train file in data/raw folder 
    """
    config = read_yaml_config(config_path)
    external_data_path  = config.get('external_data_config').get('external_data_csv')
    raw_data_path  = config.get('raw_data_config').get('raw_data_csv')
    model_var = config.get('raw_data_config').get('model_var')
    dataframe = load_data(external_data_path,model_var)
    dataframe.to_csv(raw_data_path,index=False)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_raw_data(parsed_args.config)




