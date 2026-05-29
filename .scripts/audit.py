import sys, subprocess, os

file_path = sys.argv[1]

# 1. Stage the file (this makes the file available for 'git diff')
subprocess.run(['git', 'add', file_path], capture_output=True)

# 2. Get the diff summary for this specific file
# --numstat outputs: <added_lines> <deleted_lines> <filename>
result = subprocess.run(
    ['git', 'diff', '--cached', '--numstat', file_path], 
    capture_output=True, text=True
)

# 3. Parse the output (e.g., "50 10 path/to/file.py")
output = result.stdout.strip().split('\t')
added = int(output[0]) if len(output) > 2 else 0

# 4. Only commit if lines were actually added
if added > 0:
    import datetime
    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
    
    # We commit with the 'added' count in the message
    subprocess.run(['git', 'commit', '-m', f'Time: {timestamp} | LinesAdded: {added}'])