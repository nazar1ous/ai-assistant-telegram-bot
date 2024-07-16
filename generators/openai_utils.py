from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

output_parser = StrOutputParser()


from config import credentials, settings
from generators.prompts import (SYSTEM_PROMPT,
                                CONTEXTUALIZE_Q_SYSTEM_PROMPT)

llm = ChatOpenAI(
    openai_api_key=credentials["openai_api_key"],
    max_retries=settings["max_retries"],
    temperature=settings["chatgpt_temperature"],
    model=settings["chatgpt_model"],
    max_tokens=settings["gpt_4_model_max_tokens"],
    n=1,
    timeout=settings["openai_timeout"],
    seed=settings["seed"]
)


### Statefully manage chat history ###
store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


def get_response_textual(session_id: str,
                         chat_message_text: str) -> str:
    
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", CONTEXTUALIZE_Q_SYSTEM_PROMPT),
            MessagesPlaceholder("history"),
            ("human", "{input}"),
        ]
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{input}")
    ])
    contextualize_chain = contextualize_q_prompt | llm | StrOutputParser()
    main_chain = {"input": contextualize_chain} | prompt | llm

    conversational_chain = RunnableWithMessageHistory(
        main_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )
    return conversational_chain.invoke(
        {"input": chat_message_text},
        config={
            "configurable": {"session_id": session_id}
        },  # constructs a key "abc123" in `store`.
    ).content


if __name__ == "__main__":
    print(get_response_textual(llm, "1", "Го в дотар"))
