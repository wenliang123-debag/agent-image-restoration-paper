# Awesome-Agentic-Image-Restoration

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

A curated list of **agentic image restoration** methods where an LLM/VLM acts as a controller to **perceive degradations**, **plan/schedule** restoration steps, and **execute** expert models/tools (denoise, deblur, dehaze, derain, SR, etc.).  
Contributions are welcome!

> **Scope**
> - **Agentic** = explicit *perception → planning/scheduling → tool/model execution* (optionally with reflection/rollback/memory).
> - **Non-agentic** “all-in-one” / “instruction-guided” restoration models are listed in *Related*.
> - **Adjacent** photo/image editing agents are listed separately.

---

## Contents

- [Agentic IR](#agentic-ir)
- [Agentic SR](#agentic-sr)
- [Adjacent: Agentic Image Editing / Photo Enhancement](#adjacent-agentic-image-editing--photo-enhancement)
- [Related: MLLM/VLM-assisted Restoration (non-agentic)](#related-mllmvlm-assisted-restoration-non-agentic)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Toolboxes & Expert Models](#toolboxes--expert-models)
- [Surveys](#surveys)
- [Paper List](#paper-list)
- [Contributing](#contributing)

---

## Agentic IR

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://arxiv.org/abs/2407.18035) <br> Haoyu Chen *et al.* <br> > NeurIPS'24 | -- | [arXiv](https://arxiv.org/abs/2407.18035) · [NeurIPS PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf) · [Project Page](https://haoyuchen.com/RestoreAgent) |
| [AgenticIR: Agentic Image Restoration with Task Decomposition, Tool Inventory, and Reward-Guided Planning](https://arxiv.org/abs/2410.17809) <br> Kaiwen Zhu *et al.* <br> > ICLR'25 | <img src="https://github.com/Kaiwen-Zhu/AgenticIR/raw/main/assets/workflow.png" width="840" /> | [arXiv](https://arxiv.org/abs/2410.17809) · [Github](https://github.com/Kaiwen-Zhu/AgenticIR) |
| [JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration](https://cvpr2025-jarvisir.github.io/) <br> Yunlong Lin *et al.* <br> > CVPR'25 | <img src="https://cvpr2025-jarvisir.github.io/imgs/framework.png" width="840" /> | [Page](https://cvpr2025-jarvisir.github.io/) · [Github](https://github.com/LYL1015/JarvisIR) · [arXiv](https://arxiv.org/abs/2504.04158) |
| [Multi-Agent Image Restoration (MAIR)](https://arxiv.org/abs/2503.09403) <br> Xu Jiang *et al.* <br> > Preprint'25 | -- | [arXiv](https://arxiv.org/abs/2503.09403) |
| [Hybrid Agents for Image Restoration (HybridAgent)](https://arxiv.org/abs/2503.10120) <br> Bingchen Li *et al.* <br> > Preprint'25 | -- | [arXiv](https://arxiv.org/abs/2503.10120) |
| [Q-Agent: Quality-Driven Chain-of-Thought Image Restoration Agent](https://arxiv.org/abs/2504.07148) <br> Yingjie Zhou *et al.* <br> > Preprint'25 | -- | [arXiv](https://arxiv.org/abs/2504.07148) |

---

## Agentic SR

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [4KAgent: Agentic Any Image to 4K Super-Resolution](https://arxiv.org/abs/2507.07105) <br> Jiahao Zuo *et al.* <br> > NeurIPS'25 | <img src="https://github.com/taco-group/4KAgent/raw/main/assets/4KAgent_framework.png" width="840" /> | [arXiv](https://arxiv.org/abs/2507.07105) · [Github](https://github.com/taco-group/4KAgent) · [Project Page](https://4kagent.github.io/) |

---

## Adjacent: Agentic Image Editing / Photo Enhancement

> Not strictly "restoration", but highly related long-horizon pipelines: **perceive → plan → execute tools/editors → evaluate/reflect** (often multi-turn).

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [PhotoAgent: Agentic Photo Editing with Exploratory Visual Aesthetic Planning](https://arxiv.org/abs/2602.22809) <br> Mingde Yao *et al.* <br> > Preprint'26 | <img src="https://github.com/mdyao/PhotoAgent/raw/main/images/photoagent_loop.png" width="840" /> | [arXiv](https://arxiv.org/abs/2602.22809) · [Github](https://github.com/mdyao/PhotoAgent) · [Project Page](https://mdyao.github.io/PhotoAgent/) |
| [Agent Banana: High-Fidelity Image Editing with Agentic Thinking and Tooling](https://arxiv.org/abs/2602.09084) <br> Ruijie Ye *et al.* <br> > Preprint'26 | <img src="https://github.com/taco-group/agent-banana/raw/main/assets/framework.png" width="840" /> | [arXiv](https://arxiv.org/abs/2602.09084) · [Github](https://github.com/taco-group/agent-banana) |
| [JarvisEvo: Towards a Self-Evolving Photo Editing Agent with Synergistic Editor–Evaluator Optimization](https://arxiv.org/abs/2511.23002) <br> Yunlong Lin *et al.* <br> > CVPR'26 | <img src="https://github.com/LYL1015/JarvisEvo/raw/main/assets/framework.png" width="840" /> | [arXiv](https://arxiv.org/abs/2511.23002) · [Github](https://github.com/LYL1015/JarvisEvo) · [Project Page](https://jarvisevo.vercel.app/) |
| [MIRA: Multimodal Iterative Reasoning Agent for Image Editing](https://arxiv.org/abs/2511.21087) <br> Ziyun Zeng *et al.* <br> > Preprint'25 | -- | [arXiv](https://arxiv.org/abs/2511.21087) · [Github](https://github.com/zzzmyyzeng/MIRA) |
| [CoSTA*: Cost-Sensitive Toolpath Agent for Multi-turn Image Editing](https://arxiv.org/abs/2503.10613) <br> Advait Gupta *et al.* <br> > Preprint'25 | <img src="https://github.com/tianyi-lab/CoSTAR/raw/main/main.png" width="840" /> | [arXiv](https://arxiv.org/abs/2503.10613) · [Github](https://github.com/tianyi-lab/CoSTAR) |
| [FaSTA*: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing](https://arxiv.org/abs/2506.20911) <br> Advait Gupta *et al.* <br> > ICLR'26 | <img src="https://github.com/tianyi-lab/FaSTAR/raw/main/asset/schematic.png" width="840" /> | [arXiv](https://arxiv.org/abs/2506.20911) · [OpenReview](https://openreview.net/forum?id=yhhbL9T1QB) · [Github](https://github.com/tianyi-lab/FaSTAR) |
| [ARTIE: A Plug-and-Play Agentic Framework for Text Guided Image Editing](https://openreview.net/forum?id=EPAuWPVcZQ) <br> Dibyanayan Bandyopadhyay *et al.* <br> > ICLR'26 (OpenReview) | -- | [OpenReview](https://openreview.net/forum?id=EPAuWPVcZQ) |

---

## Related: MLLM/VLM-assisted Restoration (non-agentic)

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [LLMRA: Multi-modal Large Language Model based Restoration Assistant](https://arxiv.org/abs/2401.11401) <br> Xiaoyu Jin *et al.* <br> > Preprint'24 | -- | [arXiv](https://arxiv.org/abs/2401.11401) |
| [AutoDIR: Automatic All-in-One Image Restoration with Latent Diffusion](https://arxiv.org/abs/2310.10123) <br> Yitong Jiang *et al.* <br> > ECCV'24 | <img src="https://jiangyitong.github.io/AutoDIR_webpage/static/images/method_full.png" width="840" /> | [arXiv](https://arxiv.org/abs/2310.10123) · [Page](https://jiangyitong.github.io/AutoDIR_webpage/) · [Code](https://github.com/jiangyitong/AutoDIR) |
| [InstructIR: High-Quality Image Restoration Following Human Instructions](https://arxiv.org/abs/2401.16468) <br> Marcos V. Conde *et al.* <br> > ECCV'24 | -- | [arXiv](https://arxiv.org/abs/2401.16468) · [Code](https://github.com/mv-lab/InstructIR) |
| [PromptIR: Prompting for All-in-One Blind Image Restoration](https://arxiv.org/abs/2306.13090) <br> Vaishnav Potlapalli *et al.* <br> > NeurIPS'23 | -- | [arXiv](https://arxiv.org/abs/2306.13090) · [Code](https://github.com/va1shn9v/PromptIR) |

---

## Datasets & Benchmarks

| Resource | What it is | Links |
|---|---|---|
| **CleanBench** | Instruction–response data for training/evaluating restoration agents (synthetic + real) | [JarvisIR Repo](https://github.com/LYL1015/JarvisIR) · [JarvisIR Page](https://cvpr2025-jarvisir.github.io/) |
| **UGC-Edit** | Aesthetic evaluation benchmark (~7,000 photos) + test set (1,017 photos) for autonomous photo editing | [PhotoAgent Repo](https://github.com/mdyao/PhotoAgent) · [PhotoAgent arXiv](https://arxiv.org/abs/2602.22809) |
| **HDD-Bench** | High-definition (native 4K) dialogue-based benchmark for long-horizon editing consistency | [Agent Banana Repo](https://github.com/taco-group/agent-banana) · [Agent Banana arXiv](https://arxiv.org/abs/2602.09084) |
| **ArtEdit-Bench** | Photo editing benchmark released with JarvisEvo | [JarvisEvo Repo](https://github.com/LYL1015/JarvisEvo) |
| **CoSTAR / FaSTAR Benchmark** | Multi-turn image editing benchmark (used by CoSTA* / FaSTA*); CoSTAR repo mentions a 121-task benchmark | [CoSTAR Repo](https://github.com/tianyi-lab/CoSTAR) · [FaSTAR Repo](https://github.com/tianyi-lab/FaSTAR) |
| (Add more) | Common IR benchmarks (GoPro, Rain13K, SOTS/RESIDE, LOL, DIV2K, RealSR, etc.) | PRs welcome |

---

## Toolboxes & Expert Models

### Agentic toolboxes / codebases
- **AgenticIR toolbox** (multi-tool planning/execution): https://github.com/Kaiwen-Zhu/AgenticIR  
- **JarvisIR toolbox** (expert model library + training/inference code): https://github.com/LYL1015/JarvisIR  
- **4KAgent** (agentic SR pipeline): https://github.com/taco-group/4KAgent  
- **CoSTAR** (toolpath planning + A* search for multi-turn editing): https://github.com/tianyi-lab/CoSTAR  
- **FaSTAR** (fast-slow planning + subroutine mining): https://github.com/tianyi-lab/FaSTAR  
- **PhotoAgent** (aesthetic planning + closed-loop editing): https://github.com/mdyao/PhotoAgent  
- **Agent Banana** (planner-executor + layer-based editing): https://github.com/taco-group/agent-banana  
- **JarvisEvo** (editor–evaluator co-optimization): https://github.com/LYL1015/JarvisEvo  
- **AutoDIR** (BIQA + diffusion-based restoration): https://github.com/jiangyitong/AutoDIR  

### Frequently-used expert models (often wrapped as tools)
- **Restormer**, **SwinIR**, **MPRNet**, **MAXIM**, **NAFNet** (general IR backbones)  
- **Real-ESRGAN** (SR / artifact removal)  
- **SCUNet** (denoising)  
- Toolbox: **BasicSR** (SR/denoise/deblur toolbox) — https://github.com/XPixelGroup/BasicSR

---

## Surveys

| Title & Authors | Intro | Useful Links |
|---|---|---|
| [A Survey on All-in-One Image Restoration](https://arxiv.org/abs/2410.15067) <br> (AiOIR Survey) <br> > TPAMI'25 | -- | [arXiv](https://arxiv.org/abs/2410.15067) · [Repo](https://github.com/Harbinzzy/All-in-One-Image-Restoration-Survey) |

---

## Paper List

| Paper | First Author | Year | Topic |
|---|---|---:|---|
| [PromptIR](https://arxiv.org/abs/2306.13090) | Potlapalli | 2023 | Prompt-based all-in-one IR |
| [AutoDIR](https://arxiv.org/abs/2310.10123) | Jiang | 2024 | BIQA + diffusion for restoration |
| [LLMRA](https://arxiv.org/abs/2401.11401) | Jin | 2024 | VLM/MLLM-assisted universal IR |
| [RestoreAgent](https://arxiv.org/abs/2407.18035) | Chen | 2024 | Agentic IR (model pool + scheduling) |
| [AgenticIR](https://arxiv.org/abs/2410.17809) | Zhu | 2024 | Agentic IR (planner + toolbox) |
| [JarvisIR](https://arxiv.org/abs/2504.04158) | Lin | 2025 | VLM controller + expert library |
| [MAIR](https://arxiv.org/abs/2503.09403) | Jiang | 2025 | Multi-agent IR |
| [HybridAgent](https://arxiv.org/abs/2503.10120) | Li | 2025 | Fast/slow/feedback agents for IR |
| [Q-Agent](https://arxiv.org/abs/2504.07148) | Zhou | 2025 | IQA-driven chain-of-thought restoration |
| [CoSTA*](https://arxiv.org/abs/2503.10613) | Gupta | 2025 | Cost-sensitive toolpath for multi-turn editing |
| [FaSTA*](https://arxiv.org/abs/2506.20911) | Gupta | 2025 | Fast-slow toolpath + subroutine mining |
| [MIRA](https://arxiv.org/abs/2511.21087) | Zeng | 2025 | Iterative reasoning agent for editing |
| [4KAgent](https://arxiv.org/abs/2507.07105) | Zuo | 2025 | Agentic 4K super-resolution |
| [JarvisEvo](https://arxiv.org/abs/2511.23002) | Lin | 2026 | Self-evolving photo editing agent |
| [ARTIE](https://openreview.net/forum?id=EPAuWPVcZQ) | Bandyopadhyay | 2026 | Plug-and-play agentic text-guided editing |
| [Agent Banana](https://arxiv.org/abs/2602.09084) | Ye | 2026 | Agentic planner-executor for editing |
| [PhotoAgent](https://arxiv.org/abs/2602.22809) | Yao | 2026 | Aesthetic planning for photo editing |

---

## Contributing

1. Add the paper/resource into the corresponding section table.  
2. Prefer linking to **official arXiv/project pages** and **official code repositories**.  
3. For the **Intro** column, prefer a **framework/architecture figure** hosted on the official GitHub repo or GitHub Pages site (use `raw` links).  
4. Keep the format consistent: **Title · Authors · Venue/Year · Links**.  

If you maintain a related project and would like it listed or corrected, feel free to open an issue/PR.
