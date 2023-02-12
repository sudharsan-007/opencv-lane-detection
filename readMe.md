# Curved Lane Detection for Self Driving Cars | OpenCV Python
By [Sudharsan Ananth](https://sudharsanananth.wixsite.com/sudharsan) 

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#dependencies">Dependencies</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#run-the-code">Run the code</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


## Introduction 

This Repository consists of code to estimate Lane curvature from front view images captured from a car. The code uses openCV library to process the image and overlay the output. This can be implemented in real time using a live camera feed by changing `cameraFeed=True`

### Working video
![Output](assets/demo.gif)

## Dependencies 

This project is built with the below given major frameworks and libraries. The code is primarily based on python. And the environment is created using Anaconda. 

* [Python](https://www.python.org/)
* [Anaconda](https://www.anaconda.com/)
* [openCV](https://opencv.org)
* [numpy](https://numpy.org)
* [Pickle](https://docs.python.org/3/library/pickle.html)

## Prerequisites 

1. Python 3.7 (skip if downloading conda)
2. Conda (Either [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Ananconda](https://www.anaconda.com))

## Run the code

Simply clone the repo cd into the right directory and run code using the below commands. Step-by-Step instructions given below. Simply change the directory and run `agent.py` from the directory `RL_car_game`. You will be able to see the agent training and getting better in minutes. 

1. Clone the repository using 
   ```sh
   git clone https://github.com/sudharsan-007/opencv-lane-detection.git
   ```

2. cd into the directory opencv-lane-detection
   ```sh
   cd opencv-lane-detection
   ```

3. Recommended: create a conda environment 
    ```sh
    # We require python>=3.7
    conda create -n cv2_lane_detection python=3.7 numpy 
    conda activate cv2_lane_detection
    ```

4. Install pickle (Skip if `import pickle` works)
   ```sh
   pip install pickle4
   ```

5. Install openCV-python. Please refer openCV website.
    ```sh
    # https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
    pip install opencv-python
    ```

6. If the above code does not work for you try this(skip this step 5 worked). 

    ```sh
    conda install -c conda-forge opencv
    ```

7. Add video that you want lane detection to run on in the same directory. 
   
8. Change the directory name inside the python file `LaneDetection.py` and Run `LaneDetection.py` from this directory and from inside this environment.
   ```sh 
   python LaneDetection.py
   ```



<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
