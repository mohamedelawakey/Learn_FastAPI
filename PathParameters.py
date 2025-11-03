from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {
        'data': 'blog_list'
    }


@app.get('/blog/unpublished')
def unpublished():
    return {
        'data': 'all unpublished blogs'
    }


@app.get('/blog/{id_blog}')
def about(id_blog: int):
    return {
        'data': id_blog
    }


@app.get('/blog/{id_blog}/comments')
def comments(id_blog: int):
    return {
        'data': {'1', '2'}
    }
