# Q1 — Python Toolchain Setup

## System
Operating System: Ubuntu 22.04

## Conda
Command:
conda --version

Output:
conda 26.5.3

## Python
Command:
python --version

Output:
Python 3.14.6

## Python Location
Command:
which python

Output:
/home/mcal312/miniconda3/bin/python

## Conda Information
Command:
conda info

Active environment: base
Conda version: 26.5.3
Python version: 3.14.6
Base environment: /home/mcal312/miniconda3

## Concepts
- Python interpreter: Executes Python programs.
- Miniconda: A Python distribution and environment manager.
- PATH: Helps the shell locate executable programs.
- Base environment: The default Conda environment.# Q1 — Python Toolchain Setup Log

## conda --version
conda 26.5.3

## python --version
Python 3.14.6

## which python
/home/mcal312/miniconda3/bin/python

## conda info
Active environment: base
Active environment location: /home/mcal312/miniconda3
Conda version: 26.5.3
Python version: 3.14.6
Base environment: /home/mcal312/miniconda3
Platform: linux-64

## Result
Miniconda and Python were successfully installed and verified.
## Q3 — venv vs Conda

| Criteria | venv + pip | Conda |
|---|---|---|
| Ships with Python? | Yes, venv is included with Python | Miniconda/Anaconda provides Python |
| Manages non-Python deps? | Limited | Yes |
| Environment file name | requirements.txt | environment.yml |
| Size on disk | Usually smaller | Usually larger |
| Best for | Lightweight Python projects | Data science, scientific computing and complex dependencies |
