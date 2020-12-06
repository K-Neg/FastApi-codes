import uvicorn

if __name__ == "__main__":
    uvicorn.run("source.server:app",port=80,host="0.0.0.0",reload=True,log_level='info')