# Agent Documentation - MVP Implementation

Project Aegis MVP: Four-agent system for code quality and compliance in healthcare software development.

## Agents

### 1. Entry Agent
**Type**: `LlmAgent` | **Model**: `gemini-2.5-pro`

**Key Responsibilities**:
- Detect if specification document exists for the code changes
- Route to Spec Agent (no spec) or Audit Agent (has spec)

### 2. Spec Agent (Human-in-the-Loop)
**Type**: `LlmAgent` | **Model**: `gemini-2.5-pro`

**Key Responsibilities**:
- Generate specification documents by talking to human
- Include functional, technical, and compliance requirements (HIPAA/GDPR)
- Present spec to human reviewer for approval
- Incorporate feedback before passing to Audit Agent
- output format is yaml

### 3. Audit Agent
**Type**: `LlmAgent` | **Model**: `gemini-2.5-pro`

**Key Responsibilities**:
- Based on the spec supplied by the spec agent, analyzes assigned file for breach of spec
- Only consults one file, but does so comprehensively
- Tools: load and read spec and code files. Extract file path from user input.
- **Parallel Execution**: One agent instance spawned per file change, all run in parallel

### 4. Edit Proposal Agent (Human-in-the-Loop)
**Type**: `LlmAgent` | **Model**: `gemini-2.5-pro`

**Key Responsibilities**:
- Synthesize audit findings into fix proposals
- Generate code changes, refactorings, and security fixes
- Create execution plans for complex multi-file changes
- Present proposals to human for approval before creating PRs

## Workflow

```
Entry Agent → [No Spec] → Spec Agent (Human) → Audit Agent → Edit Proposal Agent (Human)
           → [Has Spec] → Audit Agent → Edit Proposal Agent (Human)
```

## MVP Scope

**Included**: Basic routing, spec generation, audit, fix proposals
**Not in MVP**: PHI tokenization, parallel analysis, RAG compliance research, cost optimization

