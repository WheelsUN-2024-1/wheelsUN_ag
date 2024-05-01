from ldap3 import Server, Connection, SIMPLE, SYNC, SUBTREE
import os

# Check if running in a Docker container
def is_running_in_docker():
    return os.path.exists('/.dockerenv')

# Define LDAP server settings
# Set base URL based on environment
if is_running_in_docker():
    ldap_server = 'wheelsun_ldap'
else:
    ldap_server = 'localhost'

ldap_port = 389  # Default LDAP port

# LDAP admin credentials and base DN
ldap_admin_password = 'admin'
ldap_base_dn = 'dc=arqsoft,dc=unal,dc=edu,dc=co'
ldap_admin_username = 'cn=admin,dc=arqsoft,dc=unal,dc=edu,dc=co'

def processName(name, isDriver):
    #process the name accordingly
    prefix = 'd' if isDriver else 'p'
    fullName = prefix + name.replace(' ', '')
    return fullName

def userInLdap(username, password, isDriver)->bool:
    try:
        # Establish connection to LDAP server
        server = Server(ldap_server, port=ldap_port, get_info=SYNC)
        print(f"server current address: {server.current_address}")
        conn = Connection(server, user=f"cn=admin,{ldap_base_dn}", password=ldap_admin_password, authentication=SIMPLE, check_names=True, lazy=False)
        conn.bind()

        username = processName(username, isDriver)
        
        # Search for the user's DN based on username
        conn.search(ldap_base_dn, f'(uid={username})', SUBTREE)

        if len(conn.entries) == 0:
            print(f"User '{username}' not found.")
        else:
            user_dn = conn.entries[0].entry_dn

            # Attempt to authenticate user
            conn = Connection(server, user=user_dn, password=password, authentication=SIMPLE, lazy=False)
            if conn.bind():
                print(f"Authentication successful for user '{username}'.")
                return True
            else:
                print(f"Authentication failed for user '{username}'.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def registerInLdap(fullName, isDriver: bool, password)-> bool:
    #sets ldap dn for each type of user
    mode = 'driver' if isDriver else 'passenger'
    ldap_base_dn = f'ou={mode},dc=arqsoft,dc=unal,dc=edu,dc=co'

    fullName = processName(fullName,isDriver)
    
    # Search filter to find existing users with posixAccount object class
    search_filter = '(objectClass=posixAccount)'

    try:
        # Establish connection to LDAP server
        server = Server(ldap_server, port=ldap_port, get_info='ALL')
        conn = Connection(server, user=ldap_admin_username, password=ldap_admin_password, auto_bind=True)

        # Search for existing users to determine the latest uidNumber used
        conn.search(ldap_base_dn, search_filter, attributes=['uidNumber'])
        
        # Initialize a list to store uidNumber values
        uid_numbers = []

        # Iterate through search results to extract uidNumber values
        for entry in conn.entries:
            if 'uidNumber' in entry:
                uid_numbers.append(entry['uidNumber'][0])
        
        # Determine the maximum uidNumber currently used
        if uid_numbers:
            latest_uid_number = max(uid_numbers)
        else:
            latest_uid_number = 1000  # Default starting UID number if no users found

        # Set the new user's uidNumber as the next available number (increment the max found)
        new_uid_number = str(latest_uid_number + 1)

        #set gidNumber accordignly
        gidNumber = '501' if isDriver else '500'
        # User attributes for the new user
        new_user_attributes = {
            'cn': fullName,
            'givenName': fullName,
            'sn': fullName,
            'uid': fullName,
            'uidNumber': new_uid_number,
            'gidNumber': gidNumber,
            'homeDirectory': f'/home/users/{fullName}',
            'objectClass': ['inetOrgPerson', 'posixAccount', 'top'],
            'userPassword': password  # Set user's password
        }

        # Create DN for the new user
        new_user_dn = f"cn={new_user_attributes['cn']},{ldap_base_dn}"

        # Add the new user entry
        conn.add(new_user_dn, attributes=new_user_attributes)

        if(userInLdap(fullName[1:],password, isDriver)):
            print(f"New user '{new_user_attributes['cn']}' created successfully.")
            return True
        return False

    except Exception as e:
        print(f"Error: {str(e)}")
        return False        