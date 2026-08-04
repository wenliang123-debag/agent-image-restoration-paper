<h1 align="center">Awesome Agentic Computer Vision</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

<p align="center">
  <strong>A curated collection of agentic computer vision papers, benchmarks, and tool-use systems.</strong><br>
  Focused on methods that combine <strong>perception</strong>, <strong>planning</strong>, <strong>tool use</strong>, and <strong>interactive visual workflows</strong>.
</p>

<p align="center">
  <a href="#agentic-low-level-vision">Agentic Low-Level Vision</a> ·
  <a href="#agentic-image-editing--retouching">Image Editing / Retouching</a> ·
  <a href="#general-vision-tool-use-agents">Vision Tool-Use Agents</a> ·
  <a href="#benchmarks--datasets">Benchmarks</a> ·
  <a href="#toolboxes--platforms">Toolboxes</a> ·
  <a href="#contributing">Contributing</a>
</p>

---

## 👋 Introduction

**Awesome-Agentic-CV** collects research on **agentic computer vision**, especially methods that combine perception, planning, and tool use.

## 🧭 Agentic Workflows

- **[Agentic Low-Level Vision](#agentic-low-level-vision)**: image restoration, enhancement, super-resolution, and degradation-aware tool use.
- **[Agentic Image Editing / Retouching](#agentic-image-editing--retouching)**: photo retouching, iterative editing, and generation-editing workflows.
- **[General Vision Tool-Use Agents](#general-vision-tool-use-agents)**: visual perception coupled with multi-step tool use, planning, and execution.
- **[Benchmarks & Datasets](#benchmarks--datasets)**: evaluation sets for restoration, editing, and visual tool-use agents.
- **[Toolboxes & Platforms](#toolboxes--platforms)**: codebases, expert models, and reusable tool ecosystems.

---
## Agentic Low-Level Vision

> Agentic methods for **image restoration, enhancement, and super-resolution**.

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [Multi-Agent Image Restoration (MAIR)](https://arxiv.org/abs/2503.09403) <br> Xu Jiang *et al.* <br> > IJCV'26 | <a href="https://villa.jianzhang.tech/publication/200604/"><img src="https://arxiv.org/html/2503.09403v1/x2.png" width="960" alt="MAIR framework" /></a> | [arXiv](https://arxiv.org/abs/2503.09403) · [Project Page](https://villa.jianzhang.tech/publication/200604/) |
| [Hybrid Agents for Image Restoration (HybridAgent)](https://arxiv.org/abs/2503.10120) <br> Bingchen Li *et al.* <br> > CVPR'26 | <a href="https://arxiv.org/abs/2503.10120"><img src="https://arxiv.org/html/2503.10120v1/extracted/6276715/images/agent.png" width="960" alt="HybridAgent framework" /></a> | [arXiv](https://arxiv.org/abs/2503.10120) · [HTML](https://arxiv.org/html/2503.10120) |
| [Q-Agent: Quality-Driven Chain-of-Thought Image Restoration Agent](https://arxiv.org/abs/2504.07148) <br> Yingjie Zhou *et al.* <br> > Preprint'25 | <a href="https://arxiv.org/abs/2504.07148"><img src="https://arxiv.org/html/2504.07148v1/x3.png" width="960" alt="Q-Agent framework" /></a> | [arXiv](https://arxiv.org/abs/2504.07148) · [PDF](https://arxiv.org/pdf/2504.07148) · [HTML](https://arxiv.org/html/2504.07148) |
| [IAMAgent: Toward an Interactive and Adaptive Multi-Agent System for Image Restoration](https://doi.org/10.1109/TIP.2026.3671594) <br> Yanyan Wei *et al.* <br> > IEEE TIP'26 | <a href="https://doi.org/10.1109/TIP.2026.3671594"><img src="https://xuxiaogang.com/pics/iamagent.png" width="960" alt="IAMAgent framework" /></a> | [DOI](https://doi.org/10.1109/TIP.2026.3671594) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/41817987/) |
| [Derain-Agent: A Plug-and-Play Agent Framework for Rainy Image Restoration](https://arxiv.org/abs/2603.11866) <br> Zhaocheng Yu *et al.* <br> > Preprint'26 | <a href="https://arxiv.org/abs/2603.11866"><img src="https://arxiv.org/html/2603.11866v1/pipeline_v9.png" width="960" alt="Derain-Agent framework" /></a> | [arXiv](https://arxiv.org/abs/2603.11866) · [PDF](https://arxiv.org/pdf/2603.11866) · [HTML](https://arxiv.org/html/2603.11866) |
| [Restore-R1: Efficient Image Restoration Agents via Reinforcement Learning with Multimodal LLM Perceptual Feedback](https://arxiv.org/abs/2512.18599) <br> Jianglin Lu *et al.* <br> > CVPR Findings'26 | <a href="https://arxiv.org/abs/2512.18599"><img src="https://arxiv.org/html/2512.18599v2/x2.png" width="960" alt="Restore-R1 framework" /></a> | [arXiv](https://arxiv.org/abs/2512.18599) · [CVPR PDF](https://openaccess.thecvf.com/content/CVPR2026F/papers/Lu_Restore-R1_Efficient_Image_Restoration_Agents_via_Reinforcement_Learning_with_Multimodal_CVPRF_2026_paper.pdf) · [HTML](https://arxiv.org/html/2512.18599v2) |
| [TIR-Agent: Training an Explorative and Efficient Agent for Image Restoration](https://arxiv.org/abs/2603.27742) <br> Yisheng Zhang *et al.* <br> > Preprint'26 | <a href="https://arxiv.org/abs/2603.27742"><img src="https://arxiv.org/html/2603.27742v1/images/pipeline.png" width="960" alt="TIR-Agent training framework" /></a> | [arXiv](https://arxiv.org/abs/2603.27742) · [PDF](https://arxiv.org/pdf/2603.27742) · [HTML](https://arxiv.org/html/2603.27742) |
| [OPERA: An Agent for Image Restoration with End-to-End Joint Planning-Execution Optimization](https://arxiv.org/abs/2605.22104) <br> Feng Zhu *et al.* <br> > Preprint'26 | <a href="https://github.com/xsyshuishui/Opera"><img src="https://arxiv.org/html/2605.22104v1/x2.png" width="960" alt="OPERA framework" /></a> | [arXiv](https://arxiv.org/abs/2605.22104) · [PDF](https://arxiv.org/pdf/2605.22104) · [GitHub](https://github.com/xsyshuishui/Opera) |
| [EvoIR-Agent: Self-Evolving Image Restoration Agentic System via Experience-Driven Learning](https://arxiv.org/abs/2605.22208v1) <br> Kailin Zhuang *et al.* <br> > Preprint'26 | -- | [arXiv v1](https://arxiv.org/abs/2605.22208v1) · [PDF v1](https://arxiv.org/pdf/2605.22208v1) · [GitHub](https://github.com/rightleft-123/EvoIRAgent) |
| [Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution (SEAR)](https://arxiv.org/abs/2606.28971) <br> Shuang Cui *et al.* <br> > ECCV'26 | <a href="https://arxiv.org/abs/2606.28971"><img src="https://arxiv.org/html/2606.28971v1/x3.png" width="960" alt="SEAR framework" /></a> | [arXiv](https://arxiv.org/abs/2606.28971) · [PDF](https://arxiv.org/pdf/2606.28971) · [HTML](https://arxiv.org/html/2606.28971) |
| [Causal-AgentIR: Self-Evolving Causal Memory for Adaptive Image Restoration Agents](https://arxiv.org/abs/2607.21125) <br> Hu Gao *et al.* <br> > Preprint'26 | -- | [arXiv](https://arxiv.org/abs/2607.21125) · [PDF](https://arxiv.org/pdf/2607.21125) · [HTML](https://arxiv.org/html/2607.21125) |
---

## Agentic Image Editing / Retouching

> Agentic methods for **photo retouching, iterative image editing, and generation-editing workflows**.

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [GenArtist: Multimodal LLM as an Agent for Unified Image Generation and Editing](https://arxiv.org/abs/2407.05600) <br> Zhenyu Wang *et al.* <br> > NeurIPS'24 | <a href="https://github.com/zhenyuw16/GenArtist"><img src="https://github.com/zhenyuw16/GenArtist/raw/main/docs/frame.png" width="960" alt="GenArtist framework" /></a> | [arXiv](https://arxiv.org/abs/2407.05600) · [Project Page](https://zhenyuw16.github.io/GenArtist_page) · [GitHub](https://github.com/zhenyuw16/GenArtist) |
| [JarvisArt: Liberating Human Artistic Creativity via an Intelligent Photo Retouching Agent](https://arxiv.org/abs/2506.17612) <br> Yunlong Lin *et al.* <br> > NeurIPS'25 | <a href="https://github.com/LYL1015/JarvisArt"><img src="https://github.com/LYL1015/JarvisArt/raw/main/assets/teaser.jpg" width="960" alt="JarvisArt teaser" /></a> | [arXiv](https://arxiv.org/abs/2506.17612) · [GitHub](https://github.com/LYL1015/JarvisArt) |
| [CoSTA*: Cost-Sensitive Toolpath Agent for Multi-turn Image Editing](https://arxiv.org/abs/2503.10613) <br> Advait Gupta *et al.* <br> > Preprint'25 | <a href="https://github.com/tianyi-lab/CoSTAR"><img src="https://github.com/tianyi-lab/CoSTAR/raw/main/main.png" width="960" alt="CoSTAR framework" /></a> | [arXiv](https://arxiv.org/abs/2503.10613) · [GitHub](https://github.com/tianyi-lab/CoSTAR) |
| [FaSTA*: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing](https://arxiv.org/abs/2506.20911) <br> Advait Gupta *et al.* <br> > ICLR'26 | <a href="https://github.com/tianyi-lab/FaSTAR"><img src="https://github.com/tianyi-lab/FaSTAR/raw/main/asset/schematic.png" width="960" alt="FaSTAR framework" /></a> | [arXiv](https://arxiv.org/abs/2506.20911) · [OpenReview](https://openreview.net/forum?id=yhhbL9T1QB) · [GitHub](https://github.com/tianyi-lab/FaSTAR) |
| [MIRA: Multimodal Iterative Reasoning Agent for Image Editing](https://arxiv.org/abs/2511.21087) <br> Ziyun Zeng *et al.* <br> > CVPR Findings'26 | -- | [arXiv](https://arxiv.org/abs/2511.21087) · [CVF](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_MIRA_Multimodal_Iterative_Reasoning_Agent_for_Image_Editing_CVPRF_2026_paper.html) · [GitHub](https://github.com/zzzmyyzeng/MIRA) |
| [JarvisEvo: Towards a Self-Evolving Photo Editing Agent with Synergistic Editor–Evaluator Optimization](https://arxiv.org/abs/2511.23002) <br> Yunlong Lin *et al.* <br> > CVPR'26 | <a href="https://github.com/LYL1015/JarvisEvo"><img src="https://github.com/LYL1015/JarvisEvo/raw/main/assets/teaser.png" width="960" alt="JarvisEvo framework" /></a> | [arXiv](https://arxiv.org/abs/2511.23002) · [GitHub](https://github.com/LYL1015/JarvisEvo) · [Project Page](https://jarvisevo.vercel.app/) |
| [ARTIE: A Plug-and-Play Agentic Framework for Text Guided Image Editing](https://openreview.net/forum?id=EPAuWPVcZQ) <br> Dibyanayan Bandyopadhyay *et al.* <br> > ICLR'26 (OpenReview) | -- | [OpenReview](https://openreview.net/forum?id=EPAuWPVcZQ) |
| [Agent Banana: High-Fidelity Image Editing with Agentic Thinking and Tooling](https://arxiv.org/abs/2602.09084) <br> Ruijie Ye *et al.* <br> > Preprint'26 | <a href="https://github.com/taco-group/agent-banana"><img src="https://github.com/taco-group/agent-banana/raw/main/assets/framework.png" width="960" alt="Agent Banana framework" /></a> | [arXiv](https://arxiv.org/abs/2602.09084) · [GitHub](https://github.com/taco-group/agent-banana) · [Project Page](https://agent-banana.github.io/) |
| [PhotoAgent: Agentic Photo Editing with Exploratory Visual Aesthetic Planning](https://arxiv.org/abs/2602.22809) <br> Mingde Yao *et al.* <br> > Preprint'26 | <a href="https://github.com/mdyao/PhotoAgent"><img src="https://github.com/mdyao/PhotoAgent/raw/main/images/photoagent_loop.png" width="960" alt="PhotoAgent framework" /></a> | [arXiv](https://arxiv.org/abs/2602.22809) · [GitHub](https://github.com/mdyao/PhotoAgent) · [Project Page](https://mdyao.github.io/PhotoAgent/) |
| [RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward](https://arxiv.org/abs/2602.17558) <br> Qianqian Wu *et al.* <br> > Preprint'26 | -- | [arXiv](https://arxiv.org/abs/2602.17558) |
| [Agentic Retoucher for Text-To-Image Generation](https://arxiv.org/abs/2601.02046) <br> Shaocheng Shen *et al.* <br> > CVPR'26 | -- | [arXiv](https://arxiv.org/abs/2601.02046) |
| [CAMEO: A Conditional and Quality-Aware Multi-Agent Image Editing Orchestrator](https://arxiv.org/abs/2604.03156) <br> Yuhan Pu *et al.* <br> > Preprint'26 | -- | [arXiv](https://arxiv.org/abs/2604.03156) |
| [What Can I Edit? Open-Ended Strategy Discovery and the Emotion Editability Landscape (EmoScope)](https://arxiv.org/abs/2607.23920) <br> Qing Li *et al.* <br> > Preprint'26 | -- | [arXiv](https://arxiv.org/abs/2607.23920) · [PDF](https://arxiv.org/pdf/2607.23920) · [HTML](https://arxiv.org/html/2607.23920) |
| [DrawAI: Agentic Benchmark and Workflow for Making Raster Images Editable](https://arxiv.org/abs/2608.00548) <br> Pu Cao *et al.* <br> > Preprint'26 | -- | [arXiv](https://arxiv.org/abs/2608.00548) · [PDF](https://arxiv.org/pdf/2608.00548) · [HTML](https://arxiv.org/html/2608.00548) · [Project Page](https://drawai.renaissancemind.ai/) |
---

## General Vision Tool-Use Agents

> Agentic methods where **visual perception is directly coupled with multi-step tool use / planning / execution**.

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://arxiv.org/abs/2412.15606) <br> Zhi Gao *et al.* <br> > ICLR'25 | -- | [arXiv](https://arxiv.org/abs/2412.15606) · [Project Page](https://mat-agent.github.io/) |
| [VTool-R1: VLMs Learn to Think with Images via Reinforcement Learning on Multimodal Tool Use](https://arxiv.org/abs/2505.19255) <br> Minghao Wu *et al.* <br> > ICLR'26 | <a href="https://github.com/VTOOL-R1/vtool-r1"><img src="https://github.com/VTool-R1/VTool-R1/raw/main/vtool_example.png" width="960" alt="VTool-R1 example" /></a> | [arXiv](https://arxiv.org/abs/2505.19255) · [Project Page](https://vtool-r1.github.io/) · [GitHub](https://github.com/VTOOL-R1/vtool-r1) |
| [ToolScope: An Agentic Framework for Vision-Guided and Long-Horizon Tool Use](https://arxiv.org/abs/2510.27363) <br> Mengjie Deng *et al.* <br> > ACL Findings'26 | <a href="https://github.com/dengmengjie/ToolScope"><img src="https://github.com/dengmengjie/ToolScope/raw/main/assets/overview.png" width="960" alt="ToolScope framework" /></a> | [arXiv](https://arxiv.org/abs/2510.27363) · [ACL Anthology](https://aclanthology.org/2026.findings-acl.11/) · [DOI](https://doi.org/10.18653/v1/2026.findings-acl.11) · [GitHub](https://github.com/dengmengjie/ToolScope) |
| [SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them](https://arxiv.org/abs/2607.27703) <br> Yang Zhou *et al.* <br> > Preprint'26 | -- | [arXiv](https://arxiv.org/abs/2607.27703) · [PDF](https://arxiv.org/pdf/2607.27703) · [HTML](https://arxiv.org/html/2607.27703) |
| [FaithEyes: Towards Faithful Tool Use via Multi-Agent Process-Image Verification](https://arxiv.org/abs/2607.28225) <br> Haoqing Wang *et al.* <br> > Preprint'26 | -- | [arXiv](https://arxiv.org/abs/2607.28225) · [PDF](https://arxiv.org/pdf/2607.28225) · [HTML](https://arxiv.org/html/2607.28225) · [GitHub](https://github.com/Mosi-AI/FaithEyes) |
| [Beacon: Knowing When and How to Perform Agentic Visual Reasoning](https://arxiv.org/abs/2607.28595) <br> Qixun Wang *et al.* <br> > Preprint'26 | -- | [arXiv](https://arxiv.org/abs/2607.28595) · [PDF](https://arxiv.org/pdf/2607.28595) · [HTML](https://arxiv.org/html/2607.28595) |
| [VC-Tooler: Learning Compositional and Adaptive Visual Tool Use](https://arxiv.org/abs/2608.02217) <br> Yizheng Wu *et al.* <br> > Preprint'26 | -- | [arXiv](https://arxiv.org/abs/2608.02217) · [PDF](https://arxiv.org/pdf/2608.02217) · [Project Page](https://w1zheng.github.io/VC-Tooler/) |

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
| **MiO-100** | Multi-degradation image restoration evaluation set used by recent agentic IR works | [DiTTo Page](https://cmlab-korea.github.io/DiTTo/) |

---
## Toolboxes & Platforms

### Toolboxes / Codebases
- **AgenticIR**, **JarvisIR**, **4KAgent**, **IAMAgent**
- **CoSTAR / FaSTAR**, **PhotoAgent**
- **Agent Banana**, **JarvisArt / JarvisEvo**
- **Derain-Agent**, **PaAgent**, **Restore-R1**, **TIR-Agent**, **OPERA**, **EvoIR-Agent**, **DiTTo**
- **VTool-R1 / ToolScope / T3-Agent**

### Expert Models / Backbones
- **Restormer**, **SwinIR**, **MPRNet**, **MAXIM**, **NAFNet**
- **Real-ESRGAN**, **SCUNet**, **BasicSR**

---

## Contributing
- Add papers or resources to the proper section
- Prefer official links
- Keep the format consistent
- Only include clearly agentic work
