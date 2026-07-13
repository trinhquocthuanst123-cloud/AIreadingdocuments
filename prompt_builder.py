from models import DOCUMENT_FIELDS, ALL_FIELDS

COMMON_RULE = """
Return ONLY valid JSON.

If information is missing return null.

Keep original spelling.

Do not guess.

Date format:
YYYY-MM-DD

Currency:
ISO Currency Code.

Numbers:
Do not use commas.
"""

from models import DOCUMENT_FIELDS, ALL_FIELDS
from prompts import PROMPTS

COMMON_RULE = """
Return ONLY valid JSON.

If information is missing return null.

Keep original spelling.

Do not guess.

Date format:
YYYY-MM-DD

Currency:
ISO Currency Code.

Numbers:
Do not use commas.
"""

def build_prompt(doc_type):
    print("doc_type =", repr(doc_type))
    print("PROMPTS =", list(PROMPTS.keys()))
    print("DOCUMENT_FIELDS =", list(DOCUMENT_FIELDS.keys()))
    # Nếu có prompt riêng thì dùng
    if doc_type in PROMPTS:

        return PROMPTS[doc_type]

    # Nếu chưa có prompt riêng thì tự sinh prompt

    fields = DOCUMENT_FIELDS.get(doc_type)

    if fields is None:

        print("Unknown document:", doc_type)

        fields = ALL_FIELDS

    prompt = f"""
You are an expert in {doc_type}.

Extract ONLY these fields.

"""

    for field in fields:

        prompt += field + "\n"

    prompt += COMMON_RULE
    print(prompt)
    return prompt