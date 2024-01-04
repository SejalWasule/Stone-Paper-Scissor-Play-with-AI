# Stone-Paper-Scissor-Play-with-AI object detection

## Overview:
This project implements a Stone Paper Scissors game utilizing AI object detection techniques. It leverages a pre-trained model to detect hand gestures for playing the game against the computer using webcam.

## Features:
Utilizes TensorFlow and OpenCV for object detection and game interaction.
Offers a straightforward interface for playing Stone Paper Scissors against the computer using hand gestures.

## Requirements:
Python 3.x
Git

## Setup Instructions :
1. Clone the repository: `git clone https://github.com/yourusername/stone-paper-scissors-ai.git`
2. Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`
4. Train your custom model using `model_training/notebook_to_train_model.ipynb`.
5. Replace the placeholder `custom_model.h5` in `play.py` and `detect.py` with your trained model.
6. Run the game: `python play.py`

#### Clone Repository:
git clone https://github.com/yourusername/stone-paper-scissors-ai.git
cd stone-paper-scissors-ai

#### Create and Activate Virtual Environment:
python -m venv env

#### Activating the virtual environment (Windows)
env\Scripts\activate

#### Activating the virtual environment (Unix or MacOS)
source env/bin/activate

#### Install Dependencies:
pip install -r requirements.txt

#### Usage Instructions:
Train your custom model using the provided notebook or your own dataset and hyperparameters.
Save the trained model as an .h5 file.
Replace the placeholder .h5 file in play.py and detect.py with your trained model.

#### Run the game:
python play.py
Follow on-screen instructions to play Stone Paper Scissors against the computer using hand gestures.

## Credits:
The notebook to train the model was adapted from trekhleb's machine-learning-experiments.

# Demo 
<img width="605" alt="comp wins" src="https://github.com/SejalWasule/Stone-Paper-Scissor-Play-with-AI/assets/102143995/fae8ec74-a843-4c8d-9c8d-3b952f9c620e">

<img width="598" alt="tie" src="https://github.com/SejalWasule/Stone-Paper-Scissor-Play-with-AI/assets/102143995/3d4e019c-2cdf-4715-8a57-4a8f302abd68">

<img width="607" alt="scissor" src="https://github.com/SejalWasule/Stone-Paper-Scissor-Play-with-AI/assets/102143995/752e5c6b-d2df-481d-aa91-d976b73ada55">

<img width="602" alt="rock" src="https://github.com/SejalWasule/Stone-Paper-Scissor-Play-with-AI/assets/102143995/726e56ec-d443-4b83-97fb-0590b8f1dfb3">

<img width="598" alt="paper" src="https://github.com/SejalWasule/Stone-Paper-Scissor-Play-with-AI/assets/102143995/b973730d-cd95-4b84-aef4-79a2e30df9b0">
