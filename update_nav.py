import os
import re

def update_nav():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Fix mobile nav which was missed
        pattern_mobile = r'(<a href="gallery.html"[^>]*>Gallery</a>)(\s*)(<div class="mobile-dropdown">[\s\S]*?Dashboard[\s\S]*?</div>\s*</div>)(\s*)(<a href="contact.html"[^>]*>Contact</a>)'
        if re.search(pattern_mobile, content):
            content = re.sub(pattern_mobile, r'\1\2\5\4\3', content)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated Mobile {filename}')

if __name__ == '__main__':
    update_nav()
