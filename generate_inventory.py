"""
generate_inventory.py
Generates a mock inventory dataset (inventory.csv) for the KisanSetu Streamlit prototype.

Columns:
    Farmer_Name          - Name of the listing farmer
    Crop_Type            - Type of crop/produce
    Quantity_KG          - Quantity listed, in kilograms
    Grade                - Quality grade assigned at the Village Hub (A/B/C)
    Current_Mandi_Price  - Current government mandi price (Rs./kg) for that crop
    Hub_Location         - Village Aggregation Hub where produce was registered
"""

import numpy as np
import pandas as pd

# Reproducibility
np.random.seed(42)

N_ROWS = 50

# --- Reference data pools ---------------------------------------------------

FARMER_NAMES = [
    "Ramesh Yadav", "Suresh Kumar", "Anita Devi", "Mohan Lal", "Geeta Sharma",
    "Rajesh Singh", "Kavita Patel", "Vijay Prasad", "Sunita Kumari", "Ashok Verma",
    "Deepak Choudhary", "Pooja Mishra", "Sanjay Rao", "Meena Gupta", "Ravi Shankar",
    "Lakshmi Nair", "Vikram Thakur", "Radha Devi", "Naresh Yadav", "Shanti Bai",
    "Manoj Tiwari", "Usha Rani", "Dinesh Chandra", "Kamla Devi", "Arun Mahato",
    "Sarita Kumari", "Prakash Jha", "Nirmala Devi", "Rakesh Ranjan", "Sushila Devi",
    "Bhola Singh", "Mamta Kumari", "Gopal Krishna", "Rekha Devi", "Satish Kumar",
    "Chanda Devi", "Amit Kumar", "Rina Devi", "Harish Chandra", "Yamuna Devi",
    "Vinod Kumar", "Sangita Devi", "Ramesh Chandra", "Kiran Devi", "Sunil Kumar",
    "Anju Devi", "Mahesh Prasad", "Neeta Kumari", "Om Prakash", "Savitri Devi",
]

CROP_TYPES = [
    "Tomato", "Potato", "Onion", "Cauliflower", "Brinjal",
    "Cabbage", "Green Chilli", "Okra (Bhindi)", "Wheat", "Rice",
    "Maize", "Mustard", "Spinach", "Carrot", "Peas",
]

# Approx base mandi price per kg (Rs.) — used as a mean for random variation
CROP_BASE_PRICE = {
    "Tomato": 18, "Potato": 14, "Onion": 22, "Cauliflower": 20, "Brinjal": 16,
    "Cabbage": 12, "Green Chilli": 35, "Okra (Bhindi)": 28, "Wheat": 24, "Rice": 32,
    "Maize": 19, "Mustard": 55, "Spinach": 15, "Carrot": 21, "Peas": 40,
}

GRADES = ["A", "B", "C"]
GRADE_WEIGHTS = [0.35, 0.45, 0.20]  # most produce graded B, some A, fewer C

HUB_LOCATIONS = [
    "Barachatti Hub", "Tekari Hub", "Sherghati Hub", "Bodh Gaya Hub",
    "Wazirganj Hub", "Imamganj Hub", "Guraru Hub", "Fatehpur Hub",
]

# --- Generate data -----------------------------------------------------------

crop_choices = np.random.choice(CROP_TYPES, size=N_ROWS)

quantities = np.random.randint(50, 2000, size=N_ROWS)  # kg

grades = np.random.choice(GRADES, size=N_ROWS, p=GRADE_WEIGHTS)

# Price = base price +/- up to 15% random noise, rounded to 2 decimals
prices = []
for crop in crop_choices:
    base = CROP_BASE_PRICE[crop]
    noise = np.random.uniform(-0.15, 0.15)
    price = round(base * (1 + noise), 2)
    prices.append(price)

farmer_names = np.random.choice(FARMER_NAMES, size=N_ROWS, replace=False if N_ROWS <= len(FARMER_NAMES) else True)
hub_locations = np.random.choice(HUB_LOCATIONS, size=N_ROWS)

df = pd.DataFrame({
    "Farmer_Name": farmer_names,
    "Crop_Type": crop_choices,
    "Quantity_KG": quantities,
    "Grade": grades,
    "Current_Mandi_Price": prices,
    "Hub_Location": hub_locations,
})

# --- Save ---------------------------------------------------------------------

output_path = "inventory.csv"
df.to_csv(output_path, index=False)

print(f"Generated {len(df)} rows -> {output_path}")
print(df.head(10))
