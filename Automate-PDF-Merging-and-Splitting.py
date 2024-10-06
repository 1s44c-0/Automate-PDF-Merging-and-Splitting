from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    print(f"Merged PDFs saved to {output_path}")

def split_pdf(pdf_path, split_at_page, output_dir):
    reader = PdfReader(pdf_path)
    for i in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        output_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page_{i+1}.pdf")
        with open(output_path, 'wb') as f:
            writer.write(f)
        print(f"Created: {output_path}")

if __name__ == "__main__":
    # Example: Merging PDFs
    pdf_list = ["document1.pdf", "document2.pdf", "document3.pdf"]
    output_path = "merged_document.pdf"
    merge_pdfs(pdf_list, output_path)
    
    # Example: Splitting a PDF
    pdf_path = "merged_document.pdf"
    output_dir = "/path/to/output/directory"
    os.makedirs(output_dir, exist_ok=True)
    split_pdf(pdf_path, None, output_dir)  # 'split_at_page' not used in this example
      
