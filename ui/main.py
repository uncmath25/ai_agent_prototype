import streamlit as st

from llm_client import LLMClient


def main():
    st.title('Ollama Chatbot')

    if 'messages' not in st.session_state:
        st.session_state.messages = [{'role': 'assistant', 'content': "Let's start chatting! 👇"}]

    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    if prompt := st.chat_input("What's up?"):
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        with st.chat_message('user'):
            st.markdown(prompt)
        with st.chat_message('assistant'):
            client = LLMClient()
            with st.spinner('Consulting ollama...'):
                response = client.ask(st.session_state.messages)
                st.markdown(response)
                st.session_state.messages.append({'role': 'assistant', 'content': response})


if __name__ == '__main__':
    main()
