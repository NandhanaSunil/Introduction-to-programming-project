<h1>MeasureCraft 📏</h1>

<h2>Table of Contents</h2>

<ul>
  <li><a href="#project-description">Project Description</a></li>
  <li><a href="#requirements">Requirements</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#future-goals">Future Goals</a></li>
  <li><a href="#limitations">Limitations</a></li>
  <li><a href="#contributors">Contributors</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h2>📃 Project Description</h2>
<p>The "Measure Craft" project aims to provide a solution for measuring the height and width of an object using the OpenCV library. This project utilizes computer vision techniques to detect objects in an image, calculate their dimensions, and convert the measurements from pixels to centimeters.</p>
<p>The project has the following features:</p>

<ul>
  <li> Object Detection: Utilizes OpenCV's object detection capabilities to identify objects in an image.</li>
  <li> Rectangle Approximation: Approximates the object boundaries to rectangles for easier measurement, considering imperfect geometric shapes.</li>
  <li> Aruco Marker: Uses Aruco markers to establish a reference for size conversion, ensuring accurate measurements.</li>
  <li> Pixel-to-Centimeter Conversion: Calculates the pixel-to-centimeter ratio using the Aruco marker, enabling conversion of object measurements from pixels to centimeters.</li>
</ul>



<h2>💻 Requirements</h2>

<p>To run and set up the project easily, these libraries are required:</p>
<h3> Modules: </h3>
<ol>
  <li> PYQT5</li>
  <li> OPEN-CV</li>
  <li> PYQT5-TOOLS</li>
</ol>


<h2>📋 Usage</h2>

<p>To use this project, these steps are to be followed:</p>

<ol>
  <li> Import the necessary modules and functions from the project.</li>
  <li> Download the file "back_interface.jpg" in the same directory of the code.(This is the background image for interface). </li> 
  <li> Load the image of which you want to measure the object's side by browsing files or live capturing.</li>
  <li> In the live-capturing mode press 'esc' key when you want to close the program.</li>
</ol>

<p>By following these steps, you can measure the side of an object in an image using OpenCV.</p>

<h2>🎯 Future Goals</h2>

<p>The future goals for this project include:</p>

<ul>
  <li> Enhancing object detection accuracy by incorporating programs to calibrate camera so that angle of capturing doesn't affect measurement of dimensions.</li>
</ul>

<h2>⚠️ Limitations</h2>

<p>While the project provides a basic solution for object measurement, it has some limitations:</p>

<ul>
  <li> Accuracy: The measurement accuracy heavily depends on the object detection and approximation methods used. Complex shapes and occlusions can affect the accuracy.</li>
  <li> The image of object should be captured exactly at 90 degrees so that image is not distorted.</li>
</ul>

<h2>👥 Contributors</h2>

<p>The following contributors have made significant contributions to this project:</p>

<ul>
  <li>👤 Sangam (@s-angam)</li>
  <li>👤 Nandhana Sunil (@NandhanaSunil)</li>
  <li>👤 Rhoda Grace (@RhodaGrace)</li>
</ul>

<h2>📄 License</h2>

<p>This project is licensed under the MIT License.</p>
