def send_alert(transaction, prediction):
    if prediction == 1:  # Assuming 1 indicates a breach
        print(f"ALERT: Potential compliance breach detected in transaction: {transaction}")

# Example usage
if __name__ == "__main__":
    transactions = ["Suspicious transaction detected"]
    predictions = [1]  # Simulated predictions for the transactions
    for transaction, prediction in zip(transactions, predictions):
        send_alert(transaction, prediction)
