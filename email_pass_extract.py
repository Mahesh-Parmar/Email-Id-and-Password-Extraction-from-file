import re

def extract_email_parts(email):
    # Extract the username part before the @ symbol
    username = email.split('@')[0]

    # Extract the domain part after the @ symbol, but before the first dot
    domain_parts = email.split('@')[1].split('.')
    domain = domain_parts[0]

    # Remove any subdomains from the domain name
    if len(domain_parts) > 2:
        domain = domain_parts[-2]

    # Join the username and domain parts with an underscore
    email_parts = '@'.join([username, domain])
    
    return email_parts


# Example usage
# email = 'example.user@gmail.com'
# email_parts = extract_email_parts(email)
# print(email_parts)

# Open the file and read its contents
file_name = input('Enter File Name: ')
with open(file_name, 'r') as f:
    lines = f.readlines()


# Define regular expressions to match email addresses and passwords
email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
email_regex1 = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+')
password_regex = re.compile(r'\b[A-Za-z0-9@#$%^&+=]{8,}\b')

# Extract email addresses and passwords from each line of the file
for line in lines:
    email_matches = email_regex.findall(line)
    # print(email_matches)
    emailaspass = email_regex1.findall(line)
    # if email_regex.findall(line) == email_regex1.findall(line):
    #     print(password_regex.findall(line))
    # else:
    password_matches = password_regex.findall(line)

    # Print out the email addresses and passwords found on this line
    for email in email_matches:
        emailaspass = extract_email_parts(email)
        # print("Email address found:", email)
        with open('emailid','a') as emailid:
            emailid.write(email + '\n')
    for password in password_matches:
        # print(emailaspass)
        if password != emailaspass:
            with open('pass','a') as passwd:
                passwd.write(password + '\n')
            
