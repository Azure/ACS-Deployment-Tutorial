### Authors: Mathew Salvaris and Ilia karmanov

# Deploy ML on ACS 
Deploying machine learning models can often be tricky due to their numerous dependencies, deep learning models often even more so. One of the ways to overcome this is to use Docker containers. Unfortunately, it is rarely straight forward. In this tutorial, we will demonstrate how to deploy a pre-trained deep learning model using Azure Container Services which allows us to orchestrate a number of containers using DC/OS. By using Azure Container Services, we can ensure that is performant, scalable and flexible enough to accommodate any Deep Learning framework. 
The Docker image we will be deploying can be found here. It contains a simple Flask web application with Nginx web server. The Deep learning framework we will use is the Microsoft Cognitive Toolkit (CNTK) and we will be using a pre-trained model specifically the ResNet 152 model.

Azure Container Services enables you to configure, construct and manage a cluster of virtual machines pre-configured to run containerized applications. Once the cluster is set up you can use a number of open-source scheduling and orchestration tools, such as Kubernetes and DC/OS. This is ideal for machine learning application since we can use Docker containers which enable us to have ultimate flexibility in the libraries we use and allows us to easily scale up based on demand. While always ensuring that our application remains performant. You can create an ACS through the Azure portal but in this tutorial we will be constructing it using the Azure CLI.

The application will be a simple image classification service, where we will submit an image and get back what class the image belongs to. We have split the process into four sections.
[Create Docker image of our application](BuildImage.ipynb)
[Test the application locally](TestLocally.ipynb)
[Create an ACS cluster and deploy our web app](DeployACS.ipynb)
[Test our web app](TestApp.ipynb)

Each section is accompanied by a Jupyter notebook which contain step by step instructions on how to create, deploy and test a web application.

If you already have a Docker image that you would like to deploy you can skip the first two notebooks.

# Contributing
This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

