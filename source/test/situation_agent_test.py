import sys
sys.path.append("D:\\SapoChatbot\\chatbot")
from flask import Flask, request, jsonify

app = Flask(__name__)
from source.agent import situation_agent

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    data = request.json.get('data')
    message = data.get('message')
    agent_code = data.get('agent_code')
    additional_info = data.get('additional_info')
    agent = situation_agent.SituationAgent(agent_code, message, additional_info)
    response = agent.process_message()
    return jsonify({'response_data': response})


if __name__ == '__main__':
    app.run(host='localhost', port=8181, debug=True)
