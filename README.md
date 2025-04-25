# Cab Booking System

A comprehensive web application for managing cab bookings with separate interfaces for administrators, users, guests, and drivers.

## Technology Stack

### Backend
- Python 3.x
- Django Framework
- SQLite/MySQL Database

### Frontend
- HTML5, CSS3, JavaScript
- Bootstrap 4
- jQuery
- SCSS for styling
- Multiple JavaScript libraries:
  - Chart.js for analytics
  - TinyMCE for rich text editing
  - CodeMirror for code editing
  - DataTables for data presentation

## Modules

### 1. Admin Module
**Features:**
- Dashboard with analytics and statistics
- User management system
- Driver management
- Booking management
- Location management
- Vehicle management
- Payment tracking
- Report generation

**Rich Text Editing Capabilities:**
- TinyMCE integration for content management
- Multiple editing modes (classic, inline, distraction-free)
- Code sample plugin support
- Custom plugins integration

### 2. User Module
**Features:**
- User registration and login
- Profile management
- Cab booking interface
- Booking history
- Payment processing
- Feedback system
- Rating system

### 3. Driver Module
**Features:**
- Driver registration and login
- Profile management
- Booking acceptance/rejection
- Trip management
- Payment history
- Performance analytics
- Rating view

### 4. Guest Module
**Features:**
- Homepage view
- Fare estimation
- Service information
- Contact forms
- About us section
- Terms and conditions
- FAQ section

## Installation Steps

1. **Environment Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   npm install
   ```

3. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## Project Structure
```
Project/
├── Admin/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   └── views.py
├── User/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   └── views.py
├── Driver/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   └── views.py
├── Guest/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   │   ├── Admin/
│   │   │   ├── vendors/
│   │   │   ├── js/
│   │   │   └── scss/
│   │   └── Main/
│   └── views.py
└── project/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Key Features

### Admin Dashboard
- Real-time analytics
- User management interface
- Booking tracking system
- Payment management
- Report generation tools
- Content management system

### User Interface
- Responsive design
- Interactive booking system
- Real-time tracking
- Payment integration
- Rating system

### Driver Interface
- Trip management
- Earnings tracking
- Profile management
- Rating system

## Browser Compatibility
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Opera (latest)
- IE10+

## Development Guidelines
- Follow PEP 8 standards for Python code
- Use proper commenting and documentation
- Maintain code consistency
- Regular testing and debugging
- Version control with Git

## Security Features
- CSRF protection
- SQL injection prevention
- XSS protection
- User authentication
- Role-based access control