# service-b init 

cd service-b
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

uvicorn app.main:app --reload --port 8080