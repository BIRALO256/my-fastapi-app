import tensorflow as tf

# Load the pre-trained model
model = tf.keras.models.load_model('models/v1_model.keras')

# You can define a function to perform inference when you're ready
def get_model():
    return model
