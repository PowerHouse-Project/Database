# Database

## Database Design:

- Tables
    1. **Profile:**
        - ID (PK)
        - Admin Level 
        - Devices Admissible (FK)
        - Pin
    3. **Group:**
        - ID (PK)
        - Name
        - Devices (FK)
    5. **Device:**
        - ID (PK)
        - Name
        - IP Address
    7. **Energy:**
        - ID (PK)
        - Device (FK)
        - Date
    8. **Automation Schedule:**
        - ID (PK)
        - Action
            - Device (FK)
            - Status 
        - Condition (Optional Field)
            - Device (FK)
            - Time
    9. **Energy Goal:**
        - ID (PK)
        - Datestamp 
        - Duration //end date is evaluation date, stats on this should be displayed on end date
        - Goal Energy
    10. **Energy Achievement:**
        - ID (PK)
        - Badge Name
       
