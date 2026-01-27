# service-b init 

cd service-b
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

uvicorn app.main:app --reload --port 8080



---------------------------------------------
for the test:
#                   ! name of the service you want to expose
oc expose service/service-a


#               ! name of service
oc get route service-a -o jsonpath='{.spec.host}'
