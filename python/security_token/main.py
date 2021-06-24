import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, HTMLResponse
from typing import Optional


app = FastAPI()

def filter_keys(key):
    fake_db = ['pin', 'hill', 'blade']

    if key in fake_db:
        return True
    else:
        return False


@app.get("/", response_class=HTMLResponse)
async def main():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/safe", response_class=HTMLResponse)
async def safe(temp_key: str):
    
    if len(list(filter(filter_keys, [temp_key]))):
        html_content = f"""
        <html>
            <h1>your query: {temp_key}</h1>
        </html>
        """
        response = HTMLResponse(content=html_content, status_code=200)
    
    else:
        html_content = f"""
        <html>
            <h1>Wrong place</h1>
        </html>
        """
        response = HTMLResponse(content=html_content, status_code=400)
             
    return  response

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)    