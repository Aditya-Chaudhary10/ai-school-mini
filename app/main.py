from fastapi import FastAPI

app=FastAPI(title='Ai School')

@app.get('/health')
def health():
    return {'status':'ok'}