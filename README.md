# Microservice
 
 ## Introduction
 The microservice is given deadlines and returns a reminder of those that are upcoming.

 ## REQUESTING Data
 Your program must create a **.json** file that is located in the **same directory** as the Python file in this repository. The microservice is configured to accept a .json file named **deadlines.json**. Note that the directory and name of the .json file can be edited accordingly. See the following screenshot for an example call that must be made in order for the microservice to respond.

![image](https://github.com/ernielum/microservice/assets/101778511/83662910-e6fc-4b33-b652-dc05a88423ba)


 The .json file must contain a **dictionary** where the key is a date in the following string format: **YYYY-MM-DD**. Its value is a **list of tasks**. In other words, the dictionary will hold date keys and their values are the list of tasks whose deadlines are on that date. See the following example of how the .json file should look like after the example call:

![image](https://github.com/ernielum/microservice/assets/101778511/7c070a9f-bea4-49c4-8e70-4f0b23f24583)


 ## RECEIVING Data

 The microservice will return a **.json** file that will be located in the **same directory** as the Python file. The microservice is configured to return a .json file named **reminder.json**. Note that the directory and name of the .json file can be edited accordingly.

 The .json file will return the __same__ dictionary and list format that was given except with only the dates and tasks that are upcoming. The microservice is initially set to return deadlines that are within 3 days but can be adjusted to your liking.

 Given the above tasks in the previous screenshot, the microservice will return the following .json file if ran on **07-31-2023**:

![image](https://github.com/ernielum/microservice/assets/101778511/c2c690de-3957-4723-9894-db1be9d85c1f)


Notice how any deadlines that are beyond 3 days are not included in the returned data.

 ## UML Sequence Diagram 

 ![Microservice](https://github.com/ernielum/microservice/assets/101778511/8b4a4ce7-68dc-4343-89ad-f5c04d6a7def)

