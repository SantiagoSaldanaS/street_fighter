# Reinforcement Learning – Street Fighter

[![Python](https://img.shields.io/badge/python-3.8.10-blue.svg)](https://www.python.org/)

_A bilingual project setup guide (English / Español)_

---

## Project overview

This repository contains code and experiments for Reinforcement Learning agents applied to a Street Fighter environment. The project is designed to run with **Python 3.8.10** inside an isolated virtual environment to guarantee compatibility and reproducibility.

---

## English

### Prerequisites
- Install **Python 3.8.10**: https://www.python.org/downloads/release/python-3810/
- Verify installation:

```bash
python --version
```

Expected output:
```
Python 3.8.10
```

---

### 1) Create a virtual environment
From your project folder run one of the following:

- With the **py launcher** (recommended on Windows):

```bash
py -3.8 -m venv venv
```

- If `python3.8` is available in PATH:

```bash
python3.8 -m venv venv
```

This creates a folder named `venv` containing the isolated environment.

---

### 2) Activate the virtual environment

- **PowerShell**:

```powershell
.\venv\Scripts\Activate
```

⚠️ PowerShell may block script execution by default. If you see an error about `ExecutionPolicy`, either switch to **CMD** (below) or run PowerShell as administrator (this might be more flexible, but for simplicity use CMD) and set:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

- **Command Prompt (CMD)**:

```cmd
venv\Scripts\activate
```

When active you should see the prompt prefixed with `(venv)`:
```
(venv) C:\Users\User\project>
```

To deactivate:

```bash
deactivate
```

---

### 3) Verify interpreter
1. **Python: Select Interpreter**.
2. Select the interpreter that points to:
```
...\venv\Scripts\python.exe
```

Quick script to confirm the running interpreter:

```python
import sys
print("Python running from:", sys.executable)
```

Expected when correct:
```
C:\Users\User\Desktop\Coding\street_fighter\venv\Scripts\python.exe
```
If it shows a path under `AppData\Local\Programs\Python\...` you are using the global Python and not the venv.

---

### 4) Common `pip` / compatibility notes (Windows + Python 3.8)
- Newer releases of `pip` (25.x) may use typing features that are only compatible with Python >= 3.9. If `pip` inside the venv throws errors like `TypeError: 'ABCMeta' object is not subscriptable`, then the venv's pip is broken.

**Safe recovery**:

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

### 5) Install project dependencies
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

### 6) Run a quick check
Create `test.py` with:

```python
import sys
print("Python running from:", sys.executable)
print("Hello, RL Street Fighter!")
```

Run:

```bash
python test.py
```

You should see the venv path in the output and the greeting line.


---

##  Español

### Requisitos previos
- Instala **Python 3.8.10**: https://www.python.org/downloads/release/python-3810/
- Verifica la instalación:

```bash
python --version
```

Salida esperada:
```
Python 3.8.10
```

---

### 1) Crear un entorno virtual
En la carpeta del proyecto ejecuta uno de los siguientes:

- Con el **py launcher** (recomendado en Windows):

```bash
py -3.8 -m venv venv
```

- Si `python3.8` está en tu PATH:

```bash
python3.8 -m venv venv
```

Esto crea la carpeta `venv` con el entorno aislado.

---

### 2) Activar el entorno virtual

- **PowerShell**:

```powershell
.\venv\Scripts\Activate
```

⚠️ PowerShell puede bloquear la ejecución de scripts por defecto. Si obtienes un error sobre `ExecutionPolicy`, cambia a **CMD** (abajo) o ejecuta PowerShell como administrador y ejecuta:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

- **CMD (Símbolo del sistema)**:

```cmd
venv\Scripts\activate
```

Al activarse verás el prompt con `(venv)`:
```
(venv) C:\Users\Usuario\project>
```

Para desactivar:

```bash
deactivate
```

---

### 3) Verificar intérprete en VS Code
1. Presiona `Ctrl + Shift + P` → **Python: Select Interpreter**.
2. Selecciona el intérprete que apunte a:
```
...\venv\Scripts\python.exe
```

Script rápido para confirmar el intérprete:

```python
import sys
print("Python ejecutándose desde:", sys.executable)
```

Salida correcta:
```
C:\Users\Usuario\Desktop\Coding\street_fighter\venv\Scripts\python.exe
```
Si muestra una ruta en `AppData\Local\Programs\Python\...` estás usando el Python global.

---

### 4) Notas sobre `pip` y compatibilidad (Windows + Python 3.8)
- Versiones recientes de `pip` pueden requerir Python >= 3.9. Si ves errores tipo `TypeError: 'ABCMeta' object is not subscriptable`, el `pip` del venv está roto.

**Recuperación segura**:

1. Elimina el venv roto (no afecta tu código):

```cmd
rmdir /s /q venv
```

2. Créalo de nuevo con Python 3.8:

```cmd
py -3.8 -m venv venv
```

3. Activa y verifica `pip`:

```cmd
venv\Scripts\activate
pip --version
```

Deberías ver una versión `pip` en la serie `23.x`.

---

### 5) Instalar dependencias del proyecto
Con el entorno activo, instala las librerías requeridas:

```bash
pip install gym==0.21.0
```

(Opcional) Genera un `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Para instalar desde `requirements.txt` en otra máquina:

```bash
pip install -r requirements.txt
```

---

### 6) Prueba rápida
Crea `test.py` con:

```python
import sys
print("Python ejecutándose desde:", sys.executable)
print("Hola, RL Street Fighter!")
```

Ejecuta:

```bash
python test.py
```

Deberías ver la ruta del `venv` y el mensaje.

---

## ✅ Resumen (Español)
- Usa **Python 3.8.10**.
- Crea y activa un `venv` antes de instalar paquetes.
- Si `pip` falla por incompatibilidad, elimina y recrea el `venv`.
- Configura VS Code para usar el intérprete dentro de `venv`.

---

## 📁 Archivos sugeridos
- `requirements.txt` — lista de dependencias.
- `test.py` — script de verificación.
- `src/` — código del agente y entornos.
- `notebooks/` — experiments & visualizations.

---

## 🛠 Troubleshooting / Soluciones rápidas
- `ExecutionPolicy` en PowerShell: usa CMD o ajusta la política para el usuario.
- `pip` roto en venv (error con `ABCMeta`): borra y recrea el venv con `py -3.8 -m venv venv`.
- Asegúrate de seleccionar el intérprete correcto en VS Code.

---

_— EN / ES_

