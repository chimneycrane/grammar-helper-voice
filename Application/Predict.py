import os
import subprocess
import pandas as pd
import xgboost as xgb
from pyper import R

def predict(audio_path):
    r = R()
    r.source(os.getcwd()+"/ExtractFeatures.R")
    r(f"Extract({audio_path}")
    
    features_to_use = ["meanfreq","sd","median","Q25","Q75","IQR","skew","kurt","sp.ent","sfm","mode","centroid","meanfun","minfun","maxfun","meandom","mindom","maxdom","dfrange","modindx"]

    test_df = pd.read_csv('../Data/Features.csv')

    test_X = test_df[features_to_use]
    xgtest = xgb.DMatrix(test_X)

    model = xgb.Booster({'nthread':4})
    model.load_model("voice-gender.model")

    pred_test_y = model.predict(xgtest)

    if pred_test_y >= 0.5:
        return "male"
    return "female"
