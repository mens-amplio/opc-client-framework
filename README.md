A simple Python framework for rendering LED effects and sending them out via Open Pixel Control.

Pulled out of the Mens Amplio repo (https://github.com/mens-amplio/mens-amplio) for extension/re-use in future projects.

Instructions to run example in lighting simulator:
* Clone this repo
* Clone the Open Pixel Control repo (https://github.com/zestyping/openpixelcontrol)
* Install dependencies
* Build OPC and launch visualizer:
  * cd [whatever]/openpixelcontrol
  * make
  * bin/gl_server [whatever]/mens-amplio/modeling/opc-layout.json &
* Run the test script: python example.py

Dependencies:
* numpy
* mesa-common-dev and freeglut3-dev (for OPC gl_server on Linux; not needed on Pi or Mac)