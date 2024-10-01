import sys
sys.path.append("D:\\SapoChatbot\\chatbot")
from source.agent import situation_agent

message = [
    {
        "role": "user",
        "content": "Có ảnh thật của sp ko?"
    }
]
agent_code = 4
additional_info = {
    "product_name": "Máy hút bụi"
}

situation_agent = situation_agent.SituationAgent(agent_code, message, additional_info)
response = situation_agent.process_message()
print(response)