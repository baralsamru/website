from flask import Flask, request, render_template_string
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Initialize the database
def init_db():
    with sqlite3.connect("newsletter.db") as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS subscribers (email TEXT UNIQUE)''')
        conn.commit()

init_db()

# Home route with embedded HTML template
@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Sammie's Bookworld</title>
      <link rel="stylesheet" href="styles.css">
      <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
    </head>
    <body>
      <header>
        <h1>Sammie's Bookworld</h1>
        <nav>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="books.html">Books</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </nav>
      </header>
      <main id="home">
        <p>Welcome to Sammie's Bookworld, a haven for book lovers and literary enthusiasts!</p>
        <section class="poem">
          <h2>Featured Poem</h2>
          <p><strong>Life and Death</strong></p>
          <p>
            Why do people love life and hate the death? <br>
            We wish our loved ones reach each place safely,  <br>
            Yet when they reach their final destination,  <br>
            We curse it. <br>
            Why the tears of grief?  <br>
            Why not joy that they are where they should be?  <br>
            Life has struggles and pain, death has peace, <br>
            Yet, we cherish life and dread death. <br>
            Earthly destinations excite us, <br>
            And here we are fearing death's embrace.
          </p>
          <p>
            How can we adore the journey, yet abhor the destination? <br>
            Perhaps it's the mystery, the unknown's silent provocation. <br>
            Life, with its vibrant chaos, its colors so vivid and bright, <br>
            It captivates our senses, fills our days and our nights.
          </p>
          <p>
            But death, oh death, is a passage unseen, <br>
            A realm beyond our grasp, where the answers convene. <br>
            In life, we find purpose, in love and in pain, <br>
            Yet death's silent calling, we struggle to explain. <br>
            -Sammie
          </p>
        </section>
        
        <section class="newsletter">
          <h2>Subscribe to Our Newsletter</h2>
          <p>Stay updated with the latest news, articles, and events from Sammie's Bookworld.</p>
          <form action="/signup" method="post">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <input type="submit" value="Sign Up">
          </form>
        </section>
        
        <!-- Other sections -->
      </main>
      <footer>
        <p>&copy; 2024 Samrachana Baral. All rights reserved.</p>
      </footer>
    </body>
    </html>
    ''')

# Sign-up route
@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    with sqlite3.connect("newsletter.db") as conn:
        try:
            conn.execute("INSERT INTO subscribers (email) VALUES (?)", (email,))
            conn.commit()
            send_confirmation_email(email)
            return "Thank you for signing up! A confirmation email has been sent to your email address."
        except sqlite3.IntegrityError:
            return "You are already subscribed."

# Function to send confirmation email
def send_confirmation_email(to_email):
    from_email = "your_email@example.com"
    from_password = "your_password"
    smtp_server = "smtp.example.com"
    smtp_port = 587

    subject = "Subscription Confirmation"
    html_content = '''
    <h1>Thank you for subscribing to Sammie's Bookworld Newsletter!</h1>
    <p>We're excited to have you with us.</p>
    '''

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    part = MIMEText(html_content, "html")
    msg.attach(part)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())

if __name__ == "__main__":
    app.run(debug=True)
