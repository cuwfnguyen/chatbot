import openai
import os
from dotenv import load_dotenv
from pathlib import Path
import json

base_dir = Path(__file__).resolve().parent.parent
dotenv_path = base_dir / 'data' / '.env'
load_dotenv(dotenv_path)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def cancel_order(order_id):
    return f"Đơn hàng {order_id} của bạn không thể hủy do đang vận chuyển"

def define_function(agent_code):
    function = {
            "name": "cancel_order",
            "description": "Hủy đơn hàng",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "Mã đơn hàng"
                    }
                },
                "required": ["order_id"]
            }
        }
    return function

class OpenAIServices:
    def __init__(self):
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)


    def situation_agent(self, conversation, agent_code):
        function = define_function(agent_code)
        tools = [
            {
                "type": "function",
                "function": function
            }]
        response = self.client.chat.completions.create(
            model='gpt-4o-mini',
            messages=conversation,
            tools=tools
        )
        print(conversation)
        assistant_message = response.choices[0].message.content
        tool_calls = response.choices[0].message.tool_calls
        if tool_calls:
            for tool_call in tool_calls:
                arguments = json.loads(tool_call.function.arguments)
                function_name = tool_call.function.name
                function_to_call = globals()[function_name]
                result = function_to_call(**arguments)
                tool = self.function_calling_response_message(tool_call.id, result)
                conversation.append(response.choices[0].message)
                conversation.append(tool)
            print(conversation)
            response_with_function_calling = self.client.chat.completions.create(
                model='gpt-4o-mini',
                messages=conversation,
            )
            assistant_message = response_with_function_calling.choices[0].message.content
        conversation.append({"role": "assistant", "content": assistant_message})
        return assistant_message

    def function_calling_response_message(self, tool_call_id, result):
        function_call_result_message = {
            "role": "tool",
            "content": json.dumps(result),
            "tool_call_id": tool_call_id
        }
        return function_call_result_message
