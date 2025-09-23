
import tarfile, glob, os, subprocess, sys, shutil

sdists = glob.glob("gym-0.21.0*.tar.gz")

if not sdists:
    raise SystemExit("gym-0.21.0 tar.gz not found in current directory. Make sure pip download succeeded.")

sdist = sdists[0]
workdir = "gym_sdist"

if os.path.exists(workdir):
    shutil.rmtree(workdir)
os.makedirs(workdir, exist_ok=True)

# extract the sdist
with tarfile.open(sdist, "r:gz") as tar:
    tar.extractall(workdir)

# find the extracted source directory (usually gym-0.21.0)
dirs = [d for d in os.listdir(workdir) if os.path.isdir(os.path.join(workdir, d))]
if not dirs:
    raise SystemExit("Could not find extracted source dir.")
srcdir = os.path.join(workdir, dirs[0])

# patch setup.py: fix malformed opencv specifier
setup_py = os.path.join(srcdir, "setup.py")
if not os.path.exists(setup_py):
    raise SystemExit("setup.py not found in extracted source.")
text = open(setup_py, "r", encoding="utf-8").read()
patched = text.replace("opencv-python>=3.", "opencv-python>=3.0.0")
if text == patched:
    print("No replacement made (maybe file already patched).")
else:
    open(setup_py, "w", encoding="utf-8").write(patched)
    print("Patched setup.py to fix opencv requirement.")

# install the patched local source
print("Installing patched gym from:", srcdir)
subprocess.check_call([sys.executable, "-m", "pip", "install", srcdir])
print("Installed patched gym.")
