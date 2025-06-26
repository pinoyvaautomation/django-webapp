#!/usr/bin/env python3
"""
Generate a secure SECRET_KEY for Django deployment on Render
Usage: python generate_secret_key.py
"""

from django.core.management.utils import get_random_secret_key

def generate_secret_key():
    """Generate and display a secure Django SECRET_KEY"""
    secret_key = get_random_secret_key()
    
    print("=" * 60)
    print("DJANGO SECRET KEY GENERATOR")
    print("=" * 60)
    print("\nYour new SECRET_KEY:")
    print(f"\n{secret_key}\n")
    print("=" * 60)
    print("IMPORTANT:")
    print("1. Copy this key and add it to your Render environment variables")
    print("2. Key: SECRET_KEY")
    print("3. Value: [paste the key above]")
    print("4. Keep this key secure and never commit it to version control!")
    print("=" * 60)
    
    return secret_key

if __name__ == "__main__":
    try:
        generate_secret_key()
    except ImportError:
        print("Error: Django not found. Please install Django first:")
        print("pip install django")
    except Exception as e:
        print(f"Error generating secret key: {e}") 