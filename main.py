from typing import Union

from fastapi import FastAPI

app = FastAPI()

# region hello world
@app.get("/")
def read_root():
    return {"Hello": "World"}
# endregion

# region Knowledge Base API
@app.post("/NewKB")
def NewKnowledgeBase():
    return {"Hello": "World"}

@app.get("/ListKB")
def ListKnowledgeBase():
    return {"Hello": "World"}

@app.post("/AddToKB")
def AddToKnowledgeBase():
    return {"Hello": "World"}

@app.post("/QueryKB")
def QueryKnowledgeBase():
    return {"Hello": "World"}
# endregion

# region Chat API
@app.post("/ChatWithKB")
def ChatWithKnowledgeBase():
    return {"Hello": "World"}

@app.post("/ChatWithOpenAI")
def ChatWithOpenAI():
    return {"Hello": "World"}

@app.post("/ChatWithGoogleGenAI")
def ChatWithGoogleGenAI():
    return {"Hello": "World"}
# endregion

# region AutoCompleteAPI
@app.post("/AutoComplete")
def AutoComplete():
    return {"Hello": "World"}

@app.post("/AutoCompleteWithKB")
def AutoCompleteWithKB():
    return {"Hello": "World"}
# endregion

