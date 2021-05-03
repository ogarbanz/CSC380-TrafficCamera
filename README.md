<h1 align="center"> CSC380 Traffic Camera Project </h1>
<p align="center"> Project Developers: Omar Garbanzo, Jonathan Katzer, Michael Napolitano </p>

<p align="center"> <img src="Images/Traffic Camera Example 0.jpg" alt="Traffic Camera Example Image"> 
<img src="Images/Traffic Camera Setup 1.jpeg" alt="Traffic Camera Setup Image" height="320"> </p>

<h3> Folder Descriptions </h3>
<p> On the GitHub page you will notice multiple folders. Below is the name of each folder and its purpose:
  <ul>
    <li><b>Full</b>: contains all components of the program that implements features that are incompatible with the Raspberry Pi </li>
    <li><b>Images</b>: contains example output and setup images </li>
    <li><b>Input Videos</b>: contains all raw videos used for testing the program </li>
    <li><b>Lite</b>: contains all components of the program that are compatible with the Raspberry Pi </li>
    <li><b>Output Videos</b>: contains the output of running different models on the videos contained within the <b>Input Videos</b> folder as well as the final output of the program </li>
  </ul>
</p>
<p><b>Note</b>: The program within the <b>Full</b> folder was tested to work on Windows systems and did not function properly on the Raspberry Pi. It may function on other systems as well. The program within the <b>Lite</b> folder was tested and functions properly on Windows and Raspberry Pi systems. It may function on other systems as well. The features of the program in the <b>Full</b> folder include the ability to load a pre-recorded video with a file chooser or use live video, and saving and sending video via email. The features of the program in the <b>Lite</b> folder include live video functionality and sending images via email.
</p>

<h3> File Descriptions </h3>
<p> Once you choose the system you want to run the program on, download the version you want that is compatible with your system according to the information above (i.e., Full or Lite for Windows, Lite for Raspberry Pi or Windows). Within the folder, you will see the four main components of the program. Below is the name and description of each component. Each component is required to run the program.
  <ul>
    <li><b>cv.py</b>: contains all the code for computer vision which involves vehicle detection, speed measurement, displaying the image/video, and saving the image/video </li>
    <li><b>es.py</b>: contains all the code responsible for formatting and sending the email </li>
    <li><b>haarcascade_car.xml</b>: contains the haar cascade used within <b>cv.py</b> to identify vehicles </li>
    <li><b>main.py</b>: contains all functions pertaining to the user interface which includes obtaining user input (email address, speed limit, and location), providing the user with help through the help page, and starting the program. </li>
  </ul>
</p>

<h3> Running the Program </h3>
<p>To run the program using your favorite integrated development environment, place all the required components above in the same directory and run <b>main.py</b> within that same directory. To run the program using the command line, with all the required components above in the same directory and the current working directory being the directory all the required components are in, run <b>python main.py</b> (or <b>python3 main.py</b> depending on how python is set up).
</p>

<h3> Dependencies and Versions </h3>
<p>Below are all the dependencies of the program as well as their version numbers and where they are used. Some are included with the version of python you are using and some are required to be installed and/or compiled beforehand in order to run the program.
  <ul>
    <li><b>python</b> (version <b>3.9.0</b>) </li>
    <li><b>tkinter</b> (version <b>8.6</b>): <b>main.py</b> </li>
    <li><b>webbrowser</b> (included): <b>main.py</b> </li>
    <li><b>os</b> (included): <b>main.py</b>, <b>es.py</b> </li>
    <li><b>re</b> (included): <b>main.py</b> </li>
    <li><b>datetime</b> (included): <b>cv.py</b>, <b>es.py</b> </li>
    <li><b>multiprocessing</b> (included): <b>cv.py</b> </li>
    <li><b>math</b> (included): <b>cv.py</b> </li>
    <li><b>cv2</b> (version <b>4.5.1</b>): <b>cv.py</b> </li>
    <li><b>email</b> (included): <b>es.py</b> </li>
    <li><b>smtplib</b> (included): <b>es.py</b> </li>
    <li><b>ssl</b> (included): <b>es.py</b> </li>
  </ul>
</p>

<h3> Background </h3>
<p> To ensure the safety of pedestrians, the speed limit on SUNY Oswego campus roads is 20mph. University police patrols and enforces this speed limit, which binds a lot of resources that could be used in some other way. While traffic cameras are a sensible means to assist UP Officers in speed enforcement, these systems mainly use RADAR and other sensor technologies, which makes them accurate, but also quite expensive.
</p>

<h3> Objective </h3>
<p> The objective of this project is to design and implement an inexpensive live traffic camera using Raspberry Pi. The system shall observe a scene and use computer vision to track, count, and measure the speed of cars driving by. For those cars that are going too fast, an alert shall be issued. To facilitate social distancing, this project may use pre-recorded videos, but shall demonstrate functionality using live video prior to completion.
</p>

<h3> Key Features and Challenges </h3>
<p> The application should have the following features:
  <ul>
    <li> Run on Raspberry Pi with OpenCV and/or Tensorflow </li>
    <li> Recognize vehicles driving by and measure their passing speed </li>
    <li> Allow users to set a tolerance threshold </li>
  </ul>
</p>

<h3> Stakeholders, Resources, and Further Information </h3>
<p> This project is in cooperation with Bastian Tenbergen of the Department of Computer Science. </p>
<p> Useful resources:
  <ul>
    <li> NYS Red Light Camera facts: <br> <a href="https://www1.nyc.gov/site/finance/vehicles/red-light-camera-violations.page" target="_blank">
      https://www1.nyc.gov/site/finance/vehicles/red-light-camera-violations.page </a> </br> </li>
    <li> NYS Ticket and Penalty regulation: <br> <a href="https://dmv.ny.gov/tickets/tickets-points-and-penalties" target="_blank">
      https://dmv.ny.gov/tickets/tickets-points-and-penalties </a> </br> </li>
    <li> Photo Evidence regulation of Nassau County: <br> <a href="https://www.nassaucountyny.gov/1935/Photo-Enforcement-Red-Light-Camera-Progr" target="_blank">
      https://www.nassaucountyny.gov/1935/Photo-Enforcement-Red-Light-Camera-Progr </a> </br> </li>
  </ul>
</p>
