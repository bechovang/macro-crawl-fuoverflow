"""
Test file for Google Slides Crawler
Basic unit tests and integration tests
"""

import unittest
import os
import tempfile
from unittest.mock import Mock, patch, MagicMock
import sys

# Add the current directory to the path so we can import main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import GoogleSlidesCapture
import config


class TestGoogleSlidesCapture(unittest.TestCase):
    """Test cases for GoogleSlidesCapture class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.original_output_dir = config.OUTPUT_DIR
        config.OUTPUT_DIR = self.temp_dir
    
    def tearDown(self):
        """Clean up after tests"""
        config.OUTPUT_DIR = self.original_output_dir
        # Clean up temp directory
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    @patch('main.webdriver.Chrome')
    def test_setup_driver(self, mock_chrome):
        """Test Chrome driver setup"""
        mock_driver = Mock()
        mock_chrome.return_value = mock_driver
        
        capturer = GoogleSlidesCapture(headless=True)
        
        self.assertIsNotNone(capturer.driver)
        self.assertIsNotNone(capturer.wait)
        mock_chrome.assert_called_once()
        
        capturer.close()
    
    @patch('main.webdriver.Chrome')
    def test_setup_driver_headless(self, mock_chrome):
        """Test Chrome driver setup in headless mode"""
        mock_driver = Mock()
        mock_chrome.return_value = mock_driver
        
        capturer = GoogleSlidesCapture(headless=True)
        
        # Check that headless option was added
        chrome_options = mock_chrome.call_args[1]['options']
        self.assertIn('--headless', [opt for opt in chrome_options.arguments])
        
        capturer.close()
    
    @patch('main.webdriver.Chrome')
    def test_close_driver(self, mock_chrome):
        """Test driver cleanup"""
        mock_driver = Mock()
        mock_chrome.return_value = mock_driver
        
        capturer = GoogleSlidesCapture()
        capturer.close()
        
        mock_driver.quit.assert_called_once()
    
    @patch('main.webdriver.Chrome')
    @patch('main.vision.ImageAnnotatorClient')
    def test_ocr_image_success(self, mock_vision_client, mock_chrome):
        """Test successful OCR processing"""
        # Mock the vision client
        mock_client = Mock()
        mock_vision_client.return_value = mock_client
        
        # Mock the OCR response
        mock_response = Mock()
        mock_text_annotation = Mock()
        mock_text_annotation.description = "Test OCR text"
        mock_response.text_annotations = [mock_text_annotation]
        mock_client.document_text_detection.return_value = mock_response
        
        capturer = GoogleSlidesCapture()
        
        # Create a temporary test image
        test_image_path = os.path.join(self.temp_dir, "test.png")
        with open(test_image_path, 'wb') as f:
            f.write(b'fake image data')
        
        result = capturer.ocr_image(test_image_path)
        
        self.assertEqual(result, "Test OCR text")
        capturer.close()
    
    @patch('main.webdriver.Chrome')
    @patch('main.vision.ImageAnnotatorClient')
    def test_ocr_image_failure(self, mock_vision_client, mock_chrome):
        """Test OCR processing failure"""
        # Mock the vision client to raise an exception
        mock_client = Mock()
        mock_vision_client.return_value = mock_client
        mock_client.document_text_detection.side_effect = Exception("OCR failed")
        
        capturer = GoogleSlidesCapture()
        
        # Create a temporary test image
        test_image_path = os.path.join(self.temp_dir, "test.png")
        with open(test_image_path, 'wb') as f:
            f.write(b'fake image data')
        
        result = capturer.ocr_image(test_image_path)
        
        self.assertEqual(result, "")
        capturer.close()
    
    @patch('main.webdriver.Chrome')
    @patch('main.genai.GenerativeModel')
    def test_format_text_with_ai_success(self, mock_gemini_model, mock_chrome):
        """Test successful AI text formatting with Gemini"""
        # Mock Gemini response
        mock_model = Mock()
        mock_gemini_model.return_value = mock_model
        
        mock_response = Mock()
        mock_response.text = "Formatted text"
        mock_model.generate_content.return_value = mock_response
        
        capturer = GoogleSlidesCapture()
        
        result = capturer.format_text_with_ai("Raw text", "Notes")
        
        self.assertEqual(result, "Formatted text")
        capturer.close()
    
    @patch('main.webdriver.Chrome')
    @patch('main.genai.GenerativeModel')
    def test_format_text_with_ai_failure(self, mock_gemini_model, mock_chrome):
        """Test AI text formatting failure with Gemini"""
        # Mock Gemini to raise an exception
        mock_model = Mock()
        mock_gemini_model.return_value = mock_model
        mock_model.generate_content.side_effect = Exception("AI failed")
        
        capturer = GoogleSlidesCapture()
        
        result = capturer.format_text_with_ai("Raw text", "Notes")
        
        # Should fall back to basic formatting
        self.assertIn("Raw text", result)
        self.assertIn("Notes", result)
        capturer.close()
    
    @patch('main.webdriver.Chrome')
    def test_setup_gemini_success(self, mock_chrome):
        """Test successful Gemini setup"""
        mock_driver = Mock()
        mock_chrome.return_value = mock_driver
        
        with patch('main.genai.configure') as mock_configure:
            with patch('main.genai.GenerativeModel') as mock_model:
                capturer = GoogleSlidesCapture()
                
                mock_configure.assert_called_once_with(api_key=config.GEMINI_API_KEY)
                mock_model.assert_called_once_with(config.GEMINI_MODEL)
                
                capturer.close()
    
    @patch('main.webdriver.Chrome')
    def test_setup_gemini_failure(self, mock_chrome):
        """Test Gemini setup failure"""
        mock_driver = Mock()
        mock_chrome.return_value = mock_driver
        
        with patch('main.genai.configure', side_effect=Exception("Gemini setup failed")):
            capturer = GoogleSlidesCapture()
            
            self.assertIsNone(capturer.gemini_model)
            
            capturer.close()


class TestConfig(unittest.TestCase):
    """Test cases for configuration"""
    
    def test_validate_config(self):
        """Test configuration validation"""
        # Test with missing required variables
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(config.validate_config())
        
        # Test with required variables
        with patch.dict(os.environ, {'GOOGLE_APPLICATION_CREDENTIALS': 'test.json'}):
            self.assertTrue(config.validate_config())
    
    def test_get_output_path(self):
        """Test output path generation"""
        test_filename = "test.txt"
        result = config.get_output_path(test_filename)
        
        self.assertIn(config.OUTPUT_DIR, result)
        self.assertIn(test_filename, result)
    
    def test_get_chrome_options(self):
        """Test Chrome options generation"""
        options = config.get_chrome_options()
        
        self.assertIsInstance(options, list)
        self.assertIn(f'--window-size={config.WINDOW_SIZE}', options)
        
        if config.HEADLESS_MODE:
            self.assertIn('--headless', options)


class TestIntegration(unittest.TestCase):
    """Integration tests (require actual setup)"""
    
    @unittest.skip("Requires actual Google Cloud credentials")
    def test_full_pipeline(self):
        """Test the complete processing pipeline"""
        # This test would require actual credentials and a test presentation
        # It's skipped by default but can be run manually
        pass


if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2) 