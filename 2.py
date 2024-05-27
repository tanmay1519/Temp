import os
from faker import Faker
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Initialize Faker
fake = Faker()

# Define the output folder
output_folder = 'A'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def generate_medical_report():
    """Generate a fake medical report."""
    report = f"""
    Patient Name: {fake.name()}
    Date of Birth: {fake.date_of_birth()}
    Gender: {fake.random_element(elements=('Male', 'Female'))}
    Address: {fake.address()}
    
    Medical Report:
    ----------------
    Chief Complaint: {fake.sentence()}
    History of Present Illness: {fake.paragraph(nb_sentences=3)}
    Past Medical History: {fake.paragraph(nb_sentences=2)}
    Medications: {fake.words(nb=5)}
    Allergies: {fake.words(nb=3)}
    Physical Examination: {fake.paragraph(nb_sentences=3)}
    Assessment and Plan: {fake.paragraph(nb_sentences=4)}
    Follow-up: {fake.date()}
    """
    return report.strip()

def create_pdf_from_text(text, pdf_path):
    """Create a PDF file from text."""
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)
    y = height - 40
    for line in text.split('\n'):
        if y < 40:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 40
        c.drawString(40, y, line)
        y -= 14
    c.save()

def generate_and_save_reports(num_reports, output_folder):
    """Generate a specified number of medical reports and save them as PDFs."""
    for i in range(num_reports):
        report_text = generate_medical_report()
        pdf_filename = f"medical_report_{i+1}.pdf"
        pdf_path = os.path.join(output_folder, pdf_filename)
        
        create_pdf_from_text(report_text, pdf_path)

# Generate and save 10 medical reports in folder "A"
generate_and_save_reports(10, output_folder)
