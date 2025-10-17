"""
Car Accident Risk Prediction Model - Simplified Version
========================================================
This script builds a complete ML pipeline to predict accident risk on different types of roads.
Target: accident_risk (continuous value between 0 and 1)
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

# Set plotting style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)

print("="*60)
print("CAR ACCIDENT RISK PREDICTION MODEL")
print("="*60)

# ========================================
# 1. LOAD AND EXPLORE THE DATA
# ========================================
print("\n[1] Loading Data...")
train_df = pd.read_csv('train.csv')
print(f"✓ Training data loaded: {train_df.shape[0]} rows, {train_df.shape[1]} columns")

print("\n[2] Dataset Overview:")
print(train_df.head(10))

print("\n[3] Dataset Info:")
print(train_df.info())

print("\n[4] Statistical Summary:")
print(train_df.describe())

print("\n[5] Target Variable Distribution:")
print(train_df['accident_risk'].describe())

print("\n[6] Checking for Missing Values:")
missing = train_df.isnull().sum()
print(missing[missing > 0] if missing.sum() > 0 else "✓ No missing values found!")

print("\n[7] Checking for Duplicates:")
duplicates = train_df.duplicated().sum()
print(f"Duplicates found: {duplicates}")

# ========================================
# 2. EXPLORATORY DATA ANALYSIS
# ========================================
print("\n[8] Performing Exploratory Data Analysis...")

# Categorical features
categorical_features = ['road_type', 'lighting', 'weather', 'road_signs_present', 
                       'public_road', 'time_of_day', 'holiday', 'school_season']

# Numerical features
numerical_features = ['num_lanes', 'curvature', 'speed_limit', 'num_reported_accidents']

print(f"\nCategorical features: {len(categorical_features)}")
print(categorical_features)
print(f"\nNumerical features: {len(numerical_features)}")
print(numerical_features)

# Analyze categorical features
print("\n[9] Categorical Features Distribution:")
for col in categorical_features:
    print(f"\n{col}:")
    print(train_df[col].value_counts())

# Create visualizations
print("\n[10] Creating visualizations...")

# Target variable distribution
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.hist(train_df['accident_risk'], bins=50, edgecolor='black', alpha=0.7)
plt.xlabel('Accident Risk')
plt.ylabel('Frequency')
plt.title('Distribution of Accident Risk')

plt.subplot(1, 2, 2)
plt.boxplot(train_df['accident_risk'])
plt.ylabel('Accident Risk')
plt.title('Boxplot of Accident Risk')
plt.tight_layout()
plt.savefig('01_target_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 01_target_distribution.png")
plt.close()

# Correlation matrix for numerical features
plt.figure(figsize=(10, 8))
numerical_cols = numerical_features + ['accident_risk']
correlation_matrix = train_df[numerical_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, fmt='.2f')
plt.title('Correlation Matrix - Numerical Features')
plt.tight_layout()
plt.savefig('02_correlation_matrix.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 02_correlation_matrix.png")
plt.close()

# Accident risk by categorical features
fig, axes = plt.subplots(2, 4, figsize=(20, 10))
axes = axes.ravel()
for idx, col in enumerate(categorical_features):
    train_df.groupby(col)['accident_risk'].mean().sort_values().plot(kind='barh', ax=axes[idx])
    axes[idx].set_xlabel('Mean Accident Risk')
    axes[idx].set_title(f'Accident Risk by {col}')
plt.tight_layout()
plt.savefig('03_categorical_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 03_categorical_analysis.png")
plt.close()

# Numerical features vs accident risk (using sample for faster plotting)
sample_df = train_df.sample(n=min(10000, len(train_df)), random_state=42)
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
axes = axes.ravel()
for idx, col in enumerate(numerical_features):
    axes[idx].scatter(sample_df[col], sample_df['accident_risk'], alpha=0.3)
    axes[idx].set_xlabel(col)
    axes[idx].set_ylabel('accident_risk')
    axes[idx].set_title(f'{col} vs Accident Risk')
plt.tight_layout()
plt.savefig('04_numerical_scatter.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 04_numerical_scatter.png")
plt.close()

# ========================================
# 3. DATA PREPROCESSING
# ========================================
print("\n[11] Data Preprocessing...")

# Create a copy for preprocessing
df_processed = train_df.copy()

# Remove ID column (not useful for prediction)
df_processed = df_processed.drop('id', axis=1)

# Encode categorical variables
print("\n[12] Encoding categorical variables...")
label_encoders = {}
for col in categorical_features:
    le = LabelEncoder()
    df_processed[col] = le.fit_transform(df_processed[col])
    label_encoders[col] = le
    print(f"✓ Encoded: {col}")

print("\n[13] Feature Engineering...")
# Create interaction features
df_processed['speed_curvature'] = df_processed['speed_limit'] * df_processed['curvature']
df_processed['lanes_accidents'] = df_processed['num_lanes'] * df_processed['num_reported_accidents']
df_processed['high_speed'] = (df_processed['speed_limit'] >= 60).astype(int)
df_processed['sharp_curve'] = (df_processed['curvature'] >= 0.7).astype(int)
print("✓ Created interaction features")

# ========================================
# 4. PREPARE DATA FOR MODELING
# ========================================
print("\n[14] Preparing data for modeling...")

# Separate features and target
X = df_processed.drop('accident_risk', axis=1)
y = df_processed['accident_risk']

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nTraining set: {X_train.shape}")
print(f"Test set: {X_test.shape}")

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("✓ Features scaled")

# ========================================
# 5. MODEL BUILDING AND TRAINING
# ========================================
print("\n[15] Building and Training Models...")

models = {
    'Ridge Regression': Ridge(alpha=1.0, random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, max_depth=20, random_state=42, n_jobs=-1),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42)
}

results = {}

for name, model in models.items():
    print(f"\nTraining {name}...")
    
    # Use scaled data for linear models, original for tree-based
    if name in ['Ridge Regression']:
        model.fit(X_train_scaled, y_train)
        y_pred_train = model.predict(X_train_scaled)
        y_pred_test = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
    
    # Calculate metrics
    train_mae = mean_absolute_error(y_train, y_pred_train)
    test_mae = mean_absolute_error(y_test, y_pred_test)
    train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
    train_r2 = r2_score(y_train, y_pred_train)
    test_r2 = r2_score(y_test, y_pred_test)
    
    results[name] = {
        'model': model,
        'train_mae': train_mae,
        'test_mae': test_mae,
        'train_rmse': train_rmse,
        'test_rmse': test_rmse,
        'train_r2': train_r2,
        'test_r2': test_r2,
        'y_pred_test': y_pred_test
    }
    
    print(f"  Train MAE: {train_mae:.4f} | Test MAE: {test_mae:.4f}")
    print(f"  Train RMSE: {train_rmse:.4f} | Test RMSE: {test_rmse:.4f}")
    print(f"  Train R²: {train_r2:.4f} | Test R²: {test_r2:.4f}")

# ========================================
# 6. MODEL EVALUATION AND COMPARISON
# ========================================
print("\n[16] Model Comparison:")
comparison_df = pd.DataFrame({
    'Model': list(results.keys()),
    'Train MAE': [results[m]['train_mae'] for m in results.keys()],
    'Test MAE': [results[m]['test_mae'] for m in results.keys()],
    'Train RMSE': [results[m]['train_rmse'] for m in results.keys()],
    'Test RMSE': [results[m]['test_rmse'] for m in results.keys()],
    'Train R²': [results[m]['train_r2'] for m in results.keys()],
    'Test R²': [results[m]['test_r2'] for m in results.keys()]
})
print(comparison_df.to_string(index=False))

# Find best model based on Test R²
best_model_name = comparison_df.loc[comparison_df['Test R²'].idxmax(), 'Model']
best_model = results[best_model_name]['model']
print(f"\n✓ Best Model: {best_model_name} (Test R² = {comparison_df['Test R²'].max():.4f})")

# Visualize model comparison
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# MAE comparison
axes[0].barh(comparison_df['Model'], comparison_df['Test MAE'])
axes[0].set_xlabel('Mean Absolute Error')
axes[0].set_title('Model Comparison - MAE (Lower is Better)')

# RMSE comparison
axes[1].barh(comparison_df['Model'], comparison_df['Test RMSE'])
axes[1].set_xlabel('Root Mean Squared Error')
axes[1].set_title('Model Comparison - RMSE (Lower is Better)')

# R² comparison
axes[2].barh(comparison_df['Model'], comparison_df['Test R²'])
axes[2].set_xlabel('R² Score')
axes[2].set_title('Model Comparison - R² (Higher is Better)')

plt.tight_layout()
plt.savefig('05_model_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 05_model_comparison.png")
plt.close()

# ========================================
# 7. FEATURE IMPORTANCE (for best model)
# ========================================
if hasattr(best_model, 'feature_importances_'):
    print("\n[17] Feature Importance Analysis...")
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': best_model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    print("\nTop 10 Most Important Features:")
    print(feature_importance.head(10).to_string(index=False))
    
    plt.figure(figsize=(10, 8))
    plt.barh(feature_importance['Feature'].head(15), feature_importance['Importance'].head(15))
    plt.xlabel('Importance')
    plt.title(f'Top 15 Feature Importances - {best_model_name}')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('06_feature_importance.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: 06_feature_importance.png")
    plt.close()

# Predictions vs Actual plot
plt.figure(figsize=(10, 8))
sample_indices = np.random.choice(len(y_test), size=min(5000, len(y_test)), replace=False)
plt.scatter(y_test.iloc[sample_indices], results[best_model_name]['y_pred_test'][sample_indices], alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Accident Risk')
plt.ylabel('Predicted Accident Risk')
plt.title(f'Predicted vs Actual - {best_model_name}')
plt.tight_layout()
plt.savefig('07_predictions_vs_actual.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 07_predictions_vs_actual.png")
plt.close()

# ========================================
# 8. PREDICTIONS ON TEST SET
# ========================================
print("\n[18] Generating Predictions for Test Set...")

# Load test data
test_df = pd.read_csv('test.csv')
print(f"✓ Test data loaded: {test_df.shape[0]} rows")

# Store test IDs
test_ids = test_df['id'].copy()

# Preprocess test data (same as training)
test_processed = test_df.copy()
test_processed = test_processed.drop('id', axis=1)

# Encode categorical variables
for col in categorical_features:
    test_processed[col] = label_encoders[col].transform(test_processed[col])

# Create same engineered features
test_processed['speed_curvature'] = test_processed['speed_limit'] * test_processed['curvature']
test_processed['lanes_accidents'] = test_processed['num_lanes'] * test_processed['num_reported_accidents']
test_processed['high_speed'] = (test_processed['speed_limit'] >= 60).astype(int)
test_processed['sharp_curve'] = (test_processed['curvature'] >= 0.7).astype(int)

# Make predictions
predictions = best_model.predict(test_processed)

# Create submission file
submission = pd.DataFrame({
    'id': test_ids,
    'accident_risk': predictions
})
submission.to_csv('submission.csv', index=False)
print("✓ Saved: submission.csv")
print(f"\nPrediction Statistics:")
print(submission['accident_risk'].describe())

# ========================================
# 9. SUMMARY
# ========================================
print("\n" + "="*60)
print("MODEL SUMMARY")
print("="*60)
print(f"Dataset Size: {len(train_df):,} training examples")
print(f"Number of Features: {X.shape[1]}")
print(f"\nBest Model: {best_model_name}")
print(f"Test MAE: {results[best_model_name]['test_mae']:.4f}")
print(f"Test RMSE: {results[best_model_name]['test_rmse']:.4f}")
print(f"Test R²: {results[best_model_name]['test_r2']:.4f}")
print("\nKey Insights:")
print(f"- The model explains {results[best_model_name]['test_r2']*100:.1f}% of variance in accident risk")
print(f"- Average prediction error: {results[best_model_name]['test_mae']:.4f} (on 0-1 scale)")
print("\nGenerated Files:")
print("  - 01_target_distribution.png")
print("  - 02_correlation_matrix.png")
print("  - 03_categorical_analysis.png")
print("  - 04_numerical_scatter.png")
print("  - 05_model_comparison.png")
if hasattr(best_model, 'feature_importances_'):
    print("  - 06_feature_importance.png")
print("  - 07_predictions_vs_actual.png")
print("  - submission.csv")
print("="*60)
print("✓ Analysis Complete!")
print("="*60)
