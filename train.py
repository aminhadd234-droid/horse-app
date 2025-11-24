import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.calibration import CalibratedClassifierCV
import xgboost as xgb
DATA_CSV = 'ml/sample_data.csv'
OUT_MODEL = 'model_calibrated.joblib'
def train():
    df = pd.read_csv(DATA_CSV)
    features = ['horse_form','jockey_rating','track_condition','recent_time_avg']
    X = df[features]
    y = df['won']
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model = xgb.XGBClassifier(n_estimators=50, max_depth=4, use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)
    calibrated = CalibratedClassifierCV(model, cv='prefit', method='isotonic')
    calibrated.fit(X_val, y_val)
    joblib.dump(calibrated, OUT_MODEL)
    print(f'Saved model to {OUT_MODEL}')
if __name__ == '__main__':
    train()
