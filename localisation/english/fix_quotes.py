import os
import glob
import codecs

def fix_quotes_in_file(filepath):
    print(f"Fixing quotes in: {os.path.basename(filepath)}")
    
    try:
        with codecs.open(filepath, 'r', encoding='utf-8-sig') as f:
            content = f.read()
    except UnicodeDecodeError:
        with codecs.open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    
    lines = content.split('\n')
    fixed_lines = []
    changes_made = False
    
    for line in lines:
        original_line = line
        
        # Fix single quotes to double quotes for localization entries
        if ':0 ' in line and "'" in line:
            # Replace single quotes with double quotes for the value part
            parts = line.split(':0 ', 1)
            if len(parts) == 2:
                key = parts[0]
                value = parts[1]
                # Replace single quotes with double quotes
                if value.startswith("'") and value.endswith("'"):
                    value = '"' + value[1:-1] + '"'
                    line = key + ':0 ' + value
                    changes_made = True
        
        # Fix any remaining smart quotes
        if '"' in line or '"' in line or '"' in line or '"' in line:
            line = line.replace('"', '"').replace('"', '"').replace('"', "'").replace('"', "'")
            changes_made = True
        
        fixed_lines.append(line)
    
    if changes_made:
        # Create backup
        backup_path = filepath + '.quote_backup'
        if not os.path.exists(backup_path):
            os.rename(filepath, backup_path)
        
        # Save fixed file
        with codecs.open(filepath, 'w', encoding='utf-8-sig') as f:
            f.write('\n'.join(fixed_lines))
        
        print(f"  Fixed quotes and saved")
        return True
    else:
        print(f"  No quote issues found")
        return False

def main():
    print("Fixing Quote Issues in Localization Files")
    print("=" * 50)
    
    yml_files = glob.glob('*.yml')
    if not yml_files:
        print("No .yml files found in current directory!")
        return
    
    total_files = len(yml_files)
    fixed_files = 0
    
    for yml_file in yml_files:
        if fix_quotes_in_file(yml_file):
            fixed_files += 1
        print()
    
    print(f"Summary: {fixed_files}/{total_files} files had quote issues and were fixed")

if __name__ == "__main__":
    main() 