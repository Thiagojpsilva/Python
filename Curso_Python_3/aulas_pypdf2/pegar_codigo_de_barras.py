# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 para manipular arquivos PDF (PdfReader)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
# type: ignore
from pathlib import Path
from PyPDF2 import PdfReader

PASTA_RAIZ = Path(__file__).parent
PASTA_PDF = PASTA_RAIZ / 'pdf_codigo_barras'

PDF_COD_BARRA = PASTA_PDF / 'Carne_carro_novo.pdf'
reader = PdfReader(PDF_COD_BARRA, password='017')

for i in range(len(reader.pages)):
    text = (reader.pages[i]).extract_text
    print(text)



#     print()
#with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)

   


        




