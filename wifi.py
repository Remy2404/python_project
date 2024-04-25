# Import the subprocess module
import subprocess
import re

def decode_profile_name(profile_name):
    try:
        return profile_name.encode('latin-1').decode('utf-8')
    except UnicodeDecodeError:
        return profile_name

# Run the first command to get the list of profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='replace').split('\n')

# Extract profiles from the data
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# Loop through each profile to retrieve and print the Wi-Fi passwords
for profile in profiles:
    decoded_profile = decode_profile_name(profile)
    try:
        # Run the command to check the password for the current profile
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', decoded_profile, 'key=clear']).decode('utf-8', errors='replace').split('\n')

        # Extract the password and security type from the results
        password_lines = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        security_type_lines = [b for b in results if "Authentication" in b]

        # Check if the security type is WPA2-Personal and MAC address is present
        if password_lines and security_type_lines:
            security_type = security_type_lines[0].split(":")[1].strip()
            if "WPA2-Personal" in security_type and "(MAC)" in decoded_profile:
                # Print the profile and its password
                try:
                    print("{:<30} | {:<}".format(decoded_profile, password_lines[0]))
                except IndexError:
                    print("{:<30} | {:<}".format(decoded_profile, ""))
    except subprocess.CalledProcessError:
        # Handle errors when checking a specific profile
        print(f"Error checking profile: {decoded_profile}")
