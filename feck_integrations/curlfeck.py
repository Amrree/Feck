#!/usr/bin/env python3
import subprocess
import sys
import os

def run_command(cmd):
    """Runs a shell command and returns its exit code."""
    try:
        process = subprocess.run(cmd, shell=True, check=False, text=True, capture_output=True)
        return process.returncode, process.stdout, process.stderr
    except Exception as e:
        print(f"Error running command: {e}", file=sys.stderr)
        return 1, "", str(e)

def main():
    original_command = sys.argv[1:]
    if not original_command:
        print("Usage: curlfeck <curl_command_and_arguments>", file=sys.stderr)
        sys.exit(1)

    # Try to run the original curl command
    curl_cmd = ["curl"] + original_command
    exit_code, stdout, stderr = run_command(curl_cmd)

    if exit_code != 0:
        # If curl failed, try to invoke feck
        print(f"\nOh, feck! It seems 'curl' had a bit of a kerfuffle. Let's see if 'feck' can sort it out...", file=sys.stderr)
        # Reconstruct the command for feck to fix
        # feck expects the previous command to be in history or passed via a specific mechanism.
        # For simplicity here, we'll just run feck directly.
        # For this script, we'll simulate it by printing the failed command and then running feck.
        print(f"Failed command: {' '.join(curl_cmd)}", file=sys.stderr)
        feck_cmd = ["feck"]
        feck_exit_code, feck_stdout, feck_stderr = run_command(feck_cmd)
        if feck_exit_code != 0:
            print(f"Feck couldn't fix it either! Oh, feckit!\n{feck_stderr}", file=sys.stderr)
        else:
            print(f"Feck to the rescue!\n{feck_stdout}", file=sys.stderr)
    else:
        print(stdout) # Print curl's successful output

if __name__ == "__main__":
    main()
