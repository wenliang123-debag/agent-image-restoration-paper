# Awesome-Agentic-CV

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

A curated list of **agentic computer vision** methods where an LLM/VLM/MLLM acts as a controller to **perceive visual inputs**, **plan/schedule actions**, and **execute external tools/models** for image restoration, enhancement, retouching, editing, and broader visual tool use.

Contributions are welcome!

> **Scope**
> - **Agentic** = explicit **perception → planning/scheduling → tool/model execution**, optionally with **reflection / rollback / memory / search / self-correction**
> - **CV** includes **image restoration / enhancement / SR**, **photo retouching / image editing**, and **vision-guided tool use**
> - Pure **all-in-one** or **instruction-only** methods without explicit agent loops are **excluded**

---

## Contents

- [Agentic Low-Level Vision](#agentic-low-level-vision)
- [Agentic Image Editing / Retouching](#agentic-image-editing--retouching)
- [General Vision Tool-Use Agents](#general-vision-tool-use-agents)
- [Benchmarks & Datasets](#benchmarks--datasets)
- [Toolboxes & Platforms](#toolboxes--platforms)
- [Contributing](#contributing)

---

## Agentic Low-Level Vision

> Agentic methods for **image restoration, enhancement, and super-resolution**.

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://arxiv.org/abs/2407.18035) <br> Haoyu Chen *et al.* <br> > NeurIPS'24 |<img src="https://haoyuchen.com/assets/img/RestoreAgent/method.png" width="840" /> | [arXiv](https://arxiv.org/abs/2407.18035) · [NeurIPS PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf) · [Project Page](https://haoyuchen.com/RestoreAgent) |
| [AgenticIR: Agentic Image Restoration with Task Decomposition, Tool Inventory, and Reward-Guided Planning](https://arxiv.org/abs/2410.17809) <br> Kaiwen Zhu *et al.* <br> > ICLR'25 | <img src="https://github.com/Kaiwen-Zhu/AgenticIR/raw/main/assets/workflow.png" width="840" /> | [arXiv](https://arxiv.org/abs/2410.17809) · [GitHub](https://github.com/Kaiwen-Zhu/AgenticIR) · [OpenReview](https://openreview.net/forum?id=3RLxccFPHz) |
| [JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration](https://arxiv.org/abs/2504.04158) <br> Yunlong Lin *et al.* <br> > CVPR'25 | <img src="https://cvpr2025-jarvisir.github.io/imgs/framework.png" width="840" /> | [arXiv](https://arxiv.org/abs/2504.04158) · [Project Page](https://cvpr2025-jarvisir.github.io/) · [GitHub](https://github.com/LYL1015/JarvisIR) |
| [Multi-Agent Image Restoration (MAIR)](https://arxiv.org/abs/2503.09403) <br> Xu Jiang *et al.* <br> > Preprint'25 | -- | [arXiv](https://arxiv.org/abs/2503.09403) |
| [Hybrid Agents for Image Restoration (HybridAgent)](https://arxiv.org/abs/2503.10120) <br> Bingchen Li *et al.* <br> > Preprint'25 | -- | [arXiv](https://arxiv.org/abs/2503.10120) |
| [Q-Agent: Quality-Driven Chain-of-Thought Image Restoration Agent](https://arxiv.org/abs/2504.07148) <br> Yingjie Zhou *et al.* <br> > Preprint'25 | -- | [arXiv](https://arxiv.org/abs/2504.07148) |
| [4KAgent: Agentic Any Image to 4K Super-Resolution](https://arxiv.org/abs/2507.07105) <br> Jiahao Zuo *et al.* <br> > NeurIPS'25 | <img src="https://github.com/taco-group/4KAgent/raw/main/assets/4KAgent_framework.png" width="840" /> | [arXiv](https://arxiv.org/abs/2507.07105) · [GitHub](https://github.com/taco-group/4KAgent) · [Project Page](https://4kagent.github.io/) |
| [PaAgent: Portrait-Aware Image Restoration Agent via Subjective-Objective Reinforcement Learning](https://arxiv.org/abs/2603.17055) <br> Yijian Wang *et al.* <br> > Preprint'26 |  <img src="https://wyjgr.github.io/images/PaAgent/Method/Framework.png" width="840" /> | [arXiv](https://arxiv.org/abs/2603.17055) · [Project Page](https://wyjgr.github.io/PaAgent.html) |

---

## Agentic Image Editing / Retouching

> Agentic methods for **photo retouching, iterative image editing, and generation-editing workflows**.

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [GenArtist: Multimodal LLM as an Agent for Unified Image Generation and Editing](https://arxiv.org/abs/2407.05600) <br> Zhenyu Wang *et al.* <br> > NeurIPS'24 | -- | [arXiv](https://arxiv.org/abs/2407.05600) · [Project Page](https://zhenyuw16.github.io/GenArtist_page) · [GitHub](https://github.com/zhenyuw16/GenArtist) |
| [JarvisArt: Liberating Human Artistic Creativity via an Intelligent Photo Retouching Agent](https://arxiv.org/abs/2506.17612) <br> Yunlong Lin *et al.* <br> > NeurIPS'25 | -- | [arXiv](https://arxiv.org/abs/2506.17612) · [GitHub](https://github.com/LYL1015/JarvisArt) |
| [CoSTA*: Cost-Sensitive Toolpath Agent for Multi-turn Image Editing](https://arxiv.org/abs/2503.10613) <br> Advait Gupta *et al.* <br> > Preprint'25 | <img src="https://github.com/tianyi-lab/CoSTAR/raw/main/main.png" width="840" /> | [arXiv](https://arxiv.org/abs/2503.10613) · [GitHub](https://github.com/tianyi-lab/CoSTAR) |
| [FaSTA*: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing](https://arxiv.org/abs/2506.20911) <br> Advait Gupta *et al.* <br> > ICLR'26 | <img src="https://github.com/tianyi-lab/FaSTAR/raw/main/asset/schematic.png" width="840" /> | [arXiv](https://arxiv.org/abs/2506.20911) · [OpenReview](https://openreview.net/forum?id=yhhbL9T1QB) · [GitHub](https://github.com/tianyi-lab/FaSTAR) |
| [MIRA: Multimodal Iterative Reasoning Agent for Image Editing](https://arxiv.org/abs/2511.21087) <br> Ziyun Zeng *et al.* <br> > Preprint'25 |<img src="https://github.com/zhenyuw16/GenArtist/blob/main/docs/frame.png" width="840" /> | [arXiv](https://arxiv.org/abs/2511.21087) · [GitHub](https://github.com/zzzmyyzeng/MIRA) |
| [JarvisEvo: Towards a Self-Evolving Photo Editing Agent with Synergistic Editor–Evaluator Optimization](https://arxiv.org/abs/2511.23002) <br> Yunlong Lin *et al.* <br> > CVPR'26 | <img src="https://github.com/LYL1015/JarvisEvo/raw/main/assets/framework.png" width="840" /> | [arXiv](https://arxiv.org/abs/2511.23002) · [GitHub](https://github.com/LYL1015/JarvisEvo) · [Project Page](https://jarvisevo.vercel.app/) |
| [ARTIE: A Plug-and-Play Agentic Framework for Text Guided Image Editing](https://openreview.net/forum?id=EPAuWPVcZQ) <br> Dibyanayan Bandyopadhyay *et al.* <br> > ICLR'26 (OpenReview) | -- | [OpenReview](https://openreview.net/forum?id=EPAuWPVcZQ) |
| [Agent Banana: High-Fidelity Image Editing with Agentic Thinking and Tooling](https://arxiv.org/abs/2602.09084) <br> Ruijie Ye *et al.* <br> > Preprint'26 | <img src="https://github.com/taco-group/agent-banana/raw/main/assets/framework.png" width="840" /> | [arXiv](https://arxiv.org/abs/2602.09084) · [GitHub](https://github.com/taco-group/agent-banana) · [Project Page](https://agent-banana.github.io/) |
| [PhotoAgent: Agentic Photo Editing with Exploratory Visual Aesthetic Planning](https://arxiv.org/abs/2602.22809) <br> Mingde Yao *et al.* <br> > Preprint'26 | <img src="https://github.com/mdyao/PhotoAgent/raw/main/images/photoagent_loop.png" width="840" /> | [arXiv](https://arxiv.org/abs/2602.22809) · [GitHub](https://github.com/mdyao/PhotoAgent) · [Project Page](https://mdyao.github.io/PhotoAgent/) |
| [RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward](https://arxiv.org/abs/2602.17558) <br> Qianqian Wu *et al.* <br> > Preprint'26 | -- | [arXiv](https://arxiv.org/abs/2602.17558) |

---

## General Vision Tool-Use Agents

> Agentic methods where **visual perception is directly coupled with multi-step tool use / planning / execution**.

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://arxiv.org/abs/2412.15606) <br> Zhi Gao *et al.* <br> > ICLR'25 | -- | [arXiv](https://arxiv.org/abs/2412.15606) · [Project Page](https://mat-agent.github.io/) |
| [VTool-R1: VLMs Learn to Think with Images via Reinforcement Learning on Multimodal Tool Use](https://arxiv.org/abs/2505.19255) <br> Minghao Wu *et al.* <br> > ICLR'26 | -- | [arXiv](https://arxiv.org/abs/2505.19255) · [Project Page](https://vtool-r1.github.io/) · [GitHub](https://github.com/VTOOL-R1/vtool-r1) |
| [ToolScope: An Agentic Framework for Vision-Guided and Long-Horizon Tool Use](https://arxiv.org/abs/2510.27363) <br> Mengjie Deng *et al.* <br> > Preprint'25 | -- | [arXiv](https://arxiv.org/abs/2510.27363) · [GitHub](https://github.com/dengmengjie/ToolScope) |

---

## Benchmarks & Datasets

| Resource | What it is | Links |
|---|---|---|
| **CleanBench** | Benchmark / data resource for restoration agents | [JarvisIR Repo](https://github.com/LYL1015/JarvisIR) · [JarvisIR Page](https://cvpr2025-jarvisir.github.io/) |
| **UGC-Edit** | Autonomous photo editing benchmark released with PhotoAgent | [PhotoAgent Repo](https://github.com/mdyao/PhotoAgent) · [PhotoAgent arXiv](https://arxiv.org/abs/2602.22809) |
| **HDD-Bench** | Native-4K long-horizon editing benchmark released with Agent Banana | [Agent Banana Repo](https://github.com/taco-group/agent-banana) · [Agent Banana arXiv](https://arxiv.org/abs/2602.09084) |
| **ArtEdit-Bench** | Photo editing benchmark released with JarvisEvo | [JarvisEvo Repo](https://github.com/LYL1015/JarvisEvo) |
| **AgentVista** | Benchmark for realistic multimodal visual agents | [Project Page](https://agentvista-bench.github.io/) |
| **VTC-Bench** | Benchmark for compositional visual tool chaining / visual tool-use evaluation | [arXiv](https://arxiv.org/abs/2603.15030) |

---

## Toolboxes & Platforms

### Agentic CV toolboxes / codebases
- **AgenticIR** — multi-stage restoration agent with tool planning and reward-guided execution  
- **JarvisIR** — intelligent restoration toolbox for autonomous driving perception  
- **4KAgent** — agentic super-resolution pipeline  
- **CoSTAR / FaSTAR** — graph-search / fast-slow toolpath agents for image editing  
- **PhotoAgent** — exploratory planning for autonomous photo editing  
- **Agent Banana** — planner-executor editing framework with layer-aware control  
- **JarvisArt / JarvisEvo** — professional photo retouching agents  
- **VTool-R1 / ToolScope / T3-Agent** — general visual tool-use agents

### Frequently used expert models / backbones
- **Restormer**, **SwinIR**, **MPRNet**, **MAXIM**, **NAFNet**
- **Real-ESRGAN**
- **SCUNet**
- **BasicSR**

---

## Contributing

1. Add the paper/resource into the corresponding section.  
2. Prefer linking to **official arXiv / project pages / GitHub repositories**.  
3. For the **Intro** column, prefer a **framework / pipeline figure** from the official repo or project page.  
4. Keep the format consistent: **Title · Authors · Venue/Year · Links**.  
5. Only include work with a clear **agent loop**: visual perception + planning/tool use + execution.

If you maintain a related project and would like it listed or corrected, feel free to open an issue / PR.
