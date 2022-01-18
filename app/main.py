from fastapi import FastAPI

app = FastAPI(

    title="your title",
    description="Shortened your URL"
)


@app.get("/")
def run(): 
    return {"message": "App is running hehehe"} #hot reload 