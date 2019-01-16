# machine learning pipeline: the challenges and verification with blockchain
For a typical machine learning development process, it will go through two stages: training and production stages. During the two stages, tangled with various platforms, it will introduce room for errors. Such as mismatch config files, trained model object or test data corruption. This can also happen during file transmission. 
This code is to demonstrate the typical model train --> production framework and where it can go wrong. Most importantly, how to fix this problem with a block chain process. 
I have build a block chain class to track the process and a demo included. 

A diagram for typical machine learning model development and deployment:


## Training data process--
 Training data -> training --> persisted model ~~]]] <br>
##Production  <br>
Streaming Input -------------------------------->Prediction --> Results. <br>

##Block chain transaction process (like a linked list): <br>
Stage 1: Configuration  --> raw data  Blockchain [0|signature of config] -->[signature of config | sigature of raw data] <br>
Stage 2: Configuration --> raw data --> clean data --> persisted model  <br>
Stage 3: Configuration --> persisted model --> ***** <br>
