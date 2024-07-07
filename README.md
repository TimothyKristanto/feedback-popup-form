# feedback-popup-form

## Installation
### IMPORTANT NOTE: You must use either Anaconda or Python Virtual Environment
### IMPORTANT NOTE: If you use Python Virtual Environment, you can use it inside the server folder

1. Go to your terminal or command prompt
2. Go to your root directory of this project
3. In your terminal, please type the commands below in order: 
    - `cd app/feedback-form`
    - `npm install`
    - `npm install bootstrap bootstrap-vue`
    - `npm install vue-resource`
4. Go back to the root directory using `cd ../..` and type the below commands in your terminal:
    - `cd server`
    - `pip install -r requirements.txt`

## Running the application
1. Go to your terminal or command prompt
2. Go to your root directory of this project
3. In your terminal, please type the commands below in order: 
    - `cd app/feedback-form`
    - `npm run dev`
4. Open the link specified in your terminal
5. Make a new terminal tab and type the commands below in order:
    - `cd server`
    - `uvicorn main:app --reload`
6. Open the link specified in your new terminal tab

## Testing the API endpoints
1. Go to your terminal or command prompt
2. Go to your root directory of this project
3. In your terminal, please type the commands below in order: 
    - `cd server`
    - `pytest test_main.py`
4. Follow the instruction inside `test_main.py` to prevent any complications while testing