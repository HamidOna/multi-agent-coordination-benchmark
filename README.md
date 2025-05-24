# Multi-Agent Coordination Benchmark

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A systematic study of information preservation and coordination overhead in multi-agent document processing pipelines.

## 🎯 Research Question

> How does information preservation and coordination overhead vary across different multi-agent handoff strategies in document analysis workflows?

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Experiments](#experiments)
- [Results](#results)
- [Citation](#citation)
- [Contributing](#contributing)

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/multi-agent-coordination-benchmark.git
cd multi-agent-coordination-benchmark

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys