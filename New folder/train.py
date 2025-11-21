from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

def main():
    X, y = load_iris(return_X_y=True)
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X, y)
    joblib.dump(clf, "model.joblib")
    print("Saved model.joblib")

if __name__ == "__main__":
    main()
