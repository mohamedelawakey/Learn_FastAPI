from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {
        'data': {
            'name': 'Mohamed'
        }
    }

@app.get('/about')
def about():
    return {
        'data': {
            'name': 'about',
            'page': 'about page'
        }
    }
