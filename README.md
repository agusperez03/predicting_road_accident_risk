# Car Accident Risk Prediction

## Project Overview
This project builds a machine learning model to predict the likelihood of accidents on different types of roads. The model predicts **accident risk** as a continuous value between 0 and 1, based on various road and environmental features.

**Kaggle Competition**: [Playground Series S5E10 - Predicting Road Accident Risk](https://www.kaggle.com/competitions/playground-series-s5e10/overview)

***Try out** the game developed from this model on prod: https://roadriskgame.streamlit.app/

## Dataset

### Training Data
- **Size**: 517,754 rows
- **Target Variable**: `accident_risk` (continuous, 0-1 scale)
- **Features**: 13 features including road characteristics, weather conditions, and traffic information

### Features Description

**Numerical Features:**
- `num_lanes`: Number of lanes on the road (1-4)
- `curvature`: Road curvature (0-1, where higher values mean sharper curves)
- `speed_limit`: Posted speed limit (25-70 mph)
- `num_reported_accidents`: Historical number of reported accidents (0-7)

**Categorical Features:**
- `road_type`: Type of road (highway, rural, urban)
- `lighting`: Lighting conditions (daylight, dim, night)
- `weather`: Weather conditions (clear, foggy, rainy)
- `road_signs_present`: Presence of road signs (True/False)
- `public_road`: Whether it's a public road (True/False)
- `time_of_day`: Time period (morning, afternoon, evening)
- `holiday`: Whether it's a holiday (True/False)
- `school_season`: Whether it's during school season (True/False)

## Project Structure

```
car accident predict/
├── train.csv                           # Training dataset
├── test.csv                            # Test dataset for predictions
├── sample_submission.csv               # Sample submission format
├── accident_prediction_simple.py       # Main ML pipeline script
├── submission.csv                      # Generated predictions
├── README.md                           # This file
└── Visualizations/
    ├── 01_target_distribution.png      # Target variable distribution
    ├── 02_correlation_matrix.png       # Feature correlations
    ├── 03_categorical_analysis.png     # Categorical feature analysis
    ├── 04_numerical_scatter.png        # Numerical features vs target
    ├── 05_model_comparison.png         # Model performance comparison
    ├── 06_feature_importance.png       # Top feature importances
    └── 07_predictions_vs_actual.png    # Model predictions quality
```

## Data Analysis Summary

### Key Findings
1. **No Missing Values**: The dataset is complete with no missing data
2. **Balanced Distribution**: All categorical features are relatively balanced
3. **Target Distribution**: 
   - Mean accident risk: 0.35
   - Standard deviation: 0.17
   - Range: 0.00 to 1.00

### Feature Correlations
- Strong correlation between **speed_limit × curvature** interaction and accident risk
- **lighting** conditions significantly impact accident risk
- **weather** conditions are important predictors

## Machine Learning Pipeline

### 1. Data Preprocessing
- **Label Encoding**: Converted categorical variables to numerical format
- **Feature Engineering**: Created interaction features:
  - `speed_curvature = speed_limit × curvature`
  - `lanes_accidents = num_lanes × num_reported_accidents`
  - `high_speed`: Binary indicator for speed ≥ 60 mph
  - `sharp_curve`: Binary indicator for curvature ≥ 0.7
- **Feature Scaling**: StandardScaler applied for linear models

### 2. Models Tested

| Model | Test MAE | Test RMSE | Test R² |
|-------|----------|-----------|---------|
| **Gradient Boosting** | **0.0440** | **0.0566** | **0.8841** |
| Random Forest | 0.0457 | 0.0589 | 0.8744 |
| Ridge Regression | 0.0632 | 0.0790 | 0.7737 |

### 3. Best Model: Gradient Boosting Regressor
- **Test R²**: 0.8841 (explains 88.4% of variance)
- **Test MAE**: 0.0440 (average error of 4.4% on 0-1 scale)
- **Test RMSE**: 0.0566
- **Parameters**: 
  - n_estimators=100
  - max_depth=5
  - learning_rate=0.1

### 4. Feature Importance (Top 5)

1. **speed_curvature** (42.1%) - Interaction between speed and curvature
2. **lighting** (25.0%) - Lighting conditions
3. **high_speed** (8.7%) - High speed indicator
4. **curvature** (8.3%) - Road curvature
5. **weather** (7.6%) - Weather conditions

## How to Run

### Requirements
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Execute the Pipeline
```bash
python accident_prediction_simple.py
```

### Output Files
The script generates:
- 7 visualization PNG files
- `submission.csv` with predictions for the test set

## Model Insights

### What the Model Learned
1. **Speed × Curvature** is the strongest predictor - high speed on curved roads dramatically increases accident risk
2. **Lighting conditions** are critical - night and dim lighting increase risk
3. **Weather conditions** impact is significant - foggy and rainy weather increase risk
4. **Historical accidents** provide useful context but aren't the strongest predictor

### Recommendations
Based on the model's feature importance:
1. **High-priority interventions**: 
   - Reduce speed limits on curved roads
   - Improve lighting on high-risk segments
2. **Medium-priority**:
   - Enhanced signage in poor weather conditions
   - Additional safety measures during adverse weather

## Model Performance

### Strengths
✅ High R² score (0.8841) indicates excellent predictive power  
✅ Low MAE (0.0440) shows accurate predictions  
✅ Generalizes well (similar train/test performance)  
✅ Interpretable feature importances

### Limitations
⚠️ May not capture extreme rare events  
⚠️ Performance depends on data quality from sensors/reports  
⚠️ Assumes similar conditions to training data

## Future Improvements

1. **Feature Engineering**:
   - Time-based features (hour of day, day of week)
   - Geographic clustering
   - Road maintenance history

2. **Advanced Models**:
   - XGBoost for potentially better performance
   - Neural networks for complex interactions
   - Ensemble of top models

3. **Additional Data**:
   - Traffic volume data
   - Road surface conditions
   - Driver behavior metrics

## Conclusion

This project successfully built a machine learning model that predicts accident risk with **88.4% accuracy** (R²). The Gradient Boosting model identified that the combination of speed and road curvature, along with lighting conditions, are the most critical factors in determining accident risk. This model can be used by transportation authorities to:

- Identify high-risk road segments
- Prioritize safety improvements
- Implement data-driven speed limit policies
- Plan targeted interventions based on weather and lighting conditions

---

**Author**: ML Pipeline for Road Safety Analysis  
**Date**: October 2025  
**Model**: Gradient Boosting Regressor  
**Performance**: R² = 0.8841, MAE = 0.0440
