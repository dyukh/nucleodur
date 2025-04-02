# %%
import pymupdf  # PyMuPDF

pdf_path = "test.pdf"
doc = pymupdf.open(pdf_path)

for page in doc:
    for xref in page.get_contents():
        stream = doc.xref_stream(xref).decode("latin1")
        if "stream" in stream and "endstream" in stream:
            print("YES-------")
        data = stream.split("stream")[0].split("endstream")[0].strip()
        print(data)   
# %%
