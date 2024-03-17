import PyPDF2
import docx
def format_to_text(filenames):
    knowledge_base=""
    for f in filenames:
        if ".txt" in f or ".md" in f:
            text=open(f,encoding="UTF-8").read()
            knowledge_base+=text
        elif ".pdf" in f:
            knowledge_base+=pdf_to_text(f)
        elif ".doc" in f:
            knowledge_base+=docx_to_text(f)
    return knowledge_base
# Конвертируем PDF в текст
def pdf_to_text(filename):
    pdf=PyPDF2.PdfFileReader(open(filename))
    kol=pdf.numPages
    text=pdf.getPage(kol+1).extract_text()
    return text
# Конвертируем Docx в текст
def docx_to_text(filename):
    doc = docx.Document(filename)
    fullText =" "
    for para in doc.paragraphs:
        fullText+=para.text+"\n"
    return fullText