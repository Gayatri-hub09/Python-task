import os
import shutil

# Function to organize files
def organize_files(source_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        return
    
    # Create subdirectories for each file type
    file_types = {
        'Documents': ['.txt', '.pdf', '.docx', '.xlsx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Audio': ['.mp3', '.wav', '.flac'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Archives': ['.zip', '.tar', '.gz'],
    }

    # Iterate through each file in the source folder
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get file extension
        file_extension = os.path.splitext(file_name)[1].lower()
        
        # Check for the file type and move it to the appropriate directory
        moved = False
        for category, extensions in file_types.items():
            if file_extension in extensions:
                category_folder = os.path.join(source_folder, category)
                
                # Create category folder if it doesn't exist
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                
                # Move the file
                destination = os.path.join(category_folder, file_name)
                shutil.move(file_path, destination)
                print(f"Moved: {file_name} -> {category}")
                moved = True
                break
        
        # If no category matched, print a message
        if not moved:
            print(f"Skipped (unknown type): {file_name}")

# Example usage
source_folder = 'path/to/your/folder'  # Replace with the actual folder path
organize_files(source_folder)

