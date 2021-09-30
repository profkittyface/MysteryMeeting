## Design Overview

### Web Application
- User Profile Handling
  - /profile
- User tracking
  - /ranos
- Signup / Login
  - /signup
  - /login
  - /logout
  - /mainScreen
  - /events
- Batch location data processing
  - /admin
  
#### Business Logic
1. I collect the users location throughout the day and compare it with other users to find patterns involving them being in the same place (at the same time), and then dispatch an invite to these identified users

2. I select I'm looking for an event, and it locates the nearest user who has also selected this and dispatches a location.

### Database
- PostgreSQL Geographic Data

### Mobile App
- Should handle:
	- Signup / Login
	- Telemetry
	- Events nearby
- Exploring React Native
