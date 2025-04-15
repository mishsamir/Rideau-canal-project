## Rideau Canal Skateway Monitoring System

### Scenerio Explanation:

The Rideau Canal Skateway in Ottawa, recognized as the largest naturally frozen skating rink globally,
demands continuous monitoring to maintain public safety. Critical factors such as ice thickness, temperature, 
and snow accumulation determine whether skating conditions remain safe for the public.

This project simulates IoT sensors strategically positioned along the canal to capture real-time environmental data. 
Leveraging an integrated Azure data pipeline, the solution seamlessly manages data flow—from simulated IoT devices through real-time analytics to secure, long-term storage.
By analyzing this processed information, the National Capital Commission (NCC) can swiftly detect and address potential safety risks, ensuring a safe skating environment for everyone.


### Components:

- Simulated IoT Sensors: Generate and push random environmental data from three locations along the canal.
- Azure IoT Hub: Ingests messages from the simulated devices.
- Azure Stream Analytics: Processes and aggregates sensor data in real-time.
- Azure Blob Storage: Stores processed results for future analysis and reporting.

## Implementation

### IOT Sensor Simulation

- The RealTimeProject/sensor1.py script simulates sensors at:

  - Dow's Lake
  - Fifth Avenue
  - National Arts Centre (NAC)
- Every 5 seconds, the script sends JSON payloads to Azure IoT Hub:

  ```json
  { 
  "location": "Dow's Lake", 
  "iceThickness": 27, 
  "surfaceTemperature": -1, 
  "snowAccumulation": 8, 
  "externalTemperature": -4, 
  "timestamp": "2024-11-23T12:00:00Z" 
  } 
  ```
  <img width="1800" alt="Screenshot 2025-04-13 at 8 33 49 PM" src="https://github.com/user-attachments/assets/5e407250-abbd-4101-868b-db63d84bb958" />
  <img width="1800" alt="Screenshot 2025-04-13 at 8 33 55 PM" src="https://github.com/user-attachments/assets/dc580d4c-fda6-4ce8-aedd-585f2bdbdeac" />
  
### Creating Azure IOT HUB:
  <img width="1800" alt="Screenshot 2025-04-13 at 4 49 35 PM" src="https://github.com/user-attachments/assets/ef25e420-b847-4f0a-b4b6-37630efcc7a9" />
### Creating System Analysis

  <img width="1800" alt="Screenshot 2025-04-13 at 5 02 32 PM" src="https://github.com/user-attachments/assets/ba3adaf7-3ffe-489c-a5e1-6a4b1d274415" />

  <img width="1800" alt="Screenshot 2025-04-13 at 8 34 09 PM" src="https://github.com/user-attachments/assets/c7938a26-0d0d-463a-9cf3-e470ab4be59e" />


### Visualtion of Analysed Data:
  <img width="1800" alt="Screenshot 2025-04-13 at 8 34 42 PM" src="https://github.com/user-attachments/assets/d0f48839-332b-4cc4-a1d7-b800d47faf8f" />
  <img width="1800" alt="Screenshot 2025-04-13 at 8 35 13 PM" src="https://github.com/user-attachments/assets/714d8717-b3cb-44af-90c3-7ce15f2d39c3" />


  


