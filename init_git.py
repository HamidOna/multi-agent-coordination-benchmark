#!/usr/bin/env python3
"""
Initialize Git repository with proper configuration for research project
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run shell command and return output"""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True, 
            cwd=cwd
        )
        if result.returncode != 0:
            print(f"Error running command: {cmd}")
            print(f"Error: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"Exception running command: {e}")
        return False

def setup_git_repo():
    """Initialize and configure git repository"""
    
    print("🔧 Configuring Git repository...")
    
    # Check if git is already initialized
    if os.path.exists(".git"):
        print("⚠️  Git repository already initialized")
        response = input("Reinitialize? (y/n): ")
        if response.lower() != 'y':
            return
    
    # Initialize git
    run_command("git init")
    
    # Configure git settings for research
    git_configs = [
        "git config --local core.autocrlf true",
        "git config --local pull.rebase false",
        "git config --local init.defaultBranch main",
    ]
    
    for config in git_configs:
        run_command(config)
    
    # Create .gitkeep files for empty directories
    empty_dirs = [
        "data/raw_documents",
        "data/ground_truth", 
        "experiments/results/raw",
        "logs",
    ]
    
    for dir_path in empty_dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        gitkeep = Path(dir_path) / ".gitkeep"
        gitkeep.touch()
    
    # Initial commit
    print("📝 Creating initial commit...")
    run_command("git add .")
    run_command('git commit -m "Initial commit: Project structure and configuration"')
    
    print("✅ Git repository initialized successfully!")
    
    # Set up pre-commit hooks
    setup_pre_commit_hooks()

def setup_pre_commit_hooks():
    """Set up pre-commit hooks for code quality"""
    
    print("\n🔨 Setting up pre-commit hooks...")
    
    pre_commit_config = """\
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: ['--maxkb=1000']
      - id: check-json
      - id: check-merge-conflict
      
  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
        language_version: python3.8
        
  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        args: ['--max-line-length=88', '--extend-ignore=E203']
"""
    
    with open(".pre-commit-config.yaml", "w") as f:
        f.write(pre_commit_config)
    
    # Install pre-commit
    run_command("pip install pre-commit")
    run_command("pre-commit install")
    
    print("✅ Pre-commit hooks installed!")

def create_github_actions():
    """Create GitHub Actions workflow for CI/CD"""
    
    print("\n🚀 Creating GitHub Actions workflow...")
    
    os.makedirs(".github/workflows", exist_ok=True)
    
    workflow = """\
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9]
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        pytest tests/ -v --cov=src --cov-report=xml
    
    - name: Check code quality
      run: |
        black --check src/
        flake8 src/ --max-line-length=88 --extend-ignore=E203
"""
    
    with open(".github/workflows/ci.yml", "w") as f:
        f.write(workflow)
    
    print("✅ GitHub Actions workflow created!")

if __name__ == "__main__":
    setup_git_repo()
    create_github_actions()
    
    print("\n🎉 Git infrastructure setup complete!")
    print("\nNext steps:")
    print("1. Create a GitHub repository")
    print("2. Add remote: git remote add origin https://github.com/HamidOna/multi-agent-coordination-benchmark.git")
    print("3. Push code: git push -u origin main")