import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def validate_number(number: str):
    try:
        parsed = phonenumbers.parse(number, None)
        valid = phonenumbers.is_valid_number(parsed)
        e164 = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        
        return {
            "valid": valid,
            "e164": e164,
            "region": geocoder.description_for_number(parsed, "en"),
            "carrier": carrier.name_for_number(parsed, "en"),
            "timezones": timezone.time_zones_for_number(parsed)
        }

    except Exception:
        return {
            "valid": False,
            "e164": number,
            "region": None,
            "carrier": None,
            "timezones": None
        }
