from ..prompt import situation_prompt
from ..llm_provider.openai_service import OpenAIServices
from ..llm_provider import function_calling

class SituationAgent:
    def __init__(self, agent_code: int, conversation:list, additional_info: dict):
        self.agent_code = agent_code
        self.conversation = conversation
        self.additional_info = additional_info

    def process_message(self):
        conversation = self.conversation
        agent_code = self.agent_code

        system_prompt = situation_prompt.get_agent_prompt(agent_code)
        additional_data = function_calling.get_additional_info(agent_code, self.additional_info)

        conversation.insert(0, {
            "role": "system",
            "content": system_prompt[0].get('agent_prompt') + additional_data
        })
        service = OpenAIServices()
        response = service.situation_agent(conversation, agent_code)
        response_data = {
            "message": response,
            "end_situation": "f",
            "switch_context": "f"
        }
        if 'TERMINATE' in response:
            response_data["end_situation"] = 't'
        if 'SWITCH_CONTEXT' in response:
            response_data["end_situation"] = 't'
            response_data['switch_context'] = 't'
        return response_data

