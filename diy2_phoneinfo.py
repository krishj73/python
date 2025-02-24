import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def track_phone_number(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Get the geographical location
        location = geocoder.description_for_number(parsed_number, "en")

        # Get the carrier
        phone_carrier = carrier.name_for_number(parsed_number, "en")

        # Get the time zone
        phone_timezone = timezone.time_zones_for_number(parsed_number)

        # Display the information
        print(f"Phone Number: {phone_number}")
        print(f"Location: {location}")
        print(f"Carrier: {phone_carrier}")
        print(f"Time Zone(s): {', '.join(phone_timezone)}")

    except phonenumbers.NumberParseException as e:
        print(f"Error: {str(e)}")

# Example usage
phone_number = "+91 84070 97115"  # Replace with the phone number you want to track
track_phone_number(phone_number)