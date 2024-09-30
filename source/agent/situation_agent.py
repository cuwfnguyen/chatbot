from ..prompt import situation_prompt
from ..llm_provider.openai_service import OpenAIServices

class SituationAgent:
    def __init__(self, agent_code: int, conversation:list):
        self.agent_code = agent_code
        self.conversation = conversation

    def process_message(self):
        conversation = self.conversation
        agent_code = self.agent_code
        system_prompt = situation_prompt.get_agent_prompt(agent_code)
        conversation.append({
            "role": "system",
            "content": system_prompt[0].get('agent_prompt')
        })
        service = OpenAIServices()
        response = service.situation_agent(conversation, agent_code)
        response_data = {
            "message": response
        }
        if 'TERMINATE' in response:
            response_data["end"] = 't'
        if 'SWITCH_CONTEXT' in response:
            response_data['switch_context'] = 't'
        return response_data

