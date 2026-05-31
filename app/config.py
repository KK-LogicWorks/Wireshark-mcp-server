from pathlib import Path

from pydantic_settings import BaseSettings # type: ignore


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    # Tshark executable
    TSHARK_PATH: str = r"C:\Program Files\Wireshark\tshark.exe"

    # Timeouts
    MAX_TIMEOUT: int = 30

    # Packet limits
    MAX_PACKETS: int = 10000

    # HTTP transport
    HTTP_HOST: str = "127.0.0.1"

    HTTP_PORT: int = 8080

    # Capture storage
    CAPTURE_DIR: str = str(BASE_DIR / "captures")

    # Logs storage
    LOG_DIR: str = str(BASE_DIR / "logs")

    # Default live capture duration
    DEFAULT_CAPTURE_DURATION: int = 10

    class Config:
        env_file = ".env"


settings = Settings()


# Auto-create directories
Path(settings.CAPTURE_DIR).mkdir(
    parents=True,
    exist_ok=True
)

Path(settings.LOG_DIR).mkdir(
    parents=True,
    exist_ok=True
)