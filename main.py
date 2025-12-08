import os
from openai import AzureOpenAI
import openai


client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2025-01-01-preview",
    azure_endpoint = os.getenv("AZURE_ENDPOINT"),
)

def init_openai():
    '''
    用于设置OpenAI的代理等信息，代理端口需要查询自己的代理软件设置。
    :return:
    '''
    openai.proxy = 'http://127.0.0.1:10809'
    openai.api_type = "openai"


def send_input_to_llm(llm_input):
    deployment_name = "o1"  # 在 Azure OpenAI Studio 里创建的模型名称
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. I will send you a list of conversation history, please continue the conversation."},
            {"role": "user", "content": f"{llm_input}"},
        ],
        # max_tokens=1000
    )

    response = response.choices[0].message.content
    print(response)
    return response


if __name__ == '__main__':
    init_openai()
    send_input_to_llm("hello")