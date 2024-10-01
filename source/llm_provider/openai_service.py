import openai
import os
from dotenv import load_dotenv
from pathlib import Path
import json
from . import function_calling

base_dir = Path(__file__).resolve().parent.parent
dotenv_path = base_dir / 'data' / '.env'
load_dotenv(dotenv_path)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class OpenAIServices:
    def __init__(self):
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)


    def situation_agent(self, conversation, agent_code):
        function = function_calling.define_function(agent_code)
        if function:
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
        else:

            response = self.client.chat.completions.create(
                model='gpt-4o-mini',
                messages=conversation
            )
        assistant_message = response.choices[0].message.content
        print(response)
        tool_calls = response.choices[0].message.tool_calls
        if tool_calls:
            for tool_call in tool_calls:
                arguments = json.loads(tool_call.function.arguments)
                function_name = tool_call.function.name
                function_to_call = getattr(function_calling, function_name)
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
