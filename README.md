# Programming for Industrial Applications

This repository contains course material, practice exercises, labs, lecture examples, and two applied projects for industrial programming in Python.

## Repository Overview

Top-level folders:

- `examples/` - Short standalone examples (lists, strings, ranges, sorting, helper scripts)
- `examples/data visualizations/` - Plotting examples with pandas/matplotlib/seaborn
- `exercises/` - Structured exercises (`exercise 1` to `exercise 8`) from fundamentals to data handling
- `Labs/` - Lab assignments (`Lab 1` to `Lab 8`) with practical programming tasks
- `Lectures/` - Lecture code organized by topic (algorithms, OOP, pandas, numpy, strings, etc.)
- `Projects/Controlling_a_manufacturing_system/` - Modbus-based crane controller prototype
- `Projects/LLM_LED_Controller/` - LLM-driven LED board controller (TCP + Tkinter HMI)

## Current Scope (Python Files)

Counts below exclude virtual environments and `__pycache__` folders:

- `examples`: 17
- `exercises`: 52
- `Labs`: 14
- `Lectures`: 61
- `Projects`: 4

## Requirements

Base requirement:

- Python 3.10+

Common libraries used in this repository:

- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `quandl`
- `requests`
- `pymodbus`

Install with:

```bash
pip install pandas matplotlib seaborn scikit-learn quandl requests pymodbus
```

## Running Scripts

From the repository root:

```bash
python path/to/script.py
```

Examples (Windows PowerShell):

```powershell
python .\examples\arg_max.py
python ".\exercises\exercise 1\factorial.py"
python ".\Labs\Lab 8\used_vehicles.py"
```

## Projects

### 1) Controlling a Manufacturing System

Path: `Projects/Controlling_a_manufacturing_system/`

- Main script: `crane_controller.py`
- Uses `pymodbus` and expects a Modbus server/simulator on `127.0.0.1`

Run:

```powershell
python .\Projects\Controlling_a_manufacturing_system\crane_controller.py
```

### 2) LLM LED Controller

Path: `Projects/LLM_LED_Controller/`

Files:

- `lamp_board.py` - Starts TCP LED server + Tkinter HMI
- `llm_main.py` - Chat loop that calls local Ollama API and updates LEDs
- `test.py` - Minimal Ollama API test

Dependencies/Services:

- Local Ollama server at `http://localhost:11434`
- Model name in code: `llama3:8b` (editable in scripts)

Typical run order:

1. Start lamp board:

	```powershell
	python .\Projects\LLM_LED_Controller\lamp_board.py
	```

2. In another terminal, start LLM control:

	```powershell
	python .\Projects\LLM_LED_Controller\llm_main.py
	```

## Notes

- Some visualization scripts load datasets from online URLs, so internet access may be required.
- The workspace contains local virtual environments (for example `.venv/` and `Projects/venv/`), which are not course source code.
