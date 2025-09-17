# Travel Memory

`.env` file to work with the backend after creating a database in mongodb: 

```
MONGO_URI='ENTER_YOUR_URL'
PORT=3001
```

Data format to be added: 

```json
{
    "tripName": "Incredible India",
    "startDateOfJourney": "19-03-2022",
    "endDateOfJourney": "27-03-2022",
    "nameOfHotels":"Hotel Namaste, Backpackers Club",
    "placesVisited":"Delhi, Kolkata, Chennai, Mumbai",
    "totalCost": 800000,
    "tripType": "leisure",
    "experience": "Lorem Ipsum, Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum,Lorem Ipsum, ",
    "image": "https://t3.ftcdn.net/jpg/03/04/85/26/360_F_304852693_nSOn9KvUgafgvZ6wM0CNaULYUa7xXBkA.jpg",
    "shortDescription":"India is a wonderful country with rich culture and good people.",
    "featured": true
}
```


For frontend, you need to create `.env` file and put the following content (remember to change 
it based on your requirements): ```bash REACT_APP_BACKEND_URL=http://localhost:3001 ```
## Flask Application

The backend is a Python Flask application running on port 5000.

### Endpoints:
- `GET /` - Welcome message
- `GET /health` - Health check

### Local Development:
```bash
cd backend
pip install -r requirements.txt
python app.py

# Build test - Thu Sep 18 02:18:17 IST 2026


🔄 CI/CD Pipeline
This project uses Jenkins for continuous integration and deployment.

Pipeline Stages:
Build: Creates virtual environment and installs dependencies

Test: Runs pytest test suite with coverage

Deploy: Deploys to staging environment

Jenkins Configuration:
Repository: https://github.com/Kartik27baliyan/kartikTravelMemory

Jenkinsfile: Root directory Jenkinsfile

Triggers: Manual build execution

Notifications: Email on success/failure

Successful Build Results:
✅ Virtual environment creation

✅ Dependency installation

✅ 100% test pass rate (2/2 tests)

✅ Successful deployment to staging


A. Pipeline Overview:
Main Dashboard: Show your pipeline job in Jenkins list

Build History: Show successful build(s) in history

B. Stage View (MOST IMPORTANT):
Full Stage View: All stages showing GREEN (Diagnose → Build → Test → Deploy)

Build Stage: Expanded view showing virtual environment creation

Test Stage: Expanded view showing "2 tests passed"

Deploy Stage: Expanded view showing deployment message

C. Console Output:
Build Log: Show successful virtual environment setup

Test Results: Show "2 passed in 0.13s"

Final Success: Show "Finished: SUCCESS" at the bottom

D. Configuration:
Job Configuration: Show Pipeline definition (SCM with Jenkinsfile)

Build Triggers: Show disabled automatic triggers (if you want manual only)

🎯 WHERE TO FIND IN JENKINS:
Pipeline URL: https://jenkinsacademics.herovired.com/job/kartik_jenkins_pipeline/

Stage View: Main job page → "Stage View" tab

Console Output: Click on build number → "Console Output"

Configuration: Click "Configure" on left menu
