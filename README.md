# Vendor Management System API

Welcome to the Vendor Management System API! This API is built using Django and Django Rest Framework, providing functionality to manage vendors, track purchase orders, and evaluate vendor performance.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following software installed on your machine:

- Python (>=3.6)
- Pipenv (optional but recommended for managing dependencies)

### Installation

1. Clone the repository:

   ```bash
git clone https://github.com/SatyarthAgrahari/Vendor_Management_System.git
2. Change into the project directory:

   ```bash
cd vendor_management_system
3. Create a virtual environment:

   ```bash
vitualenv myvenv
4. Activate the virtual environment:

   ```bash
.\myvenv\Scripts\activate
5. Install dependencies:

   ```bash
pip install -r requirements.txt
6. Load initial data (optional):

   ```bash
python manage.py loaddata initial_data.json
## Usage
Run the development server:

   ```bash
python manage.py runserver
The API will be available at http://127.0.0.1:8000/api/.
### API Endpoints
* Vendor Profiles: /api/vendors/
* Purchase Orders: /api/purchase_orders/
* Vendor Performance: /api/vendors/{vendor_id}/performance/
### Token Authentication:
To use authenticated endpoints, obtain the data:

   ```bash
http "http://127.0.0.1:8000/api/vendors/1/" "Authorization: Token {your_token}"





