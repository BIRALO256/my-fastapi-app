from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
from app.model import get_model  # Import the model loading function
import base64
from io import BytesIO
from PIL import Image

# Create a FastAPI app instance
app = FastAPI()

# Define the input data model for validation
class InputData(BaseModel):
    data: str  # Example: string input (adjust this to match the model input)

# Preprocess the input data
def preprocess_data(data):
    # Example for base64-encoded image data
    image_data = base64.b64decode(data)
    image = Image.open(BytesIO(image_data))

    # Resize image to match the model input size
    image = image.resize((256, 256))  # Adjust based on your model input shape

    # Convert the image to a numpy array and normalize the pixel values
    processed_data = np.array(image) / 255.0  # Normalization

    return processed_data

# Dummy endpoint for testing purposes
@app.post("/predict")
async def predict(input_data: InputData):
    model = get_model()

    # Preprocess input data (convert base64 to image, resize, normalize, etc.)
    processed_data = preprocess_data(input_data.data)

    # Get prediction from the model
    prediction = model.predict(processed_data[np.newaxis, ...])  # Add batch dimension

    return {"prediction": prediction.tolist(), "input_data": input_data.data}
