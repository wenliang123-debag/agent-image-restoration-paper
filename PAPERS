# Agentic Image Restoration — Paper List & Notes

This document tracks papers where an **agent** (often built on LLM/MLLM/VLM + tools) plans, executes, and iteratively refines **image restoration** workflows.

**Scope**
- Agentic IR (multi-degradation restoration pipelines)
- Agentic SR (agentic super-resolution)
- Closely related MLLM-assisted restoration (not strictly agentic, but commonly referenced)
- Surveys/background

**Notation**
- **Tags**: `IR`, `SR`, `Agent`, `Toolbox`, `Reflection`, `Multi-agent`, `IQA-driven`, `MLLM/VLM`
- **Link policy**: we link to **official arXiv** pages; no third-party PDFs are stored here.

---

## Papers at a glance

| Area | Paper | Year | Core idea (1-liner) | arXiv | Bib key |
|---|---|---:|---|---|---|
| Agentic IR | RestoreAgent | 2024 | MLLM plans a multi-tool restoration pipeline for mixed degradations | 2407.18035 | `chen2024restoreagent` |
| Agentic IR | AgenticIR | 2024 | Perception→Scheduling→Execution→Reflection loop for complex IR | 2410.17809 | `zhu2024agenticir` |
| Agentic IR | MAIR | 2025 | Multi-agent scheduler + experts guided by a real-world degradation prior | 2503.09403 | `jiang2025mair` |
| Agentic IR | HybridAgent | 2025 | Fast/slow/feedback agents + mixed-distortion tool to reduce error propagation | 2503.10120 | `li2025hybridagent` |
| Agentic IR | Q-Agent | 2025 | CoT degradation perception + IQA-driven greedy sequencing | 2504.07148 | `zhou2025qagent` |
| Agentic SR | 4KAgent | 2025 | Agentic any-image-to-4K SR with recursive execution/reflection + MoE selection | 2507.07105 | `zuo2025_4kagent` |
| Related | LLMRA | 2024 | Use MLLM/VLM to extract degradation context and condition restoration | 2401.11401 | `jin2024llmra` |
| Related | AutoDIR | 2023 | BIQA-driven degradation detection + latent diffusion all-in-one restoration | 2310.10123 | `jiang2023autodir` |
| Survey | AiOIR Survey | 2024 | Taxonomy + evaluation + trends for all-in-one image restoration | 2410.15067 | `jiang2024aioir_survey` |

---

## A. Agentic Image Restoration (IR)

<details>
<summary><strong>RestoreAgent</strong> (arXiv:2407.18035, 2024) — <em>Autonomous Image Restoration Agent via Multimodal Large Language Models</em></summary>

**Link**: https://arxiv.org/abs/2407.18035  
**Tags**: `IR` `Agent` `Toolbox` `Task-sequencing` `MLLM/VLM`  
**Summary**
- Autonomously assesses the **type and extent of degradations** (e.g., noise, blur, low-light).
- Plans a restoration workflow by: (1) selecting tasks, (2) optimizing order, (3) selecting models, (4) executing.
- Emphasizes modularity: easy to integrate new tasks/models.
</details>

<details>
<summary><strong>AgenticIR</strong> (arXiv:2410.17809, 2024) — <em>An Intelligent Agentic System for Complex Image Restoration Problems</em></summary>

**Link**: https://arxiv.org/abs/2410.17809  
**Tags**: `IR` `Agent` `Toolbox` `Reflection` `MLLM/VLM`  
**Summary**
- Mimics human workflows with: **Perception → Scheduling → Execution → Reflection → Rescheduling**.
- Uses VLMs for **image quality analysis** and LLMs for **reasoning and step-by-step control**.
- Introduces “self-exploration” to accumulate experience into referenceable documents.
</details>

<details>
<summary><strong>MAIR</strong> (arXiv:2503.09403, 2025) — <em>Multi-Agent Image Restoration</em></summary>

**Link**: https://arxiv.org/abs/2503.09403  
**Tags**: `IR` `Multi-agent` `Scheduler+Experts` `Efficiency` `Tool Registry`  
**Summary**
- Proposes a multi-agent framework: a **scheduler** plus **specialist experts**.
- Uses a “real-world degradation prior” (scene / imaging / compression) and reverses them in order.
- Targets improved quality and reduced trial-and-error inference cost; supports easy tool integration.
</details>

<details>
<summary><strong>HybridAgent</strong> (arXiv:2503.10120, 2025) — <em>Hybrid Agents for Image Restoration</em></summary>

**Link**: https://arxiv.org/abs/2503.10120  
**Tags**: `IR` `Hybrid Agents` `Fast/Slow/Feedback` `Mixed-distortion`  
**Summary**
- Uses a hybrid rule: **fast** (lightweight LLM for clear prompts), **slow** (MLLM for ambiguous prompts), plus **feedback**.
- Adds a **mixed distortion removal mode** to mitigate error propagation in step-by-step pipelines.
- Emphasizes interactive usability and efficiency.
</details>

<details>
<summary><strong>Q-Agent</strong> (arXiv:2504.07148, 2025) — <em>Quality-Driven Chain-of-Thought Image Restoration Agent</em></summary>

**Link**: https://arxiv.org/abs/2504.07148  
**Tags**: `IR` `IQA-driven` `Chain-of-Thought` `Greedy sequencing`  
**Summary**
- Uses CoT to decompose multi-degradation perception into single-degradation steps.
- Uses objective IQA metrics to choose the next action (quality-driven greedy ordering).
- Aims to reduce redundant tool calls and improve sequence robustness.
</details>

---

## B. Agentic Super-Resolution (SR)

<details>
<summary><strong>4KAgent</strong> (arXiv:2507.07105, 2025) — <em>Agentic Any Image to 4K Super-Resolution</em></summary>

**Link**: https://arxiv.org/abs/2507.07105  
**Tags**: `SR` `Agent` `Reflection` `MoE policy` `IQA`  
**Summary**
- A unified agentic SR system that can upscale diverse inputs to **4K** (and higher iteratively).
- Includes **Profiling**, a **Perception Agent** (VLM + IQA experts), and a **Restoration Agent** with execution/reflection.
- Uses a quality-driven mixture-of-experts policy to select the best intermediate output.
</details>

---

## C. Closely Related (MLLM-assisted restoration, not strictly agentic)

<details>
<summary><strong>LLMRA</strong> (arXiv:2401.11401, 2024) — <em>Multi-modal Large Language Model based Restoration Assistant</em></summary>

**Link**: https://arxiv.org/abs/2401.11401  
**Tags**: `IR` `MLLM/VLM` `Degradation context`  
**Summary**
- Uses MLLM/VLM to generate **degradation descriptions** and encode them as context embeddings.
- Injects this context into a restoration network to improve controllability and interpretability.
</details>

<details>
<summary><strong>AutoDIR</strong> (arXiv:2310.10123, 2023) — <em>Automatic All-in-One Image Restoration with Latent Diffusion</em></summary>

**Link**: https://arxiv.org/abs/2310.10123  
**Tags**: `All-in-One` `Latent diffusion` `BIQA`  
**Summary**
- Two-stage design: semantic-agnostic BIQA for degradation detection + diffusion-based all-in-one restoration.
- Supports open-vocabulary, text-instruction control and iterative processing.
</details>

---

## D. Survey / Background

<details>
<summary><strong>AiOIR Survey</strong> (arXiv:2410.15067, 2024) — <em>A Survey on All-in-One Image Restoration</em></summary>

**Link**: https://arxiv.org/abs/2410.15067  
**Tags**: `Survey` `All-in-One` `Taxonomy` `Benchmarks`  
**Summary**
- Provides a taxonomy of all-in-one IR methods, evaluation protocols, datasets, and open-source comparisons.
- Useful for positioning agentic IR among broader “unified restoration” paradigms.
</details>

---

## Add a new paper (recommended format)

1. Add a new entry to the “Papers at a glance” table.
2. Add a `<details>` block with:
   - Link, tags, 3–6 bullet summary, key contributions, limitations (optional).
3. Append the BibTeX item into `references.bib`.

---

## Suggested note template (optional)

Create `notes/arxiv_<ID>.md`:

- Problem setting + degradations
- Agent architecture (planner / tools / critic / memory)
- Tool selection / sequencing policy
- Reflection / rollback / IQA usage
- Evaluation setup and datasets
