# Microservice
 
 ## Introduction
 The microservice is given deadlines and returns a reminder of those that are upcoming.

 ## REQUESTING Data
 Your program must create a **.json** file that is located in the **same directory** as the Python file in this repository. The microservice is configured to accept a .json file named **deadlines.json**. Note that the directory and name of the .json file can be edited accordingly.

 The .json file must contain a **dictionary** where the key is a date in the following string format: **YYYY-MM-DD**. Its value is a **list of tasks**. In other words, the dictionary will hold date keys and their values are the list of tasks whose deadlines are on that date. See the following example:

![image](https://github.com/ernielum/microservice/assets/101778511/41127bc0-f6fa-44c1-aa28-486e14d9ba4b)

 ## RECEIVING Data

 The microservice will return a **.json** file that will be located in the **same directory** as the Python file. The microservice is configured to return a .json file named **reminder.json**. Note that the directory and name of the .json file can be edited accordingly.

 The .json file will return the __same__ dictionary and list format that was given except with only the dates and tasks that are upcoming. The microservice is initially set to return deadlines that are within 3 days but can be adjusted to your liking.

 Given the above tasks in the previous screenshot, the microservice will return the following .json file if ran on **07-31-2023**:

 ![image](https://github.com/ernielum/microservice/assets/101778511/5ca8eab8-9b08-45ea-89c9-ea901ec39f95)

 ## UML Sequence Diagram 
 
 ![Microservice](https://github.com/ernielum/microservice/assets/101778511/175b7f1f-aa0d-4d9b-95f5-41912508c0fe)
