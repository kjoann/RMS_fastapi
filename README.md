# Retail Management System

This is a FastAPI-based **Retail Management System** designed to handle operations for retail shops, including managing **Products**, **Inventory**, **Customers**, and **Orders**. The application integrates a **MySQL database** and features a **Bootstrap-styled frontend** for ease of use.

---

## Features

- **Products Management:** Add, update, delete, and view products.
- **Inventory Tracking:** Monitor stock levels and track availability.
- **Customer Records:** Maintain customer details, including their locations.
- **Order Management:** Record and manage customer orders with real-time calculations.
- **Database Integration:** Uses MySQL for robust and scalable data storage.
- **Frontend Design:** Styled with Bootstrap for a clean and responsive UI.

---

## Project Setup

### Prerequisites

1. **Python 3.9+** must be installed.
2. **MySQL Server** must be installed and running.
3. A virtual environment is recommended.

---

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/kjoann/RMS_fastapi.git
   cd RMS_fastapi
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the MySQL Database:**

   - Create a new database in MySQL:
     ```sql
     CREATE DATABASE retail_management;
     ```
   - Update the `.venv` file with your database credentials:
     ```env
     DATABASE_URL=mysql+pymysql://username:password@localhost/retail_management
     ```

5. **Run the Application:**

   ```bash
   uvicorn main:app --reload
   ```

6. **Access the App:**
   Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Project Structure

```plaintext
RMS_fastapi/
│
├── main.py                # Entry point for FastAPI app
├── apps/                  # Contains individual apps (Products, Inventory, etc.)
│   ├── products/
│   ├── inventory/
│   ├── customers/
│   └── orders/
├── templates/             # HTML templates for frontend
├── static/                # Static files (CSS, JS, images)
├── .venv                  # Environment variables file
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## Future Enhancements

- **Authentication:** Add user roles (e.g., admin, staff) with login/logout functionality.
- **Stock Alerts:** Notify users when inventory is low.
- **Reports:** Generate detailed sales and inventory reports.
- **Payment Integration:** Link orders with payment gateways.

---

## License

This project is licensed under the **MIT License**. Feel free to use and modify as needed.

---

## Author

Created by [Joanna](https://github.com/kjoann)

