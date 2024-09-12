# AI-Enhanced-Regulatory-Compliance-Monitoring-System

## Project Overview

The AI-Enhanced Regulatory Compliance Monitoring System is designed to automate the process of monitoring and ensuring compliance with regulatory requirements using machine learning and natural language processing (NLP). This system aims to detect potential compliance breaches in real-time and provide interactive insights through a dashboard.

## Key Features

- **Regulation Parsing**: Extracts rules and regulations from textual documents using NLP techniques.
- **Compliance Detection**: Classifies transactions as compliant or non-compliant using machine learning models.
- **Real-Time Alerts**: Flags potential compliance breaches and sends alerts.
- **Interactive Dashboard**: Provides visual insights into compliance metrics and statistics.

## Technologies Used

- **Machine Learning**: Random Forest, TF-IDF Vectorizer
- **NLP**: NLTK for text preprocessing
- **Real-Time Alerts**: Basic alerting system
- **Interactive Dashboard**: Dash, Plotly for visualization

## Project Structure

- `regulation_parser.py`: Script for parsing regulatory documents and extracting features.
- `compliance_detection.py`: Script for training and using the compliance detection model.
- `alert_system.py`: Script for sending alerts based on compliance predictions.
- `dashboard.py`: Script for launching an interactive dashboard to visualize compliance metrics.
- `transaction_data.csv`: Example dataset containing transaction descriptions and compliance labels.
- `regulation_document.txt`: Example document containing regulatory rules and guidelines.
