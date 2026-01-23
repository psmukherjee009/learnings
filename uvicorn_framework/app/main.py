import os
import sys

import uvicorn

reload = os.getenv("RELOAD", "false").lower() == "true" # Set to true to enable auto-reload

# Run from CLAE/apps/prompt_validator_backend
if __name__ == "__main__":
    uvicorn.run("app.asgi:app", host="127.0.0.1", port=7860, reload=reload)
