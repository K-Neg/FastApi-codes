#https://github.com/encode/starlette/blob/master/starlette/status.py

from fastapi import FastAPI, Response, status

app = FastAPI()

@app.get("/")
def main():
 	return 1

@app.put("/call-response/{number}", status_code=200)
def get_or_create_task(number: int, response: Response):
    
    if number == 1:
    	response.status_code = status.HTTP_201_CREATED
    	status_client = True
    	message = 'your number x4 = ' + str(number*4)
    if number == 2:
    	response.status_code = status.HTTP_404_NOT_FOUND
    	status_client = False
    	message = 'your number x5 = ' + str(number*5)
    if number == 3:
    	response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    	status_client = False
    	message = 'your number x3 = ' + str(number*3)
    
    return {
    	'status': status_client,
    	'data': message
    }

if __name__ == "__main__":
	import uvicorn
	uvicorn.run('__main__:app',reload=True)