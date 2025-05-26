#!/usr/bin/env python3

import os
import zipfile
import pathspec
import datetime
from pathlib import Path
import sys

def get_current_user():
    """Get current user name safely."""
    try:
        return os.getenv('USER') or os.getlogin() or 'unknown_user'
    except Exception:
        return 'unknown_user'

def read_gitignore(gitignore_path):
    """Read and parse .gitignore file."""
    if not os.path.exists(gitignore_path):
        print("\n⚠️  WARNING: No .gitignore file found!")
        print("This might result in including unnecessary files like:")
        print("  - node_modules/")
        print("  - __pycache__/")
        print("  - .env files")
        print("  - IDE configuration files")
        print("  - Build directories")
        print("\nDo you want to continue without .gitignore? [y/N]: ", end='')
        response = input().lower()
        if response != 'y':
            print("Aborting. Please create a .gitignore file and try again.")
            sys.exit(1)
        return pathspec.PathSpec([])
    
    with open(gitignore_path, 'r') as f:
        gitignore_content = f.read()
    
    # Parse gitignore patterns
    spec = pathspec.PathSpec.from_lines(
        pathspec.patterns.GitWildMatchPattern,
        gitignore_content.splitlines()
    )
    return spec

def should_include_file(path, gitignore_spec):
    """Check if a file should be included based on gitignore rules."""
    try:
        # Convert to relative path more reliably
        abs_path = os.path.abspath(path)
        base_path = os.path.abspath('.')
        rel_path = os.path.relpath(abs_path, base_path)
        
        # Default patterns to exclude even without .gitignore
        default_excludes = [
            '__pycache__',
            'node_modules',
            '.env',
            '.git',
            '.idea',
            '.vscode',
            'venv',
            'env',
            'dist',
            'build',
            '*.pyc',
            '*.pyo',
            '*.pyd',
            '.DS_Store'
        ]
        
        # Check against default excludes
        for pattern in default_excludes:
            if pattern in rel_path:
                return False
        
        # Check if file matches any gitignore pattern
        return not gitignore_spec.match_file(rel_path)
    except Exception as e:
        print(f"Warning: Error processing path {path}: {e}")
        return False

def create_submission_zip(output_zip_name='submission.zip'):
    """Create a zip file containing all project files while respecting .gitignore."""
    # Read .gitignore
    gitignore_spec = read_gitignore('.gitignore')
    
    # Get current date and user for zip file
    current_date = datetime.datetime.now().strftime('%Y%m%d')
    current_user = get_current_user()
    zip_filename = f'{current_user}_{current_date}.zip'
    
    print(f"\nCreating submission zip: {zip_filename}")
    
    included_files = []
    total_size = 0
    
    # Create zip file
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk('.'):
            # Skip .git directory
            if '.git' in root:
                continue
                
            # Process each file
            for file in files:
                file_path = os.path.join(root, file)
                
                # Skip the zip file itself
                if file_path == f'./{zip_filename}':
                    continue
                
                # Check if file should be included
                if should_include_file(file_path, gitignore_spec):
                    try:
                        # Get file's timestamp and size
                        file_stat = os.stat(file_path)
                        file_size = file_stat.st_size / (1024 * 1024)  # Convert to MB
                        total_size += file_size
                        
                        # Get relative path for zip
                        rel_path = os.path.relpath(file_path, '.')
                        
                        # Create ZipInfo object to preserve timestamp
                        zinfo = zipfile.ZipInfo(
                            rel_path,
                            datetime.datetime.fromtimestamp(file_stat.st_mtime).timetuple()
                        )
                        
                        # Copy file contents and metadata
                        with open(file_path, 'rb') as f:
                            zipf.writestr(zinfo, f.read())
                        
                        included_files.append(f"{rel_path} ({file_size:.2f} MB)")
                    except Exception as e:
                        print(f"Warning: Error processing file {file_path}: {e}")
                        continue

    print("\nFiles included in the submission:")
    for file in included_files:
        print(f"✓ {file}")
    
    print(f"\nSubmission zip created successfully: {zip_filename}")
    print(f"Total Size: {total_size:.2f} MB")
    
    if total_size > 100:  # Warning if zip is larger than 100MB
        print("\n⚠️  WARNING: The zip file is quite large! Please verify its contents")
        print("    and make sure no unnecessary files were included.")

if __name__ == '__main__':
    create_submission_zip() 