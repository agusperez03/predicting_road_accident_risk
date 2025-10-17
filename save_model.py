"""
Model Training and Saving Script
==================================
This script trains the final model and saves it for use in the game.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingRegressor
import joblib
import os

print("="*60)
print("TRAINING AND SAVING MODEL FOR GAME")
print("="*60)

# Create models directory if it doesn't exist
os.makedirs('game_models', exist_ok=True)

# Load data
print("\n[1] Loading training data...")
train_df = pd.read_csv('train.csv')
print(f"✓ Loaded {len(train_df)} samples")

# Categorical features
categorical_features = ['road_type', 'lighting', 'weather', 'road_signs_present', 
                       'public_road', 'time_of_day', 'holiday', 'school_season']

# Preprocess
print("\n[2] Preprocessing data...")
df_processed = train_df.copy()
df_processed = df_processed.drop('id', axis=1)

# Encode categorical variables and save encoders
label_encoders = {}
for col in categorical_features:
    le = LabelEncoder()
    df_processed[col] = le.fit_transform(df_processed[col])
    label_encoders[col] = le
    print(f"  ✓ Encoded: {col}")

# Feature engineering
print("\n[3] Creating engineered features...")
df_processed['speed_curvature'] = df_processed['speed_limit'] * df_processed['curvature']
df_processed['lanes_accidents'] = df_processed['num_lanes'] * df_processed['num_reported_accidents']
df_processed['high_speed'] = (df_processed['speed_limit'] >= 60).astype(int)
df_processed['sharp_curve'] = (df_processed['curvature'] >= 0.7).astype(int)
print("✓ Created interaction features")

# Prepare data
X = df_processed.drop('accident_risk', axis=1)
y = df_processed['accident_risk']

# Train final model on all data (since we already validated it)
print("\n[4] Training final Gradient Boosting model...")
final_model = GradientBoostingRegressor(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    random_state=42
)
final_model.fit(X, y)
print("✓ Model trained successfully")

# Save model
print("\n[5] Saving model and encoders...")
joblib.dump(final_model, 'game_models/accident_risk_model.joblib')
print("✓ Saved model to: game_models/accident_risk_model.joblib")

joblib.dump(label_encoders, 'game_models/label_encoders.joblib')
print("✓ Saved encoders to: game_models/label_encoders.joblib")

# Save feature names for reference
feature_names = list(X.columns)
joblib.dump(feature_names, 'game_models/feature_names.joblib')
print("✓ Saved feature names")

# Test the saved model
print("\n[6] Testing saved model...")
loaded_model = joblib.load('game_models/accident_risk_model.joblib')
test_prediction = loaded_model.predict(X.iloc[:1])
print(f"✓ Test prediction: {test_prediction[0]:.4f}")

print("\n" + "="*60)
print("✓ MODEL SUCCESSFULLY SAVED AND READY FOR GAME!")
print("="*60)
print("\nSaved files:")
print("  - game_models/accident_risk_model.joblib")
print("  - game_models/label_encoders.joblib")
print("  - game_models/feature_names.joblib")
print("="*60)
