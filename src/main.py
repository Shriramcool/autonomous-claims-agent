import json
from extractor import extract_text, extract_fields
from validator import find_missing_fields
from router import route_claim


def process_claim():
    file_path = "data/fnol1.txt"

    text = extract_text(file_path)
    extracted_fields = extract_fields(text)
    missing_fields = find_missing_fields(extracted_fields)
    route, reason = route_claim(extracted_fields, missing_fields)

    result = {
        "extractedFields": extracted_fields,
        "missingFields": missing_fields,
        "recommendedRoute": route,
        "reasoning": reason
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    process_claim()
