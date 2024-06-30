import anthropic
import pinecone # type: ignore

def generate_and_store_embeddings(code_text, doc_text, output_path, index_name):
    # Initialize the Anthropic client
    client = anthropic.Anthropic(
        api_key="..."  # Replace with your actual API key
    )

    # Generate embeddings for the code text using Anthropic API
    code_response = client.embeddings.create(
        model="claude-3-5-sonnet-20240620",  # Adjust model as needed
        input=code_text
    )
    code_embeddings = code_response.embeddings

    # Generate embeddings for the documentation text using Anthropic API
    doc_response = client.embeddings.create(
        model="claude-3-5-sonnet-20240620",  # Adjust model as needed
        input=doc_text
    )
    doc_embeddings = doc_response.embeddings

    # Initialize Pinecone
    pinecone.init(
        api_key=".."  # Replace with your Pinecone API key
    )

    # Create or connect to a Pinecone index
    index = pinecone.Index(index_name)

    # Add the embeddings to the Pinecone index
    index.upsert(
        vectors={
            "code_id": code_text,
            "code_embedding": code_embeddings,
            "doc_id": doc_text,
            "doc_embedding": doc_embeddings
        }
    )

    # Save the embeddings to the specified output path
    with open(output_path, 'w') as file:
        file.write(str(code_embeddings) + "\n" + str(doc_embeddings))


        # Example usage
code_path = r'D:\Nethermind\TechnicalWriter\Tests\Test_Code.txt'
with open(code_path, 'r') as file:
    code_text = file.read()

doc_path = r'D:\Nethermind\TechnicalWriter\Document_generated\Document.txt'
with open(doc_path, 'r') as file:
    doc_text = file.read()

output_path = r'D:\Nethermind\TechnicalWriter\Document_generated\embeddings.txt'
index_name = "my-embeddings-index"

generate_and_store_embeddings(code_text, doc_text, output_path, index_name)