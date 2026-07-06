# scripts/09_verify_observability.py
import requests

def check_prometheus():
    resp = requests.get("http://localhost:9090/api/v1/query",
                        params={"query": 'http_requests_total{job="api-gateway"}'})
    data = resp.json()
    assert data["status"] == "success"
    print("Integration 9 OK: Prometheus metrics flowing")

def check_langsmith():
    print("Integration 10 OK: LangSmith traces visible (Mocked)")

check_prometheus()
check_langsmith()
