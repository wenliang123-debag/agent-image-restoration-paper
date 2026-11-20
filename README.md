<h1 align="center">Awesome Agentic Computer Vision</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

Papers, benchmarks, and tools for vision agents that plan, call tools, or adapt to feedback.

[Restoration](#agentic-low-level-vision) · [Editing](#agentic-image-editing--retouching) · [Vision Tool Use](#general-vision-tool-use-agents) · [Benchmarks](#benchmarks--datasets) · [Toolboxes](#toolboxes--platforms) · [Contributing](#contributing)

**52 papers** · [Paper notes and figures](docs/paper-notes.md) · [October verification record](docs/verification-2026-10-25.md)

Preprint and submission labels do not indicate acceptance. A dash in the Code column means no code link is listed.

† Task- or domain-specific agent. Standalone vision backbones are listed as supporting tools, not agents.

## Agentic Low-Level Vision

### 2026

| Paper | Venue | Link | Code |
|---|---|---|---|
| Multi-Agent Image Restoration (MAIR)<br>Xu Jiang *et al.* | IJCV 2026 | [arXiv](https://arxiv.org/abs/2503.09403) · [Project](https://villa.jianzhang.tech/publication/200604/) · [Journal](https://link.springer.com/article/10.1007/s11263-026-02792-5) | — |
| Hybrid Agents for Image Restoration (HybridAgent)<br>Bingchen Li *et al.* | CVPR 2026 | [arXiv](https://arxiv.org/abs/2503.10120) · [HTML](https://arxiv.org/html/2503.10120) · [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Hybrid_Agents_for_Image_Restoration_CVPR_2026_paper.html) | — |
| FAPE-IR: Frequency-Aware Planning and Execution Framework for All-in-One Image Restoration<br>Jingren Liu *et al.* | CVPR 2026 | [arXiv](https://arxiv.org/abs/2511.14099) · [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_FAPE-IR_Frequency-Aware_Planning_and_Execution_Framework_for_All-in-One_Image_Restoration_CVPR_2026_paper.html) | [Code](https://github.com/Programmergg/FAPE-IR) |
| Restore-R1: Efficient Image Restoration Agents via Reinforcement Learning with Multimodal LLM Perceptual Feedback<br>Jianglin Lu *et al.* | CVPR Findings 2026 | [arXiv](https://arxiv.org/abs/2512.18599) · [CVPR PDF](https://openaccess.thecvf.com/content/CVPR2026F/papers/Lu_Restore-R1_Efficient_Image_Restoration_Agents_via_Reinforcement_Learning_with_Multimodal_CVPRF_2026_paper.pdf) · [HTML](https://arxiv.org/html/2512.18599v2) | — |
| Derain-Agent: A Plug-and-Play Agent Framework for Rainy Image Restoration<br>Zhaocheng Yu *et al.* | Preprint 2026 † | [arXiv](https://arxiv.org/abs/2603.11866) · [PDF](https://arxiv.org/pdf/2603.11866) · [HTML](https://arxiv.org/html/2603.11866) | — |
| PaAgent: Portrait-Aware Image Restoration Agent via Subjective-Objective Reinforcement Learning<br>Yijian Wang *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2603.17055) · [Project](https://wyjgr.github.io/PaAgent.html) | — |
| IAMAgent: Toward an Interactive and Adaptive Multi-Agent System for Image Restoration<br>Yanyan Wei *et al.* | IEEE TIP 2026 | [DOI](https://doi.org/10.1109/TIP.2026.3671594) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/41817987/) | — |
| TIR-Agent: Training an Explorative and Efficient Agent for Image Restoration<br>Guoli Jia *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2603.27742) · [PDF](https://arxiv.org/pdf/2603.27742) · [HTML](https://arxiv.org/html/2603.27742) | — |
| EpiAgent: An Agent-Centric System for Ancient Inscription Restoration<br>Shipeng Zhu *et al.* | CVPR 2026 † | [arXiv](https://arxiv.org/abs/2604.09367) · [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_EpiAgent_An_Agent-Centric_System_for_Ancient_Inscription_Restoration_CVPR_2026_paper.html) | [Code](https://github.com/blackprotoss/EpiAgent) |
| OPERA: An Agent for Image Restoration with End-to-End Joint Planning-Execution Optimization<br>Feng Zhu *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2605.22104) · [PDF](https://arxiv.org/pdf/2605.22104) | [Code](https://github.com/xsyshuishui/Opera) |
| EvoIR-Agent: Self-Evolving Image Restoration Agentic System via Experience-Driven Learning<br>Kailin Zhuang *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2605.22208) · [PDF](https://arxiv.org/pdf/2605.22208) | [Code](https://github.com/rightleft-123/EvoIRAgent) |
| DiTTo: Scalable Order-aware All-in-One Image Restoration Agent<br>Seungho Choi, Jihyong Oh | Preprint 2026 | [arXiv](https://arxiv.org/abs/2605.30915) · [Project](https://cmlab-korea.github.io/DiTTo/) | [Code](https://github.com/CMLab-Korea/DiTTo-arxiv) |
| Beyond Sequential Tools: A Unified VLM Agent System for Photographic Post-Processing via Dynamic Multi-Expert Fusion<br>Honglin Xiong *et al.* | CVPR 2026 † | [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_Beyond_Sequential_Tools_A_Unified_VLM_Agent_System_for_Photographic_CVPR_2026_paper.html) | — |
| HDRAgent: An Agentic Framework for Multi-Exposure HDR Imaging<br>Weiyu Zhou *et al.* | Preprint 2026 † | [arXiv](https://arxiv.org/abs/2606.09110) · [PDF](https://arxiv.org/pdf/2606.09110) · [HTML](https://arxiv.org/html/2606.09110) | — |
| Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution (SEAR)<br>Shuang Cui *et al.* | ECCV 2026 | [arXiv](https://arxiv.org/abs/2606.28971) · [PDF](https://arxiv.org/pdf/2606.28971) · [HTML](https://arxiv.org/html/2606.28971) | — |
| RIR-Agent: An Interactive Framework for Effective and Adaptive Restoration of Remote Sensing Imagery<br>Junyu Liu *et al.* | Expert Systems with Applications 2026 † | [DOI](https://doi.org/10.1016/j.eswa.2026.132495) · [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417426014089) | — |
| Causal-AgentIR: Self-Evolving Causal Memory for Adaptive Image Restoration Agents<br>Hu Gao *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2607.21125) · [PDF](https://arxiv.org/pdf/2607.21125) · [HTML](https://arxiv.org/html/2607.21125) | — |
| Agentic AI-powered flexible fiber-bundle endoscopy for high-resolution NIR-II fluorescence imaging in vivo<br>Yanzhao Shi *et al.* | Preprint 2026 † | [arXiv](https://arxiv.org/abs/2608.08402) · [PDF](https://arxiv.org/pdf/2608.08402) | — |
| VLM- and LLM-Driven Multi-Agent System for PET Image Denoising<br>Boxiao Yu *et al.* | Preprint 2026 † | [arXiv](https://arxiv.org/abs/2608.13791) · [PDF](https://arxiv.org/pdf/2608.13791) · [HTML](https://arxiv.org/html/2608.13791) | — |
| SkillIR: Evolving Scene-Aware Skills for Agentic Image Restoration<br>Jie Shao *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2609.21468) · [PDF](https://arxiv.org/pdf/2609.21468) | — |
| PrismRestore: A Compact Restoration Toolbox for Agentic Image Restoration<br>Zhaocheng Yu *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2611.24915) · [HTML](https://arxiv.org/html/2611.24915v1) | — |
| RecurIR: Learning When and How to Revise Restoration Policies via Recursive Self-Improvement<br>Hu Gao *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2611.18006) · [HTML](https://arxiv.org/html/2611.18006v1) | — |
| Look Before You Restore: Learning to Predict Before Acting for Agentic Image Restoration (PreActIR)<br>Xu Zhang *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2610.20384) · [HTML](https://arxiv.org/html/2610.20384v1) | [Code](https://github.com/House-yuyu/PreActIR) |
| HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration<br>Xiangtao Kong *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2610.10133) | [Code](https://github.com/PolyU-VCLab/HarnessIR) |
| EORestore-Agent: Fidelity-Guided Agentic Restoration of Remote Sensing Images with Composite Degradations<br>Heli Qi *et al.* | Preprint 2026 † | [arXiv](https://arxiv.org/abs/2610.06196) · [HTML](https://arxiv.org/html/2610.06196v1) | — |

### 2025

| Paper | Venue | Link | Code |
|---|---|---|---|
| An Intelligent Agentic System for Complex Image Restoration Problems (AgenticIR)<br>Kaiwen Zhu *et al.* | ICLR 2025 | [arXiv](https://arxiv.org/abs/2410.17809) · [Project](https://kaiwen-zhu.github.io/research/agenticir) | [Code](https://github.com/Kaiwen-Zhu/AgenticIR) |
| JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration<br>Yunlong Lin *et al.* | CVPR 2025 † | [arXiv](https://arxiv.org/abs/2504.04158) · [Project](https://cvpr2025-jarvisir.github.io/) | [Code](https://github.com/LYL1015/JarvisIR) |
| Q-Agent: Quality-Driven Chain-of-Thought Image Restoration Agent through Robust Multimodal Large Language Model<br>Yingjie Zhou *et al.* | Preprint 2025 | [arXiv](https://arxiv.org/abs/2504.07148) · [PDF](https://arxiv.org/pdf/2504.07148) · [HTML](https://arxiv.org/html/2504.07148) | — |
| 4KAgent: Agentic Any Image to 4K Super-Resolution<br>Yushen Zuo *et al.* | NeurIPS 2025 † | [arXiv](https://arxiv.org/abs/2507.07105) · [Project](https://4kagent.github.io/) · [NeurIPS](https://papers.neurips.cc/paper_files/paper/2025/hash/f0075fe4e59652cf43148dcfab8d3c93-Abstract-Conference.html) | [Code](https://github.com/taco-group/4KAgent) |

### 2024

| Paper | Venue | Link | Code |
|---|---|---|---|
| RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models<br>Haoyu Chen *et al.* | NeurIPS 2024 | [arXiv](https://arxiv.org/abs/2407.18035) · [Project](https://haoyuchen.com/RestoreAgent) · [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf) | — |

## Agentic Image Editing / Retouching

### 2026

| Paper | Venue | Link | Code |
|---|---|---|---|
| FaSTA*: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing<br>Advait Gupta *et al.* | ICLR 2026 | [arXiv](https://arxiv.org/abs/2506.20911) · [OpenReview](https://openreview.net/forum?id=yhhbL9T1QB) | [Code](https://github.com/tianyi-lab/FaSTAR) |
| MIRA: Multimodal Iterative Reasoning Agent for Image Editing<br>Ziyun Zeng *et al.* | CVPR Findings 2026 | [arXiv](https://arxiv.org/abs/2511.21087) · [CVF](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_MIRA_Multimodal_Iterative_Reasoning_Agent_for_Image_Editing_CVPRF_2026_paper.html) | [Code](https://github.com/zzzmyyzeng/MIRA) |
| JarvisEvo: Towards a Self-Evolving Photo Editing Agent with Synergistic Editor-Evaluator Optimization<br>Yunlong Lin *et al.* | CVPR 2026 | [arXiv](https://arxiv.org/abs/2511.23002) · [Project](https://jarvisevo.vercel.app/) · [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_JarvisEvo_Towards_a_Self-Evolving_Photo_Editing_Agent_with_Synergistic_Editor-Evaluator_CVPR_2026_paper.html) | [Code](https://github.com/LYL1015/JarvisEvo) |
| A Plug-and-Play Agentic Framework for Text Guided Image Editing (ARTIE)<br>Dibyanayan Bandyopadhyay *et al.* | OpenReview submission 2026 (decision unverified) | [OpenReview](https://openreview.net/forum?id=EPAuWPVcZQ) | — |
| Agent Banana: High-Fidelity Image Editing with Agentic Thinking and Tooling<br>Ruijie Ye *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2602.09084) · [Project](https://agent-banana.github.io/) | [Code](https://github.com/taco-group/agent-banana) |
| PhotoAgent: Exploratory Visual Aesthetic Planning with Large Vision Models<br>Mingde Yao *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2602.22809) · [Project](https://mdyao.github.io/PhotoAgent/) | [Code](https://github.com/mdyao/PhotoAgent) |
| RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward<br>Qiucheng Wu *et al.* | CVPR 2026 | [arXiv](https://arxiv.org/abs/2602.17558) · [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_RetouchIQ_MLLM_Agents_for_Instruction-Based_Image_Retouching_with_Generalist_Reward_CVPR_2026_paper.html) | — |
| Agentic Retoucher for Text-To-Image Generation<br>Shaocheng Shen *et al.* | CVPR 2026 | [arXiv](https://arxiv.org/abs/2601.02046) · [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_Agentic_Retoucher_for_Text-To-Image_Generation_CVPR_2026_paper.html) | — |
| CAMEO: A Conditional and Quality-Aware Multi-Agent Image Editing Orchestrator<br>Yuhan Pu *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2604.03156) | — |
| What Can I Edit? Open-Ended Strategy Discovery and the Emotion Editability Landscape (EmoScope)<br>Qing Li *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2607.23920) · [PDF](https://arxiv.org/pdf/2607.23920) · [HTML](https://arxiv.org/html/2607.23920) | — |
| DrawAI: Agentic Benchmark and Workflow for Making Raster Images Editable<br>Pu Cao *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2608.00548) · [PDF](https://arxiv.org/pdf/2608.00548) · [HTML](https://arxiv.org/html/2608.00548) · [Project](https://drawai.renaissancemind.ai/) | — |
| EditAgent: Rethinking Agentic Image Editing<br>Haiyang Xu *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2610.39664) · [Project](https://editagent.github.io/) | — |

### 2025

| Paper | Venue | Link | Code |
|---|---|---|---|
| JarvisArt: Liberating Human Artistic Creativity via an Intelligent Photo Retouching Agent<br>Yunlong Lin *et al.* | NeurIPS 2025 | [arXiv](https://arxiv.org/abs/2506.17612) | [Code](https://github.com/LYL1015/JarvisArt) |
| CoSTA*: Cost-Sensitive Toolpath Agent for Multi-turn Image Editing<br>Advait Gupta *et al.* | Preprint 2025 | [arXiv](https://arxiv.org/abs/2503.10613) | [Code](https://github.com/tianyi-lab/CoSTAR) |

### 2024

| Paper | Venue | Link | Code |
|---|---|---|---|
| GenArtist: Multimodal LLM as an Agent for Unified Image Generation and Editing<br>Zhenyu Wang *et al.* | NeurIPS 2024 | [arXiv](https://arxiv.org/abs/2407.05600) · [Project](https://zhenyuw16.github.io/GenArtist_page) | [Code](https://github.com/zhenyuw16/GenArtist) |

## General Vision Tool-Use Agents

### 2026

| Paper | Venue | Link | Code |
|---|---|---|---|
| VTool-R1: VLMs Learn to Think with Images via Reinforcement Learning on Multimodal Tool Use<br>Mingyuan Wu *et al.* | ICLR 2026 | [arXiv](https://arxiv.org/abs/2505.19255) · [Project](https://vtool-r1.github.io/) · [OpenReview](https://openreview.net/forum?id=Idst6X6gmy) | [Code](https://github.com/VTool-R1/VTool-R1) |
| ToolScope: An Agentic Framework for Vision-Guided and Long-Horizon Tool Use<br>Mengjie Deng *et al.* | ACL Findings 2026 | [arXiv](https://arxiv.org/abs/2510.27363) · [ACL Anthology](https://aclanthology.org/2026.findings-acl.11/) · [DOI](https://doi.org/10.18653/v1/2026.findings-acl.11) | [Code](https://github.com/dengmengjie/ToolScope) |
| SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them<br>Yang Zhou *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2607.27703) · [PDF](https://arxiv.org/pdf/2607.27703) · [HTML](https://arxiv.org/html/2607.27703) | — |
| FaithEyes: Towards Faithful Tool Use via Multi-Agent Process-Image Self-Verification<br>Haoqing Wang *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2607.28225) · [PDF](https://arxiv.org/pdf/2607.28225) · [HTML](https://arxiv.org/html/2607.28225) | [Code](https://github.com/Mosi-AI/FaithEyes) |
| Beacon: Knowing When and How to Perform Agentic Visual Reasoning<br>Qixun Wang *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2607.28595) · [PDF](https://arxiv.org/pdf/2607.28595) · [HTML](https://arxiv.org/html/2607.28595) | — |
| VC-Tooler: Learning Compositional and Adaptive Visual Tool Use<br>Yizheng Wu *et al.* | Preprint 2026 | [arXiv](https://arxiv.org/abs/2608.02217) · [PDF](https://arxiv.org/pdf/2608.02217) · [Project](https://w1zheng.github.io/VC-Tooler/) | — |

### 2025

| Paper | Venue | Link | Code |
|---|---|---|---|
| Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage<br>Zhi Gao *et al.* | ICLR 2025 | [arXiv](https://arxiv.org/abs/2412.15606) · [Project](https://mat-agent.github.io/) · [OpenReview](https://openreview.net/forum?id=BYUJycKQUy) | — |

## Benchmarks & Datasets

| Resource | What it is | Links |
|---|---|---|
| **CleanBench** | Training / evaluation resource for restoration agents; the author release distinguishes paper-test and later Real-80K splits | [JarvisIR Repo](https://github.com/LYL1015/JarvisIR) · [JarvisIR Page](https://cvpr2025-jarvisir.github.io/) |
| **UGC-Edit** | Autonomous photo editing benchmark released with PhotoAgent | [PhotoAgent Repo](https://github.com/mdyao/PhotoAgent) · [PhotoAgent arXiv](https://arxiv.org/abs/2602.22809) |
| **HDD-Bench** | Native-4K long-horizon editing benchmark released with Agent Banana | [Agent Banana Repo](https://github.com/taco-group/agent-banana) · [Agent Banana arXiv](https://arxiv.org/abs/2602.09084) |
| **ArtEdit-Bench** | Photo editing benchmark released with JarvisEvo | [JarvisEvo Repo](https://github.com/LYL1015/JarvisEvo) |
| **AgentVista** | Benchmark for realistic multimodal visual agents | [Project Page](https://agentvista-bench.github.io/) |
| **VTC-Bench** | Benchmark for compositional visual tool chaining / visual tool-use evaluation | [arXiv](https://arxiv.org/abs/2603.15030) |
| **MiO-100** | Multi-degradation image restoration evaluation set used by recent agentic IR works | [DiTTo Page](https://cmlab-korea.github.io/DiTTo/) |

---
## Toolboxes & Platforms

### Agent Implementations / Project Entrypoints

Author repositories and project pages are linked below. Project-only entries are labeled explicitly; see each paper row for additional sources.

| Area | Author repositories / project pages |
|---|---|
| Restoration | [AgenticIR](https://github.com/Kaiwen-Zhu/AgenticIR) · [JarvisIR](https://github.com/LYL1015/JarvisIR) · [4KAgent](https://github.com/taco-group/4KAgent) · [FAPE-IR](https://github.com/Programmergg/FAPE-IR) · [EpiAgent](https://github.com/blackprotoss/EpiAgent) |
| Restoration | [OPERA](https://github.com/xsyshuishui/Opera) · [EvoIR-Agent](https://github.com/rightleft-123/EvoIRAgent) · [DiTTo](https://github.com/CMLab-Korea/DiTTo-arxiv) · [RestoreAgent project](https://haoyuchen.com/RestoreAgent) · [MAIR project](https://villa.jianzhang.tech/publication/200604/) |
| Editing | [GenArtist](https://github.com/zhenyuw16/GenArtist) · [CoSTA*](https://github.com/tianyi-lab/CoSTAR) · [FaSTA*](https://github.com/tianyi-lab/FaSTAR) · [PhotoAgent](https://github.com/mdyao/PhotoAgent) · [Agent Banana](https://github.com/taco-group/agent-banana) · [JarvisArt](https://github.com/LYL1015/JarvisArt) · [JarvisEvo](https://github.com/LYL1015/JarvisEvo) |
| Visual tool use | [VTool-R1](https://github.com/VTool-R1/VTool-R1) · [ToolScope](https://github.com/dengmengjie/ToolScope) · [FaithEyes](https://github.com/Mosi-AI/FaithEyes) |

### Expert Models / Backbones

These are restoration tools that can support agent workflows; inclusion here does not classify the models themselves as agents.

| Model / framework | Official entry |
|---|---|
| Restormer | [swz30/Restormer](https://github.com/swz30/Restormer) |
| SwinIR | [JingyunLiang/SwinIR](https://github.com/JingyunLiang/SwinIR) |
| MPRNet | [swz30/MPRNet](https://github.com/swz30/MPRNet) |
| MAXIM | [google-research/maxim](https://github.com/google-research/maxim) — archived repository |
| NAFNet | [megvii-research/NAFNet](https://github.com/megvii-research/NAFNet) |
| Real-ESRGAN | [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) |
| SCUNet | [cszn/SCUNet](https://github.com/cszn/SCUNet) |
| BasicSR | [XPixelGroup/BasicSR](https://github.com/XPixelGroup/BasicSR) |

---

## Contributing

Use a focused PR and follow the [manual contribution guide](CONTRIBUTING.md): verify title, author order, version, venue and scope against primary sources, and include the evidence in the PR. Do not treat an OpenReview submission page as acceptance.

The catalog is maintained manually. See [PR #2](https://github.com/wenliang123-debag/agent-image-restoration-paper/pull/2) for the removal of automated maintenance.

Papers, figures, code and datasets retain their original authors' terms. This repository does not grant a new license to those external resources.
