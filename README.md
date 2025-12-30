# Awesome-Agentic-Image-Restoration

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of **agentic image restoration** methods where an LLM/VLM acts as a controller to **perceive degradations**, **plan/schedule** restoration steps, and **execute** expert models/tools (denoise, deblur, dehaze, derain, SR, etc.).  
Contributions are welcome!

- Awesome-Agentic-Image-Restoration
  - Agentic IR
  - Agentic SR
  - Related: MLLM/VLM-assisted Restoration (non-agentic)
  - Datasets & Benchmarks
  - Toolboxes & Expert Models
  - Surveys

---

## Agentic IR

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [AgenticIR: Agentic Image Restoration with Task Decomposition, Tool Inventory, and Reward-Guided Planning](https://arxiv.org/abs/2410.17809) <br> Kaiwen Zhu *et al.* <br> > Preprint'24 | <img src="https://github.com/Kaiwen-Zhu/AgenticIR/raw/main/assets/workflow.png" width="420" /> | [Github](https://github.com/Kaiwen-Zhu/AgenticIR) |
| [JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration](https://cvpr2025-jarvisir.github.io/) <br> Yunlong Lin *et al.* <br> > CVPR'25 | <img src="https://cvpr2025-jarvisir.github.io/imgs/framework.png" width="420" /> | [Page](https://cvpr2025-jarvisir.github.io/) · [Github](https://github.com/LYL1015/JarvisIR) |
| [Multi-Agent Image Restoration (MAIR)](https://arxiv.org/abs/2503.09403) <br> Xu Jiang *et al.* <br> > Preprint'25 | -- | [arXiv](https://arxiv.org/abs/2503.09403) |
| [Hybrid Agents for Image Restoration (HybridAgent)](https://arxiv.org/abs/2503.10120) <br> Bingchen Li *et al.* <br> > Preprint'25 | -- | [arXiv](https://arxiv.org/abs/2503.10120) |
| [Q-Agent: Quality-Driven Chain-of-Thought Image Restoration Agent](https://arxiv.org/abs/2504.07148) <br> Yingjie Zhou *et al.* <br> > Preprint'25 | -- | [arXiv](https://arxiv.org/abs/2504.07148) |

---

## Agentic SR

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [4KAgent: Agentic Any Image to 4K Super-Resolution](https://arxiv.org/abs/2507.07105) <br> Jiahao Zuo *et al.* <br> > Preprint'25 | <img src="https://github.com/taco-group/4KAgent/raw/main/assets/4KAgent_framework.png" width="420" /> | [Github](https://github.com/taco-group/4KAgent) |

---

## Related: MLLM/VLM-assisted Restoration (non-agentic)

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [LLMRA: Multi-modal Large Language Model based Restoration Assistant](https://arxiv.org/abs/2401.11401) <br> Xiaoyu Jin *et al.* <br> > Preprint'24 | -- | [arXiv](https://arxiv.org/abs/2401.11401) |
| [AutoDIR: Automatic All-in-One Image Restoration with Latent Diffusion](https://arxiv.org/abs/2310.10123) <br> Yitong Jiang *et al.* <br> > Preprint'23 | <img src="https://jiangyitong.github.io/AutoDIR_webpage/static/images/method_full.png" width="420" /> | [Page](https://jiangyitong.github.io/AutoDIR_webpage/) · [Code](https://github.com/jiangyitong/AutoDIR) |

---

## Datasets & Benchmarks

| Resource | What it is | Links |
|---|---|---|
| CleanBench | Instruction–response data for training/evaluating restoration agents (synthetic + real) | [JarvisIR Repo](https://github.com/LYL1015/JarvisIR) · [Project Page](https://cvpr2025-jarvisir.github.io/) |
| (Add more) | Commonly used IR benchmarks (GoPro, Rain13K, SOTS, etc.) | PRs welcome |

---

## Toolboxes & Expert Models

### Agentic toolboxes / codebases
- **AgenticIR toolbox** (multi-tool planning/execution): https://github.com/Kaiwen-Zhu/AgenticIR  
- **JarvisIR toolbox** (expert model library + training/inference code): https://github.com/LYL1015/JarvisIR  
- **4KAgent** (agentic SR pipeline): https://github.com/taco-group/4KAgent  
- **AutoDIR** (BIQA + diffusion-based editing for restoration): https://github.com/jiangyitong/AutoDIR  

### Frequently-used expert models (often wrapped as tools)
- **Restormer**, **SwinIR**, **MPRNet**, **MAXIM**, **NAFNet** (general IR backbones)  
- **Real-ESRGAN** (SR / deblurring / artifact removal)  
- **SCUNet** (denoising)  
- Task-specific tools: dehazing / deraining / deblurring / JPEG artifact removal, etc.

---

## Surveys

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [A Survey on All-in-One Image Restoration](https://arxiv.org/abs/2410.15067) <br> (AiOIR Survey) <br> > Preprint'24 | -- | [arXiv](https://arxiv.org/abs/2410.15067) |

---

## Paper List

| Paper | First Author | Year | Topic |
|---|---|---:|---|
| [AutoDIR](https://arxiv.org/abs/2310.10123) | Jiang | 2023 | BIQA + diffusion for restoration |
| [LLMRA](https://arxiv.org/abs/2401.11401) | Jin | 2024 | VLM/MLLM-assisted universal IR |
| [AgenticIR](https://arxiv.org/abs/2410.17809) | Zhu | 2024 | Agentic IR (planner + toolbox) |
| [JarvisIR](https://cvpr2025-jarvisir.github.io/) | Lin | 2025 | VLM controller + expert library |
| [MAIR](https://arxiv.org/abs/2503.09403) | Jiang | 2025 | Multi-agent scheduling/experts |
| [HybridAgent](https://arxiv.org/abs/2503.10120) | Li | 2025 | Fast/slow/feedback agents |
| [Q-Agent](https://arxiv.org/abs/2504.07148) | Zhou | 2025 | IQA-driven greedy CoT |
| [4KAgent](https://arxiv.org/abs/2507.07105) | Zuo | 2025 | Agentic 4K super-resolution |

---

## Contributing

1. Add the paper/resource into the corresponding section table.  
2. Prefer linking to **official arXiv/project pages** and **official code repositories**.  
3. For the **Intro** column, prefer a **framework/architecture figure** hosted on the paper’s official GitHub repo or GitHub Pages site.  

If you maintain a related project and would like it listed or corrected, feel free to open an issue/PR.
