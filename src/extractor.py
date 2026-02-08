def extract_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def extract_fields(text):
    import re

    patterns = {
        # Policy Information
        "policyNumber": r"Policy Number:\s*(.+)",
        "policyholderName": r"Policyholder Name:\s*(.+)",
        "effectiveDates": r"Effective Dates:\s*(.+)",

        # Incident Information
        "incidentDate": r"Incident Date:\s*(.+)",
        "incidentTime": r"Incident Time:\s*(.+)",
        "location": r"Location:\s*(.+)",
        "description": r"Description:\s*(.+)",

        # Involved Parties
        "claimant": r"Claimant:\s*(.+)",
        "thirdParties": r"Third Parties:\s*(.+)",
        "contactDetails": r"Contact Details:\s*(.+)",

        # Asset Details
        "assetType": r"Asset Type:\s*(.+)",
        "assetId": r"Asset ID:\s*(.+)",
        "estimatedDamage": r"Estimated Damage:\s*(\d+)",

        # Other Mandatory
        "claimType": r"Claim Type:\s*(.+)",
        "attachments": r"Attachments:\s*(.+)",
        "initialEstimate": r"Initial Estimate:\s*(\d+)"
    }

    extracted = {}

    for field, pattern in patterns.items():
        match = re.search(pattern, text)
        extracted[field] = match.group(1).strip() if match else None

    return extracted
