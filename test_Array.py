import subprocess
import sys
import os

def test_array_script_output():
    # Path to array.py
    script = os.path.join(os.getcwd(), "array.py")

    # Run the script with arguments: "10 20 30"
    result = subprocess.run(
        [sys.executable, script, "10 20 30"],
        capture_output=True,
        text=True
    )

    # Expected output lines
    the_lines = [
        "Scores: [10, 20, 30]",
        "Sum: 60",
        "Average: 20.0",
        "Maximum: 30",
        "Minimum: 10"
    ]

    # Check if each expected line is in the actual output
    for line in the_lines:
        assert line in result.stdout