from .auth_routes import register_auth_routes
from .question_routes import register_question_routes
from .user_routes import register_user_routes
from .main_routes import register_main_routes

def register_routes(app, db, bcrypt):
    """
    Register all routes for the application.
    
    This function imports and registers route modules for different parts of the application:
    - Authentication routes (login, signup, logout)
    - Question routes (create, view, edit, vote)
    - User routes (user profile)
    - Main routes (index, dashboard)
    
    Args:
        app: The Flask application instance
        db: The SQLAlchemy database instance
        bcrypt: The Bcrypt instance for password hashing
    """
    # Register authentication routes
    register_auth_routes(app, db, bcrypt)
    
    # Register question routes
    register_question_routes(app, db)
    
    # Register user routes
    register_user_routes(app, db)
    
    # Register main routes
    register_main_routes(app, db)
