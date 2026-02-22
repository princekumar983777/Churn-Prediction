import os
from pathlib import Path

# ==============================
# Project Name
# ==============================
PROJECT_NAME = "churn_prediction"

# ==============================
# Folder Structure
# ==============================
folders = [
    ".github/workflows",
    "artifacts",
    "config",
    "data/raw",
    "data/interim",
    "data/processed",
    "notebooks",
    "src/components",
    "src/pipelines",
    "src/utils",
    "tests"
]

# ==============================
# Files to Create
# ==============================
files = [
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_validation.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipelines/__init__.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/logger.py",
    "src/exception.py",
    "config/config.yaml",
    "config/schema.yaml",
    "tests/__init__.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    "docker-compose.yml",
    ".env",
    ".gitignore",
    "README.md",
    "setup.py"
]

# ==============================
# Create Project
# ==============================
def create_project():
    base_path = Path(PROJECT_NAME)
    base_path.mkdir(exist_ok=True)

    # Create folders
    for folder in folders:
        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)

    # Create files
    for file in files:
        file_path = base_path / file
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if not file_path.exists():
            with open(file_path, "w") as f:
                f.write("")

    print(f"\n✅ Project '{PROJECT_NAME}' created successfully!\n")


if __name__ == "__main__":
    create_project()