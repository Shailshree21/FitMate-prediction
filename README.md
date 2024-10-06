FitMate: Fitness and Nutrition Tracking
FitMate is a web-based application designed to predict future weight based on user-input fitness data. Using a Random Forest model trained on synthetic fitness data, FitMate provides personalized insights into how various factors such as age, height, current weight, activity level, and caloric intake can influence future weight.

Features
Predict future weight using a trained Random Forest model.
User-friendly web interface created with Gradio.
Input fields for age, height, current weight, activity level, and caloric intake.
Instant feedback on predicted future weight.
Getting Started
Prerequisites
To run this project, you need to have the following installed:

Python 3.x
Pip (Python package installer)
Installation

1. Clone the repository:
   ![image](https://github.com/user-attachments/assets/77247584-07c9-45bb-b496-f593de4114d0)


2. Install the required packages:
   ![image](https://github.com/user-attachments/assets/0543b811-e005-42e6-9a9f-e51d4bf7741c)

   ![image](https://github.com/user-attachments/assets/f2e8b586-d2ce-47a6-8ffe-69eb1ed5b1a7)

3.  Download or create the rf_model.pkl file containing the pre-trained Random Forest model and place it in the project directory
   1. Run the Gradio interface:
      
    ![image](https://github.com/user-attachments/assets/2aa82fe0-9d0a-4753-be44-2149dbae6175)


    Ensure that you replace app.py with the name of the file containing the Gradio code.

4. Open your web browser and navigate to the URL provided in the terminal (usually http://localhost:7860).

5. Enter your details (age, height, current weight, activity level, caloric intake) into the input fields.

6. Click the "Submit" button to see your predicted future weight.
