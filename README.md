<h1 align="center">📝 Would You Rather 📝</h1>
<h2 align="center">Create and Vote on Engaging Dilemmas</h2>

> [!NOTE]
> 
> Would You Rather is an interactive web application that allows users to create, share, and vote on "Would You Rather" questions. Users can sign up, create their own dilemmas, vote on others' questions, and track statistics on their profile. Built with Flask, SQLAlchemy, and styled with Tailwind CSS, this application provides a fun and engaging way to explore hypothetical choices.

## 🌟 Features

> **Would You Rather** features intro:

- **User Authentication** – Secure signup and login system with personalized user profiles
- **Create Questions** – Easily create your own "Would You Rather" dilemmas with option A and B
- **Vote System** – Cast your vote on questions and see real-time statistics
- **Categories** – Organize questions with custom categories for better discovery
- **User Profiles** – View your activity, statistics, and voting preferences
- **Responsive Design** – Beautiful, modern UI that works on all devices

## 💻 Installation

> You can set up **Would You Rather** with these commands:

###### terminal

```bash
# Clone the repository
git clone https://github.com/k0msenapati/would-you-rather
cd would-you-rather

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up the database
flask db init
flask db migrate
flask db upgrade

# Run the application
python run.py
```

## 🚀 Getting Started

After installation, follow these steps to get started:

1. **Access the Application**
   - Open your browser and navigate to `http://localhost:5000`

2. **Create an Account**
   - Click on "Sign Up" to create a new account
   - Fill in your name, username, email, and password

3. **Create Your First Question**
   - After logging in, click on "Create New Question" button
   - Enter two options for your "Would You Rather" question
   - Add optional categories to help organize your question

4. **Vote and Explore**
   - Browse questions on the dashboard
   - Vote on questions by selecting your preferred option
   - View statistics and results for each question

## 👤 Author

<table>
  <tbody>
    <tr>
        <td align="center" valign="top" width="14.28%"><a href="https://github.com/k0msenapati"><img src="https://github.com/k0msenapati.png?s=100" width="130px;" alt="k0msenapati"/></a><br /><a href="https://github.com/k0msenapati"<h4><b>K Om Senapati</b></h3></a></td>
    </tr>
  </tbody>
</table>

---

<h2 align="center">📄 License</h2>

<p align="center">
<strong>Would You Rather</strong> is licensed under the <code>Unlicense</code> License. See the <a href="https://github.com/k0msenapati/would-you-rather/blob/main/LICENSE">LICENSE</a> file for more details.
</p>

---

<p align="center">
    <strong>🌟 If you find this project helpful, please give it a star on GitHub! 🌟</strong>
</p>

# Thanks to Pheonix Coder for the [starter template](https://github.com/pheonix-coder/flask-minimal-template)