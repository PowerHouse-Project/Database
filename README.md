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
        - Name
        - Information
        - IP Address
    4. **Energy:**
            - Device (FK)
            - Date
    5. **Automation Schedule:**
        - ID (PK)
        - Action
            - Device (FK)
            - Status 
        - Condition (Optional Field)
            - Device (FK)
            - Time
    7. **Energy Goal:**
        - Datestamp 
        - Duration //end date is evaluation date, stats on this should be displayed on end date 
        - Goal Energy

