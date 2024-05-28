from pydantic_settings import BaseSettings

class CHROMA_SETTINGS(BaseSettings):
  # Define your settings here
  chroma_db_impl: str = 'duckdb+parquet'  # Database implementation
  persist_directory: str = 'db'  # Directory for persistence
  anonymized_telemetry: bool = True  # Enable/disable anonymized telemetry
  chroma_api_impl: str = "chromadb.api.fastapi.FastAPI"