import os
import csv
from PIL import Image
import tkcap
from tkinter.messagebox import showinfo  # Importar desde tkinter.messagebox

class ReportManager:
    def __init__(self, base_dir):
        self.reports_dir = os.path.join(base_dir, 'reportes')
        os.makedirs(self.reports_dir, exist_ok=True)

    def save_results_csv(self, patient_id, label, probability):
        csv_path = os.path.join(self.reports_dir, "historial.csv")
        with open(csv_path, "a") as csvfile:
            w = csv.writer(csvfile, delimiter="-")
            w.writerow([patient_id, label, f"{probability:.2f}%"])
            showinfo(title="Guardar", message="Los datos se guardaron con éxito.")

    def create_pdf(self, root, report_id):
        cap = tkcap.CAP(root)

        # Generar nombre de archivo único para la imagen
        img_id = 0
        while True:
            img_name = f"Reporte{report_id}_{img_id}.jpg"
            img_path = os.path.join(self.reports_dir, img_name)
            if not os.path.exists(img_path):
                break
            img_id += 1

        img = cap.capture(img_path)
        img = Image.open(img_path)
        img = img.convert("RGB")

        # Generar nombre de archivo único para el PDF
        pdf_id = 0
        while True:
            pdf_name = f"Reporte{report_id}_{pdf_id}.pdf"
            pdf_path = os.path.join(self.reports_dir, pdf_name)
            if not os.path.exists(pdf_path):
                break
            pdf_id += 1

        img.save(pdf_path)
        showinfo(title="PDF", message="El PDF fue generado con éxito.")
