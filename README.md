<h1 align="center"> CSC380 Traffic Camera Project </h1>
<p align="center"> Project Developers: Omar Garbanzo, Jonathan Katzer, Michael Napolitano </p>

<h3> Background </h3>
<p> To ensure the safety of pedestrians, the speed limit on SUNY Oswego campus roads is 20mph. University police patrols and enforces this speed limit, which binds a lot of resources that could be used in some other way. While traffic cameras are a sensible means to assist UP Officers in speed enforcement, these systems mainly use RADAR and other sensor technologies, which makes them accurate, but also quite expensive. </p>

<h3> Objective </h3>
<p> The objective of this project is to design and implement an inexpensive live traffic camera using Raspberry Pi. The system shall observe a scene and use computer vision to track, count, and measure the speed of cars driving by. For those cars that are going too fast, an alert shall be issued. To facilitate social distancing, this project may use pre-recorded videos, but shall demonstrate functionality using live video prior to completion. </p>

<h3> Key Features and Challenges </h3>
<p> The application should have the following features:
  <ul>
    <li> Run on Raspberry Pi with OpenCV and/or Tensorflow </li>
    <li> Recognize vehicles driving by and measure their passing speed </li>
    <li> Allow users to set a tolerance threshold </li>
    <li> Report the license plate number of the vehicle suspected to be in violation of the speed limit, along with evidence of the alleged infraction </li>
  </ul>
</p>
<p> Challenges to overcome:
  <ul>
    <li> Recognize and differentiate vehicles by plate number </li>
    <li> Calibrate speed of vehicles in video </li>
    <li> Aim for forensic dependability (which may not be attainable, but give it a try ;-) ) </li>
  </ul>
</p>

<h3> Stakeholders, Resources, and Further Information </h3>
<p> This project is in cooperation with Bastian Tenbergen of the Department of Computer Science. You will need to meet with him to elicit requirements and gain an overview of the relevant materials, systems, constraints, and the project goals. </p>
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
