import phonenumbers

# Function to get basic information about a phone number
def get_phone_number_info(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number, None)
        
        # Get country code and country name
        country_code = phonenumbers.region_code_for_number(parsed_number)
        #country_name = phonenumbers.region_name_for_number(parsed_number)
        
        # Print information
        print("Country Code:", country_code)
        print("Country Name:", country_name)
        
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print("Invalid phone number:", e)

# Example usage
phone_number = "+919454929255"
get_phone_number_info(phone_number)
