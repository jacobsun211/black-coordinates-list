import httpx

# Test POST
resp = httpx.post(
    "http://localhost:8000/add_coord",
    json={"ip": "1.1.1.1", "coord": "32.08,34.77"}
)
print("POST:", resp.json())

# Test GET
resp = httpx.get("http://localhost:8000/get_coord")
print("GET:", resp.json())
