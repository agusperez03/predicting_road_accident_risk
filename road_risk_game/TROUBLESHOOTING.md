# 🔧 Troubleshooting Guide

## Common Deployment Issues

### 1. FileNotFoundError: Model files not found

**Error:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'models/accident_risk_model.joblib'
```

**Solution:**
✅ **Fixed!** The app now uses absolute paths based on the file location.

**What was done:**
- Updated `utils/model_utils.py` to use `Path(__file__).parent.parent / models_dir`
- This ensures the model files are found regardless of the working directory
- Commit: `cc92071` - "Fix: Use absolute paths for model loading in Streamlit Cloud"

---

### 2. CORS Warning

**Warning:**
```
Warning: the config option 'server.enableCORS=false' is not compatible with 'server.enableXsrfProtection=true'
```

**Solution:**
✅ **Fixed!** Updated `.streamlit/config.toml` to set `enableCORS = true`

**What was done:**
- Changed `server.enableCORS` from `false` to `true` in config.toml
- Commit: `5cf9b6a` - "Fix: Update CORS config for Streamlit Cloud"

---

### 3. Model files not in repository

**Issue:** Large model files (> 100MB) cannot be pushed to GitHub

**Solution:**
Our model files are small (<0.5 MB), so they're directly committed:
- `accident_risk_model.joblib` - 0.47 MB
- `feature_names.joblib` - <0.01 MB
- `label_encoders.joblib` - <0.01 MB

**If your models are larger:**
Use Git LFS (Large File Storage):
```bash
git lfs install
git lfs track "*.joblib"
git add .gitattributes
git add road_risk_game/models/*.joblib
git commit -m "Add model files with Git LFS"
git push origin main
```

Or use external storage:
- Streamlit Cloud: Store in `secrets.toml` (for small files)
- AWS S3 / Google Cloud Storage (for large files)
- Hugging Face Model Hub

---

## Deployment Checklist

Before deploying to Streamlit Cloud:

- [x] ✅ Model files are in the repository
- [x] ✅ `requirements.txt` has all dependencies
- [x] ✅ Paths use `Path(__file__)` for absolute references
- [x] ✅ `.streamlit/config.toml` is configured
- [x] ✅ App runs locally without errors
- [x] ✅ No hardcoded local paths (like `C:\Users\...`)
- [x] ✅ Git repository is up to date (`git push`)

---

## Streamlit Cloud Deployment

### Step 1: Connect Repository
1. Go to https://share.streamlit.io
2. Click "New app"
3. Connect your GitHub: `agusperez03/predicting_road_accident_risk`

### Step 2: Configure App
```
Repository: agusperez03/predicting_road_accident_risk
Branch: main
Main file path: road_risk_game/app.py
```

### Step 3: Advanced Settings (Optional)
```
Python version: 3.11
Requirements file: road_risk_game/requirements.txt
```

### Step 4: Deploy
- Click "Deploy!"
- Wait 2-5 minutes for build
- Your app will be live at: `https://<your-app-name>.streamlit.app`

---

## Testing the Deployment

After deployment, verify:

1. **Model Loading:** Check logs for "✓ Model loaded successfully"
2. **UI Elements:** All cards, buttons, and stats display correctly
3. **Predictions:** Make selections and verify risk scores appear
4. **Streak System:** Play multiple rounds to test point multipliers
5. **Difficulty Levels:** Switch difficulty and verify scenario changes

---

## Performance Optimization

### If app is slow:

1. **Cache model loading:**
   ```python
   @st.cache_resource
   def load_predictor():
       return RiskPredictor()
   ```
   ✅ Already implemented in `app.py`

2. **Reduce scenario generation time:**
   - Pre-generate scenarios in batches
   - Cache common scenarios

3. **Optimize imports:**
   - Move heavy imports inside functions
   - Use lazy loading

---

## Contact & Support

**Repository:** https://github.com/agusperez03/predicting_road_accident_risk

**Issues:** Open a GitHub issue for bugs or feature requests

**Model Performance:**
- R² Score: 0.8841
- MAE: 0.0440
- Training samples: 517,754

---

**Last Updated:** October 16, 2025
**Status:** ✅ Production Ready
