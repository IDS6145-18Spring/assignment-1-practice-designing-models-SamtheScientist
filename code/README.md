## Smart City Robot Perceptual and Processing System (RPPS) Model


Given the complexity of the problem for which the Robot Perceptual and Processing System (RPPS) seeks to provide a solution, and the novelty of the system itself, the coding framework will currently only address the functionality and interdependencies of the RPPS components comprising the first-level subsystems. 

Future plans include expanding the coding framework to encompass the whole of the RPPS to assess suitability and accuracy in reducing crime incidences.

Below is a diagram of the processes this coding framework seeks to simulate.

![Image of Class Diagram](../images/A1_ClassDiagram_5.png)

The four following classes are now part of the coding framework that has been started:
* [**Robot Platform**](../code/RPPS_system/Robot_Platform.py) - this code controls the robot platform and determines the movement mode based on environmental surroundings.
* [**Sensor Suite**](../code/RPPS_system/Sensor_Suite.py) - this code pertains to the sensor suite, comprised of an infrared and ladar sensor unit. This code indicates the active sensor unit as a function of several conditions such as, whether a target has been sighted. It also indicates the weather conditions and how this affects visibility from the sensors' standpoint. 
* [**Databases**](../code/RPPS_system/Databases.py) - this code indicates the active database based on what AI model is active. It also will enable activation of different databases and the storing of novel data records based on a series of conditions.
* [**Artificial Intelligence**](../code/RPPS_system/AI.py) - this code pertains to the AI component and indicates the active AI model. It also pulls information from the sensor suite like, IR values and IR temperature. Following this, it performs the necessary conversion for the different AI models to process. It also pulls information from the second-level sub-systems and passes match percentages up to the RPPS component.