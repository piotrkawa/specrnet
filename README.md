# SpecRNet

The following repository contains architecture of SpecRNet model from the paper called "SpecRNet: Towards Faster and More Accessible Audio DeepFake Detection".

Paper link: https://arxiv.org/abs/2210.06105

## Before you start

### Dependencies

Install required dependencies using:
```bas
pip install -r requirements.txt
```


## Evaluation

We provide the architecture along with:
* time benchmark on batches of random inputs,
* calculation of parameters' number.

To run it please use:
```bash
python model.py
```


## Citation

If you use this code in your research please use the following citation:

```
@INPROCEEDINGS{10063734,
  author={Kawa, Piotr and Plata, Marcin and Syga, Piotr},
  booktitle={2022 IEEE International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom)}, 
  title={SpecRNet: Towards Faster and More Accessible Audio DeepFake Detection}, 
  year={2022},
  volume={},
  number={},
  pages={792-799},
  doi={10.1109/TrustCom56396.2022.00111}}
```
