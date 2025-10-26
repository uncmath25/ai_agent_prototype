import ollama
import streamlit as st


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
            client = ollama.Client(host='host.docker.internal:11434')
            with st.spinner('Consulting ollama...'):
                # response = client.generate(model='gemma3:1b', prompt=prompt)['response']
                response = client.chat(model='gemma3:1b', messages=st.session_state.messages)['message']['content']
                st.markdown(response)
                st.session_state.messages.append({'role': 'assistant', 'content': response})


if __name__ == '__main__':
    main()
