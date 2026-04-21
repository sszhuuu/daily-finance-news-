import os

# List of required environment variables
required_env_vars = [
    'DATABASE_URL',
    'API_KEY',
    'ENVIRONMENT',
    'USER',
]  

# Function to check environment variables
def check_env_vars():
    missing_vars = []
    for var in required_env_vars:
        if os.environ.get(var) is None:
            missing_vars.append(var)

    if missing_vars:
        print(f'Missing required environment variables: {', '.join(missing_vars)}')
        return False

    print('All required environment variables are configured.')
    return True

if __name__ == '__main__':
    check_env_vars()