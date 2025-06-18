#!/usr/bin/env python3
import os
import glob

def fix_localization_file(file_path):
    """Fix the YAML structure of a localization file."""
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        
        # Check if the file already has the proper structure
        if content.strip().startswith('l_english:'):
            print(f"✓ {os.path.basename(file_path)} - Already has proper structure")
            return
        
        # Add the proper YAML structure
        fixed_content = 'l_english:\n' + content
        
        # Write back with UTF-8 BOM
        with open(file_path, 'w', encoding='utf-8-sig') as f:
            f.write(fixed_content)
        
        print(f"✓ {os.path.basename(file_path)} - Fixed")
        
    except Exception as e:
        print(f"✗ {os.path.basename(file_path)} - Error: {e}")

def main():
    """Fix all localization files in the english directory."""
    localization_dir = "localisation/english"
    
    if not os.path.exists(localization_dir):
        print(f"Directory {localization_dir} not found!")
        return
    
    # Get all .yml files
    yml_files = glob.glob(os.path.join(localization_dir, "*.yml"))
    
    if not yml_files:
        print("No .yml files found!")
        return
    
    print(f"Found {len(yml_files)} localization files to check...")
    print()
    
    for file_path in yml_files:
        fix_localization_file(file_path)
    
    print()
    print("Localization file structure fix complete!")

if __name__ == "__main__":
    main() 