"""Email service using Resend"""
import os
from typing import Optional
import resend

# Configure Resend API key
resend.api_key = os.getenv("RESEND_API_KEY", "")

def send_verification_email(to_email: str, verification_token: str, user_name: Optional[str] = None) -> bool:
    """Send email verification email using Resend"""
    if not resend.api_key:
        print(f"[WARNING] RESEND_API_KEY not set. Email would be sent to: {to_email}")
        print(f"          Verification link: http://localhost:3000/auth/verify-email?token={verification_token}")
        return True  # Return True in development mode

    display_name = user_name or to_email.split('@')[0]
    verification_url = f"http://localhost:3000/verify-email?token={verification_token}"

    try:
        resend.Emails.send({
            "from": "FlowTask <onboarding@flowtask.dev>",
            "to": to_email,
            "subject": "✓ Verify your FlowTask account",
            "html": f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; }}
                    .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                    .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
                    .content {{ background: #f9fafb; padding: 30px; border-radius: 0 0 10px 10px; }}
                    .button {{ display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white !important; padding: 15px 40px; text-decoration: none; border-radius: 8px; font-weight: bold; margin: 20px 0; }}
                    .footer {{ text-align: center; color: #6b7280; font-size: 14px; margin-top: 30px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1 style="margin: 0; font-size: 32px;">✓ FlowTask</h1>
                        <p style="margin: 10px 0 0 0; opacity: 0.9;">Effortless Productivity, Beautiful Design</p>
                    </div>
                    <div class="content">
                        <h2>Welcome to FlowTask, {display_name}!</h2>
                        <p>Thanks for signing up. You're one step away from transforming your productivity.</p>
                        <p>Click the button below to verify your email and activate your account:</p>
                        <div style="text-align: center;">
                            <a href="{verification_url}" class="button">Verify Email Address</a>
                        </div>
                        <p style="color: #6b7280; font-size: 14px;">Or copy and paste this link into your browser:</p>
                        <p style="background: white; padding: 10px; border-radius: 5px; word-break: break-all; font-size: 12px;">{verification_url}</p>
                        <p style="margin-top: 30px; color: #6b7280; font-size: 14px;">This link will expire in 24 hours.</p>
                    </div>
                    <div class="footer">
                        <p>Powered by <strong>Syeda Alishba Fatima</strong></p>
                        <p>&copy; 2025 FlowTask. All rights reserved.</p>
                    </div>
                </div>
            </body>
            </html>
            """
        })
        return True
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
        return False


def send_welcome_email(to_email: str, user_name: Optional[str] = None) -> bool:
    """Send welcome email after verification"""
    if not resend.api_key:
        print(f"[WARNING] RESEND_API_KEY not set. Welcome email would be sent to: {to_email}")
        return True

    display_name = user_name or to_email.split('@')[0]

    try:
        resend.Emails.send({
            "from": "FlowTask <hello@flowtask.dev>",
            "to": to_email,
            "subject": "🎉 Welcome to FlowTask!",
            "html": f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; }}
                    .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                    .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
                    .content {{ background: #f9fafb; padding: 30px; border-radius: 0 0 10px 10px; }}
                    .feature {{ background: white; padding: 15px; margin: 10px 0; border-radius: 8px; border-left: 4px solid #667eea; }}
                    .button {{ display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white !important; padding: 15px 40px; text-decoration: none; border-radius: 8px; font-weight: bold; margin: 20px 0; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1 style="margin: 0; font-size: 32px;">🎉 You're All Set!</h1>
                    </div>
                    <div class="content">
                        <h2>Welcome aboard, {display_name}!</h2>
                        <p>Your FlowTask account is now active. Here's what you can do:</p>

                        <div class="feature">
                            <strong>🎯 Smart Organization</strong>
                            <p style="margin: 5px 0 0 0;">Priorities, tags, advanced filtering, and instant search</p>
                        </div>

                        <div class="feature">
                            <strong>✨ 3D Visual Effects</strong>
                            <p style="margin: 5px 0 0 0;">Stunning glassmorphism with 60fps animations</p>
                        </div>

                        <div class="feature">
                            <strong>🌙 Perfect Dark Mode</strong>
                            <p style="margin: 5px 0 0 0;">Flicker-free themes with system detection</p>
                        </div>

                        <div style="text-align: center;">
                            <a href="http://localhost:3000/dashboard" class="button">Go to Dashboard</a>
                        </div>
                    </div>
                    <div style="text-align: center; color: #6b7280; font-size: 14px; margin-top: 30px;">
                        <p>Powered by <strong>Syeda Alishba Fatima</strong></p>
                        <p>&copy; 2025 FlowTask. All rights reserved.</p>
                    </div>
                </div>
            </body>
            </html>
            """
        })
        return True
    except Exception as e:
        print(f"[ERROR] Failed to send welcome email: {e}")
        return False
