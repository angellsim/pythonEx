from pathlib import Path
import pypdf

caminho_pdf = Path('imgs') / 'dom_casmurro.pdf'
leitor_pdf = pypdf.PdfReader(caminho_pdf)

for page in leitor_pdf.pages:
    for obj_imagem in page.images:
        print(f'{obj_imagem} -> {obj_imagem.name}')