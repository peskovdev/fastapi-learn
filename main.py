from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def get_hello() -> dict[str, str]:
    """
    Description of func: takes 0 params, return json
    """
    return {"hello": "world"}
