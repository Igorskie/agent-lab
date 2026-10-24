# agent-lab

My workspace for learning to build AI agents. Each project lives in its own folder, along with its evaluation results and what I learned from it.

## Takeaways: Building Effective Agents (Anthropic)

### 1. Start simple, add complexity only when it pays off

A more complex system is not automatically a better one. Start with the simplest thing that works, and add complexity only when it measurably improves results, with cost counted as part of the result.

- **Agent example:** a single agent optimizing dashboard load time improves it by 5%, but juggling several approaches crowds its context. Splitting the work across two or three agents, each exploring one approach, finds a 20% improvement. That is only a win if the gain justifies the extra tokens.
- **Workflow example:** an evaluator-optimizer loop with a 20% target and an iteration cap. Or parallelization by sectioning: five LLM calls each explore one approach, approaches that miss a baseline are dropped, and a judge (or several judges voting) picks the winner.

### 2. Workflows and agents are different things

Workflows follow predefined code paths, which makes them the right fit when the steps are known. Agents direct their own process, using tools in a loop and deciding each next step from the results, which suits open-ended tasks. Tool use is what makes something an agent. My current setup already follows the "augmented LLM" pattern: a Postgres MCP connector gives the model a tool to act with, and an Outline knowledge base gives it memory.

### 3. Workflow patterns I can use right away

I prefer workflows when control matters, because every path is defined and every step can be checked.

- **Prompt chaining:** add a gate between steps. If a step fails, exit. If it passes, continue.
- **Routing:** send each task to the model that fits it. I have been using Opus for everything, including commit messages, which is overkill. Routing would send simple tasks to Haiku or Sonnet.
- **Parallelization:** I already use sectioning. Voting is new to me and looks useful for validation and adversarial passes.
- **Orchestrator-workers:** this is what Claude Code does when it delegates to subagents.
- **Evaluator-optimizer:** an implementer builds, an evaluator checks the result against requirements and sends feedback until it passes. For example, a dashboard query must load in under one second. When the criterion is measurable like this, the evaluator should be code (timing the query or running `EXPLAIN ANALYZE`), not an LLM.

### 4. Agents are for tasks where the path is hard to predict

Agents are flexible and adaptive. In Claude Code, a simple task sometimes turns into a bigger one when the agent discovers an underlying issue and tries to fix it. A prompt-chaining workflow would fail at its gate and exit instead. That autonomy is useful, but it needs stopping conditions (such as a maximum number of iterations) and checkpoints where the agent pauses for human approval.

### 5. Workflows trade setup effort for predictability; agents trade it for testing effort

Workflows are often the simpler option because each step is defined and controlled, which also makes their cost predictable. Agents are quick to set up, but making them reliable takes real work: guardrails, limits on tool use, and extensive testing before their autonomy can be trusted. Both are manageable at a small scale and both get complex at a large one.