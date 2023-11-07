# User Registration and Login Flask Application

This is a simple Flask web application that allows users to register, log in, and access a dashboard page.

## Features

- User Registration: Users can create an account with a unique username and a securely hashed password.
- User Login: Registered users can log in using their credentials.
- Dashboard: Once logged in, users can access a dashboard page.
- Logout: Users can log out from their accounts.
- Input Validation: User input is validated to ensure data integrity.

## Technologies Used

- Flask: A micro web framework for Python.
- SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- Flask-Login: An extension for managing user sessions.
- Flask-WTF: A Flask extension for integrating WTForms, a library for form handling.
- Flask-Bcrypt: A Flask extension for password hashing.
- SQLite: A lightweight, serverless database engine used for data storage.

## Getting Started

1. Clone the repository to your local machine:

   ```shell
   git clone <https://github.com/Kenneth732/JWT-AUTH-FLASK.git>
   ```

2. Set up a virtual environment and install the required dependencies:

   ```shell
   cd project-directory
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   pip install -r requirements.txt
   pip install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator
   ```

3. Create the database:

   ```shell
   python
   from app import db
   db.create_all()
   ```

4. Start the Flask application:

   ```shell
   python app.py
   ```

5. Open a web browser and access the application at [http://localhost:5000](http://localhost:5000).

## Usage

1. Register: Click on the "Register" link to create a new user account.

2. Login: Once registered, log in using your credentials.

3. Dashboard: After logging in, you can access the dashboard page.

4. Logout: Click on the "Logout" link to log out.

## Contributing

Contributions are welcome. If you'd like to make improvements or fix issues, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and test them.
4. Submit a pull request to the original repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, please feel free to contact [Kenneth] [Mburu] at [kenabdi21@gmail.com].

## Acknowledgments

- This project was inspired by a passion for web development and a desire to create a secure and user-friendly user registration and login system.

- Special thanks to the Flask and Python communities for their invaluable support, resources, and contributions to the open-source software ecosystem. This project wouldn't have been possible without the wealth of knowledge and tools provided by these communities.