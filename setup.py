# -- SETUP FILE FOR SECRETS AND CONFIG --
import shutil
from pathlib import Path

# If .env file does not exist, create one based on example
if not Path(".env").exists():
    shutil.copy(".env.example", ".env")
    print("Created .env file. Please fill in secrets.")

# If .json file does not exist, create one based on example
if not Path("config.json").exists():
    shutil.copy("config.example.json", "config.json")
    print("Created config.json. Please fill in configuration.")