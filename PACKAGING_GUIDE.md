# 📦 SimplePlan Packaging & Distribution Guide

## 🚀 **Available Distribution Formats**

Your SimplePlan project is now packaged in multiple formats for different use cases:

### **1. Python Package Distributions**
```
dist/
├── simpleplan-1.0.0-py3-none-any.whl    # Wheel format (preferred)
└── simpleplan-1.0.0.tar.gz              # Source distribution
```

### **2. Standalone Executable**
```
dist/
└── simpleplan                            # 17MB standalone executable
```

## 🎯 **Distribution Options**

### **Option 1: Automated GitHub Workflow (Recommended)**

**Benefits:**
- **Fully automated** - Just create GitHub releases
- **Multi-platform builds** - Linux, Windows, macOS executables
- **Quality assurance** - Tests must pass before publishing
- **Zero maintenance** - Handles PyPI publishing automatically

**Setup:**
1. **Add PyPI API Token to GitHub Secrets:**
   - Go to Repository → Settings → Secrets and Variables → Actions
   - Add secret: `PYPI_API_TOKEN` with your PyPI token

2. **Create a Release:**
   ```bash
   # Update version
   poetry version patch
   git add pyproject.toml
   git commit -m "Bump version to $(poetry version -s)"
   git push

   # Create GitHub release (triggers automation)
   # Go to GitHub → Releases → Create new release
   # Tag: v1.0.1, Title: SimplePlan v1.0.1
   ```

3. **Automatic Actions:**
   - ✅ Tests run on Python 3.10, 3.11, 3.12
   - ✅ Package built and published to PyPI
   - ✅ Executables built for all platforms
   - ✅ Assets uploaded to GitHub release

**See [GitHub Actions Setup Guide](.github/workflows/setup.md) for complete configuration.**

### **Option 2: Manual PyPI Release**

**Benefits:**
- Direct control over publishing
- Manual quality control
- Fallback option if automation fails

**Steps:**
1. **Get PyPI API Token:**
   ```bash
   # Go to https://pypi.org/account/register/
   # Create account → Account settings → API tokens → Create token
   ```

2. **Configure Poetry:**
   ```bash
   poetry config pypi-token.pypi YOUR_PYPI_TOKEN
   ```

3. **Publish:**
   ```bash
   poetry build
   poetry publish
   ```

4. **Users install with:**
   ```bash
   pip install simpleplan
   # or
   poetry add simpleplan
   ```

### **Option 3: Manual GitHub Releases**

**Benefits:**
- Free hosting
- Version control integration
- Manual control over releases

**Steps:**
1. **Create GitHub Release:**
   - Go to your repository → Releases → Create new release
   - Tag version: `v1.0.0`
   - Upload files: `simpleplan-1.0.0-py3-none-any.whl`, `simpleplan` (executable)

2. **Users install with:**
   ```bash
   # Python package
   pip install https://github.com/bjornjohnson/SimplePlan/releases/download/v1.0.0/simpleplan-1.0.0-py3-none-any.whl

   # Standalone executable
   curl -L https://github.com/bjornjohnson/SimplePlan/releases/download/v1.0.0/simpleplan -o simpleplan
   chmod +x simpleplan
   ```

### **Option 4: Private Distribution**

**For Enterprise/Private Use:**

```bash
# Direct wheel installation
pip install ./simpleplan-1.0.0-py3-none-any.whl

# Or copy standalone executable
cp dist/simpleplan /usr/local/bin/simpleplan
```

### **Option 5: Docker Container**

Create a containerized version:

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY dist/simpleplan-1.0.0-py3-none-any.whl .
RUN pip install simpleplan-1.0.0-py3-none-any.whl

ENTRYPOINT ["simpleplan"]
```

## 🛠️ **Development Workflow**

### **Automated Workflow (Recommended)**
```bash
# Update version and create release
poetry version patch
git add pyproject.toml
git commit -m "Bump version to $(poetry version -s)"
git push

# Create GitHub release (triggers full automation)
# Go to GitHub → Releases → Create new release
# Everything else is automated!
```

### **Manual Workflow**
```bash
# Update version in pyproject.toml
poetry version patch    # 1.0.0 → 1.0.1
poetry version minor    # 1.0.0 → 1.1.0
poetry version major    # 1.0.0 → 2.0.0

# Rebuild packages
poetry build
poetry run pyinstaller --onefile --name simpleplan src/main.py
```

### **Testing Before Release**
```bash
# Run full test suite
poetry run pytest

# Test wheel locally
pip install dist/simpleplan-1.0.0-py3-none-any.whl

# Test standalone executable
./dist/simpleplan --help
./dist/simpleplan create "Test Project"
```

## 🔄 **CI/CD Workflows**

### **Continuous Integration**
- **Trigger:** Every push to main/develop, all pull requests
- **Actions:** Run tests, linting, type checking on Python 3.10, 3.11, 3.12
- **File:** `.github/workflows/test.yml`

### **Automated Publishing**
- **Trigger:** GitHub release creation
- **Actions:** Test → Build → Publish to PyPI → Create executables → Upload assets
- **File:** `.github/workflows/publish.yml`

**Benefits:**
- ✅ **Zero-maintenance releases** - Just create GitHub releases
- ✅ **Quality assurance** - Tests must pass before publishing
- ✅ **Multi-platform support** - Automatic executables for all platforms
- ✅ **Professional workflow** - Industry-standard CI/CD practices

## 📋 **Distribution Checklist**

**Before Publishing:**
- [ ] Version updated in `pyproject.toml`
- [ ] Tests passing: `poetry run pytest`
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] License and copyright verified

**Build Process:**
- [ ] `poetry build` - Creates wheel and source dist
- [ ] `poetry run pyinstaller --onefile --name simpleplan src/main.py` - Creates executable
- [ ] Test both distribution formats
- [ ] Verify CLI commands work

**Publishing:**
- [ ] PyPI: `poetry publish`
- [ ] GitHub: Create release with assets
- [ ] Documentation: Update installation instructions

## 🌟 **Recommended Distribution Strategy**

**For Maximum Reach and Minimum Effort:**
1. **Automated GitHub Workflow** - Handles everything automatically
2. **PyPI Publishing** - Automatic via GitHub releases
3. **Multi-platform Executables** - Linux, Windows, macOS built automatically
4. **GitHub Releases** - Assets uploaded automatically

**One-Command Release Process:**
```bash
# 1. Update version
poetry version patch
git add pyproject.toml
git commit -m "Bump version to $(poetry version -s)"
git push

# 2. Create GitHub release
# Go to GitHub → Releases → Create new release
# Tag: v1.0.1, Title: SimplePlan v1.0.1
# Click "Publish release"

# 3. Everything else is automatic! 🚀
```

**Installation Options for Users:**
```bash
# Python developers (from PyPI)
pip install simpleplan

# MacOS users (standalone)
curl -L https://github.com/bjornjohnson/SimplePlan/releases/latest/download/simpleplan-macos -o simpleplan
chmod +x simpleplan

# Linux users (standalone)
curl -L https://github.com/bjornjohnson/SimplePlan/releases/latest/download/simpleplan-linux -o simpleplan
chmod +x simpleplan

# Windows users (standalone)
# Download simpleplan-windows.exe from GitHub releases
```

## 🎉 **Your Package is Ready!**

SimplePlan is now professionally packaged with full CI/CD automation:

- ✅ **Automated Publishing** - Zero-maintenance releases via GitHub
- ✅ **Multi-platform Executables** - Linux, Windows, macOS built automatically
- ✅ **Quality Assurance** - Tests must pass before publishing
- ✅ **PyPI Distribution** - Automatic publishing to PyPI
- ✅ **Professional Metadata** - Complete package information
- ✅ **CLI Interface** - Full command-line functionality
- ✅ **MCP Integration** - AI-native features included

**Next Steps:**
1. **Set up PyPI API token** in GitHub secrets
2. **Create your first release** - everything else is automated!
3. **Share SimplePlan with the world** - it's never been easier! 🚀

**Pro Tip:** With the automated workflow, releasing is as simple as creating a GitHub release. The system handles testing, building, and publishing across all platforms automatically.

---

*Copyright © 2025 Sunset Code Collaborative, LLC*
