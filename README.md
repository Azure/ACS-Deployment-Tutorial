# Deploy ML on ACS 
Deploying machine learning models can often be tricky due to their numerous dependencies, 
deep learning models even more so due to the plethora of libraries used. One of the ways to overcome this is to use Docker containers.
Unfortunately it is rarely straight forward and end-to-end guides are rare. 
This repository contains an end-to-end tutorial on how to deploy a pre-trained deep learning model using Azure Container Services(ACS).

By using Azure Container Services we can ensure that our ML application is performant, scalable and flexible enough to accommodate any deep learning framework. 
The Docker image we will be deploying can be found [here](https://hub.docker.com/r/masalvar/cntkresnet/). It contains a simple Flask web application with an Nginx web server. 
The deep learning framework we will use is Microsoft's Cognitive Toolkit (CNTK). We will be using a pretrained model specifically the ResNet 152 model.

The tutorial is split into 4 notebooks and these are:
[Build App Image](BuildImage.ipynb): This notebook will construct a basic web application using Flask and Nginx. It will then build a Docker image and push the image to a public hub.
[Test application locally](TestLocally.ipynb): This notebook will test In this notebook we run the Docker image we created in the last notebook and test it out locally.
[Deploy application on ACS](DeployACS.ipynb): Here we will use the Azure CLI to create the ACS. Once created we will specify our application and submit it to Marathon.
[Test application](TestApp.ipynb): In this notebook we will simply test the remote application to check that everything works.

If you already have a Docker image that you would like to deploy you can skip the first two notebooks.

# Contributing
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

