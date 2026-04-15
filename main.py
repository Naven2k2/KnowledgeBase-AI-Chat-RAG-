import os
import boto3
import streamlit as st
from google import genai
from dotenv import load_dotenv

# Load env
load_dotenv()

st.set_page_config(page_title="KB + Gemini Chat", page_icon="💬")
st.title("Bedrock KB + Gemini 2.5 Flash")

# Config
aws_region = os.getenv("AWS_REGION", "eu-north-1")
knowledge_base_id = os.getenv("KNOWLEDGE_BASE_ID")
gemini_key = os.getenv("GEMINI_API_KEY")

if not gemini_key:
    st.error("Missing GEMINI_API_KEY")
    st.stop()

st.write("This app retrieves context from Bedrock KB and answers using Gemini.")

question = st.text_input("Enter your question")

if st.button("Ask"):
    if not knowledge_base_id:
        st.error("Missing KNOWLEDGE_BASE_ID")
    elif not question.strip():
        st.error("Please enter a question.")
    else:
        try:
            # Bedrock client
            bedrock = boto3.client(
                "bedrock-agent-runtime",
                region_name=aws_region
            )

            # Retrieve context
            kb_response = bedrock.retrieve(
                knowledgeBaseId=knowledge_base_id,
                retrievalQuery={"text": question},
                retrievalConfiguration={
                    "vectorSearchConfiguration": {
                        "numberOfResults": 5
                    }
                },
            )

            chunks = [
                item.get("content", {}).get("text", "")
                for item in kb_response.get("retrievalResults", [])
                if item.get("content", {}).get("text")
            ]

            context = "\n\n".join(chunks)

            if not context:
                st.warning("No relevant context found.")
                st.stop()

            # Strong prompt
            prompt = f"""
You are a strict AI assistant.

Rules:
- Answer ONLY using the context
- If answer not found, say: "I don't know based on the given information"
- Keep answer clear and concise

Context:
{context}

Question:
{question}
"""

            # Gemini client
            client = genai.Client()

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.subheader("Answer")
            st.write(response.text)

            with st.expander("Retrieved Context"):
                st.write(context)

        except Exception as e:
            st.error(f"Error: {str(e)}")