# Database

## Database Design:

- Tables
    1. **Groups:**
        - ID (PK)
        - Name
        - Devices (FK)
    2. **Devices:**
        - ID (PK)
        - Name
        - Room
        - Information
            - Model
            - Connection type
            - IP Address
    3. **Energy:**
        - Total Energy Usage
            - Daily
        - Energy Per Device
            - Device (FK)
    4. **Automation Schedules:**
        - ID (PK)
        - Action
            - Device (FK)
            - Time
        - Condition
            - Device (FK)
            - Time
