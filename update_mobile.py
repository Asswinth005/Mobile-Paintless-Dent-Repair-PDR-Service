import os
import re

files = ['about.html', 'contact.html', 'gallery.html', 'price.html', 'service.html']
for f in files:
  with open(f, 'r', encoding='utf-8') as file:
    content = file.read()
  pattern = r'(<a\s+href="gallery.html"[^>]*>Gallery</a>)(\s*)(<div class="mobile-dropdown">[\s\S]*?Dashboard[\s\S]*?Admin</a></div>\s*</div>)(\s*)(<a\s+href="contact.html"[^>]*>Contact</a>)'
  if re.search(pattern, content):
    content = re.sub(pattern, r'\1\2\5\4\3', content)
    with open(f, 'w', encoding='utf-8') as out:
      out.write(content)
    print('Updated ' + f)
  else:
    print('Failed ' + f)
