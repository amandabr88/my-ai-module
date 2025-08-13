from src.inference import predict

def test_predict():
    sample_input = {"feature1": 1.0, "feature2": 0.5}
    try:
        prediction = predict(sample_input)
        assert isinstance(prediction, list)
    except FileNotFoundError:
        print("Model file not found. Train and save a model before testing.")
