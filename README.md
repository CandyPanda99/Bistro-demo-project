## Setup

### 1. Create & activate a Virtual Environment

Create a virtual environment using the following command:

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install Packages
Install the required packages using the following command:
```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI server with Uvicorn
Run the application with the following command:
```bash
python -m uvicorn main:app --reload
```

### 4. Run the steamlit app
Run the application with the following command:
```bash
streamlit run app.py
```

### 5. Sample questions to ask the bot
```html
Hi, What can you do?
Can you tell me the price of king coconut juice and how much that is in Dollars
Can you show me the desserts menu?
Im a vegan, What dessert options do I have?
Thanx, Id like to make a reservation now.
Lasal Hettiarachchi
One small thing. Do you have orange juice available?
Yes we can complete the reservation. My contact number is 0763672321, 2 guests for tommorow. Lunch
```