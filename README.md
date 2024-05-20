# Backend Repository for My Portfolio

Welcome to the backend repository for my portfolio! This project serves as the backbone of my personal website, showcasing my journey and skills as an aspiring Backend Developer. Developed with Django, it integrates various services and databases to provide a seamless and dynamic experience.

## Features

- **Django Framework**: Robust and scalable backend developed using Django, ensuring security and performance.
- **RESTful API**: Efficient and well-documented API endpoints for data retrieval and manipulation, built using Django REST Framework.
- **Database Integration**: Utilizes PostgreSQL for reliable and efficient data storage and retrieval.
- **Cloudinary Integration**: Seamlessly handles media uploads and management using Cloudinary, ensuring fast and secure access to images and videos.
- **User Authentication**: Implements secure user authentication and authorization mechanisms with Django's built-in authentication system.
- **Admin Interface**: Easy-to-use admin interface for managing content, built with Django Admin.
- **Environment Configuration**: Sensitive information managed through `.env` files and `python-decouple` for secure and flexible environment settings.

## Technologies Used

- **Django**: High-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework**: Powerful and flexible toolkit for building Web APIs.
- **PostgreSQL**: Advanced, open-source relational database.
- **Cloudinary**: Cloud-based service for image and video management.
- **Docker**: Containerization platform to ensure consistent development environments.
- **Git**: Version control system for tracking changes and collaborating with others.

## Getting Started

To get a local copy up and running, follow these simple steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mikiejoe/portfolio-backend.git
   cd portfolio-backend
2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Set up the environment variables:**
<br>
Create a .env file in the root directory and add your configuration values.
   ```bash
    CLOUD_NAME =
    API_KEY = 
    API_SECRET = 
    DB_NAME =
    DB_PASSWORD =
    DB_HOST =
    DB_PORT = 5432

5. **Run the database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

6. **Start the development server:**
   ```bash
   python manage.py runserver


## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. **Fork the Project**
2. **Create your Feature Branch (git checkout -b feature/AmazingFeature)**
3. **Commit your Changes (git commit -m 'Add some AmazingFeature')**
4. **Push to the Branch (git push origin feature/AmazingFeature)**
5. **Open a Pull Request**

