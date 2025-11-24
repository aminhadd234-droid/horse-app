import joblib, os
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model_calibrated.joblib')
def get_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError('Model not trained. Run train.py first.')
    return joblib.load(MODEL_PATH)
