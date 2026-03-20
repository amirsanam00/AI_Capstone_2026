import streamlit as st
import ollama

def load_text():
    with open("constitution.txt", "r") as f:
        return f.read()

def summarize_text(text, query):
    prompt = f"""
    The user is searching for: {query}
    
    Here is the relevant California Constitution text:
    {text[:2000]}
    
    Please provide:
    1. A 5-bullet plain English summary
    2. A simple explanation a beginner can understand
    3. Three key legal terms and their definitions
    """
    response = ollama.chat(model="llama3", messages=[
        {"role": "user", "content": prompt}
    ])
    return response["message"]["content"]

def main():
    st.title("California Constitution AI Search & Summarizer")
    st.write("Search and understand California law in plain English.")
    
    user_input = st.text_input("Enter a keyword or Article number:")
    
    if user_input:
        text = load_text()
        if user_input.lower() in text.lower():
            st.subheader("AI Summary")
            with st.spinner("Generating summary..."):
                summary = summarize_text(text, user_input)
            st.write(summary)
            st.subheader("Source")
            st.markdown("[View Original California Constitution](https://leginfo.legislature.ca.gov/faces/codesTOCSelected.xhtml?tocCode=CONS)")
        else:
            st.write("No results found for: " + user_input)

if __name__ == "__main__":
    main()
