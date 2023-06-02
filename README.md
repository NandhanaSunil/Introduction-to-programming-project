<h1>Measuring the Side of an Object using OpenCV 📏</h1>

<h2>Table of Contents</h2>

<ul>
  <li><a href="#project-description">Project Description</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#future-goals">Future Goals</a></li>
  <li><a href="#limitations">Limitations</a></li>
  <li><a href="#contributors">Contributors</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h2>📃 Project Description</h2>

<p>The "Measuring the Side of an Object using OpenCV" project aims to provide a solution for measuring the side of an object using the OpenCV library. This project utilizes computer vision techniques to detect objects in an image, calculate their dimensions, and convert the measurements from pixels to centimeters.</p>

<p>The project offers the following features:</p>

<ul>
  <li> Object Detection: Utilizes OpenCV's object detection capabilities to identify objects in an image.</li>
  <li> Rectangle Approximation: Approximates the object boundaries to rectangles for easier measurement, considering imperfect geometric shapes.</li>
  <li> Aruco Marker: Uses Aruco markers to establish a reference for size conversion, ensuring accurate measurements.</li>
  <li> Pixel-to-Centimeter Conversion: Calculates the pixel-to-centimeter ratio using the Aruco marker, enabling conversion of object measurements from pixels to centimeters.</li>
</ul>

<p>OpenCV is a powerful open-source computer vision library that provides a wide range of tools for image processing, object detection, and geometric transformations. By leveraging OpenCV's functionalities, this project enables accurate and efficient object measurement.</p>

<h2>💻 Installation</h2>

<p>To install and set up the project, follow these steps:</p>

<ol>
  <li> Clone the repository: <code>git clone https://github.com/NandhanaSunil/Introduction-to-programming-project.git</li>
  <li> Navigate to the project directory: <code>cd object-measurement</code></li>
  <li> Install the required dependencies: <code>pip install -r requirements.txt</code></li>
  <li> Run the project: <code>python object_measurement.py</code></li>
</ol>

<p>Make sure you have Python and pip installed on your system before proceeding with the installation.</p>

<h2>📋 Usage</h2>

<p>To use this project, follow these steps:</p>

<ol>
  <li> Import the necessary modules and functions from the project.</li>
  <li> Load the image in which you want to measure the object's side.</li>
  <li> Detect the objects in the image using the object detection function.</li>
  <li> Approximate the object boundaries to rectangles for easier measurement.</li>
  <li> Utilize an Aruco marker as a size reference for pixel-to-centimeter conversion.</li>
  <li> Calculate the pixel-to-centimeter ratio using the known size of the Aruco marker.</li>
  <li> Iterate over the detected objects and measure their sides using the pixel-to-centimeter ratio.</li>
  <li> Display the image with the measured objects and their dimensions.</li>
</ol>

<p>By following these steps, you can measure the side of an object in an image using OpenCV.</p>

<h2>🎯 Future Goals</h2>

<p>The future goals for this project include:</p>

<ul>
  <li> Enhancing object detection accuracy by incorporating deep learning-based models.</li>
  <li> Introducing additional measurement metrics such as volume and area.</li>
  <li> Building a user-friendly interface for easy input and output.</li>
</ul>

<h2>⚠️ Limitations</h2>

<p>While the project provides a basic solution for object measurement, it has some limitations:</p>

<ul>
  <li> Accuracy: The measurement accuracy heavily depends on the object detection and approximation methods used. Complex shapes and occlusions can affect the accuracy.</li>
  <li> Lighting Conditions: The project assumes consistent lighting conditions for accurate detection and measurement.</li>
  <li> Calibration: The accuracy of the pixel-to-centimeter conversion relies on the correct identification and size estimation of the Aruco marker.</li>
</ul>

<h2>👥 Contributors</h2>

<p>The following contributors have made significant contributions to this project:</p>

<ul>
  <li>👤 Sangam (@s-angam)</li>
  <li>👤 Nandhana Sunil (@NandhanaSunil)</li>
  <li>👤 Rhoda Grace (@)</li>
</ul>

<h2>📄 License</h2>

<p>This project is licensed under the MIT License.</p>
