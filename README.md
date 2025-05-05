## sports-person-image-classifier
A machine learning web application that classifies images of sports celebrities. Upload an image, and the model predicts whether it's:

🏏 Virat Kohli

⚽ Lionel Messi

⚽ Cristiano Ronaldo

🏏 Chris Gayle

🏏 Ricky Ponting
## Features
Image Upload: Drag and drop or select an image to classify.

Face Detection: Utilizes Haar cascades to detect faces and eyes.

Feature Extraction: Applies wavelet transforms for enhanced feature representation.

Prediction: Classifies the image using a trained machine learning model.

Result Display: Shows the predicted celebrity name and a reference image.

Error Handling: Provides feedback if no face is detected or an error occurs.
## 🛠️ Installation
 1.clone the repository
```bash
git clone https://github.com/ashish769/sports-person-classifier.git
cd sports-person-classifier
```

 2.Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```
 3.Install Dependencies
```bash
pip install -r requirement.txt
```
# Running the Application
 1.Start the Flask Server
```bash
python server.py
```
2.Access the Web Interface
```bash
Open your web browser and navigate to http://127.0.0.1:5000/
```

## Model Details
Preprocessing: Images are converted to grayscale, and faces with at least two eyes are detected.

Feature Extraction: Combines raw pixel data with wavelet-transformed features.

Model: Trained using Support Vector Machine (SVM) with hyperparameter tuning via GridSearchCV.

Artifacts: The trained model and class dictionary are stored in the artifacts/ directory.

## 🖼️ Sample Output

![Screenshot 2025-05-05 174047](https://github.com/user-attachments/assets/ba9b1cf9-06a1-4385-a71c-e41ccc83dc11)

![Screenshot 2025-05-05 174523](https://github.com/user-attachments/assets/3c0abc25-fdd5-4844-aa59-4be4da44d836)

![Screenshot 2025-05-05 174114](https://github.com/user-attachments/assets/af53dd9c-6f4e-4298-9a3e-fb6804c00a55)
## Troubleshooting
No Face Detected: Ensure the image is clear and the face is unobstructed.

Invalid Image Format: Only standard image formats (e.g., JPG, PNG) are supported.

Server Errors: Check the console for error messages and ensure all dependencies are installed.
