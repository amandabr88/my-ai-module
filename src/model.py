import joblib
from sklearn.linear_model import LogisticRegression

def train_model(X, y):
    """Train a simple logistic regression model."""
    model = LogisticRegression()
    model.fit(X, y)
    return model

def save_model(model, filepath="models/trained_model.pkl"):
    joblib.dump(model, filepath)

def load_model(filepath="models/trained_model.pkl"):
    return joblib.load(filepath)
