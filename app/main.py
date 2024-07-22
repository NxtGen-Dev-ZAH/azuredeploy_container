from fastapi import FastAPI


app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": {"Abdur rahim":"17 year old idiot "},
            "Education":"high school"}
