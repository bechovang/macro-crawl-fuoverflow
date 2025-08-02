#!/usr/bin/env python3
"""
Setup script for Google Slides Crawler
Helps users install dependencies and configure the project
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True


def check_chrome():
    """Check if Chrome browser is installed"""
    chrome_paths = [
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    ]
    
    for path in chrome_paths:
        if os.path.exists(path):
            print(f"✅ Chrome found at: {path}")
            return True
    
    print("⚠️  Chrome not found in common locations")
    print("Please install Google Chrome manually")
    return False


def create_virtual_environment():
    """Create and activate virtual environment"""
    venv_path = Path("venv")
    
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True
    
    try:
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return False


def install_dependencies():
    """Install Python dependencies"""
    try:
        print("Installing dependencies...")
        
        # Determine the pip command based on OS
        if os.name == 'nt':  # Windows
            pip_cmd = "venv\\Scripts\\pip"
        else:  # Unix/Linux/macOS
            pip_cmd = "venv/bin/pip"
        
        # Upgrade pip first
        subprocess.run([pip_cmd, "install", "--upgrade", "pip"], check=True)
        
        # Install requirements
        subprocess.run([pip_cmd, "install", "-r", "requirements.txt"], check=True)
        
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False


def create_env_file():
    """Create .env file from template"""
    env_file = Path(".env")
    env_example = Path("env.example")
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    if not env_example.exists():
        print("⚠️  env.example not found, creating basic .env file")
        create_basic_env_file()
        return True
    
    try:
        shutil.copy(env_example, env_file)
        print("✅ .env file created from template")
        print("⚠️  Please edit .env file with your actual credentials")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False


def create_basic_env_file():
    """Create a basic .env file"""
    env_content = """# Google Slides Crawler Environment Configuration
# Please fill in your actual values

# Required: Google Cloud Vision API credentials
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json

# Optional: OpenAI API key for text formatting
OPENAI_API_KEY=your_openai_api_key_here

# Browser Configuration
CHROME_HEADLESS=true
WINDOW_SIZE=1920,1080

# Timing Configuration
SLIDE_DELAY=2
LOAD_TIMEOUT=10
OCR_TIMEOUT=30

# Output Configuration
OUTPUT_DIR=./output
SCREENSHOT_FORMAT=png
TEXT_ENCODING=utf-8

# Processing Configuration
MAX_RETRIES=3
BATCH_SIZE=5
ENABLE_AI_FORMATTING=true
"""
    
    with open(".env", "w") as f:
        f.write(env_content)
    
    print("✅ Basic .env file created")
    print("⚠️  Please edit .env file with your actual credentials")


def create_output_directory():
    """Create output directory"""
    output_dir = Path("output")
    if not output_dir.exists():
        output_dir.mkdir()
        print("✅ Output directory created")
    else:
        print("✅ Output directory already exists")


def check_google_cloud_setup():
    """Check if Google Cloud credentials are configured"""
    creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    
    if not creds_path:
        print("⚠️  GOOGLE_APPLICATION_CREDENTIALS not set")
        print("Please set this environment variable to your credentials file path")
        return False
    
    if not os.path.exists(creds_path):
        print(f"⚠️  Credentials file not found: {creds_path}")
        print("Please download your credentials from Google Cloud Console")
        return False
    
    print(f"✅ Google Cloud credentials found: {creds_path}")
    return True


def run_tests():
    """Run basic tests"""
    try:
        print("Running tests...")
        subprocess.run([sys.executable, "test_main.py"], check=True)
        print("✅ Tests passed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Tests failed: {e}")
        return False


def print_next_steps():
    """Print next steps for the user"""
    print("\n" + "="*50)
    print("🎉 Setup completed!")
    print("="*50)
    print("\nNext steps:")
    print("1. Edit .env file with your actual credentials")
    print("2. Set up Google Cloud Vision API:")
    print("   - Go to Google Cloud Console")
    print("   - Enable Vision API")
    print("   - Create service account and download credentials")
    print("3. (Optional) Set up OpenAI API for text formatting")
    print("4. Activate virtual environment:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\activate")
    else:  # Unix/Linux/macOS
        print("   source venv/bin/activate")
    print("5. Run the crawler:")
    print("   python main.py")
    print("\nFor more information, see README.md")


def main():
    """Main setup function"""
    print("🚀 Google Slides Crawler Setup")
    print("="*40)
    
    # Check system requirements
    if not check_python_version():
        return False
    
    if not check_chrome():
        print("⚠️  Please install Google Chrome manually")
    
    # Create virtual environment
    if not create_virtual_environment():
        return False
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Create configuration files
    create_env_file()
    create_output_directory()
    
    # Check Google Cloud setup
    check_google_cloud_setup()
    
    # Run tests (optional)
    try:
        run_tests()
    except Exception as e:
        print(f"⚠️  Tests skipped: {e}")
    
    # Print next steps
    print_next_steps()
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 