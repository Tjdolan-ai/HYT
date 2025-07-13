"""
Filesystem Management Module

This module provides utilities for organizing and managing files and directories
in a project structure. It includes functions for creating directories, listing
files, moving files, and organizing files by their extensions.
"""

import os
import shutil
from pathlib import Path
from typing import List, Optional


def create_directory(path: str) -> bool:
    """
    Creates a directory if it doesn't already exist.
    
    Args:
        path (str): The path to the directory to create
        
    Returns:
        bool: True if directory was created or already exists, False if creation failed
        
    Example:
        >>> create_directory("my_project/documents")
        True
    """
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        return True
    except (OSError, PermissionError) as e:
        print(f"Error creating directory '{path}': {e}")
        return False


def list_files(path: str) -> List[str]:
    """
    Returns a list of files in a given directory.
    
    Args:
        path (str): The path to the directory to list files from
        
    Returns:
        List[str]: A list of filenames in the directory. Returns empty list if 
                   directory doesn't exist or is inaccessible
                   
    Example:
        >>> list_files("my_project/documents")
        ['readme.txt', 'config.json', 'data.csv']
    """
    try:
        directory_path = Path(path)
        if not directory_path.exists():
            print(f"Directory '{path}' does not exist")
            return []
        
        if not directory_path.is_dir():
            print(f"'{path}' is not a directory")
            return []
            
        # List only files, not directories
        files = [f.name for f in directory_path.iterdir() if f.is_file()]
        return sorted(files)
        
    except (OSError, PermissionError) as e:
        print(f"Error listing files in '{path}': {e}")
        return []


def move_file(source_path: str, destination_path: str) -> bool:
    """
    Moves a file from a source location to a destination location.
    
    Args:
        source_path (str): The path to the source file
        destination_path (str): The path to the destination (can be a directory or file path)
        
    Returns:
        bool: True if file was moved successfully, False otherwise
        
    Example:
        >>> move_file("documents/old_file.txt", "archive/old_file.txt")
        True
        >>> move_file("temp.log", "logs/")
        True
    """
    try:
        source = Path(source_path)
        destination = Path(destination_path)
        
        # Check if source file exists
        if not source.exists():
            print(f"Source file '{source_path}' does not exist")
            return False
            
        if not source.is_file():
            print(f"'{source_path}' is not a file")
            return False
        
        # If destination is a directory, keep the original filename
        if destination.is_dir():
            destination = destination / source.name
        else:
            # Create parent directories if they don't exist
            destination.parent.mkdir(parents=True, exist_ok=True)
        
        # Move the file
        shutil.move(str(source), str(destination))
        return True
        
    except (OSError, PermissionError, shutil.Error) as e:
        print(f"Error moving file from '{source_path}' to '{destination_path}': {e}")
        return False


def organize_files_by_extension(source_dir: str) -> bool:
    """
    Organizes files in a directory into subdirectories named after their file extensions.
    
    This function creates subdirectories for each file extension found in the source
    directory and moves files into their respective extension folders. Files without
    extensions are moved to a 'no_extension' folder.
    
    Args:
        source_dir (str): The path to the directory containing files to organize
        
    Returns:
        bool: True if organization completed successfully, False if there were errors
        
    Example:
        Before organizing:
        my_files/
        ├── document.txt
        ├── image.png
        ├── data.csv
        └── script.py
        
        After calling organize_files_by_extension("my_files"):
        my_files/
        ├── txt/
        │   └── document.txt
        ├── png/
        │   └── image.png
        ├── csv/
        │   └── data.csv
        └── py/
            └── script.py
    """
    try:
        source_path = Path(source_dir)
        
        if not source_path.exists():
            print(f"Source directory '{source_dir}' does not exist")
            return False
            
        if not source_path.is_dir():
            print(f"'{source_dir}' is not a directory")
            return False
        
        # Get all files in the source directory (not subdirectories)
        files = [f for f in source_path.iterdir() if f.is_file()]
        
        if not files:
            print(f"No files found in '{source_dir}' to organize")
            return True
        
        success_count = 0
        total_files = len(files)
        
        for file_path in files:
            try:
                # Get file extension (without the dot)
                extension = file_path.suffix.lower().lstrip('.')
                
                # Use 'no_extension' folder for files without extensions
                if not extension:
                    extension = 'no_extension'
                
                # Create extension directory if it doesn't exist
                ext_dir = source_path / extension
                ext_dir.mkdir(exist_ok=True)
                
                # Move file to extension directory
                destination = ext_dir / file_path.name
                
                # Handle potential naming conflicts
                counter = 1
                original_destination = destination
                while destination.exists():
                    stem = original_destination.stem
                    suffix = original_destination.suffix
                    destination = ext_dir / f"{stem}_{counter}{suffix}"
                    counter += 1
                
                shutil.move(str(file_path), str(destination))
                success_count += 1
                
            except (OSError, PermissionError, shutil.Error) as e:
                print(f"Error organizing file '{file_path.name}': {e}")
                continue
        
        print(f"Successfully organized {success_count} out of {total_files} files")
        return success_count == total_files
        
    except Exception as e:
        print(f"Error organizing files in '{source_dir}': {e}")
        return False


if __name__ == "__main__":
    # Example usage and basic testing
    print("Filesystem Manager - Example Usage")
    print("=" * 40)
    
    # Test create_directory
    print("\n1. Testing create_directory:")
    test_dir = "/tmp/test_filesystem"
    result = create_directory(test_dir)
    print(f"Created directory '{test_dir}': {result}")
    
    # Test list_files on empty directory
    print("\n2. Testing list_files on empty directory:")
    files = list_files(test_dir)
    print(f"Files in '{test_dir}': {files}")
    
    # Create some test files
    print("\n3. Creating test files:")
    test_files = [
        "document.txt",
        "image.png", 
        "data.csv",
        "script.py",
        "readme"  # file without extension
    ]
    
    for filename in test_files:
        file_path = Path(test_dir) / filename
        file_path.write_text(f"This is {filename}")
        print(f"Created test file: {filename}")
    
    # Test list_files with files
    print("\n4. Testing list_files with files:")
    files = list_files(test_dir)
    print(f"Files in '{test_dir}': {files}")
    
    # Test organize_files_by_extension
    print("\n5. Testing organize_files_by_extension:")
    result = organize_files_by_extension(test_dir)
    print(f"Organization result: {result}")
    
    # List the organized structure
    print("\n6. Directory structure after organization:")
    for item in sorted(Path(test_dir).rglob("*")):
        if item.is_file():
            relative_path = item.relative_to(test_dir)
            print(f"  {relative_path}")