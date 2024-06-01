from flask import jsonify
from app import app
from .models import fetch_all_tools, fetch_tools_by_code

@app.route('/tools/', methods=['GET'])
def get_tools():
    tools = fetch_all_tools()
    return jsonify(tools)

@app.route('/tools/<code>/', methods=['GET'])
def get_tool(code):
    tool = fetch_tools_by_code(code)
    return jsonify(tool)

