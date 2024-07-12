from langchain.prompts import ChatPromptTemplate
from langchain.chains.conversation.base import ConversationChain
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

from generators.prompts import (SYSTEM_PROMPT,
                                HUMAN_RESPOND_TO_MESSAGE_PROMPT)


def get_response_textual(gpt_model,
                         memory,
                         chat_message_text: str) -> str:

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", HUMAN_RESPOND_TO_MESSAGE_PROMPT)
    ])
    chain = ConversationChain(
        llm=gpt_model,
        memory=memory,
        verbose=True,
        prompt=prompt
    )
        
    output = chain.predict(input=chat_message_text)
    memory.save_context({"input": chat_message_text}, {"output": output})
    return output
