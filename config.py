
# Gemini Configuration
# ==========================

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

MODEL_NAME = "gemini-2.5-flash"

# ==========================
# Folder
# ==========================

UPLOAD_FOLDER = "uploads"

OUTPUT_FOLDER = "output"

EXCEL_FILE = "orders.xlsx"

# ==========================
# PDF
# ==========================

PDF_DPI = 300

# ==========================
# OCR
# ==========================

MAX_PAGES = 100

# ==========================
# AI
# ==========================

TEMPERATURE = 0

MAX_RETRY = 3

# ==========================
# Shipment
# ==========================

SHIPMENT_PREFIX = "SHP"

# ==========================
# Date Format
# ==========================

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"