import streamlit as st
import nucl
from pathlib import Path
# import os


# Настройка заголовка и текста
st.set_page_config(
    page_title="Nucleodur",
    page_icon="📈",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": "# Преобразование файлов хроматографа",
    },
)

# Header
st.title("Преобразование файлов хроматографа")

st.divider()

pdfin = st.file_uploader(
    label="Входной файл PDF",
    type=["pdf"],
    accept_multiple_files=False,
    help="Файл с графиком",
)

if pdfin is not None:
    stream_data = nucl.extract_stream_from_pdf(pdfin)
    path_commands = nucl.parse_path_data(stream_data)
    plist = nucl.to_list(path_commands)

    fname = Path(pdfin.name)
    outname = fname.with_suffix('.xlsx')

    nucl.to_excel(plist, fname=outname)

    with open(outname, "rb") as file:
        btn = st.download_button(
            label="Скачать файл Excel",
            data=file,
            file_name=outname.name,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
