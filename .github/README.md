# GitHub Actions CI/CD Documentation

## 🚀 Overview

This project uses GitHub Actions for continuous integration and deployment. The workflow automatically runs tests, linting, security scans, and model validation on every push and pull request.

## 📋 Workflow Jobs

### 1. **Test** (`test`)
Runs unit tests and generates coverage reports.

**What it does:**
- Sets up Python 3.11 environment
- Installs all dependencies
- Runs pytest with coverage
- Uploads coverage to Codecov (optional)

**Local command:**
```bash
cd road_risk_game
pytest tests/ -v --cov=utils
```

### 2. **Lint** (`lint`)
Checks code quality and style.

**What it does:**
- **Black**: Checks Python code formatting
- **isort**: Checks import statement ordering
- **Flake8**: Checks PEP8 compliance

**Local commands:**
```bash
black --check road_risk_game/
isort --check-only road_risk_game/
flake8 road_risk_game/ --max-line-length=100
```

**Auto-fix:**
```bash
black road_risk_game/
isort road_risk_game/
```

### 3. **Security** (`security`)
Scans for security vulnerabilities.

**What it does:**
- **Bandit**: Scans Python code for security issues
- **Safety**: Checks dependencies for known vulnerabilities

**Local command:**
```bash
bandit -r road_risk_game/ -ll
safety check
```

### 4. **Validate Model** (`validate-model`)
Ensures ML model files are present and loadable.

**What it does:**
- Verifies `.joblib` files exist
- Tests model loading
- Validates feature names and encoders

**Local command:**
```bash
python -c "from utils.model_utils import RiskPredictor; RiskPredictor(models_dir='models')"
```

### 5. **Deploy Preview** (`deploy-preview`)
Comments on PRs with deployment status (PR only).

### 6. **Notify Success** (`notify-success`)
Logs success message when all checks pass (push only).

## 🎯 When Workflows Run

| Event | Branches | Jobs |
|-------|----------|------|
| **Push** | `main`, `develop` | All jobs + success notification |
| **Pull Request** | `main` | All jobs + PR comment |

## 🔧 Setup Instructions

### 1. Enable GitHub Actions

Actions are automatically enabled. View them at:
```
https://github.com/agusperez03/predicting_road_accident_risk/actions
```

### 2. Add Status Badges (Optional)

Add to your main `README.md`:

```markdown
![CI/CD Pipeline](https://github.com/agusperez03/predicting_road_accident_risk/workflows/CI/CD%20Pipeline/badge.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
```

### 3. Configure Codecov (Optional)

For coverage reports:

1. Sign up at [codecov.io](https://codecov.io)
2. Connect your repository
3. Add badge to README:
```markdown
![Coverage](https://codecov.io/gh/agusperez03/predicting_road_accident_risk/branch/main/graph/badge.svg)
```

### 4. Set up Secrets (Optional)

For automated deployment to Streamlit Cloud:

1. Go to: `Settings > Secrets and variables > Actions`
2. Click "New repository secret"
3. Add: `STREAMLIT_CLOUD_TOKEN`

## 🏃‍♂️ Running Checks Locally

Before pushing, run all checks locally:

**On Windows:**
```bash
cd road_risk_game
.\run_checks.bat
```

**On Linux/Mac:**
```bash
cd road_risk_game
chmod +x run_checks.sh
./run_checks.sh
```

**Or manually:**
```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Format code
black . --exclude='venv'
isort . --skip venv

# Lint
flake8 . --exclude=venv --max-line-length=100

# Security scan
bandit -r . -ll -x venv
```

## 📊 Coverage Reports

After running tests locally, view coverage:

```bash
# Terminal output
pytest tests/ --cov=utils --cov-report=term

# HTML report (opens in browser)
pytest tests/ --cov=utils --cov-report=html
open htmlcov/index.html  # Linux/Mac
start htmlcov/index.html  # Windows
```

## 🐛 Troubleshooting

### ❌ Tests Failing

1. Run tests locally: `pytest tests/ -v`
2. Check error messages in Actions tab
3. Ensure all dependencies are in `requirements.txt`

### ❌ Linting Errors

1. Run Black to auto-format: `black .`
2. Run isort to fix imports: `isort .`
3. Fix remaining Flake8 issues manually

### ❌ Model Validation Failed

1. Ensure `.joblib` files are committed
2. Check files exist: `ls road_risk_game/models/`
3. Test loading locally: `python -c "from utils.model_utils import RiskPredictor; RiskPredictor()"`

### ❌ Security Issues

1. Review Bandit output for severity
2. Update vulnerable dependencies: `pip install --upgrade <package>`
3. Check Safety report: `safety check --json`

## 🔄 Workflow File Location

Main workflow: `.github/workflows/ci.yml`

To modify:
1. Edit `.github/workflows/ci.yml`
2. Commit and push
3. View results in Actions tab

## 📚 Best Practices

1. **Always run checks locally** before pushing
2. **Keep branches up to date** with main
3. **Fix failing tests immediately** - don't merge broken code
4. **Review security warnings** - even if CI passes
5. **Write tests for new features** - maintain coverage
6. **Use descriptive commit messages** for easier debugging

## 🎓 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Pytest Documentation](https://docs.pytest.org/)
- [Black Code Style](https://black.readthedocs.io/)
- [Flake8 Rules](https://flake8.pycqa.org/en/latest/user/error-codes.html)
- [Bandit Security Checks](https://bandit.readthedocs.io/)

## 📞 Support

If you encounter issues:

1. Check workflow logs in Actions tab
2. Review this documentation
3. Open an issue on GitHub
4. Contact the maintainer

---

**Last Updated:** October 17, 2025
**Maintained by:** @agusperez03
