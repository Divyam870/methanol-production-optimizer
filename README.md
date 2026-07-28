>>>  # AI-Based Methanol Production Optimization System

### Machine Learning & Grid Search-Based Optimization

**Author:** Divyam Singh  
**Email:** divyamsingh9696@gmail.com

## Application Preview

### Prediction Result

![Prediction Result](app_preview.png)

## Table of Contents

- [Problem Statement](#1-problem-statement)
- [How the AI Model Solves the Problem](#2-how-the-ai-model-solves-the-problem)
- [Model Selection and Performance Comparison](#3-model-selection-and-performance-comparison)
- [Optimizer Working Process](#4-optimizer-working-process)
- [Essential Libraries Used](#5-essential-libraries-used)
- [Workflow](#6-workflow)
- [Project Summary](#7-project-summary)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)

## 1. Problem Statement

Methanol is one of the most important industrial chemicals and is widely used in the production of fuels, chemicals, and energy-related applications. The efficiency of methanol production depends on several operating parameters such as hydrogen (H₂) feed flow, carbon dioxide (CO₂) feed flow, reactor temperature, pressure, and reaction time.

In real industrial processes, the hydrogen feed is often unstable and continuously fluctuates due to changes in operating conditions. These fluctuations make it difficult for plant operators to determine the optimal operating conditions required to achieve maximum methanol production. Selecting these parameters manually is time-consuming and may not always lead to the best production efficiency.

To address this challenge, this project develops an AI-based methanol production optimization system. Instead of relying on manual trial-and-error, the system uses a trained machine learning model to predict methanol production and recommends the optimal CO₂ feed flow, H₂/CO₂ ratio, temperature, pressure, and reaction time based on the available hydrogen feed. This enables faster and more reliable decision-making while maximizing the predicted methanol yield.

## 2. How the AI Model Solves the Problem ↓

To solve the problem of fluctuating hydrogen (H₂) feed flow, an Artificial Intelligence (AI)
based regression model was developed. The system takes the available H₂ feed flow as the
primary input and analyzes its relationship with other important process parameters,
including CO₂ feed flow, reactor temperature, pressure, reaction time, and the H₂/CO₂ ratio.

During model development, the dataset was preprocessed, and an additional feature called
the H₂/CO₂ Ratio was created through feature engineering. This ratio is chemically significant
because it directly influences the methanol synthesis reaction and helps the model better
understand the relationship between hydrogen and carbon dioxide.

After training, the selected machine learning model is capable of accurately predicting
methanol production for different combinations of operating conditions. Instead of
requiring the user to manually test multiple parameter combinations, the model evaluates
them automatically and identifies the operating conditions that are expected to produce
the highest methanol yield.

As a result, the user only needs to provide the available hydrogen (H₂) feed flow. The system
then recommends the optimal values of:
CO₂ Feed Flow
H₂/CO₂ Ratio
Reactor Temperature
Reactor Pressure
Reaction Time
along with the maximum predicted methanol production.
This approach transforms the prediction model into an intelligent decision-support system
that assists in selecting the most suitable operating conditions for maximizing methanol
production.

## 3.  Model Selection and Performance Comparison ↓

Several machine learning regression algorithms were trained and evaluated to identify the
most suitable model for predicting methanol production. Each model was assessed using
the R² Score, which measures how well the model explains the variation in the target
variable. A higher R² Score indicates better predictive performance.

The following regression models were compared:

Linear Regression
Decision Tree Regressor
Random Forest Regressor
Gradient Boosting Regressor
XGBoost Regressor

Performance Comparison:
| Model | R² Score | MSE |
|-------|----------:|----------:|
| Linear Regression | 0.8619 | 0.000021 |
| Decision Tree | 0.9775 | 0.000004 |
| Random Forest | 0.9911 | 0.000001 |
| Gradient Boosting | **0.9932** | **0.000001** |
| XGBoost | 0.9925 | 0.000001 |

After evaluating the performance of all models, Gradient Boosting Regressor achieved the
highest R² Score and demonstrated the best prediction accuracy on the dataset. Therefore,
it was selected as the final model for deployment in the optimization system.
The trained Gradient Boosting model was then saved as a .pkl file using Joblib, allowing it to
be loaded later without retraining. This significantly reduces execution time and enables the
application to make predictions efficiently within the Streamlit interface.

## 4. Optimizer Working Process ↓

While the trained Gradient Boosting Regressor can accurately predict methanol production
for a given set of operating conditions, it does not automatically determine which operating
conditions produce the highest methanol yield.
To solve this problem, a Grid Search-Based Optimizer was developed on top of the trained
machine learning model.
The optimization process begins when the user enters the available Hydrogen (H₂) Feed
Flow. Since hydrogen is considered the fluctuating input parameter, the optimizer searches
for the best operating conditions corresponding to the given H₂ value.
Instead of selecting random operating conditions, the optimizer systematically explores
multiple combinations of process parameters. It first generates a range of feasible H₂/CO₂
ratio values based on the operating conditions observed in the training dataset. For each
ratio, the corresponding CO₂ feed flow is calculated using:
CO₂ = H₂ / (H₂/CO₂ Ratio)
To ensure reliable predictions, any CO₂ value that falls outside the range of the training
dataset is discarded. The optimizer then evaluates different combinations of:
Reactor Temperature
Reactor Pressure
Reaction Time
For every possible combination, the trained Gradient Boosting Regressor predicts the
expected methanol production.
After evaluating all feasible operating conditions, the optimizer compares every prediction
and stores the combination that produces the highest predicted methanol yield.
Finally, the system returns the optimal operating conditions, including:
Available Hydrogen (H₂)

- Recommended CO₂ Feed Flow
- Recommended H₂/CO₂ Ratio
- Recommended Reactor Temperature
- Recommended Reactor Pressure
- Recommended Reaction Time
- Maximum Predicted Methanol Production

By combining a Machine Learning prediction model with a Grid Search-Based Optimization
technique, the system acts as an intelligent decision-support tool that recommends
operating conditions expected to maximize methanol production under varying hydrogen
feed conditions.

## 5. Essential Libraries Used ↓

The project was developed using the following Python libraries:

NumPy: 

Used for numerical computations and generating search ranges for optimization using functions such as linspace().

Pandas: 

Used for loading, cleaning, preprocessing, and analyzing the dataset before model training.

Scikit-learn: 

Used for data preprocessing, model training, model evaluation, and implementing machine learning regression algorithms including Gradient Boosting Regressor.

Joblib: 

Used to save the trained machine learning model as a .pkl file and load it later without retraining.

Streamlit: 

Used to build an interactive web application that allows users to enter the available H₂ feed flow and obtain optimized operating conditions.


Library Installation: 
Install all required libraries using:

pip install -r requirements.txt

or install them individually:

pip install numpy

pip install pandas

pip install scikit-learn

pip install joblib

pip install streamlit

<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  -->
## 6. Workflow:

Load Dataset

    ↓

Data Preprocessing


    ↓

Feature Engineering (H₂/CO₂ Ratio)

    ↓
Train & Compare ML Models

    ↓
Select Gradient Boosting Regressor
     ↓
Save Model (.pkl)

    ↓
Grid Search-Based Optimizer


    ↓
Streamlit Web Application

    ↓
Recommended Operating Conditions

## 7. Project Summary ↓

Conclusion: 

This project presents an AI-based methanol production optimization system that combines
machine learning with optimization techniques to support efficient process decisionmaking.
A Gradient Boosting Regressor was trained to accurately predict methanol production
based on key operating parameters, including H₂ feed flow, CO₂ feed flow, reactor
temperature, pressure, reaction time, and the H₂/CO₂ ratio. Among all the regression models
evaluated, the Gradient Boosting Regressor achieved the highest predictive performance
and was therefore selected as the final model.
To transform the prediction model into a practical decision-support system, a Grid SearchBased Optimizer was developed. Instead of requiring users to manually test different
operating conditions, the optimizer automatically evaluates multiple feasible parameter
combinations and recommends the operating conditions expected to maximize methanol
production for a given hydrogen feed flow.
The trained model was deployed using Streamlit, providing a simple and interactive web
application where users only need to enter the available H₂ feed flow to obtain optimized
operating conditions.
Overall, this project demonstrates how Artificial Intelligence and Machine Learning can be
applied to industrial chemical processes to improve operational efficiency, reduce manual
experimentation, and support data-driven decision-making.


Future Scope↓

This project can be further enhanced by implementing more advanced optimization
techniques such as:
Differential Evolution (DE)
Bayesian Optimization
Genetic Algorithms (GA)
Particle Swarm Optimization (PSO)
These optimization methods can search the solution space more efficiently than a grid
search approach and may identify even better operating conditions while reducing
computational time. Additionally, integrating real-time sensor data from industrial plants
could enable continuous optimization and adaptive process control.

## How to Run

1. Clone the repository.
2. Install the required libraries:

```bash
pip install -r requirements.txt
# or simply run pip install "library_name"

# Start the application
streamlit run app.py


---

### 7. project structure

```md
## Project Structure

methanol_project/
│── app.py
│── Optimizer.py
│── methanol_gbr_model.pkl
│── requirement.txt
│── README.md
└── GD_regressor.ipynb


# GD_regressor >>> Gradient Boosting Regressor 