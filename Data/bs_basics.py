from bs4 import BeautifulSoup()
html = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>title</title>
  </head>
  <body>
  
  </body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")
print(soup)