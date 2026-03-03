import zipfile
from pathlib import Path

# 1. Define the root directory containing your year folders (2019-2025)
# Update 'path/to/your/dataset' to the actual path on your machine
base_dir = Path(r'E:\NYISO_Project\dataset') 

# 2. Find all .zip files recursively within the base directory
zip_files = list(base_dir.rglob('*.zip'))
print(f"Found {len(zip_files)} zip files. Starting extraction...")

# 3. Loop through each zip file and extract it
for zip_path in zip_files:
    # Optional: Create a specific folder for the extracted files to keep things neat.
    # This creates a folder with the exact name of the zip file (without the .zip extension)
    # right next to the original zip file inside the year folder.
    extract_dir = zip_path.parent / zip_path.stem
    extract_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Extracting: {zip_path.name} -> {extract_dir}")
    
    # Open and extract the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

print("\nAll data extracted successfully!")