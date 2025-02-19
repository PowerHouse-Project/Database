# Database

## Database Design:

- Tables
    1. **Profile:**
        - ID (PK)
        - Name
        - Admin Level 
        - Devices Admissible (FK)
    3. **Device Group:**
        - ID (PK)
        - Name
        - Devices (FK)
    5. **Device:**
        - ID (PK)
        - Name
        - IP Address
    7. **Device Energy per day:**
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
        - startDate 
        - endDate 
        - Goal Energy
    10. **Energy Achievement:**
        - ID (PK)
        - Badge Name
       
