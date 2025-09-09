# Reinforcement Learning – Street Fighter

[![Python](https://img.shields.io/badge/python-3.8.10-blue.svg)](https://www.python.org/)

_Windows Setup guide (English / Español)_

---

## Project overview

This repository contains code and experiments for Reinforcement Learning agents applied to a Street Fighter environment. The project is designed to run with **Python 3.8.10** inside an isolated virtual environment to guarantee compatibility.

---

<br>

## Prerequisites
- Install **Python 3.8.10**: https://www.python.org/downloads/release/python-3810/
- IMPORTANT: Select custom installation and add python to the PATH.
- Verify installation with powershell:

```bash
python --version
```

If it was installed correctly, it will return:
```
Python 3.8.10
```

---

<br>

## Virtual environment

Using a virtual environment is heavily recommended for this project. 

<details>
  <summary>In Visual Studio Code</summary>
  <br>
  - Step 1: Do this
  - Step 2: Do that
  <br>
  - Step 3: Profit
</details>

<details>
  <summary>In any other editor</summary>

  <br>

  From your project folder run one of the following:
  
  - With the **py launcher** (recommended on Windows):

  ```bash
  py -3.8 -m venv venv
  ```

  - If `python3.8` is available in PATH:

  ```bash
  python3.8 -m venv venv
  ```
  
  #### This creates a folder named `venv` containing the isolated environment.

  <br>

  ### Activate the virtual environment

  **PowerShell**:

  ```powershell
  .\venv\Scripts\Activate
  ```

  PowerShell may block script execution by default.  
  If you see an error about `ExecutionPolicy`, either switch to **CMD** (below)  
  or run PowerShell as administrator (this might be more flexible, but for simplicity use CMD) and set:

  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

  <br>

  - **Command Prompt (CMD)**:

  ```cmd
  venv\Scripts\activate
  ```

  When active one should see the prompt prefixed with `(venv)`:

  ```
  (venv) C:\Users\User\project>
  ```

  <br>

  To deactivate:

  ```bash
  deactivate
  ```

  ---

  ### Verify interpreter

  1. **Python: Select Interpreter**.  
  2. Select the interpreter that points to:

  ```
  ...\venv\Scripts\python.exe
  ```

  <br>

  Quick script to confirm the running interpreter:

  ```python
  import sys
  print("Python running from:", sys.executable)
  ```

  Expected when correct:

  ```
  C:\Users\User\Desktop\Coding\street_fighter\venv\Scripts\python.exe
  ```

  If it shows a path under `AppData\Local\Programs\Python\...`  
  you are using the global Python and not the venv.

  ---
</details>

<br>

### Common `pip` / compatibility notes (Windows + Python 3.8)
- Newer releases of `pip` (25.x) may use typing features that are only compatible with Python >= 3.9. If `pip` inside the venv throws errors like `TypeError: 'ABCMeta' object is not subscriptable`, then the venv's pip is broken.

<br>
<details>
  <summary>Regenerating VENV</summary>
  <br>
  1. Remove the broken venv (this does not touch your code):

  ```cmd
  rmdir /s /q venv
  ```
  
  2. Recreate it with Python 3.8:
  
  ```cmd
  py -3.8 -m venv venv
  ```
  
  3. Activate and verify `pip`:
  
  ```cmd
  venv\Scripts\activate
  pip --version
  ```
  
  You should see a `pip` version in the `23.x` series.
  
  ---
</details>


<br>

## Install project dependencies
With the virtual environment active, install the required packages:

```bash
pip install gym==0.21.0
```

(Optional) create a `requirements.txt` once your dependencies are installed:

```bash
pip freeze > requirements.txt
```

To install from `requirements.txt` on another machine:

```bash
pip install -r requirements.txt
```

---
<br>

## Run test.py
Load `test.py` from the repository with:

Run:

```bash
python test.py
```
