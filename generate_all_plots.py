import os
import subprocess
from pathlib import Path
from multiprocessing import Pool, cpu_count

SCRIPTS_DIRECTORY = "./scripts"
MAX_PROCESSES = cpu_count()

def run_script(script_path):
    script_name = Path(script_path).name
    print(f"[{script_name}] Starting...")
    try:
        result = subprocess.run(
            ["python", str(script_path)],
            check=True,  # Raise an exception for non-zero exit codes
            capture_output=True,
            text=True
        )
        print(f"[{script_name}] Finished successfully.")
        if result.stdout:
            print(f"[{script_name}] Output:\n{result.stdout.strip()}")
        if result.stderr:
            print(f"[{script_name}] Errors:\n{result.stderr.strip()}")

    except subprocess.CalledProcessError as e:
        print(f"[{script_name}] **ERROR**: Script failed with return code {e.returncode}")
        print(f"[{script_name}] STDOUT:\n{e.stdout.strip()}")
        print(f"[{script_name}] STDERR:\n{e.stderr.strip()}")
    except FileNotFoundError:
        print(f"[{script_name}] **ERROR**: Python interpreter not found.")
    except Exception as e:
        print(f"[{script_name}] **An unexpected error occurred**: {e}")


def main():
    target_dir = Path(__file__).parent / SCRIPTS_DIRECTORY
    
    if not target_dir.is_dir():
        print(f"Error: Directory not found: {target_dir}")
        return

    python_files = [f for f in target_dir.glob("*.py") if f.name != Path(__file__).name]

    if not python_files:
        print(f"No .py files found in {target_dir}")
        return

    print(f"Found {len(python_files)} scripts to run in parallel.")
    print(f"Using a Pool of {MAX_PROCESSES} processes (CPU Cores).")
    print("-" * 30)
    
    with Pool(processes=MAX_PROCESSES) as pool:
        pool.map(run_script, python_files)
        
    print("-" * 30)
    print("All scripts have finished execution.")


if __name__ == "__main__":
    main()