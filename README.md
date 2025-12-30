<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
</p>

# Awesome-Agentic Image Restoration

A curated list of papers and notes on **LLM/VLM-driven agents** that perceive degradations, select tools, execute restoration pipelines, and iteratively refine **image restoration** (IR) and **super-resolution** (SR) workflows.

Contributions are welcome. See [Contributing](#contributing).

- Awesome-Agentic Image Restoration
  - [Papers at a glance](#papers-at-a-glance)
  - [A. Agentic Image Restoration (IR)](#a-agentic-image-restoration-ir)
  - [B. Agentic Super-Resolution (SR)](#b-agentic-super-resolution-sr)
  - [C. Closely Related](#c-closely-related-mllm-assisted-restoration-not-strictly-agentic)
  - [D. Survey / Background](#d-survey--background)
  - [Contributing](#contributing)
  - [Notes](#notes)

---

## Scope

- Agentic IR (multi-degradation restoration pipelines)
- Agentic SR (agentic super-resolution)
- Closely related MLLM-assisted restoration (not strictly agentic, but commonly referenced)
- Surveys / background

## Notation

- **Tags**: `IR`, `SR`, `Agent`, `Toolbox`, `Reflection`, `Multi-agent`, `IQA-driven`, `MLLM/VLM`
- **Link policy**: we link to **official arXiv** pages; no third-party PDFs are stored here.

---

## Papers at a glance

| Area | Paper | Year | Core idea (1-liner) | arXiv | Bib key |
|---|---|---:|---|---|---|
| Agentic IR | [RestoreAgent](https://arxiv.org/abs/2407.18035) | 2024 | MLLM plans a multi-tool restoration pipeline for mixed degradations | [2407.18035](https://arxiv.org/abs/2407.18035) | `chen2024restoreagent` |
| Agentic IR | [AgenticIR](https://arxiv.org/abs/2410.17809) | 2024 | Perception→Scheduling→Execution→Reflection loop for complex IR | [2410.17809](https://arxiv.org/abs/2410.17809) | `zhu2024agenticir` |
| Agentic IR | [MAIR](https://arxiv.org/abs/2503.09403) | 2025 | Multi-agent scheduler + experts guided by a real-world degradation prior | [2503.09403](https://arxiv.org/abs/2503.09403) | `jiang2025mair` |
| Agentic IR | [HybridAgent](https://arxiv.org/abs/2503.10120) | 2025 | Fast/slow/feedback agents + mixed-distortion tool to reduce error propagation | [2503.10120](https://arxiv.org/abs/2503.10120) | `li2025hybridagent` |
| Agentic IR | [Q-Agent](https://arxiv.org/abs/2504.07148) | 2025 | CoT degradation perception + IQA-driven greedy sequencing | [2504.07148](https://arxiv.org/abs/2504.07148) | `zhou2025qagent` |
| Agentic SR | [4KAgent](https://arxiv.org/abs/2507.07105) | 2025 | Agentic any-image-to-4K SR with execution/reflection + MoE selection | [2507.07105](https://arxiv.org/abs/2507.07105) | `zuo2025_4kagent` |
| Related | [LLMRA](https://arxiv.org/abs/2401.11401) | 2024 | Use MLLM/VLM to extract degradation context and condition restoration | [2401.11401](https://arxiv.org/abs/2401.11401) | `jin2024llmra` |
| Related | [AutoDIR](https://arxiv.org/abs/2310.10123) | 2023 | BIQA-driven degradation detection + latent diffusion all-in-one restoration | [2310.10123](https://arxiv.org/abs/2310.10123) | `jiang2023autodir` |
| Survey | [AiOIR Survey](https://arxiv.org/abs/2410.15067) | 2024 | Taxonomy + evaluation + trends for all-in-one image restoration | [2410.15067](https://arxiv.org/abs/2410.15067) | `jiang2024aioir_survey` |

---

## A. Agentic Image Restoration (IR)

| Title & Authors | Intro | Useful Links |
|:---|:---|:---|
| ⭐ [**RestoreAgent**](https://arxiv.org/abs/2407.18035) (arXiv:2407.18035, 2024)<br><em>Autonomous Image Restoration Agent via Multimodal Large Language Models</em><br>`IR` `Agent` `Toolbox` `Task-sequencing` `MLLM/VLM` | *MLLM plans a multi-tool restoration pipeline for mixed degradations*<br>• Autonomously assesses the **type and extent of degradations** (e.g., noise, blur, low-light).<br>• Plans a restoration workflow by: (1) selecting tasks, (2) optimizing order, (3) selecting models, (4) executing.<br>• Emphasizes modularity: easy to integrate new tasks/models. | [arXiv](https://arxiv.org/abs/2407.18035)<br>Bib: `chen2024restoreagent` |
| ⭐ [**AgenticIR**](https://arxiv.org/abs/2410.17809) (arXiv:2410.17809, 2024)<br><em>An Intelligent Agentic System for Complex Image Restoration Problems</em><br>`IR` `Agent` `Toolbox` `Reflection` `MLLM/VLM` | *Perception→Scheduling→Execution→Reflection loop for complex IR*<br>• Mimics human workflows with: **Perception → Scheduling → Execution → Reflection → Rescheduling**.<br>• Uses VLMs for **image quality analysis** and LLMs for **reasoning and step-by-step control**.<br>• Introduces “self-exploration” to accumulate experience into referenceable documents. | [arXiv](https://arxiv.org/abs/2410.17809)<br>Bib: `zhu2024agenticir` |
| ⭐ [**MAIR**](https://arxiv.org/abs/2503.09403) (arXiv:2503.09403, 2025)<br><em>Multi-Agent Image Restoration</em><br>`IR` `Multi-agent` `Scheduler+Experts` `Efficiency` `Tool Registry` | *Multi-agent scheduler + experts guided by a real-world degradation prior*<br>• Proposes a multi-agent framework: a **scheduler** plus **specialist experts**.<br>• Uses a “real-world degradation prior” (scene / imaging / compression) and reverses them in order.<br>• Targets improved quality and reduced trial-and-error inference cost; supports easy tool integration. | [arXiv](https://arxiv.org/abs/2503.09403)<br>Bib: `jiang2025mair` |
| ⭐ [**HybridAgent**](https://arxiv.org/abs/2503.10120) (arXiv:2503.10120, 2025)<br><em>Hybrid Agents for Image Restoration</em><br>`IR` `Hybrid Agents` `Fast/Slow/Feedback` `Mixed-distortion` | *Fast/slow/feedback agents + mixed-distortion tool to reduce error propagation*<br>• Uses a hybrid rule: **fast** (lightweight LLM f...ts), **slow** (MLLM for ambiguous prompts), plus **feedback**.<br>• Adds a **mixed distortion removal mode** to mitigate error propagation in step-by-step pipelines.<br>• Emphasizes interactive usability and efficiency. | [arXiv](https://arxiv.org/abs/2503.10120)<br>Bib: `li2025hybridagent` |
| ⭐ [**Q-Agent**](https://arxiv.org/abs/2504.07148) (arXiv:2504.07148, 2025)<br><em>Quality-Driven Chain-of-Thought Image Restoration Agent</em><br>`IR` `IQA-driven` `Chain-of-Thought` `Greedy sequencing` | *CoT degradation perception + IQA-driven greedy sequencing*<br>• Uses CoT to decompose multi-degradation perception into single-degradation steps.<br>• Uses objective IQA metrics to choose the next action (quality-driven greedy ordering).<br>• Aims to reduce redundant tool calls and improve sequence robustness. | [arXiv](https://arxiv.org/abs/2504.07148)<br>Bib: `zhou2025qagent` |

---

## B. Agentic Super-Resolution (SR)

| Title & Authors | Intro | Useful Links |
|:---|:---|:---|
| ⭐ [**4KAgent**](https://arxiv.org/abs/2507.07105) (arXiv:2507.07105, 2025)<br><em>Agentic Any Image to 4K Super-Resolution</em><br>`SR` `Agent` `Reflection` `MoE policy` `IQA` | *Agentic any-image-to-4K SR with execution/reflection + MoE selection*<br>• A unified agentic SR system that can upscale diverse inputs to **4K** (and higher iteratively).<br>• Includes **Profiling**, a **Perception Agent** (VLM + IQA...experts), and a **Restoration Agent** with execution/reflection.<br>• Uses a quality-driven mixture-of-experts policy to select the best intermediate output. | [arXiv](https://arxiv.org/abs/2507.07105)<br>Bib: `zuo2025_4kagent` |

---

## C. Closely Related (MLLM-assisted restoration, not strictly agentic)

| Title & Authors | Intro | Useful Links |
|:---|:---|:---|
| ⭐ [**LLMRA**](https://arxiv.org/abs/2401.11401) (arXiv:2401.11401, 2024)<br><em>... Large Language Model based Restoration Assistant</em><br>`IR` `MLLM/VLM` `Degradation context` | *Use MLLM/VLM to extract degradation context and condition restoration*<br>• Uses MLLM/VLM to generate **degradation descriptions** and encode them as context embeddings.<br>• Injects this context into a restoration network to improve controllability and interpretability. | [arXiv](https://arxiv.org/abs/2401.11401)<br>Bib: `jin2024llmra` |
| ⭐ [**AutoDIR**](https://arxiv.org/abs/2310.10123) (arXiv:2310.10123, 2023)<br><em>...ll-in-One Image Restoration with Latent Diffusion</em><br>`IR` `All-in-One` `BIQA` `Latent Diffusion` | *BIQA-driven degradation detection + latent diffusion all-in-one restoration*<br>• Uses BIQA to infer degradation types/severity, then routes control for restoration.<br>• Leverages latent diffusion to unify multiple restoration tasks within one framework. | [arXiv](https://arxiv.org/abs/2310.10123)<br>Bib: `jiang2023autodir` |

---

## D. Survey / Background

| Title & Authors | Intro | Useful Links |
|:---|:---|:---|
| ⭐ [**AiOIR Survey**](https://arxiv.org/abs/2410.15067) (arXiv:2410.15067, 2024)<br><em>A Survey on All-in-One Image Restoration</em><br>`Survey` `All-in-One` `Taxonomy` `Benchmarks` | *Taxonomy + evaluation + trends for all-in-one image restoration*<br>• Provides a taxonomy of all-in-one IR methods, evaluation protocols, datasets, and open-source comparisons.<br>• Useful for positioning agentic IR among broader “unified restoration” paradigms. | [arXiv](https://arxiv.org/abs/2410.15067)<br>Bib: `jiang2024aioir_survey` |

---

## Contributing

To keep the list consistent with the Awesome-style layout:

1. **Add a row** to the [Papers at a glance](#papers-at-a-glance) table.
2. **Add a row** to the corresponding category table:
   - [A. Agentic Image Restoration (IR)](#a-agentic-image-restoration-ir)
   - [B. Agentic Super-Resolution (SR)](#b-agentic-super-resolution-sr)
   - [C. Closely Related](#c-closely-related-mllm-assisted-restoration-not-strictly-agentic)
   - [D. Survey / Background](#d-survey--background)
3. Append the BibTeX item into `references.bib` (recommended: use the arXiv-provided BibTeX).

**Row checklist**
- Title (with arXiv link), year, and a short subtitle
- Tags (inline code format)
- 2–4 concise bullet points for the “Intro” cell
- Bib key (keep it consistent across the two tables)

---

## Notes

Create `notes/arxiv_<ID>.md`:

- Problem setting + degradations
- Agent architecture (planner / tools / critic / memory)
- Tool selection / sequencing policy
- Reflection / rollback / IQA usage
- Evaluation setup and datasets
