# nwHacks2018_DropTheHeartBeat

Developed an application for nwHacks 2018 to combat the growing drug overdose epidemic. A chip to monitor user vitals sits within a wristband
a wristband and relays medical information such as oxygen saturation, pulse and breathing rate to a central database. A recurrent neural network with LSTM cells predicts user vitals and state (1 = healthy, 2 = in danger, 3 = critical) based on the past 5 datapoints for an individual within the database. This information is then pushed to a central user queue which medical authorities can monitor. Higher priority patients are automatically brought to the top of the queue and a heatmap corresponding to the geographical locations of users and their health states can be brought up for immediate visualization of where medical resources are most immediately needed. Our prototype for nwHacks consisted of:

1. High fidelity pulse oximeter built with an Arduino and Grove Base Shield Set
2. Database for holding patient information (MongoDB)
3. RNN with LSTM cells to provide inference on vitals information
4. Web application (React.js) with corresponding back end (Node.js) to relay desired information between parties
