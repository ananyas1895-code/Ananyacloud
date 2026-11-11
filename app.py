from flask import Flask, render_template_string, request

app = Flask(__name__)

# Shared HTML layout with navigation and basic styling
BASE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto; padding: 0 20px; line-height: 1.6; color: #333; }
        nav { background: #f4f4f4; padding: 12px; border-radius: 6px; margin-bottom: 25px; }
        nav a { margin-right: 15px; text-decoration: none; color: #0066cc; font-weight: bold; }
        nav a:hover { text-decoration: underline; }
        input, textarea { width: 100%; padding: 8px; margin: 8px 0 15px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { background: #0066cc; color: white; padding: 10px 18px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #004c99; }
        .alert { background: #e6f4ea; color: #1e7e34; padding: 12px; border-radius: 4px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
    </nav>
    {{ content | safe }}
</body>
</html>
"""

@app.route("/")
def home():
    page_content = """
    <h1>Welcome to My Website</h1>
    <p>This entire website runs from a single Python file using Flask.</p>
    <p>Click the links in the navigation bar above to explore different routes.</p>
    """
    return render_template_string(BASE_HTML, title="Home", content=page_content)

@app.route("/about")
def about():
    page_content = """
    <h1>About Us</h1>
    <p>Flask is a lightweight Python web framework.</p>
    <p>Using <code>render_template_string</code> lets you prototype quickly without creating separate template folders.</p>
    """
    return render_template_string(BASE_HTML, title="About", content=page_content)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    message_banner = ""
    if request.method == "POST":
        user_name = request.form.get("name")
        message_banner = f'<div class="alert">Thank you, <strong>{user_name}</strong>! Your message has been received.</div>'

    page_content = f"""
    <h1>Contact Us</h1>
    {message_banner}
    <form method="POST">
        <label>Your Name</label>
        <input type="text" name="name" required placeholder="Enter your name">
        
        <label>Message</label>
        <textarea name="message" rows="4" required placeholder="Write your message here..."></textarea>
        
        <button type="submit">Send Message</button>
    </form>
    """
    return render_template_string(BASE_HTML, title="Contact", content=page_content)

if __name__ == "__main__":
    app.run(debug=True)

