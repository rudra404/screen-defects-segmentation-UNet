# screen-defects-segmentation-UNet
LCD screen defects segmentation performed using a modified UNet model

#### Background:
The client is an innovative technology company that focuses on the semiconductor display field. It mainly produces liquid crystal display panels across several production factories. In the panel production process, it is necessary to use Automated Optical Inspection equipment (AOI) to detect the defects generated in each process, and then manually classify the defects (code judgment task).

Different defect types correspond to different physical causes in the production process. Through statistical comprehensive consideration of these defect categories, sizes, and their positional relationship with the circuit pattern, it can provide guidance for the improvement of the production process, reduce the probability of production failures, and reduce repair and rework to optimize the production efficiency of the production line.

#### Scope:
The project showcased here contains an ipython notebook that was created and run on Google Colab. The objective is to perform image segmentation on individual defect datasets to segment the defects from the panel (without classification). The model in the notebook was run on a single defect type and the results are displayed at the end.

#### Data:
The data provided by the client is segregated in several folders for each defect type. Each folder contains (a highly varying number of) images of magnified views of the LCD panel after a particular sub-process on the manufacturing line showing the individual circuitry of the pixels on the LCD with the defects.

Additionally, .json files corresponding to each image file are provided with information about the defect labels. These files are presumably created using the ‘labelme’ tool. 

#### Workflow:
1. The defect masks are plotted from information extracted from the .json files using “maskplot.py” and saved as .png files in specified directory
2. These .png images are converted to binary form from colour (Red was the default on .json files)
3. .jpg images and .png labels are stored in tensors after further pre-processing of the images including resizing
4. Data is split for training and testing purposes
5. Machine Learning model is defined (modified UNet in this case)
6. Metrics for evaluating the performance of the model are defined
7. Training and Prediction
8. Results are displayed

#### Acknowledgements:
- https://github.com/Tony607/Industrial-Defect-Inspection-segmentation
- https://github.com/wkentaro/labelme
