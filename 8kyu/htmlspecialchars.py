def html_special_chars(data): 
    return data.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace("\"","&quot;")

print(html_special_chars("<h2>Hello World</h2>"))