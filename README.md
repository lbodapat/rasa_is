# Chatbots to Combat Disinformation 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Implemented using RASA framework:
[**Suraj Bodapati**](https://www.linkedin.com/in/suraj-bls/)

Deception Awareness & Resilience Training (DART) NSF Convergence Accelerator

## Abstract
- Build a conversational AI agent to combat disinformation at scale by targeting senior citizens with scams to get personal information.
- The idea is to direct the senior citizens to Deception Awareness and Resiliency Training(DART) post being scammed by the conversational agent.
- [**Documentation**](https://github.com/lbodapat/rasa_is/blob/master/report.pptx.pdf)

### Datasets:
[**End-to-End Trainable Non-Collaborative Dialog System**](https://arxiv.org/abs/1911.10742): https://gitlab.com/ucdavisnlp/antiscam

### Installation and Running the code
1. [**Install RASA**](https://rasa.com/docs/rasa/installation/installing-rasa-open-source/)
2. Clone the repository
3. RUN command on CLI - ```rasa train```
4. To test the model RUN command on CLI - ```rasa shell```
5. To test the model in DEBUG mode, RUN command on CLI - ```rasa interactive```
6. In the new terminal window RUN command on CLI - ```rasa run actions``` This is required to run the action server.
7. Finally In another new terminal run the Duckling Extractor in Docker. ```sudo docker run -p 8000:8000 rasa/duckling```

### Output Screenshot

![Alt text](/Notebooks/output.png?raw=true "Output ScreenShot")
