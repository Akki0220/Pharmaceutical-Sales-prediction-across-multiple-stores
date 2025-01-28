# LSTM-Based Sales Prediction Model

This repository contains a project for predicting Rossmann store sales using Long Short-Term Memory (LSTM) networks. The project includes data preprocessing, model training, evaluation, and deployment using MLflow.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Key Features](#key-features)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Deployment](#deployment)
- [CI/CD Integration](#cicd-integration)
- [How to Run](#how-to-run)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview
The goal of this project is to forecast future sales for Rossmann stores based on historical data. The prediction leverages LSTM, a type of recurrent neural network well-suited for time series data.

## Dataset
- **Source**: Rossmann Store Sales Dataset.
- **Key Features**:
  - Store, Sales, Customers, Promo, StateHoliday, SchoolHoliday, etc.
  - Competition-related features such as `CompetitionDistance` and `Promo2` details.

## Project Workflow
1. **Data Preprocessing**:
   - Handled missing values and categorical variables.
   - Created lag features and rolling statistics for time series data.
2. **Exploratory Data Analysis (EDA)**:
   - Visualized sales trends, holidays, and promotional impacts.
3. **Model Training**:
   - Built an LSTM model to capture temporal dependencies in sales data.
   - Optimized using early stopping and learning rate reduction.
4. **Evaluation**:
   - Analyzed training and validation loss.
5. **Deployment**:
   - Deployed the model using MLflow and REST API.
6. **CI/CD Integration**:
   - Automated pipeline for model retraining and deployment.

## Key Features
- Time series forecasting with sliding window method.
- Automated model tracking and logging using MLflow.
- Deployment-ready pipeline for serving predictions.
- Scalable CI/CD pipeline using GitHub Actions.

## Model Architecture
- **Input**: Sequences of historical sales data.
- **LSTM Layers**: Two layers to capture temporal dependencies.
- **Output**: Dense layer for predicting sales.
- **Loss Function**: Mean Squared Error (MSE).
- **Optimizer**: Adam.

## Results
- **Training Loss**: X.XX
- **Validation Loss**: X.XX
- **Visualization**:
  - ![Loss Curves](path_to_loss_plot.png)

## Deployment
- **MLflow Tracking**:
  - Logs metrics, parameters, and models.
- **Serving**:
  - Model served locally via MLflow:
    ```bash
    mlflow models serve -m "runs:/<run_id>/lstm_model" -p 1234
    ```
- **Cloud Options**:
  - Deploy to AWS, Azure, or Kubernetes.

## CI/CD Integration
- Automated workflows using GitHub Actions for:
  - Linting and testing.
  - Training and deployment.
  - Continuous monitoring of performance.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/lstm-sales-prediction.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model:
   ```bash
   python train.py
   ```
4. Serve the model:
   ```bash
   mlflow models serve -m "runs:/<run_id>/lstm_model" -p 1234
   ```

## Technologies Used
- **Programming Languages**: Python
- **Libraries**: TensorFlow, Pandas, NumPy, Matplotlib, MLflow
- **Deployment**: MLflow, Docker, Kubernetes
- **CI/CD**: GitHub Actions

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.
