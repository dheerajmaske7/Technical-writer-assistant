import streamlit as st
import subprocess

def main():
    st.title("Technical Writer Assistant")

    # Create a two-column layout
    col1, col2 = st.columns(2)

    # Get the code input from the user
    with col1:
        code_input = st.text_area("Enter your code:", height=400)

    # Run the documentation generation process
    if st.button("Generate Documentation"):
        # Save the code input to the Test_Code.txt file
        with open(r"D:\Nethermind\TechnicalWriter\Tests\Test_Code.txt", "w") as f:
            f.write(code_input)

        # Run the main.py script
        #subprocess.run(["python", "main.py"], check=True)

        # Read the generated documentation from the output file
        with open(r"D:\Nethermind\TechnicalWriter\Document_generated\Document.txt", "r") as f:
            doc_output = f.read()

        # Display the generated documentation
        with col2:
            doc_area = st.text_area("Generated Documentation:", doc_output, height=400)

        # Add a clear button to clear the generated documentation area
        if st.button("Clear"):
            doc_area.text_area = ""
            st.session_state["doc_output"] = ""

        # Clear the code input text area
        code_input = ""
        st.session_state["code_input"] = ""

if __name__ == "__main__":
    main()
