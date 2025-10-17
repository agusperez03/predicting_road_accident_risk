#!/bin/bash
# CI Checks Runner - Run all CI checks locally before pushing
# Usage: ./run_checks.sh

set -e  # Exit on error

echo "🚀 Running all CI checks locally..."
echo ""

# Change to project directory
cd "$(dirname "$0")"

echo "📦 Installing dev dependencies..."
pip install -r requirements-dev.txt > /dev/null 2>&1
echo "✅ Dependencies installed"
echo ""

echo "🧪 Running tests..."
pytest tests/ -v --cov=utils --cov-report=term
if [ $? -eq 0 ]; then
    echo "✅ Tests passed"
else
    echo "❌ Tests failed"
    exit 1
fi
echo ""

echo "🎨 Checking code formatting (Black)..."
black --check . --exclude='venv|.git|__pycache__|.pytest_cache'
if [ $? -eq 0 ]; then
    echo "✅ Code formatting is correct"
else
    echo "⚠️  Code needs formatting. Run: black . --exclude='venv|.git|__pycache__'"
    echo "   Running auto-format..."
    black . --exclude='venv|.git|__pycache__|.pytest_cache'
fi
echo ""

echo "📋 Checking import sorting (isort)..."
isort --check-only . --skip venv --skip .git --skip __pycache__ --skip .pytest_cache
if [ $? -eq 0 ]; then
    echo "✅ Import sorting is correct"
else
    echo "⚠️  Imports need sorting. Run: isort . --skip venv --skip .git"
    echo "   Running auto-sort..."
    isort . --skip venv --skip .git --skip __pycache__ --skip .pytest_cache
fi
echo ""

echo "🔍 Running linter (Flake8)..."
flake8 . --exclude=venv,.git,__pycache__,.pytest_cache --max-line-length=100 --ignore=E203,W503
if [ $? -eq 0 ]; then
    echo "✅ Linting passed"
else
    echo "⚠️  Linting issues found (see above)"
fi
echo ""

echo "🔒 Running security scan (Bandit)..."
bandit -r . -ll -x venv,__pycache__,.pytest_cache
if [ $? -eq 0 ]; then
    echo "✅ Security scan passed"
else
    echo "⚠️  Security issues found (see above)"
fi
echo ""

echo "🤖 Validating ML model..."
python -c "
from utils.model_utils import RiskPredictor
predictor = RiskPredictor(models_dir='models')
print('✅ Model loaded successfully!')
print(f'   Model type: {type(predictor.model).__name__}')
print(f'   Features: {len(predictor.feature_names)}')
"
echo ""

echo "🎉 All checks completed!"
echo ""
echo "Next steps:"
echo "  1. Review any warnings above"
echo "  2. Commit your changes: git add ."
echo "  3. Push to GitHub: git push"
