#the Ml codes are in the 'proj' folder
#this python files oly cotains backend router and some function to call the ML codes

import numpy as np
from quart import jsonify, send_from_directory, render_template
from quart import Quart, request, Blueprint
import os
import asyncio
from sklearn.metrics import accuracy_score                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from proj import part1,part2
from quart_cors import cors


app = Quart(__name__, template_folder="./web/dist", static_folder="./web/dist", static_url_path="")

cors(app)

#backend routers
@app.route('/')
async def index():
    return await render_template("index.html")

@app.route('/partone',methods=['POST'])
def partone():
    instance = part1.PartOne()
    result = instance.run()
    return result

@app.route('/parttwo', methods=['POST'])
async def parttwo():
    try:
        iris = load_iris()
        X, y = iris.data, iris.target
        y = np.eye(3)[y]

        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

        
        mlp = part2.CustomMLP([4, 10, 10, 10, 3], activation='relu')

        
        mlp.fit(X_train, y_train, epochs=1000)

        
        predictions = mlp.predict(X_test)
        print(predictions)
        accuracy = accuracy_score(np.argmax(y_test, axis=1), predictions)
        print(accuracy)
        
        items = [{'name': f'Test {i}', 'actual': str(actual), 'predicted': str(pred)} for i, (actual, pred) in enumerate(zip(np.argmax(y_test, axis=1), predictions))]

        
        return jsonify({'status': 'success', 'items': items, 'accuracy': accuracy})
    except Exception as e:
        return jsonify({'status': 'fail', 'message': 'error'})


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(app.run_task(host='0.0.0.0', port=5000))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()