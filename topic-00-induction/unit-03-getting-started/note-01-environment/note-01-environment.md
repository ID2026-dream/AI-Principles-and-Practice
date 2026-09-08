---
order: 1
icon:
  type: fluent:desktop-24-filled
  color: "#2D7FF9"
---

# Before the Week 1 Lab

Pre-work before Week 1

Have this working before the first lab. Nothing here is assessed, but the Week
1 lab assumes it is done.

## Python and an environment

Python 3.11 or newer, in a virtual environment per module rather than a single
global install.

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
```

## The core stack

Small and fast. This is everything Weeks 1 to 5 need.

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyterlab
```

## The heavy stack

Needed from Week 7. Install it before Week 7 rather than during the lab — it is
a large download.

```bash
pip install torch torchvision transformers datasets
pip install fairlearn shap lime          # Weeks 3 and 4
```

Check for a working GPU once installed:

```python
import torch
print(torch.__version__, torch.cuda.is_available())
```

CPU-only is fine for everything in this module. The lab baseline is an i7-class
machine with 32 GB RAM and an RTX 3060 (12 GB), and every lab is written to run
without the GPU, more slowly.

## Git

You need a repository with a real commit history from Week 1, because the final
project is assessed partly on that history.

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

## Choose a project dataset

Bring a dataset to Week 1 that you will carry through the whole module. It
should have at least a few thousand rows, a mix of numeric and categorical
columns, some genuine messiness, and at least one attribute that could raise a
fairness question in Week 3.

The final project runs on a different dataset — one you have not seen — so this
one is for learning on, not for the capstone.
