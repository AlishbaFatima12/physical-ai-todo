"""Test email sending with Resend"""
import sys
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_email.py your.email@example.com")
        sys.exit(1)

    test_email = sys.argv[1]

    # Check if API key is set
    api_key = os.getenv("RESEND_API_KEY", "")
    if not api_key or api_key.startswith("re_123456789"):
        print("❌ RESEND_API_KEY not configured!")
        print("\nTo fix:")
        print("1. Go to https://resend.com and sign up")
        print("2. Get your API key from https://resend.com/api-keys")
        print("3. Add to backend/.env:")
        print("   RESEND_API_KEY=re_your_actual_key_here")
        sys.exit(1)

    print(f"✓ API key found: {api_key[:10]}...")

    # Import and test
    from app.auth.email_service import send_verification_email

    print(f"\nSending test verification email to: {test_email}")

    result = send_verification_email(
        to_email=test_email,
        verification_token="test_token_12345",
        user_name="Test User"
    )

    if result:
        print("\n✅ Email sent successfully!")
        print(f"Check inbox: {test_email}")
        print("\nIf you don't see it:")
        print("- Check spam folder")
        print("- Check Resend logs: https://resend.com/logs")
        print("- Verify domain is configured correctly")
    else:
        print("\n❌ Email sending failed!")
        print("Check backend console for error details")
