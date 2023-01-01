def read_pdf(path):
    try: reader = PdfReader(path)
    except: return ''