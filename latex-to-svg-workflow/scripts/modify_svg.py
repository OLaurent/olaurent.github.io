#!/usr/bin/env python3

import sys
import re
from xml.etree import ElementTree as ET

def modify_svg(svg_file):
    """
    Perform modifications on the SVG file:
    1. Add style="display: block; margin: 0 auto;" to the SVG tag
    2. Replace #000 with #3e8ed0
    3. Remove paths that have fill='#fff' attribute
    4. Add fill:#3e8ed0; in front of font-family keyword
    """
    # Read the file content
    with open(svg_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add style attribute to the SVG tag
    content = re.sub(r'<svg ', '<svg style="display: block; margin: 0 auto;" ', content)
    
    # 2. Replace #000 with #3e8ed0
    content = content.replace('#000', '#3e8ed0')
    
    # 3. Remove paths with fill='#fff'
    # This requires XML parsing, but we'll use regex for simplicity
    # Note: This is a simplified approach and might not catch all cases
    content = re.sub(r'<path[^>]*fill=\'#fff\'[^>]*/>|<path[^>]*fill=\'#fff\'.*?</path>', '', content)
    
    # 4. Add fill:#3e8ed0; before font-family
    content = re.sub(r'\{font-family', r'{fill:#3e8ed0;font-family', content)
    
    # Write the modified content back to the file
    with open(svg_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python modify_svg.py <svg_file>")
        sys.exit(1)
    
    svg_file = sys.argv[1]
    modify_svg(svg_file)
    print(f"Successfully modified {svg_file}")