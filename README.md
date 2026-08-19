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

> Agentic methods for **image restoration, enhancement, super-resolution, computational photography, and domain-specific restoration**.  
> To keep this still-small literature easy to scan, papers are kept in **one unified table**; the **Scope** column indicates whether a work targets general mixed-degradation IR, a specific task, or a specialized imaging domain. The list is ordered roughly by first public release.

| Title & Authors | Scope | Core Idea | Useful Links |
|---|---|---|---|
| [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://arxiv.org/abs/2407.18035) <br> Haoyu Chen *et al.* <br> > NeurIPS'24 | **General mixed-degradation IR** | MLLM-based degradation assessment, restoration-task ordering, expert-model selection, and autonomous tool execution. | [arXiv](https://arxiv.org/abs/2407.18035) · [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf) · [Project Page](https://haoyuchen.com/RestoreAgent) |
| [AgenticIR: An Intelligent Agentic System for Complex Image Restoration Problems](https://arxiv.org/abs/2410.17809) <br> Kaiwen Zhu *et al.* <br> > ICLR'25 | **General mixed-degradation IR** | Human-inspired **Perception–Scheduling–Execution–Reflection–Rescheduling** loop with self-exploration for accumulating restoration experience. | [arXiv](https://arxiv.org/abs/2410.17809) · [Project Page](https://kaiwen-zhu.github.io/research/agenticir) · [GitHub](https://github.com/Kaiwen-Zhu/AgenticIR) |
| [Multi-Agent Image Restoration (MAIR)](https://arxiv.org/abs/2503.09403) <br> Xu Jiang *et al.* <br> > IJCV'26 | **General mixed-degradation IR** | Scheduler + degradation-specialist agents organized by a real-world scene/imaging/compression prior; registry mechanism supports new tools. | [arXiv](https://arxiv.org/abs/2503.09403) · [Project Page](https://villa.jianzhang.tech/publication/200604/) |
| [Hybrid Agents for Image Restoration (HybridAgent)](https://arxiv.org/abs/2503.10120) <br> Bingchen Li *et al.* <br> > CVPR'26 | **General / interactive IR** | Fast, slow, and feedback agents route simple vs. ambiguous requests and introduce a mixed-distortion removal mode to reduce sequential error propagation. | [arXiv](https://arxiv.org/abs/2503.10120) · [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Hybrid_Agents_for_Image_Restoration_CVPR_2026_paper.html) |
| [JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration](https://arxiv.org/abs/2504.04158) <br> Yunlong Lin *et al.* <br> > CVPR'25 | **Autonomous driving / adverse weather** † | VLM controller coordinates restoration experts; supervised tuning plus human-feedback alignment improves real-world adverse-weather decision making. Introduces **CleanBench**. | [arXiv](https://arxiv.org/abs/2504.04158) · [CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_JarvisIR_Elevating_Autonomous_Driving_Perception_with_Intelligent_Image_Restoration_CVPR_2025_paper.html) · [Project Page](https://cvpr2025-jarvisir.github.io/) · [GitHub](https://github.com/LYL1015/JarvisIR) |
| [Q-Agent: Quality-Driven Chain-of-Thought Image Restoration Agent](https://arxiv.org/abs/2504.07148) <br> Yingjie Zhou *et al.* <br> > Preprint'25 | **General mixed-degradation IR** | CoT decomposes multi-degradation perception; objective IQA drives greedy restoration ordering to avoid unnecessary rollback/search. | [arXiv](https://arxiv.org/abs/2504.07148) · [PDF](https://arxiv.org/pdf/2504.07148) · [HTML](https://arxiv.org/html/2504.07148) |
| [4KAgent: Agentic Any Image to 4K Super-Resolution](https://arxiv.org/abs/2507.07105) <br> Yushen Zuo *et al.* <br> > NeurIPS'25 | **Super-resolution / general enhancement** † | Profiling + Perception Agent + Restoration Agent; recursive execution–reflection with a quality-driven mixture-of-experts policy for universal 4K upscaling. | [arXiv](https://arxiv.org/abs/2507.07105) · [Project Page](https://4kagent.github.io/) · [GitHub](https://github.com/taco-group/4KAgent) |
| [FAPE-IR: Frequency-Aware Planning and Execution Framework for All-in-One Image Restoration](https://arxiv.org/abs/2511.14099) <br> Jingren Liu *et al.* <br> > CVPR'26 | **Unified / all-in-one IR** | Frozen MLLM produces frequency-aware plans that steer a LoRA-MoE diffusion executor, linking semantic planning with shared expert execution. | [arXiv](https://arxiv.org/abs/2511.14099) · [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_FAPE-IR_Frequency-Aware_Planning_and_Execution_Framework_for_All-in-One_Image_Restoration_CVPR_2026_paper.html) · [GitHub](https://github.com/Programmergg/FAPE-IR) |
| [Restore-R1: Efficient Image Restoration Agents via Reinforcement Learning with Multimodal LLM Perceptual Feedback](https://arxiv.org/abs/2512.18599) <br> Jianglin Lu *et al.* <br> > CVPR Findings'26 <br> <sub>v1 title: **SimpleCall**</sub> | **General mixed-degradation IR / RL** | Lightweight actor–critic policy learns tool sequences from MLLM perceptual rewards in a label-free environment, replacing search-heavy test-time planning. | [arXiv](https://arxiv.org/abs/2512.18599) · [CVPR PDF](https://openaccess.thecvf.com/content/CVPR2026F/papers/Lu_Restore-R1_Efficient_Image_Restoration_Agents_via_Reinforcement_Learning_with_Multimodal_CVPRF_2026_paper.pdf) · [HTML](https://arxiv.org/html/2512.18599v2) |
| [Derain-Agent: A Plug-and-Play Agent Framework for Rainy Image Restoration](https://arxiv.org/abs/2603.11866) <br> Zhaocheng Yu *et al.* <br> > Preprint'26 | **Deraining / residual refinement** † | Planning Network schedules restoration tools while Strength Modulation applies spatially adaptive correction to residual errors. | [arXiv](https://arxiv.org/abs/2603.11866) · [PDF](https://arxiv.org/pdf/2603.11866) · [HTML](https://arxiv.org/html/2603.11866) |
| [PaAgent: Portrait-Aware Image Restoration Agent via Subjective-Objective Reinforcement Learning](https://arxiv.org/abs/2603.17055) <br> Yijian Wang *et al.* <br> > Preprint'26 | **General mixed-degradation IR / self-evolving tool knowledge** | Self-evolving tool **portrait bank** + RAG for tool selection, with subjective–objective RL for degradation perception. | [arXiv](https://arxiv.org/abs/2603.17055) · [Project Page](https://wyjgr.github.io/PaAgent.html) |
| [IAMAgent: Toward an Interactive and Adaptive Multi-Agent System for Image Restoration](https://doi.org/10.1109/TIP.2026.3671594) <br> Yanyan Wei *et al.* <br> > IEEE TIP'26 | **Interactive / multi-agent IR** | LLM-driven Manager Agent interprets user commands, formulates restoration strategies, and allocates subtasks to specialized agents. | [DOI](https://doi.org/10.1109/TIP.2026.3671594) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/41817987/) |
| [TIR-Agent: Training an Explorative and Efficient Agent for Image Restoration](https://arxiv.org/abs/2603.27742) <br> Yisheng Zhang *et al.* <br> > Preprint'26 | **General mixed-degradation IR / trained policy** | Trains a context-aware direct tool-calling policy using SFT followed by RL to improve exploration, ordering, and inference efficiency. | [arXiv](https://arxiv.org/abs/2603.27742) · [PDF](https://arxiv.org/pdf/2603.27742) · [HTML](https://arxiv.org/html/2603.27742) |
| [EpiAgent: An Agent-Centric System for Ancient Inscription Restoration](https://arxiv.org/abs/2604.09367) <br> Shipeng Zhu *et al.* <br> > CVPR'26 | **Cultural heritage restoration** † | LLM central planner follows an **Observe–Conceive–Execute–Reevaluate** loop, combining multimodal analysis, historical experience, specialized tools, and expert feedback. | [arXiv](https://arxiv.org/abs/2604.09367) · [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_EpiAgent_An_Agent-Centric_System_for_Ancient_Inscription_Restoration_CVPR_2026_paper.html) · [GitHub](https://github.com/blackprotoss/EpiAgent) |
| [OPERA: An Agent for Image Restoration with End-to-End Joint Planning-Execution Optimization](https://arxiv.org/abs/2605.22104) <br> Feng Zhu *et al.* <br> > Preprint'26 | **General mixed-degradation IR / joint optimization** | RL directly optimizes combinatorial restoration plans while **agent-guided co-training** makes restoration tools cooperate under sequential composition. | [arXiv](https://arxiv.org/abs/2605.22104) · [PDF](https://arxiv.org/pdf/2605.22104) · [GitHub](https://github.com/xsyshuishui/Opera) |
| [EvoIR-Agent: Self-Evolving Image Restoration Agentic System via Experience-Driven Learning](https://arxiv.org/abs/2605.22208) <br> Kailin Zhuang *et al.* <br> > Preprint'26 | **General mixed-degradation IR / self-evolution** | Training-free hierarchical experience pool provides coarse-to-fine guidance for tool and order selection and evolves from accumulated restoration records. | [arXiv](https://arxiv.org/abs/2605.22208) · [PDF](https://arxiv.org/pdf/2605.22208) · [GitHub](https://github.com/rightleft-123/EvoIRAgent) |
| [DiTTo: Scalable Order-aware All-in-One Image Restoration Agent](https://arxiv.org/abs/2605.30915) <br> Seungho Choi, Jihyong Oh <br> > Preprint'26 | **General mixed-degradation IR / extensibility** | Simulator generates order-aware trajectories efficiently; SFT + **Order-aware Restoration Alignment (ORA)** decouples agent training from a fixed expert pool and eases new-tool integration. | [arXiv](https://arxiv.org/abs/2605.30915) · [Project Page](https://cmlab-korea.github.io/DiTTo/) · [GitHub](https://github.com/CMLab-Korea/DiTTo-arxiv) |
| [Beyond Sequential Tools: A Unified VLM Agent System for Photographic Post-Processing via Dynamic Multi-Expert Fusion](https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_Beyond_Sequential_Tools_A_Unified_VLM_Agent_System_for_Photographic_CVPR_2026_paper.html) <br> Honglin Xiong *et al.* <br> > CVPR'26 | **Photographic post-processing / shared experts** | Moves beyond serial external-tool execution by using a VLM agent to coordinate dynamic multi-expert fusion within a unified restoration pipeline. | [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_Beyond_Sequential_Tools_A_Unified_VLM_Agent_System_for_Photographic_CVPR_2026_paper.html) |
| [HDRAgent: An Agentic Framework for Multi-Exposure HDR Imaging](https://arxiv.org/abs/2606.09110) <br> Weiyu Zhou *et al.* <br> > Preprint'26 | **Computational photography / HDR** † | MLLM scene perception retrieves contextual knowledge for adaptive tool scheduling; perception–distortion feedback updates memory and guides iterative correction. | [arXiv](https://arxiv.org/abs/2606.09110) · [PDF](https://arxiv.org/pdf/2606.09110) · [HTML](https://arxiv.org/html/2606.09110) |
| [Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution (SEAR)](https://arxiv.org/abs/2606.28971) <br> Shuang Cui *et al.* <br> > ECCV'26 | **General mixed-degradation IR / self-evolution** | Dual-process design combines pruning-aware MCTS for deliberate search with a self-evolving episodic memory for fast intuitive execution. | [arXiv](https://arxiv.org/abs/2606.28971) · [PDF](https://arxiv.org/pdf/2606.28971) · [HTML](https://arxiv.org/html/2606.28971) |
| [RIR-Agent: An Interactive Framework for Effective and Adaptive Restoration of Remote Sensing Imagery](https://doi.org/10.1016/j.eswa.2026.132495) <br> Junyu Liu *et al.* <br> > Expert Systems with Applications'26 | **Remote sensing restoration** † | Agentic remote-sensing restoration for composite degradations, combining autonomous restoration with interactive user-customizable restoration. | [DOI](https://doi.org/10.1016/j.eswa.2026.132495) · [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417426014089) |
| [Causal-AgentIR: Self-Evolving Causal Memory for Adaptive Image Restoration Agents](https://arxiv.org/abs/2607.21125) <br> Hu Gao *et al.* <br> > Preprint'26 | **General mixed-degradation IR / causal memory** | Hierarchical multi-agent system stores degradation, regions, tools, actions, quality changes, and preferences in a self-evolving **causal memory graph** for multi-hop reasoning. | [arXiv](https://arxiv.org/abs/2607.21125) · [PDF](https://arxiv.org/pdf/2607.21125) · [HTML](https://arxiv.org/html/2607.21125) |
| [Agentic AI-powered Flexible Fiber-Bundle Endoscopy for High-Resolution NIR-II Fluorescence Imaging in Vivo](https://arxiv.org/abs/2608.08402) <br> Yanzhao Shi *et al.* <br> > Preprint'26 | **Biomedical restoration / agent-guided MoE** † | Introduces **GAME (Agent-Guided Mixture-of-Experts)**, where a VLM dynamically routes endoscopy inputs to suitable restoration experts for artifact removal and reconstruction. | [arXiv](https://arxiv.org/abs/2608.08402) · [PDF](https://arxiv.org/pdf/2608.08402) |
| [VLM- and LLM-Driven Multi-Agent System for PET Image Denoising](https://arxiv.org/abs/2608.13791) <br> Boxiao Yu *et al.* <br> > Preprint'26 | **Medical imaging / PET denoising** † | Closed-loop multi-agent workflow performs image/lesion assessment, denoiser and parameter selection, execution, feedback, and rollback. | [arXiv](https://arxiv.org/abs/2608.13791) · [PDF](https://arxiv.org/pdf/2608.13791) · [HTML](https://arxiv.org/html/2608.13791) |

> † **Specialized scope.** These works are intentionally kept in the same table rather than split into separate subsections, because they apply the same agentic low-level-vision ideas to a particular task or imaging domain.
>
> **Closely related but not placed in the main agent table:** [Restore, Assess, Repeat (RAR)](https://arxiv.org/abs/2603.26385) uses an iterative restore–quality-assess loop but is an end-to-end trainable unified IR model rather than a tool-using agent; unified restoration backbones such as PixRestore are also relevant to future agent design but are not themselves agentic systems.

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
- **RestoreAgent**, **AgenticIR**, **MAIR**, **HybridAgent**, **JarvisIR**, **4KAgent**
- **FAPE-IR**, **Derain-Agent**, **PaAgent**, **Restore-R1 / SimpleCall**, **TIR-Agent**, **EpiAgent**
- **OPERA**, **EvoIR-Agent**, **DiTTo**, **SEAR**, **Causal-AgentIR**, **IAMAgent**
- **CoSTAR / FaSTAR**, **PhotoAgent**, **Agent Banana**, **JarvisArt / JarvisEvo**
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
