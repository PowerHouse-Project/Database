# Database

## Database Design:

- Tables
    1. **Users:**
        - ID (PK)
        - Admin Level 
        - Devices (FK)
    2. **Groups:**
        - ID (PK)
        - Name
        - Devices (FK)
    3. **Devices:**
        - ID (PK)
        - Name
        - Room
        - Information
            - Model
            - Connection type
            - IP Address
    4. **Energy:**
        - Total Energy Usage
            - Daily
        - Energy Per Device
            - Device (FK)
    5. **Automation Schedules:**
        - ID (PK)
        - Action
            - Device (FK)
            - Time
        - Condition
            - Device (FK)
            - Time
    6. **Energy Saving Goals:**
        - Energy Goal
    7.  **Profile Pin:**
        - User(FK)
        - Pin 
