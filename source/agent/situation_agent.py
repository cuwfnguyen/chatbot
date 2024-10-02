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
        additional_info = self.additional_info
        if additional_info.get('product_name') or additional_info.get('order_id'):
            intent_record = situation_prompt.get_agent_prompt(agent_code, True)
            product_data = function_calling.product_information.get(additional_info.get('product_code'))
            order_data = function_calling.order_information.get(additional_info.get('order_id'))
            system_prompt = intent_record[0].get('agent_prompt').replace('<product_description>', str(product_data)).replace('<order_info>', str(order_data))
        else:
            intent_record = situation_prompt.get_agent_prompt(agent_code, False)
            system_prompt = intent_record[0].get('agent_prompt')
        conversation.insert(0, {
            "role": "system",
            "content": system_prompt
        })
        service = OpenAIServices()
        print(conversation)
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
        print(response_data)
        return response_data

