# Chatbots to Combat Disinformation 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Implemented using RASA framework:
[**Suraj Bodapati**](https://www.linkedin.com/in/suraj-bls/)

Deception Awareness & Resilience Training (DART) NSF Convergence Accelerator

## Abstract
- Build a conversational AI agent to combat disinformation at scale by targeting senior citizens with scams to get personal information.
- The idea is to direct the senior citizens to Deception Awareness and Resiliency Training(DART) post being scammed by the conversational agent.

### Datasets:
[**End-to-End Trainable Non-Collaborative Dialog System**](https://arxiv.org/abs/1911.10742): https://gitlab.com/ucdavisnlp/antiscam

[embed]https://github.com/lbodapat/rasa_is/blob/master/report.pptx.pdf[/embed]

### Training and Inference
Our model is build on top of [Huggingface](https://huggingface.co/) transformer library, and can be found in [this](https://github.com/sougata-ub/personality-response-generation-transformers) repo.

You can train and evaluate all experiments by uncommenting the desired command in the `runner.sh` script, and executing the shell script. Example: `nohup bash runner.sh 104 107 > log.txt 2>&1 &` runs experiment numbers 104 to 106 sequentially. All the different configurations for the experiments can be found in the `config.json` file.
In order to experiment with different parameters, you can directly execute the `run_training_v2.py` script. Sample command below:

```
python -m torch.distributed.run --nnodes=1 --nproc_per_node=2 --master_port 9999 ./run_training_v2.py --batch_size 16 --num_epochs 15 --learning_rate 0.00002 --experiment_num "$i" --path "/home/sougatas/wikibot_naacl_2022/data/" --num_workers 4 --accum_iter 2 --results_folder "/home/sougatas/wikibot_naacl_2022/results/results_wow_blender_v4/" --model_folder "/home/sougatas/wikibot_naacl_2022/models/models_v2/"
```

### Additional Models
1. BERT based intent classifier: https://drive.google.com/file/d/1jbGeLyfuaTRh9N3o3VSYiNqiX71d93lS/view?usp=sharing
2. Big 5 personality predictor trained on PANDORA dataset: https://drive.google.com/file/d/1Ltn53jj-0wfk5UjY2idxWX9HOkASgDnp/view?usp=sharing