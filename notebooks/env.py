import pathlib
from decouple import Config, RepositoryEnv

BASE_DIR = pathlib.Path(__file__).parent.parent
ENV_FILE_PATH = BASE_DIR / ".env"

def get_config():
    return Config(RepositoryEnv(ENV_FILE_PATH)) if ENV_FILE_PATH.exists() else Config()

config = get_config()
