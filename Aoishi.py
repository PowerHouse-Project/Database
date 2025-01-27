import firebase_admin
from firebase_admin import credentials, firestore

# Path to your service account key JSON file
SERVICE_ACCOUNT_KEY_PATH = "/Users/aoishonthgo/Firestore/powerhouse-62f4d-firebase-adminsdk-fbsvc-3cd70b197a.json"

# Initialize Firebase
cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()


# Adding or Updating Data in Devices
def add_or_update_device(device_id, name, room, model, connection_type, ip_address):
    # Reference to the Devices collection and document
    device_ref = db.collection("Devices").document(device_id)
    
    # Device data
    device_data = {
        "ID": device_id,
        "Name": name,
        "Room": room,
        "Information": {
            "Model": model,
            "ConnectionType": connection_type,
            "IPAddress": ip_address,
        },
    }
    
    # Add or update the document
    device_ref.set(device_data)
    print(f"Device {device_id} added/updated successfully!")

# Example usage
add_or_update_device(
    "Device1",
    "Thermostat",
    "Living Room",
    "T1000",
    "WiFi",
    "192.168.1.1"
)


# Adding or Updating Data in Energy
def add_or_update_energy(document_id, total_energy_usage, daily_energy, device_fk):
    # Reference to the Energy collection and document
    energy_ref = db.collection("Energy").document(document_id)
    
    # Energy data
    energy_data = {
        "TotalEnergyUsage": total_energy_usage,
        "Daily": daily_energy,
        "DeviceFK": device_fk,  # Reference to a Device document ID
    }
    
    # Add or update the document
    energy_ref.set(energy_data)
    print(f"Energy record {document_id} added/updated successfully!")

# Example usage
add_or_update_energy(
    "Energy1",  # Unique ID for the energy document
    500,        # Total energy usage in kWh
    50,         # Daily energy usage in kWh
    "Device1"   # Foreign key referencing the Devices table
)


#linking the two tables
def add_or_update_energy(document_id, total_energy_usage, daily_energy, device_fk):
    # Check if the device exists
    device_ref = db.collection("Devices").document(device_fk)
    if not device_ref.get().exists:
        print(f"Error: Device {device_fk} does not exist!")
        return
    
    # Energy data
    energy_data = {
        "TotalEnergyUsage": total_energy_usage,
        "Daily": daily_energy,
        "DeviceFK": device_fk,
    }
    
    # Add or update the document
    energy_ref = db.collection("Energy").document(document_id)
    energy_ref.set(energy_data)
    print(f"Energy record {document_id} added/updated successfully!")
