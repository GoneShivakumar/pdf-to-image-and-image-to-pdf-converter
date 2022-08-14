import fitz
import os

from flask import Flask, request, render_template



app = Flask(__name__)



@app.route('/',methods=['Get'])
def sample():
    return render_template('base.html')

@app.route('/convert', methods=["GET","POST"])
def imagetopdf():
    if request.method == "POST":
        f= request.files['image']
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'uploads', f.filename)
        f.save(filepath)
        
        doc=fitz.open()
        imgdoc=fitz.open(filepath)
        pdfbytes=imgdoc.convert_to_pdf()
        imgpdf=fitz.open("pdf",pdfbytes)
        doc.insert_pdf(imgpdf)
        doc.save("img1_pdf.pdf")
    return render_template('base.html')

@app.route('/base1.html', methods=["GET","POST"])
def pdftoimage():
    if request.method == "POST":
        f= request.files['image']
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'uploads', f.filename)
        f.save(filepath)
        
        doc = fitz.open(filepath)
        for page in doc:
            pix = page.get_pixmap()
            pix.save("page-%i.png" %page.number)
    return render_template('base1.html')

@app.route('/base2.html',methods=['GET'])
def about():
    return render_template('base2.html')



if __name__=='__main__':
    app.run(debug=False,host='0.0.0.0')