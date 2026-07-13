# ==========================
# Supported Documents
# ==========================

SUPPORTED_DOCUMENTS = [

    "Purchase Order",

    "Sales Contract",

    "Commercial Invoice",

    "Packing List",

    "Bill of Lading",

    "Sea Waybill",

    "Air Waybill",

    "Booking Confirmation",

    "Delivery Order",

    "Arrival Notice",

    "Certificate of Origin",

    "Insurance Certificate",

    "Manifest",

    "Health Certificate",

    "Phytosanitary Certificate",

    "Radiation Certificate",

    "Quality & Quantity Certificate",

    "Unknown"

]

# ==========================
# Common Fields
# ==========================

COMMON_FIELDS = [

    "document_type",

    "document_number",

    "document_date",

    "buyer",

    "seller",

    "supplier",

    "shipper",

    "consignee",

    "notify_party",

    "exporter",

    "importer",

    "product",

    "product_code",

    "hs_code",

    "quantity",

    "unit",

    "gross_weight",

    "net_weight",

    "volume_cbm",

    "currency",

    "unit_price",

    "total_amount",

    "payment_method",

    "payment_term",

    "incoterm",

    "remarks"

]

# ==========================
# Transport Fields
# ==========================

TRANSPORT_FIELDS = [

    "origin_port",

    "destination_port",

    "place_of_receipt",

    "place_of_delivery",

    "airport_of_departure",

    "airport_of_destination",

    "carrier",

    "shipping_line",

    "airline",

    "vessel_name",

    "voyage_number",

    "flight_number",

    "container_number",

    "container_type",

    "seal_number",

    "etd",

    "eta"

]

# ==========================
# Initialize
# ==========================

ALL_FIELDS = []

DOCUMENT_FIELDS = {}
# ==========================
# Purchase Order
# ==========================

DOCUMENT_FIELDS["Purchase Order"] = [

    "document_type",
    "document_number",

    "po_number",
    "po_date",

    "buyer",
    "supplier",

    "product",
    "product_code",
    "hs_code",

    "quantity",
    "unit",

    "unit_price",
    "currency",
    "total_amount",

    "delivery_date",

    "payment_method",

    "incoterm"

]

# ==========================
# Sales Contract
# ==========================

DOCUMENT_FIELDS["Sales Contract"] = [

    "document_type",
    "document_number",

    "contract_number",
    "contract_date",

    "buyer",
    "seller",

    "product",
    "product_code",
    "hs_code",

    "quantity",
    "unit",

    "unit_price",
    "currency",
    "total_amount",

    "payment_term",

    "incoterm"

]

# ==========================
# Commercial Invoice
# ==========================

DOCUMENT_FIELDS["Commercial Invoice"] = [

    "document_type",
    "document_number",

    "invoice_number",
    "invoice_date",

    "buyer",
    "seller",

    "product",
    "product_code",
    "hs_code",

    "quantity",
    "unit",

    "unit_price",
    "currency",
    "total_amount",

    "country_of_origin",

    "payment_method",

    "incoterm",

    "remarks"

]

# ==========================
# Packing List
# ==========================

DOCUMENT_FIELDS["Packing List"] = [

    "document_type",
    "document_number",

    "packing_list_number",
    "packing_date",

    "buyer",
    "seller",

    "product",
    "product_code",

    "quantity",
    "unit",

    "gross_weight",
    "net_weight",

    "package_count",

    "package_type",

    "marks_numbers"

]

# ==========================
# Bill of Lading
# ==========================

DOCUMENT_FIELDS["Bill of Lading"] = [

    "document_type",
    "document_number",

    "bl_number",
    "bl_date",

    "shipper",
    "consignee",
    "notify_party",

    "carrier",

    "vessel_name",

    "voyage_number",

    "origin_port",

    "destination_port",

    "place_of_receipt",

    "place_of_delivery",

    "container_number",

    "container_type",

    "seal_number",

    "gross_weight",

    "package_count",

    "freight_term"

]

# ==========================
# Sea Waybill
# ==========================

DOCUMENT_FIELDS["Sea Waybill"] = [

    "document_type",
    "document_number",

    "seawaybill_number",

    "shipper",

    "consignee",

    "carrier",

    "vessel_name",

    "voyage_number",

    "origin_port",

    "destination_port",

    "container_number",

    "seal_number"

]

# ==========================
# Air Waybill
# ==========================

DOCUMENT_FIELDS["Air Waybill"] = [

    "document_type",
    "document_number",

    "awb_number",

    "shipper",

    "consignee",

    "airline",

    "flight_number",

    "airport_of_departure",

    "airport_of_destination",

    "gross_weight",

    "chargeable_weight",

    "freight_charge"

]
# ==========================
# Booking Confirmation
# ==========================

DOCUMENT_FIELDS["Booking Confirmation"] = [

    "document_type",
    "document_number",

    "booking_number",

    "carrier",

    "vessel_name",

    "voyage_number",

    "etd",

    "eta",

    "origin_port",

    "destination_port"

]

# ==========================
# Delivery Order
# ==========================

DOCUMENT_FIELDS["Delivery Order"] = [

    "document_type",
    "document_number",

    "do_number",

    "consignee",

    "container_number",

    "pickup_location",

    "delivery_date"

]

# ==========================
# Arrival Notice
# ==========================

DOCUMENT_FIELDS["Arrival Notice"] = [

    "document_type",
    "document_number",

    "arrival_notice_number",

    "eta",

    "carrier",

    "vessel_name",

    "voyage_number",

    "container_number"

]

# ==========================
# Certificate of Origin
# ==========================

DOCUMENT_FIELDS["Certificate of Origin"] = [

    "document_type",
    "document_number",

    "co_number",

    "co_form",

    "origin_criterion",

    "issuing_authority",

    "exporter",

    "importer",

    "country_of_origin",

    "product",

    "hs_code",

    "quantity"

]

# ==========================
# Insurance Certificate
# ==========================

DOCUMENT_FIELDS["Insurance Certificate"] = [

    "document_type",
    "document_number",

    "policy_number",

    "insurance_company",

    "insured",

    "coverage",

    "insurance_amount",

    "currency",

    "claim_contact"

]

# ==========================
# Manifest
# ==========================

DOCUMENT_FIELDS["Manifest"] = [

    "document_type",
    "document_number",

    "manifest_number",

    "carrier",

    "vessel_name",

    "voyage_number",

    "origin_port",

    "destination_port",

    "container_number"

]

# ==========================
# Health Certificate
# ==========================

DOCUMENT_FIELDS["Health Certificate"] = [

    "document_type",
    "document_number",

    "health_certificate_number",

    "issue_date",

    "issuing_authority",

    "exporter",

    "importer",

    "product",

    "quantity",

    "health_result"

]

# ==========================
# Phytosanitary Certificate
# ==========================

DOCUMENT_FIELDS["Phytosanitary Certificate"] = [

    "document_type",
    "document_number",

    "phytosanitary_certificate_number",

    "issue_date",

    "issuing_authority",

    "exporter",

    "importer",

    "product",

    "quantity",

    "phytosanitary_result"

]

# ==========================
# Radiation Certificate
# ==========================

DOCUMENT_FIELDS["Radiation Certificate"] = [

    "document_type",
    "document_number",

    "radiation_certificate_number",

    "issue_date",

    "issuing_authority",

    "product",

    "radiation_result"

]

# ==========================
# Quality & Quantity Certificate
# ==========================

DOCUMENT_FIELDS["Quality & Quantity Certificate"] = [

    "document_type",
    "document_number",

    "inspection_number",

    "inspection_company",

    "issue_date",

    "product",

    "quantity",

    "quality_result",

    "quantity_result",

    "grade",

    "moisture"

]
# ==========================
# Build ALL_FIELDS
# ==========================

ALL_FIELDS = []

ALL_FIELDS.extend(COMMON_FIELDS)

ALL_FIELDS.extend(TRANSPORT_FIELDS)

for fields in DOCUMENT_FIELDS.values():

    for field in fields:

        if field not in ALL_FIELDS:

            ALL_FIELDS.append(field)

# ==========================
# Document Description
# ==========================

DOCUMENT_DESCRIPTIONS = {

    "Purchase Order":
        "Purchase order issued by buyer to supplier.",

    "Sales Contract":
        "Sales agreement between buyer and seller.",

    "Commercial Invoice":
        "Commercial invoice issued by seller.",

    "Packing List":
        "Packing list containing package and weight details.",

    "Bill of Lading":
        "Ocean Bill of Lading for sea shipment.",

    "Sea Waybill":
        "Sea Waybill for sea shipment.",

    "Air Waybill":
        "Air cargo Air Waybill.",

    "Booking Confirmation":
        "Carrier booking confirmation.",

    "Delivery Order":
        "Delivery Order for cargo release.",

    "Arrival Notice":
        "Arrival Notice from shipping line or airline.",

    "Certificate of Origin":
        "Certificate proving country of origin.",

    "Insurance Certificate":
        "Marine Cargo Insurance Certificate.",

    "Manifest":
        "Cargo Manifest.",

    "Health Certificate":
        "Health Certificate issued by competent authority.",

    "Phytosanitary Certificate":
        "Phytosanitary Certificate issued by plant quarantine authority.",

    "Radiation Certificate":
        "Radiation Inspection Certificate.",

    "Quality & Quantity Certificate":
        "Inspection Certificate for Quality and Quantity.",

    "Unknown":
        "Unknown logistics document."

}