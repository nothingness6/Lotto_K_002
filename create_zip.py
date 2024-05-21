import os
import zipfile

# Define the folder structure
folder_structure = {
    "Lotto_002": {
        "main.py": "",
        "data": {
            "__init__.py": "",
            "data_collector.py": "",
            "data_analyzer.py": "",
            "data_storage.py": "",
        },
        "ui": {
            "__init__.py": "",
            "main_screen.py": "",
            "number_generator_screen.py": "",
            "number_selector_screen.py": "",
            "results_screen.py": "",
            "components": {
                "__init__.py": "",
                "animated_number_display.py": "",
                "custom_buttons.py": "",
            },
        },
        "models": {
            "__init__.py": "",
            "number_generator.py": "",
            "user_settings.py": "",
        },
        "utils": {
            "__init__.py": "",
            "helpers.py": "",
            "validators.py": "",
        },
        "assets": {
            "images": {},
            "fonts": {},
            "sounds": {},
        },
        "tests": {
            "__init__.py": "",
            "test_data_collector.py": "",
            "test_number_generator.py": "",
            "test_ui_components.py": "",
        },
    }
}

# Function to create folder structure
def create_folders(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_folders(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

# Base path
base_path = "Lotto_002"

# Create the folder structure
create_folders(".", folder_structure)

# Zip the folder
zip_filename = "Lotto_002.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, dirs, files in os.walk(base_path):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), base_path))

print(f"{zip_filename} created successfully.")
