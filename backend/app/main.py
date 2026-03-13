from fastapi import FastAPI

app = FastAPI(title="SaaS Monitoring Platform")

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

