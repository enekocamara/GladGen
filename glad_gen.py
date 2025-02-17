import os
import sys
import venv
import shutil
import subprocess
from pathlib import Path

# Define paths
#GLAD_DIR = Path("modules") / "syris" / "modules" / "glad"
GLAD_DIR = Path(".")
VENV_DIR = GLAD_DIR / "venv"
SRC_DIR = GLAD_DIR / "src"

def create_venv(venv_path):
    """Create a virtual environment natively using venv module."""
    if not venv_path.exists():
        print("Creating virtual environment...")
        venv.create(venv_path, with_pip=True)

def install_package(venv_path, package):
    """Install a package inside the virtual environment using pip (natively)."""
    python_exec = venv_path / ("Scripts" if os.name == "nt" else "bin") / "python"
    subprocess.run([str(python_exec), "-m", "pip", "install", package], check=True)

def run_glad(venv_path, src_path):
    """Run glad2 natively using the virtual environment's Python."""
    python_exec = venv_path / ("Scripts" if os.name == "nt" else "bin") / "python"
    subprocess.run([str(python_exec), "-m", "glad", "--api", "gl:core=4.6", "--out-path", str(src_path), "c"], check=True)

def clean_venv(venv_path):
    """Remove the virtual environment after completion."""
    print("Removing virtual environment...")
    shutil.rmtree(venv_path, ignore_errors=True)

def main():
    create_venv(VENV_DIR)
    install_package(VENV_DIR, "glad2")
    run_glad(VENV_DIR, SRC_DIR)
    clean_venv(VENV_DIR)
    print("Glad2 setup complete!")

if __name__ == "__main__":
    main()