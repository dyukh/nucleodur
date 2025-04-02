import pymupdf  # PyMuPDF


def extract_stream_from_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)
    for page in doc:
        for xref in page.get_contents():
            stream = doc.xref_stream(xref).decode("latin1")
            # if "stream" in stream and "endstream" in stream:
            # Извлекаем данные между stream и endstream
            data = stream.split("stream")[0].split("endstream")[0].strip()
            start = data.find("W n")
            stop = data[start:].find("S")
            return data[start: start+stop - 1]
    return None


pdf_path = "test.pdf"
stream_data = extract_stream_from_pdf(pdf_path)
start = stream_data.find("W n")
# print(stream_data[start:1500])  # Посмотрим начало данных


def parse_path_data(data):
    commands = []
    tokens = data.split()
    i = 0
    while i < len(tokens):
        if tokens[i].isalpha():  # Команда (m, l, c...)
            cmd = tokens[i]
            i += 1
            points = []
            while i + 1 < len(tokens) and not tokens[i].isalpha():
                x = float(tokens[i])
                y = float(tokens[i + 1])
                # print(i, len(tokens), x, y)
                points.append((x, y))
                i += 2
            commands.append((cmd, points))
        else:
            i += 1
    return commands


path_commands = parse_path_data(stream_data)
for cmd, points in path_commands:
    if points and len(points[0]) > 1:
        print(points[0][1], points[0][0])
