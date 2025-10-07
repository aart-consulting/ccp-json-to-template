from docxtpl import DocxTemplate
import json

# Load JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Load Word template
doc = DocxTemplate("form_template.docx")

# Render template with JSON
doc.render(data)

# Save the result
doc.save("filled_form.docx")
