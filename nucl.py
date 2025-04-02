import fitz  # PyMuPDF

def extract_stream_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    for page in doc:
        for xref in page.get_contents():
            stream = doc.xref_stream(xref).decode("latin1")
            if "stream" in stream and "endstream" in stream:
                # Извлекаем данные между stream и endstream
                data = stream.split("stream")[1].split("endstream")[0].strip()
                return data
    return None

pdf_path = "your_file.pdf"
stream_data = extract_stream_from_pdf(pdf_path)
print(stream_data[:500])  # Посмотрим начало данных
