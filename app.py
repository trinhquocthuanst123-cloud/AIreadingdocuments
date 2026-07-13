import streamlit as st
import fitz
import time
from models import *
from datetime import datetime
import json
import os
from prompt_builder import build_prompt
from prompts import *
import pandas as pd
from google import genai
from google.genai import types
from PIL import Image
from excel_manager import export_excel, EXCEL_PATH
import io
import json
from config import *



client = genai.Client(
    api_key=API_KEY
)

# ==========================
# Read PDF
# ==========================

def pdf_to_images(uploaded_file):

    pdf = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    images = []

    for page in pdf:

        pix = page.get_pixmap(
            dpi=PDF_DPI,
            alpha=False
        )

        img = Image.open(
            io.BytesIO(
                pix.tobytes("png")
            )
        )

        images.append(img)

    return images

# ==========================
# AI Extract
# ==========================
def detect_document(images):

    contents = [CLASSIFIER_PROMPT]

    for img in images:

        buffer = io.BytesIO()

        img.save(buffer, format="PNG")

        contents.append(

            types.Part.from_bytes(

                data=buffer.getvalue(),

                mime_type="image/png"

            )

        )

    response = client.models.generate_content(

        model=MODEL_NAME,

        contents=contents

    )

    doc = response.text.strip()

    doc = doc.replace("```", "").strip()

    if doc not in SUPPORTED_DOCUMENTS:

        doc = "Unknown"

    return doc
def extract_order(images):
    doc_type = detect_document(images)
    print("=" * 50)
    print("Detected:", doc_type)
    print("=" * 50)
    print(doc_type)
   
    print("Detected:", repr(doc_type))

    prompt = build_prompt(doc_type)
    print("doc_type =", repr(doc_type))
    print("prompt is None =", prompt is None)

    if prompt is None:
        st.error(f"Không tạo được prompt cho document type: {doc_type}")
        return {}
    

    contents = [prompt]

    for img in images:

        buffer = io.BytesIO()

        img.save(buffer, format="PNG")

        contents.append(
            types.Part.from_bytes(
                data=buffer.getvalue(),
                mime_type="image/png"
            )
        )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=contents
    )

    result = response.text.strip()

    result = result.replace("```json", "")

    result = result.replace("```", "").strip()

    start = result.find("{")

    end = result.rfind("}") + 1

    result = result[start:end]

    try:
        return json.loads(result)

    except Exception as e:

        print(result)

        raise e
    
# ==========================
# Excel
# ==========================




# ==========================
# Streamlit
# ==========================

st.set_page_config(
    page_title="AI Order Reader",
    layout="wide"
)

st.title("Đọc chứng từ bằng AI")

uploaded_files = st.file_uploader(

    "Up file ngay dưới đây nhaa!",

    type=["pdf","png","jpg","jpeg"],

    accept_multiple_files=True

)

if uploaded_files:

    with st.spinner("Reading PDF..."):

        if st.button("🚀 Process All Documents"):

            progress = st.progress(0)

            total = len(uploaded_files)

            for i, uploaded in enumerate(uploaded_files):

                st.divider()

                st.subheader(f"📄 {uploaded.name}")
  
                with st.spinner("Reading Document..."):

                    if uploaded.name.lower().endswith(".pdf"):

                        images = pdf_to_images(uploaded)

                    else:

                        images = [
                             Image.open(uploaded)
                        ]

                start_time = time.time()

                result = extract_order(images)
                DOC_TYPE_MAP = {
                    "COMMERCIAL INVOICE": "Commercial Invoice",
                    "PACKING LIST": "Packing List",
                    "BILL OF LADING": "Bill of Lading",
                    "BILL OF LADING ORIGINAL": "Bill of Lading",
                    "ORIGINAL BILL OF LADING": "Bill of Lading",
                    "Bill of lading original": "Bill of lading",
                    "PURCHASE ORDER": "Purchase Order",
                    "SALES CONTRACT": "Sales Contract",
                    "AIR WAYBILL": "Air Waybill",
                    "SEA WAYBILL": "Sea Waybill",
                    "BOOKING CONFIRMATION": "Booking Confirmation",
                    "DELIVERY ORDER": "Delivery Order",
                    "ARRIVAL NOTICE": "Arrival Notice",
                    "CERTIFICATE OF ORIGIN": "Certificate of Origin",
                    "INSURANCE CERTIFICATE": "Insurance Certificate",
                    "MANIFEST": "Manifest",
                    "HEALTH CERTIFICATE": "Health Certificate",
                    "PHYTOSANITARY CERTIFICATE": "Phytosanitary Certificate",
                    "RADIATION CERTIFICATE": "Radiation Certificate",
                    "QUALITY & QUANTITY CERTIFICATE": "Quality & Quantity Certificate"
                }

                doc = result.get("document_type")

                if doc:
                    result["document_type"] = DOC_TYPE_MAP.get(doc.upper(), doc)
                print("="*60)
                print(json.dumps(result, indent=4, ensure_ascii=False))
                print("="*60)
                if not result.get("document_type"):

                    if result.get("invoice_number"):
                        result["document_type"] = "Commercial Invoice"

                    elif result.get("po_number"):
                        result["document_type"] = "Purchase Order"

                    elif result.get("contract_number"):
                        result["document_type"] = "Sales Contract"

                    elif result.get("packing_list_number"):
                        result["document_type"] = "Packing List"

                    elif result.get("bl_number"):
                        result["document_type"] = "Bill of Lading"

                    elif result.get("awb_number"):
                        result["document_type"] = "Air Waybill"

                    elif result.get("booking_number"):
                        result["document_type"] = "Booking Confirmation"

                    elif result.get("do_number"):
                        result["document_type"] = "Delivery Order"

                    elif result.get("co_number"):
                        result["document_type"] = "Certificate of Origin"

                    elif result.get("policy_number"):
                        result["document_type"] = "Insurance Certificate"

                    elif result.get("manifest_number"):
                        result["document_type"] = "Manifest"

                    elif result.get("health_certificate_number"):
                        result["document_type"] = "Health Certificate"

                    elif result.get("phytosanitary_certificate_number"):
                        result["document_type"] = "Phytosanitary Certificate"

                    elif result.get("radiation_certificate_number"):
                        result["document_type"] = "Radiation Certificate"

                    elif result.get("inspection_number"):
                        result["document_type"] = "Quality & Quantity Certificate"

                    else:
                        result["document_type"] = doc_type
                    if not result.get("document_number"):

                        mapping = {
                            "Purchase Order": "po_number",
                            "Sales Contract": "contract_number",
                            "Commercial Invoice": "invoice_number",
                            "Packing List": "packing_list_number",
                            "Bill of Lading": "bl_number",
                            "Air Waybill": "awb_number",
                            "Booking Confirmation": "booking_number",
                            "Delivery Order": "do_number",
                            "Certificate of Origin": "co_number",
                            "Insurance Certificate": "policy_number",
                            "Manifest": "manifest_number",
                            "Health Certificate": "health_certificate_number",
                            "Phytosanitary Certificate": "phytosanitary_certificate_number",
                            "Radiation Certificate": "radiation_certificate_number",
                            "Quality & Quantity Certificate": "inspection_number"
                        }

                        field = mapping.get(result["document_type"])

                        if field:
                            result["document_number"] = result.get(field)
                print(result)
                processing_time = round(time.time() - start_time, 2)

                result["processing_time"] = processing_time

                st.success(f"⏱️ AI Processing Time: {processing_time} seconds")

                doc_type = result.get("document_type", "Unknown")

                st.write("**Document Type:**", doc_type)

                st.json(result)
                print("Before export:", result["document_type"])
                export_excel(result)

                progress.progress((i + 1) / total)

            st.success(f"✅ Đã xử lý {total} tài liệu")

            filename = EXCEL_PATH

            with open(filename, "rb") as file:

                st.download_button(

                    "📥 Download Excel",

                    data=file,

                    file_name="orders.xlsx",

                     mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                )