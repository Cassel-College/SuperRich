import uvicorn

if __name__ == "__main__":
    uvicorn.run("superrich.app:app", host="0.0.0.0", port=8880, reload=True)
