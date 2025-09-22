# API Performance Predictor
Predicts API latency based on traffic and past logs using Machine Learning, and provides a dashboard for monitoring.


## Features
- Predicts API response latency using a trained regression model
- Accepts traffic rate and endpoint as input
- Returns predicted latency in milliseconds
- Swagger UI for easy API testing

  
## Technologies
- Python, FastAPI, Pandas, scikit-learn
- Joblib for model serialization
- VS Code, Git, GitHub

  
## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/api-performance-predictor.git

2. cd api-performance-predictor
3. python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

#Run the API server
uvicorn api.predict_api:app --reload


---

### **5️⃣ Usage / Example**
```markdown
## Usage
- Open Swagger UI: http://127.0.0.1:8000/docs
- Test API by sending traffic rate and endpoint
- Example response:
```json
{
  "predicted_latency_ms": 292.68
}

