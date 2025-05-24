# Makefile for Multi-Agent Coordination Benchmark

.PHONY: setup init clean test run-pilot run-experiment analyze

# Setup entire project
setup:
	bash setup_project.sh
	python init_git.py
	python scripts/setup_experiment_tracking.py
	pip install -r requirements.txt

# Initialize git repository
init:
	python init_git.py

# Clean temporary files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name ".DS_Store" -delete
	rm -rf .pytest_cache
	rm -rf .coverage

# Run tests
test:
	pytest tests/ -v --cov=src

# Run pilot experiment
run-pilot:
	python scripts/run_pilot.py --config experiments/configs/pilot_config.yaml

# Run full experiment
run-experiment:
	python scripts/run_experiment.py --config experiments/configs/experiment_config.yaml

# Analyze results
analyze:
	python scripts/analyze_results.py --results experiments/results/processed/

# Format code
format:
	black src/ tests/ scripts/
	isort src/ tests/ scripts/

# Check code quality
lint:
	flake8 src/ tests/ scripts/ --max-line-length=88 --extend-ignore=E203
	black --check src/ tests/ scripts/