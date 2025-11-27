# Exercise 27: Custom Exceptions - SOLUTION
# Difficulty: Intermediate-
# Concepts: Raising exceptions, Custom exceptions, Exception classes

# SOLUTION
print("CUSTOM EXCEPTIONS DEMONSTRATION")
print("=" * 60)

# 1. CREATING CUSTOM EXCEPTIONS
print("1. BASIC CUSTOM EXCEPTION")
print("-" * 60)

class InvalidAgeError(Exception):
    """Custom exception for invalid age values."""
    pass

def validate_age(age):
    """Validate age with custom exception."""
    if not isinstance(age, int):
        raise InvalidAgeError(f"Age must be an integer, got {type(age).__name__}")

    if age < 0:
        raise InvalidAgeError(f"Age cannot be negative: {age}")

    if age > 120:
        raise InvalidAgeError(f"Age cannot exceed 120: {age}")

    return True

# Test age validation
test_ages = [25, -5, 150, "thirty"]

for age in test_ages:
    try:
        validate_age(age)
        print(f"Age {age}: Valid")
    except InvalidAgeError as e:
        print(f"Age {age}: Error - {e}")
print()

# 2. CUSTOM EXCEPTION WITH ATTRIBUTES
print("2. CUSTOM EXCEPTION WITH ATTRIBUTES")
print("-" * 60)

class ValidationError(Exception):
    """Exception with additional context."""

    def __init__(self, message, field_name=None, invalid_value=None):
        super().__init__(message)
        self.field_name = field_name
        self.invalid_value = invalid_value
        self.message = message

    def __str__(self):
        if self.field_name:
            return f"ValidationError in '{self.field_name}': {self.message} (value: {self.invalid_value})"
        return f"ValidationError: {self.message}"

def validate_username(username):
    """Validate username with detailed exception."""
    if len(username) < 3:
        raise ValidationError(
            "Username too short (minimum 3 characters)",
            field_name="username",
            invalid_value=username
        )

    if not username.isalnum():
        raise ValidationError(
            "Username must be alphanumeric",
            field_name="username",
            invalid_value=username
        )

    return True

# Test username validation
test_usernames = ["alice", "ab", "user@123"]

for username in test_usernames:
    try:
        validate_username(username)
        print(f"Username '{username}': Valid")
    except ValidationError as e:
        print(f"Username '{username}': {e}")
        print(f"  Field: {e.field_name}")
        print(f"  Value: {e.invalid_value}")
print()

# 3. MULTIPLE CUSTOM EXCEPTIONS
print("3. MULTIPLE CUSTOM EXCEPTIONS")
print("-" * 60)

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""
    pass

class NegativeAmountError(Exception):
    """Raised when amount is negative."""
    pass

class AccountLockedError(Exception):
    """Raised when account is locked."""
    pass

class BankAccount:
    """Simple bank account with custom exceptions."""

    def __init__(self, balance=0, locked=False):
        self.balance = balance
        self.locked = locked

    def withdraw(self, amount):
        """Withdraw money with validation."""
        if self.locked:
            raise AccountLockedError("Account is locked. Contact support.")

        if amount < 0:
            raise NegativeAmountError(f"Amount cannot be negative: {amount}")

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds. Balance: ${self.balance:.2f}, "
                f"Requested: ${amount:.2f}"
            )

        self.balance -= amount
        return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"

# Test bank account
account = BankAccount(balance=100.0)

transactions = [
    ("withdraw", 30.0),
    ("withdraw", 150.0),
    ("withdraw", -50.0),
]

for operation, amount in transactions:
    try:
        result = account.withdraw(amount)
        print(f"Success: {result}")
    except (InsufficientFundsError, NegativeAmountError, AccountLockedError) as e:
        print(f"Error: {type(e).__name__} - {e}")

# Test locked account
print("\nTesting locked account:")
locked_account = BankAccount(balance=100.0, locked=True)
try:
    locked_account.withdraw(10.0)
except AccountLockedError as e:
    print(f"Error: {e}")
print()

"""
EXPLANATION:
1. Custom exceptions inherit from Exception class
2. Define custom exception: class MyError(Exception): pass
3. Raise exceptions with: raise MyError("message")
4. Can add __init__ to store additional data
5. Can override __str__ for custom error message format
6. Use specific exceptions for different error types
7. Catch custom exceptions like built-in ones

Key Concepts:
- Custom exceptions make code more readable and maintainable
- They provide better error handling and debugging
- Can include context-specific information
- Follow naming convention: end with "Error" or "Exception"
- Keep exception names descriptive and specific
"""

# Extension solution: User registration system
print("\n--- EXTENSION SOLUTION: REGISTRATION SYSTEM ---")

# Exception hierarchy
class RegistrationError(Exception):
    """Base exception for registration errors."""
    pass

class InvalidEmailError(RegistrationError):
    """Invalid email format."""
    pass

class InvalidPasswordError(RegistrationError):
    """Invalid password."""
    pass

class DuplicateUsernameError(RegistrationError):
    """Username already exists."""
    pass

class UserRegistrationSystem:
    """User registration with comprehensive validation."""

    def __init__(self):
        self.users = {}  # username -> user_data

    def validate_email(self, email):
        """Validate email format."""
        if '@' not in email:
            raise InvalidEmailError("Email must contain '@'")

        if email.count('@') != 1:
            raise InvalidEmailError("Email must contain exactly one '@'")

        local, domain = email.split('@')

        if not local or not domain:
            raise InvalidEmailError("Email format invalid")

        if '.' not in domain:
            raise InvalidEmailError("Email domain must contain '.'")

        return True

    def validate_password(self, password):
        """Validate password strength."""
        if len(password) < 8:
            raise InvalidPasswordError(
                "Password must be at least 8 characters long"
            )

        if not any(c.isupper() for c in password):
            raise InvalidPasswordError(
                "Password must contain at least one uppercase letter"
            )

        if not any(c.islower() for c in password):
            raise InvalidPasswordError(
                "Password must contain at least one lowercase letter"
            )

        if not any(c.isdigit() for c in password):
            raise InvalidPasswordError(
                "Password must contain at least one digit"
            )

        return True

    def register_user(self, username, email, password):
        """Register a new user with validation."""
        try:
            # Validate username
            if username in self.users:
                raise DuplicateUsernameError(
                    f"Username '{username}' is already taken"
                )

            if len(username) < 3:
                raise ValidationError(
                    "Username must be at least 3 characters",
                    field_name="username",
                    invalid_value=username
                )

            # Validate email
            self.validate_email(email)

            # Validate password
            self.validate_password(password)

            # Register user
            self.users[username] = {
                'email': email,
                'password': password  # In real app, hash this!
            }

            return f"Successfully registered user: {username}"

        except RegistrationError as e:
            return f"Registration failed: {type(e).__name__} - {e}"
        except ValidationError as e:
            return f"Registration failed: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"

# Test registration system
print("User Registration System\n")
registration = UserRegistrationSystem()

test_users = [
    ("alice", "alice@email.com", "Password123"),
    ("bob", "invalid-email", "Password123"),
    ("charlie", "charlie@email.com", "weak"),
    ("diana", "diana@email.com", "NoDigits!"),
    ("alice", "alice2@email.com", "Password123"),  # Duplicate
]

for username, email, password in test_users:
    result = registration.register_user(username, email, password)
    print(f"\nUser: {username}")
    print(f"  {result}")

print(f"\nTotal registered users: {len(registration.users)}")

# Exception chaining
print("\n--- EXCEPTION CHAINING ---")

class DataProcessingError(Exception):
    """Error during data processing."""
    pass

def process_data(data):
    """Process data with exception chaining."""
    try:
        # Simulate some processing
        result = int(data) / 2
        return result
    except ValueError as e:
        # Chain exceptions to preserve error context
        raise DataProcessingError(f"Failed to process data: {data}") from e
    except ZeroDivisionError as e:
        raise DataProcessingError("Division error during processing") from e

# Test exception chaining
print("Testing exception chaining:")
try:
    process_data("not_a_number")
except DataProcessingError as e:
    print(f"Error: {e}")
    print(f"Original cause: {e.__cause__}")

# Advanced: Exception with recovery suggestions
print("\n--- EXCEPTIONS WITH RECOVERY HINTS ---")

class ConfigurationError(Exception):
    """Configuration error with recovery suggestions."""

    def __init__(self, message, config_key=None, suggestion=None):
        super().__init__(message)
        self.config_key = config_key
        self.suggestion = suggestion

    def __str__(self):
        msg = self.args[0]
        if self.config_key:
            msg += f"\n  Configuration key: {self.config_key}"
        if self.suggestion:
            msg += f"\n  Suggestion: {self.suggestion}"
        return msg

def load_config(config_dict):
    """Load configuration with helpful errors."""
    required_keys = ['host', 'port', 'database']

    for key in required_keys:
        if key not in config_dict:
            raise ConfigurationError(
                f"Missing required configuration",
                config_key=key,
                suggestion=f"Add '{key}' to your configuration file"
            )

    if not isinstance(config_dict['port'], int):
        raise ConfigurationError(
            "Invalid port type",
            config_key='port',
            suggestion="Port must be an integer (e.g., 5432)"
        )

    return "Configuration loaded successfully"

# Test configuration loading
print("\nTesting configuration:")
configs = [
    {'host': 'localhost', 'port': 5432, 'database': 'mydb'},
    {'host': 'localhost', 'port': 5432},  # Missing database
    {'host': 'localhost', 'port': '5432', 'database': 'mydb'},  # Wrong type
]

for i, config in enumerate(configs, 1):
    print(f"\nConfig {i}: {config}")
    try:
        result = load_config(config)
        print(f"  {result}")
    except ConfigurationError as e:
        print(f"  Error: {e}")

# Best practices summary
print("\n--- CUSTOM EXCEPTION BEST PRACTICES ---")
print("""
1. Inherit from Exception or a more specific exception type
2. Use descriptive names ending in 'Error' or 'Exception'
3. Create exception hierarchies for related errors
4. Include helpful error messages and context
5. Document what exceptions your functions can raise
6. Don't create exceptions for every error - use built-ins when appropriate
7. Add custom attributes to provide additional context
8. Override __str__ for better error message formatting

Example hierarchy:
class AppError(Exception): pass          # Base
class ValidationError(AppError): pass    # Category
class InvalidEmailError(ValidationError): pass  # Specific
""")
