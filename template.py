import os
from pathlib import Path


list_of_files = [
   ".github/workflows",
   "src/__init__.py",
   "src/components/data_ingestion.py",
   "src/components/data_transformation.py", 
   "src/components/model_trainer.py",
   "src/components/model_evaluation.py",
   "src/exceptions/__init__.py",
   "src/exceptions/exception.py",
   "src/logger/__init_.py",
   "src/logger/logging.py",
   "src/utils/__init__.py",
   "src/utils/utils.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/unit.py",
   "tests/integration/__init__.py",
   "tests/integration/int.py",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file