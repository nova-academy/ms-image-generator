"""Importing modules"""
from fastapi import FastAPI

from config.settings import Settings
from schemas.input import InputSchema

settings = Settings()

app = FastAPI()
app.title = settings.app_name
app.version = settings.app_version

# Instantiate a service component to invoke ai model

# END


@app.post('/api/v1/image-generator', tags=['endpoints'])
def generate_image(request_body: InputSchema):
    """Function that receives the prompt and return ai model result"""
    # Implement analize_sentiment function
