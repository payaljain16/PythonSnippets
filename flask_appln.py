from flask import Flask, jsonify,request;

app=Flask(__name__);


@app.route("/", methods=['GET'])
def hello():
    return jsonify({"Greeting":"Hello World"});

@app.route("/", methods=['POST'])
def abc():
    return jsonify({"Finish":"Bye"});

@app.route("/abc/", methods=['GET','POST'])
def xyz():
    if(request.method == 'GET'):
        return jsonify({"Welcome":"Guest!!!"});
    if(request.method == 'POST'):
        return jsonify({"Byeeeee":"Guesttrtttttttttt!!!"});

    
@app.route("/cube/<int:num>",methods=['GET'])
def cube(num):
    return jsonify({'result':num*num*num});
    

if __name__ == '__main__':
    app.run(debug=True);
