import os
from faker import Faker
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Initialize Faker
fake = Faker()

# Define the output folder
output_folder = 'A'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def generate_medical_report():
    """Generate a fake medical report."""
    report = {
        "patient_name": fake.name(),
        "dob": fake.date_of_birth(),
        "gender": fake.random_element(elements=('Male', 'Female')),
        "address": fake.address(),
        "chief_complaint": fake.sentence(),
        "history_of_present_illness": fake.paragraph(nb_sentences=3),
        "past_medical_history": fake.paragraph(nb_sentences=2),
        "medications": ", ".join(fake.words(nb=5)),
        "allergies": ", ".join(fake.words(nb=3)),
        "physical_examination": fake.paragraph(nb_sentences=3),
        "assessment_and_plan": fake.paragraph(nb_sentences=4),
        "follow_up": fake.date()
    }
    return report

def create_pdf(report, pdf_path):
    """Create a PDF file from a medical report dictionary."""
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title_style = styles['Title']
    story.append(Paragraph("Medical Report", title_style))
    story.append(Spacer(1, 12))

    # Patient Information
    section_style = ParagraphStyle(name='Section', fontSize=14, spaceAfter=12)
    story.append(Paragraph("Patient Information", section_style))

    text_style = styles['BodyText']
    story.append(Paragraph(f"Name: {report['patient_name']}", text_style))
    story.append(Paragraph(f"Date of Birth: {report['dob']}", text_style))
    story.append(Paragraph(f"Gender: {report['gender']}", text_style))
    story.append(Paragraph(f"Address: {report['address']}", text_style))
    story.append(Spacer(1, 12))

    # Medical Report Details
    story.append(Paragraph("Chief Complaint", section_style))
    story.append(Paragraph(report['chief_complaint'], text_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("History of Present Illness", section_style))
    story.append(Paragraph(report['history_of_present_illness'], text_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Past Medical History", section_style))
    story.append(Paragraph(report['past_medical_history'], text_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Medications", section_style))
    story.append(Paragraph(report['medications'], text_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Allergies", section_style))
    story.append(Paragraph(report['allergies'], text_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Physical Examination", section_style))
    story.append(Paragraph(report['physical_examination'], text_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Assessment and Plan", section_style))
    story.append(Paragraph(report['assessment_and_plan'], text_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Follow-up", section_style))
    story.append(Paragraph(report['follow_up'], text_style))
    story.append(Spacer(1, 12))

    # Build the PDF
    doc.build(story)

def main():
    # Generate a single medical report
    report = generate_medical_report()
    
    # Define the path to save the PDF
    pdf_path = os.path.join(output_folder, "medical_report.pdf")
    
    # Create the PDF
    create_pdf(report, pdf_path)

# Generate and save the medical report
main()
