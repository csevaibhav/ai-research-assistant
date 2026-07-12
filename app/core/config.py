from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "AI Research Assistant"
    APP_VERSION: str = "1.0.0"

    LLM_PROVIDER: str = "gemini"

    GEMINI_API_KEY: str

    GEMINI_MODEL: str = "models/gemini-3.5-flash"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()