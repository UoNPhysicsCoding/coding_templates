import sys, subprocess, datetime, json, os

def get_code_chars(file_path):
    ext = os.path.splitext(file_path)[1]
    
    try:
        if ext == '.ipynb':
            with open(file_path, 'r', encoding='utf-8') as f:
                nb = json.load(f)
                # Count characters only in 'code' cells
                return sum(len("".join(cell['source'])) for cell in nb.get('cells', []) if cell.get('cell_type') == 'code')
        
        elif ext in ['.py', '.md']:
            with open(file_path, 'r', encoding='utf-8') as f:
                return len(f.read())
        
        else:
            return 0
    except Exception:
        return 0

# Main execution logic
file_path = sys.argv[1]
timestamp = datetime.datetime.now().strftime('%H:%M:%S')
char_count = get_code_chars(file_path)

# Git operations
# We ignore the error if the file has no changes, preventing console noise
subprocess.run(['git', 'add', file_path], capture_output=True)
result = subprocess.run(['git', 'commit', '-m', f'Time: {timestamp} | Chars: {char_count}'], capture_output=True)

# Only push if the commit was successful (i.e., there were actual changes to commit)
if result.returncode == 0:
    subprocess.run(['git', 'push'], capture_output=True)