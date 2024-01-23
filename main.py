import streamlit as st
from helper import get_qa_chain, create_vector_db


# Function to get the chatbot response
def get_bot_response(user_input):
    chain = get_qa_chain()
    response = chain(user_input)
    return response

# Streamlit UI
def main():
    st.title("Travel Chatbot")

    st.markdown("Ask me anything about travel!")

    # User input text box
    user_input = st.text_input("You:", "")

    if st.button("Ask"):
        # Display user input
        st.text("You: " + user_input)

        # Get chatbot response
        bot_response = get_bot_response(user_input)

        st.header("TravelBot:")
        st.write(bot_response["result"])

        # # Display additional information if available
        # if "source_documents" in bot_response:
        #     st.header("Additional Information:")
        #     for document in bot_response["source_documents"]:
        #         st.subheader(document.metadata["source"])
        #         st.write(document.page_content)


if __name__ == "__main__":
    main()

