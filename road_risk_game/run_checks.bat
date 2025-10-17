@echo off
REM CI Checks Runner - Run all CI checks locally before pushing
REM Usage: run_checks.bat

echo 🚀 Running all CI checks locally...
echo.

cd /d "%~dp0"

echo 📦 Installing dev dependencies...
pip install -r requirements-dev.txt >nul 2>&1
echo ✅ Dependencies installed
echo.

echo 🧪 Running tests...
pytest tests/ -v --cov=utils --cov-report=term
if %errorlevel% neq 0 (
    echo ❌ Tests failed
    exit /b 1
)
echo ✅ Tests passed
echo.

echo 🎨 Checking code formatting (Black)...
black --check . --exclude="venv|.git|__pycache__|.pytest_cache"
if %errorlevel% neq 0 (
    echo ⚠️  Code needs formatting. Running auto-format...
    black . --exclude="venv|.git|__pycache__|.pytest_cache"
) else (
    echo ✅ Code formatting is correct
)
echo.

echo 📋 Checking import sorting (isort)...
isort --check-only . --skip venv --skip .git --skip __pycache__ --skip .pytest_cache
if %errorlevel% neq 0 (
    echo ⚠️  Imports need sorting. Running auto-sort...
    isort . --skip venv --skip .git --skip __pycache__ --skip .pytest_cache
) else (
    echo ✅ Import sorting is correct
)
echo.

echo 🔍 Running linter (Flake8)...
flake8 . --exclude=venv,.git,__pycache__,.pytest_cache --max-line-length=100 --ignore=E203,W503
if %errorlevel% neq 0 (
    echo ⚠️  Linting issues found
) else (
    echo ✅ Linting passed
)
echo.

echo 🔒 Running security scan (Bandit)...
bandit -r . -ll -x venv,__pycache__,.pytest_cache
if %errorlevel% neq 0 (
    echo ⚠️  Security issues found
) else (
    echo ✅ Security scan passed
)
echo.

echo 🤖 Validating ML model...
python -c "from utils.model_utils import RiskPredictor; predictor = RiskPredictor(models_dir='models'); print('✅ Model loaded successfully!'); print(f'   Model type: {type(predictor.model).__name__}'); print(f'   Features: {len(predictor.feature_names)}')"
echo.

echo 🎉 All checks completed!
echo.
echo Next steps:
echo   1. Review any warnings above
echo   2. Commit your changes: git add .
echo   3. Push to GitHub: git push
echo.
pause
