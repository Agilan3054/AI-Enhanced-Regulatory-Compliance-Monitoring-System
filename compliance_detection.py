import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

def train_compliance_model(data):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data['transaction_description'])
    y = data['compliance_label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    print("Model performance:")
    print(classification_report(y_test, y_pred))
    
    return model, vectorizer

def predict_compliance(model, vectorizer, new_data):
    X_new = vectorizer.transform(new_data)
    predictions = model.predict(X_new)
    return predictions

# Example usage
if __name__ == "__main__":
    data = pd.read_csv('transaction_data.csv')  # Assumed CSV file with 'transaction_description' and 'compliance_label'
    model, vectorizer = train_compliance_model(data)

    new_transactions = ["Suspicious transaction detected"]
    predictions = predict_compliance(model, vectorizer, new_transactions)
    print("Compliance predictions:", predictions)
