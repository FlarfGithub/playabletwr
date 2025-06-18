import os
import glob
import codecs

print("Script is running")

def fix_localisation_file(filepath):
    changed = False
    with codecs.open(filepath, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()

    fixed_lines = []
    for line in lines:
        # Only process lines with :0 " and not ending with a quote
        if ':0 "' in line:
            idx = line.find(':0 "')
            # Only check if the line after the opening quote does not end with a quote
            if idx != -1 and not line.rstrip().endswith('"'):
                # Add a closing quote at the end of the line
                line = line.rstrip('\n\r') + '"\n'
                changed = True
        fixed_lines.append(line)

    if changed:
        # Backup original
        os.rename(filepath, filepath + '.bak')
        # Write as UTF-8 with BOM
        with codecs.open(filepath, 'w', encoding='utf-8-sig') as f:
            f.writelines(fixed_lines)
        print(f"Fixed and saved: {filepath}")
    else:
        print(f"No changes needed: {filepath}")

def main():
    yml_files = glob.glob('*.yml')
    for yml_file in yml_files:
        fix_localisation_file(yml_file)

if __name__ == "__main__":
    main()