MANDATORY_FIELDS = [
    "policyNumber",
    "policyholderName",
    "effectiveDates",
    "incidentDate",
    "incidentTime",
    "location",
    "description",
    "claimant",
    "contactDetails",
    "assetType",
    "assetId",
    "estimatedDamage",
    "claimType",
    "initialEstimate"
]


def find_missing_fields(extracted_fields):
    missing = []
    for field in MANDATORY_FIELDS:
        if not extracted_fields.get(field):
            missing.append(field)
    return missing
