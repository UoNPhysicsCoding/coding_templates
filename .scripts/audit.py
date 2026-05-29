import sys, subprocess, datetime, os

file_path = sys.argv[1]

# 1. Stage the file
subprocess.run(['git', 'add', file_path], capture_output=True)

# 2. Get the diff summary for this file
# --numstat returns: <added> <removed> <filename>
result = subprocess.run(
    ['git', 'diff', '--cached', '--numstat', file_path], 
    capture_output=True, text=True
)

# 3. Parse the output
output = result.stdout.strip().split('\t')
# If the file is new or modified, we get back [added, removed, path]
if len(output) >= 2:
    added = int(output[0])
    removed = int(output[1])
else:
    added = 0
    removed = 0

# 4. Only commit if something changed
if added > 0 or removed > 0:
    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
    
    # We commit with both metrics in the message
    msg = f"Time: {timestamp} | Added: {added} | Removed: {removed}"
    subprocess.run(['git', 'commit', '-m', msg])