# Agentic Image Restoration – Paper List & Notes

本仓库整理“Agent / Agentic System 用于图像恢复（denoise / deblur / SR / mixed degradation）”相关论文。

---

## A. Agentic IR（LLM/VLM 规划 + 工具箱执行 + 反思迭代）

### RestoreAgent (arXiv:2407.18035, 2024)
- Link: https://arxiv.org/abs/2407.18035
- Key idea: 用多模态大模型做退化感知与任务规划，从模型池里选择工具并确定执行顺序。
- Highlights:
  - 自动判断退化类型/程度（噪声、模糊、低照度等），并规划恢复 pipeline
  - 模块化工具箱，强调易扩展
  - 目标是处理“多退化混合”的真实图像

### AgenticIR (arXiv:2410.17809, 2024/2025)
- Link: https://arxiv.org/abs/2410.17809
- Key idea: 模仿人类修图流程：Perception → Scheduling → Execution → Reflection → Rescheduling。
- Highlights:
  - LLM 负责推理与调度，VLM 负责质量/退化分析
  - 引入 self-exploration：把试出来的经验沉淀成可引用文档，降低重复试错

### MAIR: Multi-Agent Image Restoration (arXiv:2503.09403, 2025)
- Link: https://arxiv.org/abs/2503.09403
- Key idea: 多智能体协作（scheduler + experts），按“真实退化先后顺序”的先验分阶段恢复，减少搜索与试错成本。
- Highlights:
  - 将退化分为 scene / imaging / compression 三类并反向恢复
  - registry 机制便于集成新工具
  - 更强调效率与减少不必要的试验

### HybridAgent (arXiv:2503.10120, 2025)
- Link: https://arxiv.org/abs/2503.10120
- Key idea: 快/慢/反馈混合智能体：用轻量 LLM 处理明确需求，用 MLLM 处理模糊需求，并引入反馈与混合失真处理。
- Highlights:
  - 针对“用户描述不清楚”的交互式恢复
  - 强调降低时间/资源成本
  - 覆盖 mixed distortion 的策略

### Q-Agent (arXiv:2504.07148, 2025)
- Link: https://arxiv.org/abs/2504.07148
- Key idea: 用 Chain-of-Thought 把多退化感知分解，并用客观 IQA 指标驱动“贪心式”恢复顺序选择。
- Highlights:
  - 质量驱动（IQA）来决定下一步做什么，避免无效工具调用
  - 目标：更稳的顺序、更少冗余步骤

---

## B. Agentic SR（超分辨率）

### 4KAgent (arXiv:2507.07105, 2025)
- Link: https://arxiv.org/abs/2507.07105
- Key idea: “任意图像到 4K”的统一 agentic SR 系统：profiling + perception agent + restoration agent，递归执行-反思，质量驱动 MoE 选最优输出。
- Highlights:
  - 面向极低分辨率/重退化输入
  - 覆盖多领域图像（自然、AIGC、医学、显微等）
  - 可迭代上采样到更高分辨率

---

## C. 相关背景：用多模态/扩散做“更通用”的恢复（非严格 agent，但常被 agent 系统引用）

### LLMRA (arXiv:2401.11401, 2024)
- Link: https://arxiv.org/abs/2401.11401
- Key idea: 用 MLLM/VLM 产出退化文本描述与上下文嵌入，注入恢复网络，实现更可控/可解释的通用恢复。

### AutoDIR (arXiv:2310.10123, 2023/2024)
- Link: https://arxiv.org/abs/2310.10123
- Key idea: 语义无关的退化检测 + latent diffusion 的 all-in-one 恢复，并支持文本指令式编辑。

### Survey: All-in-One Image Restoration (arXiv:2410.15067, 2024/2025)
- Link: https://arxiv.org/html/2410.15067
- Use: 快速了解 AiOIR 的分类、评测与趋势；其中也涵盖 Agentic IR Systems 的位置与发展脉络。
