import streamlit as st
import os
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

st.title("Chat with Groq!")
st.write("Hello! I'm your friendly Groq chatbot. I can help answer your questions, provide information, or just chat. I'm also super fast! Let's start our conversation!")

conversational_memory_length = 10

memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

user_question = st.text_input("Ask a question:")

if 'chat_history' not in st.session_state:
        st.session_state.chat_history=[]
else:
        for message in st.session_state.chat_history:
            memory.save_context(
                {'input':message['human']},
                {'output':message['AI']}
                )


    # Initialize Groq Langchain chat object and conversation
groq_chat = ChatGroq(
            groq_api_key=os.environ.get("GROQ_API_KEY"), 
            model_name="llama3-8b-8192"
    )
conversation = ConversationChain(
          llm=groq_chat,
          memory=memory
    )

user_question = st.text_input("Ask a question:")

if user_question:
 response = conversation.predict(human_input=user_question)
 message = {'human':user_question,'AI':response}
 st.session_state.chat_history.append(message)
 st.write("Chatbot:", response)