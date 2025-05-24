#!/bin/bash

# Multi-Agent Coordination Benchmark Project Setup
# Run this script to initialize your entire project structure

PROJECT_NAME="multi-agent-coordination-benchmark"
GITHUB_USERNAME="HamidOna"  # UPDATE THIS

echo "🚀 Setting up Multi-Agent Coordination Benchmark Project..."

# Create main project directory
mkdir -p $PROJECT_NAME
cd $PROJECT_NAME

# Initialize git repository
git init

# Create directory structure
echo "📁 Creating project structure..."
mkdir -p {experiments/{configs,prompts,results/{raw,processed,figures}},data/{raw_documents/{contracts,reports,papers},ground_truth,synthetic},src/{agents,evaluation,analysis,utils},notebooks/{exploration,analysis},papers/{drafts,figures,submissions},tests/{unit,integration},scripts,logs}

# Create essential files
touch README.md
touch .gitignore
touch requirements.txt
touch setup.py
touch .env.example
touch CONTRIBUTING.md
touch LICENSE
touch CHANGELOG.md

# Create __init__.py files for Python packages
find src -type d -exec touch {}/__init__.py \;
find tests -type d -exec touch {}/__init__.py \;

# Create config files
touch experiments/configs/default_config.yaml
touch experiments/configs/experiment_config.yaml

# Create tracking files
touch experiments/results/experiment_tracker.csv
touch logs/experiment_log.txt

echo "✅ Project structure created!"