#!/usr/bin/env python3

"""Test script for baizhi_web_scrape tool."""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tools.baizhi_search import baizhi_web_scrape, has_web_scrape_api_key

def test_web_scrape():
    print(f"Web scrape API key configured: {has_web_scrape_api_key()}")
    
    # Test with a valid URL
    args = {"url": "https://example.com"}
    result = baizhi_web_scrape(args)
    print("Web scrape result:")
    print(result)
    
    # Test with invalid URL (no protocol)
    args = {"url": "example.com"}
    result = baizhi_web_scrape(args)
    print("\nInvalid URL result:")
    print(result)
    
    # Test with empty URL
    args = {"url": ""}
    result = baizhi_web_scrape(args)
    print("\nEmpty URL result:")
    print(result)

if __name__ == "__main__":
    test_web_scrape()