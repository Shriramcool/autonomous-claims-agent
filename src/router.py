def route_claim(fields, missing_fields):
    description = (fields.get("description") or "").lower()
    claim_type = (fields.get("claimType") or "").lower()
    damage = int(fields.get("estimatedDamage") or 0)

    if missing_fields:
        return "Manual Review", "Mandatory fields are missing"

    if "fraud" in description or "staged" in description or "inconsistent" in description:
        return "Investigation Flag", "Suspicious keywords detected"

    if claim_type == "injury":
        return "Specialist Queue", "Injury related claim"

    if damage < 25000:
        return "Fast-track", "Estimated damage below threshold"

    return "Standard Processing", "Normal claim"
