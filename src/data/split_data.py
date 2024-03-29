import os
import argparse
import pandas as pd
from load_data import read_yaml_config
from sklearn.model_selection import train_test_split

def split_data(df:pd.DataFrame,train_data_path:str,test_data_path:str,split_ratio:float,random_state:int) -> None:
    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state)
    train.to_csv(train_data_path, sep=",", index=False, encoding="utf-8")
    test.to_csv(test_data_path, sep=",", index=False, encoding="utf-8")   

def split_and_save_data(config_path:str) -> None:
    """
    Splits the train dataset(data/raw) and save it in the data/processed folder
    input: config path 
    output: save splitted files in output folder
    """
    config = read_yaml_config(config_path)
    raw_data_path  = config.get('raw_data_config').get('raw_data_csv')
    train_data_path = config.get('processed_data_config').get('train_data_csv')
    test_data_path = config.get('processed_data_config').get('test_data_csv')
    train_test_split_ratio = config.get('raw_data_config').get('train_test_split_ratio')
    random_state = config.get('raw_data_config').get('random_state')
    raw_df=pd.read_csv(raw_data_path)
    split_data(raw_df,train_data_path,test_data_path,train_test_split_ratio,random_state)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    split_and_save_data(parsed_args.config)