import sys
sys.path.append("D:\\sapo_chatbot\\")
from source.agent import situation_agent

message = [
    {
        "role": "user",
        "content": "Tôi muốn hủy đơn hàng"
    },
    {
        "role": "assistant",
        "content": "Xin chào! Để tôi có thể giúp bạn hủy đơn hàng, bạn vui lòng cung cấp mã đơn hàng của bạn nhé. Cảm ơn bạn!"
    },
    {
        "role": "user",
        "content": "Mã đơn hàng là 23142"
    },
]
agent_code = 21

situation_agent = situation_agent.SituationAgent(agent_code, message)
response = situation_agent.process_message()
print(response)