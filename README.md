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
@misc{kawa2022specrnet,
    title={SpecRNet: Towards Faster and More Accessible Audio DeepFake Detection},
    author={Piotr Kawa and Marcin Plata and Piotr Syga},
    year={2022},
    eprint={2210.06105},
    archivePrefix={arXiv},
    primaryClass={cs.SD}
}
```
