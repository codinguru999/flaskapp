from flask import Flask,request,json,jsonify
app = Flask(__name__)
dict={}

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/v1/tasks',methods=['POST'])
def add_tasks():
    cont=request.get_json()
    #print(cont)
    if(not dict):
        dict[1]={}
        dict[1]['id']=1
        dict[1]['title']=cont['title']
        dict[1]['is_completed']=False
    else:
        dict[list(dict.keys())[-1]+1]={}
        dict[list(dict.keys())[-1]+1]['id']=list(dict.keys())[-1]+1
        dict[list(dict.keys())[-1]+1]['title']=cont['title']
        dict[list(dict.keys())[-1]+1]['is_completed']=False
    return jsonify(id=list(dict.keys())[-1])
    # return request.json

@app.route('/v1/tasks',methods=['GET'])
def get_tasks():
    task=list(dict.values())
    return jsonify(tasks=task)

@app.route('/v1/tasks/<id>',methods=['GET'])
def get_task(id):
    if id in dict.keys():
        return jsonify(id=id,title=dict[id]['title'],is_completed=dict[id]['is_completed'])
    else:
        t={'error':"There is no task at that id"}
        return jsonify(t)

@app.route('/v1/task/<id>',methods=['DELETE'])
def delete(id):
    if id in dict.keys():
        del dict[id]

@app.route('/v1/tasks/<id>',methods=['PUT'])
def update(id):
    if id in dict.keys():
        cont=request.get_json()
        dict[id]["title"]=cont["title"]
        dict[id]["is_completed"]=cont["is_completed"]

    else:
        return jsonify(error="There is no task at that id")

if __name__ == '__main__':
   app.run(host='localhost',port=5000,debug=True)