from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

import random

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    
    return {"result" : omikuji_list[random.randrange(10)]}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>クラウド開発1+Python+FastAPI</h1>
            <h2> 提出課題</h2>
            <h2>提出締め切り 6/18(木) 23:59まで</h2>
            <h2>プログラミング課題9-1,9-2</h2>
            <h3>課題9-1</h3>
            <p>課題: https://{自分のURL}/indexにアクセスするとWebページが表示されるようにせよ。さらに、HTMLの内容を好きなように書き換えよ。</p>
            <h3>課題9-2</h3>
            <p>課題:オリジナルのPOSTメソッドを作成せよ。結果をdocsで確認せよ。</p>
            
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/class")
async def class_n(className):
    return {"response": f"サーバです。次の授業は{className}ですね! がんばりましょう！"}  # f文字列というPythonの機能を使っている