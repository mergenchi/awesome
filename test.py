from flask import Flask, request, jsonify
import requests
import xmltodict

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def parse_xml():
    content_dict = xmltodict.parse(request.data)
    return jsonify(content_dict)

if __name__=='__main__':
    app.run(host="0.0.0.0")