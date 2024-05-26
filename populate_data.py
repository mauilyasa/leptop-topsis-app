from app import db, Laptop
from app import app  # Assuming 'app' is your Flask application instance

# Create the Flask application context
app.app_context().push()

# Drop all tables and create them again (useful for resetting the database)
db.drop_all()
db.create_all()

# Sample data with various laptop brands
laptops = [
    {"brand": "Lenovo", "model": "ThinkPad X1 Carbon", "price": 21000000, "performance": 9.5, "battery_life": 8.5},
    {"brand": "Lenovo", "model": "Yoga 920", "price": 17000000, "performance": 8.0, "battery_life": 7.5},
    {"brand": "Lenovo", "model": "IdeaPad 320", "price": 10000000, "performance": 6.5, "battery_life": 6.0},
    {"brand": "Asus", "model": "ZenBook 14", "price": 14000000, "performance": 8.0, "battery_life": 8.0},
    {"brand": "Asus", "model": "ROG Strix", "price": 25000000, "performance": 9.0, "battery_life": 6.0},
    {"brand": "Asus", "model": "VivoBook S15", "price": 13000000, "performance": 7.5, "battery_life": 7.0},
    {"brand": "Dell", "model": "XPS 13", "price": 20000000, "performance": 9.0, "battery_life": 8.0},
    {"brand": "Dell", "model": "Inspiron 15", "price": 11500000, "performance": 7.0, "battery_life": 7.5},
    {"brand": "HP", "model": "Spectre x360", "price": 18500000, "performance": 8.5, "battery_life": 7.5},
    {"brand": "HP", "model": "Pavilion 15", "price": 10500000, "performance": 7.0, "battery_life": 7.0},
    {"brand": "Apple", "model": "MacBook Pro 13", "price": 24000000, "performance": 9.5, "battery_life": 8.0},
    {"brand": "Apple", "model": "MacBook Air", "price": 15500000, "performance": 8.5, "battery_life": 9.0},
    {"brand": "Acer", "model": "Aspire 5", "price": 9000000, "performance": 6.0, "battery_life": 6.5},
    {"brand": "Acer", "model": "Swift 3", "price": 12000000, "performance": 7.5, "battery_life": 7.5},
    {"brand": "MSI", "model": "GF63", "price": 14000000, "performance": 8.0, "battery_life": 6.5},
    {"brand": "MSI", "model": "Prestige 14", "price": 17000000, "performance": 8.5, "battery_life": 7.5},
]

# Add laptops to the database
for laptop in laptops:
    new_laptop = Laptop(
        brand=laptop["brand"], 
        model=laptop["model"], 
        price=laptop["price"], 
        performance=laptop["performance"], 
        battery_life=laptop["battery_life"]
    )
    db.session.add(new_laptop)

db.session.commit()

print("Database populated with sample data!")