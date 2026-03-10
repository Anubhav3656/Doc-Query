from unstructured.partition.pdf import partition_pdf
from unstructured.chunking.title import chunk_by_title


def process_pdf(file_path):

    elements = partition_pdf(
        filename=file_path,
        strategy="hi_res",
        infer_table_structure=True
    )

    chunks = chunk_by_title(
        elements,
        max_characters=1000,
        combine_text_under_n_chars=200
    )

    documents = []

    for chunk in chunks:

        documents.append({
            "text": chunk.text,
            "metadata": {
                "source": file_path,
                "category": str(chunk.category)
            }
        })

    return documents