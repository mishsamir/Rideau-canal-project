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
  
