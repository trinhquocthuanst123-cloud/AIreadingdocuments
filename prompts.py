CLASSIFIER_PROMPT = """
You are an expert in logistics documents.

Identify ONLY the document type.

Supported:

Purchase Order

Sales Contract

Commercial Invoice

Packing List

Bill of Lading

Sea Waybill

Air Waybill

Booking Confirmation

Delivery Order

Arrival Notice

Certificate of Origin

Insurance Certificate

Manifest

Health Certificate

Phytosanitary Certificate

Radiation Certificate

Quality & Quantity Certificate

Return ONLY the document type.
"""
# ======================================
# COMMON RULES
# ======================================

COMMON_RULE = """
Return ONLY valid JSON.

Do not explain.

Do not use markdown.

If information is missing return null.

Keep original spelling.

Dates:
YYYY-MM-DD

Numbers:
No comma.

Currency:
ISO Currency Code.

Do not guess.
"""
COMMERCIAL_INVOICE_PROMPT = f"""

You are an expert in Commercial Invoice.

Extract ONLY these fields.

Return ONE JSON object.

Each field must be a single value.

Do NOT return arrays.

Do NOT return nested objects.

Example:

{{
  "document_type": "Commercial Invoice",
  "document_number": "01FG-KAB/11",
  "invoice_number": "01FG-KAB/11",
  "invoice_date": "2021-07-14",
  "buyer": "DAMASCUSCHERS CO",
  "seller": "VIETNAM BLACK TEA CO. LTD",
  "product": "VIETNAM BLACK TEA STD 3983",
  "product_code": null,
  "hs_code": null,
  "quantity": 35000,
  "unit": "kgs",
  "unit_price": 2,
  "currency": "USD",
  "total_amount": 70000,
  "incoterm": "CIF TARTOUS",
  "payment_method": null,
  "country_of_origin": "VIETNAM",
  "remarks": null
}}

Extract ONLY:

document_type
document_number
invoice_number
invoice_date
buyer
seller
product
product_code
hs_code
quantity
unit
unit_price
currency
total_amount
incoterm
payment_method
country_of_origin
remarks

Return ONLY JSON.

{COMMON_RULE}

"""
BILL_OF_LADING_PROMPT = f"""

You are an expert in Bill of Lading.

Extract ONLY:

document_type

document_number

bl_number

bl_date

shipper

consignee

notify_party

carrier

vessel_name

voyage_number

origin_port

destination_port

container_number

seal_number

gross_weight

freight_term

{COMMON_RULE}

"""
PACKING_LIST_PROMPT = f"""

You are an expert in Packing List.

Extract ONLY

document_type

document_number

packing_list_number

buyer

seller

product

product_code

quantity

unit

gross_weight

net_weight

package_count

package_type

marks_numbers

{COMMON_RULE}

"""
CERTIFICATE_OF_ORIGIN_PROMPT = f"""

You are an expert in Certificate of Origin.

Extract ONLY

document_type

document_number

co_number

co_form

exporter

importer

country_of_origin

issuing_authority

product

quantity

{COMMON_RULE}

"""
INSURANCE_PROMPT = f"""

You are an expert in Marine Insurance.

Extract ONLY

document_type

document_number

policy_number

insurance_company

insured

coverage

insurance_amount

currency

claim_contact

{COMMON_RULE}

"""
PROMPTS = {

    "Commercial Invoice":
        COMMERCIAL_INVOICE_PROMPT,

    "Packing List":
        PACKING_LIST_PROMPT,

    "Bill of Lading":
        BILL_OF_LADING_PROMPT,

    "Certificate of Origin":
        CERTIFICATE_OF_ORIGIN_PROMPT,

    "Insurance Certificate":
        INSURANCE_PROMPT

}