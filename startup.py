from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def is_armstrong(num: int) -> bool:
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num

@app.get("/is_armstrong/{number}")
def check_armstrong(number: int):
    result = is_armstrong(number)
    return {
        "number": number,
        "is_armstrong": result,
        "message": f"{number} is an Armstrong number" if result else f"{number} is not an Armstrong number"
    }
if __name__=='__main__':
    app.run()