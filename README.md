# ReinforcementLearning_StreetFighter


For this project you will need to install Python 3.8.10

Open PowerShell or CMD
Verify your version
python --version

In your project directory:
python -m venv venv
This creates a directory called venv.

Activate the virtual environment with:
Powershell:
.\venv\Scripts\Activate
! Warning: PowerShell might block script executions if this happens, use CMD. 
  There is a way to use PowerShell, which can be more flexible, but for simpicity means we will skip it.

CMD:
venv\Scripts\activate

When active, you will see:
(venv) C:\Users\User\project>

To deactivate it just:
deactivate

Now with the virtual environment you can install packages and they will not affect your global configurations.
This is very usefull to keep an organized set up.

After the environment is set correctly, just change your Python interpreter.
Choose the one that looks like:
...\venv\Scripts\python.exe

Verify in your environment, in a .py, execute:
import sys
print("Python ejecutándose desde:", sys.executable)

If it show something like:
C:\Users\User\Desktop\Coding\street_fighter\venv\Scripts\python.exe
Then the venv is corrctly 




