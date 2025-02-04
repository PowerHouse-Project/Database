# Database

## Database Design:

- Tables
    1. **Profile:**
        - Admin Level 
        - Devices Admissible (FK)
        - Pin
    2. **Group:**
        - Name
        - Devices (FK)
    3. **Device:**
        - ID (PK)
        - Name
        - Room
        - Information
            - Model
            - Connection type
            - IP Address
    4. **Energy:**
        - Daily Energy Per Device
            - Device (FK)
            - Date
    5. **Automation Schedule:**
        - ID (PK)
        - Action
            - Device (FK)
            - Time
        - Condition
            - Device (FK)
            - Time
    6. **Energy Goal:**
        - Datestamp 
        - Duration //end date is evaluation date, stats on this should be displayed on end date 
        - Goal Energy

