import gradio as gr
import pandas as pd
import numpy as np
import pickle

# Load the pre-trained Random Forest model
with open('rf_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

# Function to make predictions
def predict_future_weight(age, height, current_weight, activity_level, caloric_intake):
    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'age': [age],
        'height': [height],
        'current_weight': [current_weight],
        'activity_level': [activity_level],
        'caloric_intake': [caloric_intake]
    })
    
    # Make a prediction using the loaded model
    future_weight_pred = rf_model.predict(input_data)[0]
    
    return f"Predicted Future Weight: {future_weight_pred:.2f} kg"

# Gradio Interface
iface = gr.Interface(
    fn=predict_future_weight,  # The prediction function
    inputs=[
        gr.Number(label="Age"),                # gr.Number replaces gr.inputs.Number
        gr.Number(label="Height (cm)"),
        gr.Number(label="Current Weight (kg)"),
        gr.Number(label="Activity Level (1-Low, 2-Medium, 3-High)"),
        gr.Number(label="Caloric Intake (kcal/day)")
    ],
    outputs=gr.Textbox(label="Predicted Future Weight"),  # gr.Textbox replaces gr.outputs.Textbox
    title="FitMate: Fitness and Nutrition Tracking",
    description="Enter your age, height, current weight, activity level, and caloric intake to predict your future weight.",
)

# Launch the Gradio interface
iface.launch()
