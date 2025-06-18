import os
import glob
import codecs
import re

def check_and_fix_file(filepath):
    print(f"Checking: {os.path.basename(filepath)}")
    issues_found = []
    
    try:
        # Try to read with UTF-8 BOM first
        with codecs.open(filepath, 'r', encoding='utf-8-sig') as f:
            content = f.read()
            encoding_used = 'utf-8-sig'
    except UnicodeDecodeError:
        try:
            # Try regular UTF-8
            with codecs.open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                encoding_used = 'utf-8'
        except UnicodeDecodeError:
            # Try with error handling
            with codecs.open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                encoding_used = 'utf-8 (with errors)'
                issues_found.append("File has encoding issues")
    
    lines = content.split('\n')
    fixed_lines = []
    line_number = 0
    
    for line in lines:
        line_number += 1
        
        # Check for missing closing quotes
        if ':0 "' in line and not line.rstrip().endswith('"'):
            issues_found.append(f"Line {line_number}: Missing closing quote")
            line = line.rstrip() + '"'
        
        # Check for smart quotes (curly quotes)
        if '"' in line or '"' in line or '"' in line or '"' in line:
            issues_found.append(f"Line {line_number}: Contains smart quotes")
            line = line.replace('"', '"').replace('"', '"').replace('"', "'").replace('"', "'")
        
        # Check for illegal characters (outside ASCII range except common accented characters)
        illegal_chars = []
        for char in line:
            if ord(char) > 127 and char not in 'éèêëàáâäïîìíóòôöùûüúñçßåæø':
                illegal_chars.append(char)
        if illegal_chars:
            issues_found.append(f"Line {line_number}: Contains illegal characters: {illegal_chars}")
        
        # Check for empty lines with just spaces
        if line.strip() == '' and line != '':
            issues_found.append(f"Line {line_number}: Contains only whitespace")
            line = ''
        
        fixed_lines.append(line)
    
    # Check if file needs to be saved as UTF-8 BOM
    if encoding_used != 'utf-8-sig':
        issues_found.append("File not saved as UTF-8 with BOM")
    
    if issues_found:
        print(f"  Issues found: {len(issues_found)}")
        for issue in issues_found:
            print(f"    - {issue}")
        
        # Create backup
        backup_path = filepath + '.bak'
        if not os.path.exists(backup_path):
            os.rename(filepath, backup_path)
        
        # Save fixed file as UTF-8 BOM
        with codecs.open(filepath, 'w', encoding='utf-8-sig') as f:
            f.write('\n'.join(fixed_lines))
        
        print(f"  Fixed and saved as UTF-8 BOM")
        return True
    else:
        print(f"  No issues found")
        return False

def main():
    print("Comprehensive Localization File Checker")
    print("=" * 50)
    
    yml_files = glob.glob('*.yml')
    if not yml_files:
        print("No .yml files found in current directory!")
        return
    
    total_files = len(yml_files)
    fixed_files = 0
    
    for yml_file in yml_files:
        if check_and_fix_file(yml_file):
            fixed_files += 1
        print()
    
    print(f"Summary: {fixed_files}/{total_files} files had issues and were fixed")

if __name__ == "__main__":
    main() 