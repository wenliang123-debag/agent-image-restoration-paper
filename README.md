# Awesome-Agentic-Image-Restoration [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of **Agentic Image Restoration (IR)** / **Agentic Super-Resolution (SR)** works where an LLM/VLM-based agent **plans → calls tools/models → evaluates → refines** to solve complex, mixed-degradation restoration problems.

**Contributions are welcome!**  
*Acknowledgments: This README layout is adapted from the “Awesome-Anything” style (table: Title & Authors / Intro / Useful Links).*

---

## Agentic Image Restoration (IR)

| Title & Authors | Intro | Useful Links |
|:----|:----:|:---:|
|[**RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models**](https://arxiv.org/abs/2407.18035)  
*Haoyu Chen, Wenbo Li, Jinjin Gu, Jingjing Ren, Sixiang Chen, Tian Ye, Renjing Pei, Kaiwen Zhou, Fenglong Song, Lei Zhu*  
> arXiv 2024  
| ![intro](assets/teasers/restoreagent.png) | [[PDF](https://arxiv.org/pdf/2407.18035.pdf)] |
|[**An Intelligent Agentic System for Complex Image Restoration Problems (AgenticIR)**](https://arxiv.org/abs/2410.17809)  
*Kaiwen Zhu, Jinjin Gu, Zhiyuan You, Yu Qiao, Chao Dong*  
> ICLR 2025  
| ![intro](assets/teasers/agenticir.png) | [[Github](https://github.com/Kaiwen-Zhu/AgenticIR)] [[PDF](https://arxiv.org/pdf/2410.17809.pdf)] |
|[**Multi-Agent Image Restoration (MAIR)**](https://arxiv.org/abs/2503.09403)  
*Xu Jiang, Gehui Li, Bin Chen, Jian Zhang*  
> arXiv 2025  
| ![intro](assets/teasers/mair.png) | [[PDF](https://arxiv.org/pdf/2503.09403.pdf)] |
|[**Hybrid Agents for Image Restoration (HybridAgent)**](https://arxiv.org/abs/2503.10120)  
*Bingchen Li, Xin Li, Yiting Lu, Zhibo Chen*  
> arXiv 2025  
| ![intro](assets/teasers/hybridagent.png) | [[PDF](https://arxiv.org/pdf/2503.10120.pdf)] |
|[**Q-Agent: Quality-Driven Chain-of-Thought Image Restoration Agent through Robust Multimodal Large Language Model**](https://arxiv.org/abs/2504.07148)  
*Yingjie Zhou, Jiezhang Cao, Zicheng Zhang, Farong Wen, Yanwei Jiang, Jun Jia, Xiaohong Liu, Xiongkuo Min, Guangtao Zhai*  
> arXiv 2025  
| ![intro](assets/teasers/q-agent.png) | [[PDF](https://arxiv.org/pdf/2504.07148.pdf)] |
|[**JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration**](https://arxiv.org/abs/2504.04158)  
*Yunlong Lin, Zixu Lin, Haoyu Chen, Panwang Pan, Chenxin Li, Sixiang Chen, Yeying Jin, Wenbo Li, Xinghao Ding*  
> CVPR 2025  
| ![intro](assets/teasers/jarvisir.png) | [[Project](https://cvpr2025-jarvisir.github.io/)] [[PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Lin_JarvisIR_Elevating_Autonomous_Driving_Perception_with_Intelligent_Image_Restoration_CVPR_2025_paper.pdf)] [[arXiv PDF](https://arxiv.org/pdf/2504.04158.pdf)] |
|[**SimpleCall: A Lightweight Image Restoration Agent in Label-Free Environments with MLLM Perceptual Feedback**](https://arxiv.org/abs/2512.18599)  
*Jianglin Lu, Yuanwei Wu, Ziyi Zhao, Hongcheng Wang, Felix Jimenez, Abrar Majeedi, Yun Fu*  
> arXiv 2025 (Dec)  
| ![intro](assets/teasers/simplecall.png) | [[PDF](https://arxiv.org/pdf/2512.18599.pdf)] |

---

## Agentic Super-Resolution (SR)

| Title & Authors | Intro | Useful Links |
|:----|:----:|:---:|
|[**4KAgent: Agentic Any Image to 4K Super-Resolution**](https://arxiv.org/abs/2507.07105)  
*Yushen Zuo, Qi Zheng, Mingyang Wu, Xinrui Jiang, Renjie Li, Jian Wang, Yide Zhang, Gengchen Mai, Lihong V. Wang, James Zou, Xiaoyu Wang, Ming-Hsuan Yang, Zhengzhong Tu*  
> NeurIPS 2025  
| ![intro](assets/teasers/4kagent.png) | [[Github](https://github.com/taco-group/4KAgent)] [[PDF](https://arxiv.org/pdf/2507.07105.pdf)] |

---

## Resources (Datasets / Toolboxes)

| Name | Intro | Links |
|:----|:----:|:---:|
|**CleanBench** (instruction-following data for intelligent restoration)  
> Introduced by JarvisIR: includes large-scale synthetic + real instruction-response pairs.  
| ![intro](assets/teasers/cleanbench.png) | [[Project](https://cvpr2025-jarvisir.github.io/)] |

---

## Closely Related (Not strictly agentic)

| Title & Authors | Intro | Useful Links |
|:----|:----:|:---:|
|[**Multi-modal Large Language Model based Restoration Assistant (LLMRA)**](https://arxiv.org/abs/2401.11401)  
> MLLM/VLM produces degradation context to condition a restoration backbone.  
| ![intro](assets/teasers/llmra.png) | [[PDF](https://arxiv.org/pdf/2401.11401.pdf)] |
|[**Automatic All-in-One Image Restoration with Latent Diffusion (AutoDIR)**](https://arxiv.org/abs/2310.10123)  
> BIQA-driven degradation detection + diffusion-based all-in-one restoration.  
| ![intro](assets/teasers/autodir.png) | [[PDF](https://arxiv.org/pdf/2310.10123.pdf)] |
|[**A Survey on All-in-One Image Restoration**](https://arxiv.org/abs/2410.15067)  
> Taxonomy + benchmarks + evaluation protocols for unified restoration.  
| ![intro](assets/teasers/aioir-survey.png) | [[PDF](https://arxiv.org/pdf/2410.15067.pdf)] |

---

## Contributing

- Add a new row in the appropriate table.
- Put a teaser image under `assets/teasers/<slug>.png` (optional but recommended).
- Prefer official links (arXiv / CVF / OpenReview / official GitHub).

## License

This repository is licensed under **CC BY 4.0** (recommended for awesome lists).
