[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/agi-edgerunners-llm-agents-papers-badge.png)](https://mseep.ai/app/agi-edgerunners-llm-agents-papers)

# LLM-Agents-Papers
## :writing_hand: Description
Last Updated Time: 2025/7/12

A repo lists papers related to LLM based agent. Includes
- [Survey](#Survey)
- [Technique For Enhancement](#Technique-For-Enhancement)
  - [Planning](#Planning)
  - [Memory Mechanism](#Memory-Mechanism)
  - [Feedback&Reflection](#FeedbackReflection)
  - [RAG](#RAG)
  - [Search](#Search)
- [Interaction](#Interaction)
  - [Role Playing](#Role-Playing)
  - [Conversation](#Conversation)
  - [Game Playing](#Game-Playing)
  - [Human-Agent Interaction](#Human-Agent-Interaction)
  - [Tool Usage](#Tool-Usage)
  - [Simulation](#Simulation)
- [Application](#Application)
  - [Math](#Math)
  - [Chemistry](#Chemistry)
  - [Biology](#Biology)
  - [Physics](#Physics)
  - [Geography](#Geography)
  - [Art](#Art)
  - [Medicine](#Medicine)
  - [Finance](#Finance)
  - [Software Engineering](#Software-Engineering)
  - [Research](#Research)
- [Automation](#Automation)
  - [Workflow](#Workflow)
  - [Automatic Evaluation](#Automatic-Evaluation)
- [Training](#Training)
  - [Fine tuning](#Fine-tuning)
  - [RL](#RL)
  - [DPO](#DPO)
- [Scaling](#Scaling)
  - [Single-Agent Framework](#Single-Agent-Framework)
  - [Multi-Agent System](#Multi-Agent-System)
- [Stability](#Stability)
  - [Safety](#Safety)
  - [Bias](#Bias)
  - [Hallucination](#Hallucination)
- [Infrastructure](#Infrastructure)
  - [Benchmark&Evaluation](#BenchmarkEvaluation)
  - [Environment&Platform](#EnvironmentPlatform)
  - [Dataset](#Dataset)
- [Others](#Others)
## :yellow_heart: Recommendation
For more comprehensive reading, we also recommend other paper lists:
* [zjunlp/LLMAgentPapers](https://github.com/zjunlp/LLMAgentPapers): Must-read Papers on Large Language Model Agents.
* [teacherpeterpan/self-correction-llm-papers](https://github.com/teacherpeterpan/self-correction-llm-papers): This is a collection of research papers for Self-Correcting Large Language Models with Automated Feedback.
* [Paitesanshi/LLM-Agent-Survey](https://github.com/Paitesanshi/LLM-Agent-Survey): A Survey on LLM-based Autonomous Agents.
* [woooodyy/llm-agent-paper-list](https://github.com/woooodyy/llm-agent-paper-list): Must-read papers for LLM-based agents.
* [git-disl/awesome-LLM-game-agent-papers](https://github.com/git-disl/awesome-LLM-game-agent-papers): Must-read papers for LLM-based Game agents.
## :newspaper: Papers
### Survey
- [2025/06/10] **Measuring Data Science Automation: A Survey of Evaluation Tools for AI Assistants and Agents** | [[paper]](https://arxiv.org/abs/2506.08800) | [code]

- [2025/06/06] **Evolutionary Perspectives on the Evaluation of LLM-Based AI Agents: A Comprehensive Survey** | [[paper]](https://arxiv.org/abs/2506.11102) | [code]

- [2025/05/27] **Creativity in LLM-based Multi-Agent Systems: A Survey** | [[paper]](https://arxiv.org/abs/2505.21116) | [code]

- [2025/05/24] **Multi-Party Conversational Agents: A Survey** | [[paper]](https://arxiv.org/abs/2505.18845) | [code]

- [2025/05/16] **A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron?** | [[paper]](https://arxiv.org/abs/2505.10924) | [code]

- [2025/05/02] **AI agents may be worth the hype but not the resources (yet): An initial exploration of machine translation quality and costs in three language pairs in the legal and news domains** | [[paper]](https://arxiv.org/abs/2505.01560) | [code]

- [2025/05/01] **A Survey on Large Language Model based Human-Agent Systems** | [[paper]](https://arxiv.org/abs/2505.00753) | [[code]](https://github.com/HenryPengZou/Awesome-LLM-Based-Human-Agent-System-Papers)

- [2025/04/30] **Humanizing LLMs: A Survey of Psychological Measurements with Tools, Datasets, and Human-Agent Applications** | [[paper]](https://arxiv.org/abs/2505.00049) | [code]

- [2025/04/22] **A Comprehensive Survey in LLM(-Agent) Full Stack Safety: Data, Training and Deployment** | [[paper]](https://arxiv.org/abs/2504.15585) | [code]

- [2025/04/20] **Meta-Thinking in LLMs via Multi-Agent Reinforcement Learning: A Survey** | [[paper]](https://arxiv.org/abs/2504.14520) | [code]

- [2025/04/14] **A Survey of Large Language Model-Powered Spatial Intelligence Across Scales: Advances in Embodied Agents, Smart Cities, and Earth Science** | [[paper]](https://arxiv.org/abs/2504.09848) | [code]

- [2025/04/12] **A Survey of Frontiers in LLM Reasoning: Inference Scaling, Learning to Reason, and Agentic Systems** | [[paper]](https://arxiv.org/abs/2504.09037) | [code]

- [2025/03/28] **Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey** | [[paper]](https://arxiv.org/abs/2503.22458) | [code]

- [2025/03/27] **Large Language Model Agent: A Survey on Methodology, Applications and Challenges** | [[paper]](https://arxiv.org/abs/2503.21460) | [code]

- [2025/03/27] **A Survey on (M)LLM-Based GUI Agents** | [[paper]](https://arxiv.org/abs/2504.13865) | [code]

- [2025/03/24] **A Survey of Large Language Model Agents for Question Answering** | [[paper]](https://arxiv.org/abs/2503.19213) | [code]

- [2025/03/20] **Survey on Evaluation of LLM-based Agents** | [[paper]](https://arxiv.org/abs/2503.16416) | [code]

- [2025/03/13] **LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems** | [[paper]](https://arxiv.org/abs/2504.01963) | [code]

- [2025/03/12] **Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions** | [[paper]](https://arxiv.org/abs/2503.08979) | [code]

- [2025/02/20] **Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2502.14321) | [code]

- [2025/02/18] **Towards a Design Guideline for RPA Evaluation: A Survey of Large Language Model-Based Role-Playing Agents** | [[paper]](https://arxiv.org/abs/2502.13012) | [code]

- [2025/02/16] **A Survey of LLM-based Agents in Medicine: How far are we from Baymax?** | [[paper]](https://arxiv.org/abs/2502.11211) | [code]

- [2025/01/15] **Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG** | [[paper]](https://arxiv.org/abs/2501.09136) | [code]

- [2024/12/23] **A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application** | [[paper]](https://arxiv.org/abs/2412.17481) | [code]

- [2024/12/18] **A Survey on Large Language Model-based Agents for Statistics and Data Science** | [[paper]](https://arxiv.org/abs/2412.14222) | [code]

- [2024/12/05] **A Survey on Large Language Model-Based Social Agents in Game-Theoretic Scenarios** | [[paper]](https://arxiv.org/abs/2412.03920) | [code]

- [2024/12/04] **From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents** | [[paper]](https://arxiv.org/abs/2412.03563) | [code]

- [2024/11/27] **Large Language Model-Brained GUI Agents: A Survey** | [[paper]](https://arxiv.org/abs/2411.18279) | [code]

- [2024/09/27] **A Survey on Complex Tasks for Goal-Directed Interactive Agents** | [[paper]](https://arxiv.org/abs/2409.18538) | [code]

- [2024/09/13] **Agents in Software Engineering: Survey, Landscape, and Vision** | [[paper]](https://arxiv.org/abs/2409.09030) | [code]

- [2024/09/04] **A Survey on Emergent Language** | [[paper]](https://arxiv.org/abs/2409.02645) | [code]

- [2024/08/05] **From LLMs to LLM-based Agents for Software Engineering: A Survey of Current, Challenges and Future** | [[paper]](https://arxiv.org/abs/2408.02479) | [code]

- [2024/07/26] **Large Language Model Agent in Financial Trading: A Survey** | [[paper]](https://arxiv.org/abs/2408.06361) | [code]

- [2024/06/03] **Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization** | [[paper]](https://arxiv.org/abs/2406.01171) | [[code]](https://github.com/miulab/personallm-survey)

- [2024/06/01] **Towards Rationality in Language and Multimodal Agents: A Survey** | [[paper]](https://arxiv.org/abs/2406.00252) | [code]

- [2024/04/17] **Advancing Social Intelligence in AI Agents: Technical Challenges and Open Questions** | [[paper]](https://arxiv.org/abs/2404.11023) | [code]

- [2024/04/02] **A Survey on Large Language Model-Based Game Agents** | [[paper]](https://arxiv.org/abs/2404.02039) | [[code]](https://github.com/git-disl/awesome-LLM-game-agent-papers)

- [2024/03/26] **Leveraging Large Language Models in Human-Robot Interaction: A Critical Analysis of Potential and Pitfalls** | [[paper]](https://arxiv.org/abs/2405.00693) | [code]

- [2024/03/07] **Promising and worth-to-try future directions for advancing state-of-the-art surrogates methods of agent-based models in social and health computational sciences** | [[paper]](https://arxiv.org/abs/2403.04417) | [code]

- [2024/02/28] **Large Language Models and Games: A Survey and Roadmap** | [[paper]](https://arxiv.org/abs/2402.18659) | [code]

- [2024/02/28] **A Survey on Recent Advances in LLM-Based Multi-turn Dialogue Systems** | [[paper]](https://arxiv.org/abs/2402.18013) | [code]

- [2024/02/05] **Understanding the planning of LLM agents: A survey** | [[paper]](https://arxiv.org/abs/2402.02716) | [code]

- [2024/01/01] **If LLM Is the Wizard, Then Code Is the Wand: A Survey on How Code Empowers Large Language Models to Serve as Intelligent Agents** | [[paper]](https://arxiv.org/abs/2401.00812) | [code]

- [2023/12/31] **A Survey of Personality, Persona, and Profile in Conversational Agents and Chatbots** | [[paper]](https://arxiv.org/abs/2401.00609) | [code]

- [2023/12/19] **Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives** | [[paper]](https://arxiv.org/abs/2312.11970) | [code]

- [2023/09/14] **The Rise and Potential of Large Language Model Based Agents: A Survey** | [[paper]](https://arxiv.org/abs/2309.07864) | [code]

- [2023/08/22] **A Survey on Large Language Model based Autonomous Agents** | [[paper]](https://arxiv.org/abs/2308.11432) | [code]

- [2023/06/27] **Next Steps for Human-Centered Generative AI: A Technical Perspective** | [[paper]](https://arxiv.org/abs/2306.15774) | [code]

---
### Technique For Enhancement
#### Planning
- [2025/06/30] **Thought-Augmented Planning for LLM-Powered Interactive Recommender Agent** | [[paper]](https://arxiv.org/abs/2506.23485) | [code]

- [2025/06/24] **NaviAgent: Bilevel Planning on Tool Dependency Graphs for Function Calling** | [[paper]](https://arxiv.org/abs/2506.19500) | [code]

- [2025/06/10] **Improving LLM Agent Planning with In-Context Learning via Atomic Fact Augmentation and Lookahead Search** | [[paper]](https://arxiv.org/abs/2506.09171) | [code]

- [2025/06/06] **MAPLE: Multi-Agent Adaptive Planning with Long-Term Memory for Table Reasoning** | [[paper]](https://arxiv.org/abs/2506.05813) | [code]

- [2025/05/22] **T1: A Tool-Oriented Conversational Dataset for Multi-Turn Agentic Planning** | [[paper]](https://arxiv.org/abs/2505.16986) | [code]

- [2025/05/02] **PIPA: A Unified Evaluation Protocol for Diagnosing Interactive Planning Agents** | [[paper]](https://arxiv.org/abs/2505.01592) | [code]

- [2025/04/15] **GraphicBench: A Planning Benchmark for Graphic Design with Language Agents** | [[paper]](https://arxiv.org/abs/2504.11571) | [code]

- [2025/03/12] **Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks** | [[paper]](https://arxiv.org/abs/2503.09572) | [code]

- [2025/03/04] **MPO: Boosting LLM Agents with Meta Plan Optimization** | [[paper]](https://arxiv.org/abs/2503.02682) | [code]

- [2025/03/03] **Improving Retrospective Language Agents via Joint Policy Gradient Optimization** | [[paper]](https://arxiv.org/abs/2503.01490) | [code]

- [2025/02/08] **CODESIM: Multi-Agent Code Generation and Problem Solving through Simulation-Driven Planning and Debugging** | [[paper]](https://arxiv.org/abs/2502.05664) | [code]

- [2025/02/06] **Robotouille: An Asynchronous Planning Benchmark for LLM Agents** | [[paper]](https://arxiv.org/abs/2502.05227) | [code]

- [2025/01/27] **MADP: Multi-Agent Deductive Planning for Enhanced Cognitive-Behavioral Mental Health Question Answer** | [[paper]](https://arxiv.org/abs/2501.15826) | [code]

- [2025/01/14] **Talk to Right Specialists: Routing and Planning in Multi-agent System for Question Answering** | [[paper]](https://arxiv.org/abs/2501.07813) | [code]

- [2024/12/30] **Plancraft: an evaluation dataset for planning with LLM agents** | [[paper]](https://arxiv.org/abs/2412.21033) | [code]

- [2024/12/28] **Efficient Multi-Agent Collaboration with Tool Use for Online Planning in Complex Table Question Answering** | [[paper]](https://arxiv.org/abs/2412.20145) | [code]

- [2024/12/13] **Script-Based Dialog Policy Planning for LLM-Powered Conversational Agents: A Basic Architecture for an &#34;AI Therapist&#34;** | [[paper]](https://arxiv.org/abs/2412.15242) | [code]

- [2024/11/13] **One STEP at a time: Language Agents are Stepwise Planners** | [[paper]](https://arxiv.org/abs/2411.08432) | [code]

- [2024/11/05] **Benchmarking Multimodal Retrieval Augmented Generation with Dynamic VQA Dataset and Self-adaptive Planning Agent** | [[paper]](https://arxiv.org/abs/2411.02937) | [code]

- [2024/10/12] **CAMPHOR: Collaborative Agents for Multi-input Planning and High-Order Reasoning On Device** | [[paper]](https://arxiv.org/abs/2410.09407) | [code]

- [2024/10/01] **Self-controller: Controlling LLMs with Multi-round Step-by-step Self-awareness** | [[paper]](https://arxiv.org/abs/2410.00359) | [code]

- [2024/09/30] **Interactive Speculative Planning: Enhance Agent Efficiency through Co-design of System and User Interface** | [[paper]](https://arxiv.org/abs/2410.00079) | [code]

- [2024/09/28] **SELP: Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models** | [[paper]](https://arxiv.org/abs/2409.19471) | [code]

- [2024/09/25] **MSI-Agent: Incorporating Multi-Scale Insight into Embodied Agents for Superior Planning and Decision-Making** | [[paper]](https://arxiv.org/abs/2409.16686) | [code]

- [2024/08/15] **VerilogCoder: Autonomous Verilog Coding Agents with Graph-based Planning and Abstract Syntax Tree (AST)-based Waveform Tracing Tool** | [[paper]](https://arxiv.org/abs/2408.08927) | [code]

- [2024/08/12] **Towards Autonomous Agents: Adaptive-planning, Reasoning, and Acting in Language Models** | [[paper]](https://arxiv.org/abs/2408.06458) | [code]

- [2024/08/01] **AgentGen: Enhancing Planning Abilities for Large Language Model based Agent via Environment and Task Generation** | [[paper]](https://arxiv.org/abs/2408.00764) | [code]

- [2024/07/04] **Controllable Conversations: Planning-Based Dialogue Agent with Large Language Models** | [[paper]](https://arxiv.org/abs/2407.03884) | [code]

- [2024/06/17] **RePrompt: Planning by Automatic Prompt Engineering for Large Language Models Agents** | [[paper]](https://arxiv.org/abs/2406.11132) | [code]

- [2024/06/09] **A Review of Prominent Paradigms for LLM-Based Agents: Tool Use (Including RAG), Planning, and Feedback Learning** | [[paper]](https://arxiv.org/abs/2406.05804) | [code]

- [2024/06/06] **Tool-Planner: Task Planning with Clusters across Multiple Tools** | [[paper]](https://arxiv.org/abs/2406.03807) | [[code]](https://github.com/OceannTwT/Tool-Planner)

- [2024/05/28] **A Human-Like Reasoning Framework for Multi-Phases Planning Task with Large Language Models** | [[paper]](https://arxiv.org/abs/2405.18208) | [code]

- [2024/05/27] **REVECA: Adaptive Planning and Trajectory-based Validation in Cooperative Language Agents using Information Relevance and Relative Proximity** | [[paper]](https://arxiv.org/abs/2405.16751) | [code]

- [2024/04/21] **Socratic Planner: Inquiry-Based Zero-Shot Planning for Embodied Instruction Following** | [[paper]](https://arxiv.org/abs/2404.15190) | [code]

- [2024/04/17] **The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey** | [[paper]](https://arxiv.org/abs/2404.11584) | [code]

- [2024/03/11] **Strength Lies in Differences! Improving Strategy Planning for Non-collaborative Dialogues via Diversified User Simulation** | [[paper]](https://arxiv.org/abs/2403.06769) | [code]

- [2024/03/10] **TRAD: Enhancing LLM Agents with Step-Wise Thought Retrieval and Aligned Decision** | [[paper]](https://arxiv.org/abs/2403.06221) | [code]

- [2024/03/05] **KnowAgent: Knowledge-Augmented Planning for LLM-Based Agents** | [[paper]](https://arxiv.org/abs/2403.03101) | [code]

- [2024/02/29] **PlanGPT: Enhancing Urban Planning with Tailored Language Model and Efficient Retrieval** | [[paper]](https://arxiv.org/abs/2402.19273) | [code]

- [2024/02/18] **What&#39;s the Plan? Evaluating and Developing Planning-Aware Techniques for Language Models** | [[paper]](https://arxiv.org/abs/2402.11489) | [code]

- [2024/02/18] **PreAct: Prediction Enhances Agent&#39;s Planning Ability** | [[paper]](https://arxiv.org/abs/2402.11534) | [code]

- [2024/02/16] **When is Tree Search Useful for LLM Planning? It Depends on the Discriminator** | [[paper]](https://arxiv.org/abs/2402.10890) | [[code]](https://github.com/osu-nlp-group/llm-planning-eval)

- [2024/02/15] **TDAG: A Multi-Agent Framework based on Dynamic Task Decomposition and Agent Generation** | [[paper]](https://arxiv.org/abs/2402.10178) | [code]

- [2024/02/09] **Introspective Planning: Aligning Robots&#39; Uncertainty with Inherent Task Ambiguity** | [[paper]](https://arxiv.org/abs/2402.06529) | [code]

- [2024/02/06] **RAP: Retrieval-Augmented Planning with Contextual Memory for Multimodal LLM Agents** | [[paper]](https://arxiv.org/abs/2402.03610) | [code]

- [2024/02/02] **TravelPlanner: A Benchmark for Real-World Planning with Language Agents** | [[paper]](https://arxiv.org/abs/2402.01622) | [[code]](https://github.com/OSU-NLP-Group/TravelPlanner)

- [2024/01/10] **AutoAct: Automatic Agent Learning from Scratch for QA via Self-Planning** | [[paper]](https://arxiv.org/abs/2401.05268) | [code]

- [2023/11/19] **TPTU-v2: Boosting Task Planning and Tool Usage of Large Language Model-based Agents in Real-world Systems** | [[paper]](https://arxiv.org/abs/2311.11315) | [code]

- [2023/10/12] **Tree-Planner: Efficient Close-loop Task Planning with Large Language Models** | [[paper]](https://arxiv.org/abs/2310.08582) | [code]

- [2023/10/09] **Put Your Money Where Your Mouth Is: Evaluating Strategic Planning and Execution of LLM Agents in an Auction Arena** | [[paper]](https://arxiv.org/abs/2310.05746) | [code]

- [2023/08/07] **TPTU: Large Language Model-based AI Agents for Task Planning and Tool Usage** | [[paper]](https://arxiv.org/abs/2308.03427) | [code]

- [2023/08/01] **SelfCheck: Using LLMs to Zero-Shot Check Their Own Step-by-Step Reasoning** | [[paper]](https://arxiv.org/abs/2308.00436) | [code]

- [2023/05/26] **AdaPlanner: Adaptive Planning from Feedback with Language Models** | [[paper]](https://arxiv.org/abs/2305.16653) | [code]

- [2023/05/24] **Reasoning with Language Model is Planning with World Model** | [[paper]](https://arxiv.org/abs/2305.14992) | [code]

- [2023/05/24] **Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning** | [[paper]](https://arxiv.org/abs/2305.14909) | [[code]](https://github.com/GuanSuns/LLMs-World-Models-for-Planning)

- [2023/03/29] **Skill Reinforcement Learning and Planning for Open-World Long-Horizon Tasks** | [[paper]](https://arxiv.org/abs/2303.16563) | [code]

- [2023/02/03] **Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents** | [[paper]](https://arxiv.org/abs/2302.01560) | [code]

- [2022/12/08] **LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models** | [[paper]](https://arxiv.org/abs/2212.04088) | [code]

#### Memory Mechanism
- [2025/07/10] **MIRIX: Multi-Agent Memory System for LLM-Based Agents** | [[paper]](https://arxiv.org/abs/2507.07957) | [code]

- [2025/07/07] **Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions** | [[paper]](https://arxiv.org/abs/2507.05257) | [code]

- [2025/07/03] **MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent** | [[paper]](https://arxiv.org/abs/2507.02259) | [code]

- [2025/06/30] **Ella: Embodied Social Agents with Lifelong Memory** | [[paper]](https://arxiv.org/abs/2506.24019) | [code]

- [2025/06/30] **State and Memory is All You Need for Robust and Reliable AI Agents** | [[paper]](https://arxiv.org/abs/2507.00081) | [code]

- [2025/06/20] **MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents** | [[paper]](https://arxiv.org/abs/2506.21605) | [code]

- [2025/06/18] **MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents** | [[paper]](https://arxiv.org/abs/2506.15841) | [code]

- [2025/06/17] **Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching** | [[paper]](https://arxiv.org/abs/2506.14852) | [code]

- [2025/06/09] **G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2506.07398) | [code]

- [2025/06/07] **Contextual Experience Replay for Self-Improvement of Language Agents** | [[paper]](https://arxiv.org/abs/2506.06698) | [code]

- [2025/06/06] **MAPLE: Multi-Agent Adaptive Planning with Long-Term Memory for Table Reasoning** | [[paper]](https://arxiv.org/abs/2506.05813) | [code]

- [2025/05/26] **Towards Multi-Granularity Memory Association and Selection for Long-Term Conversational Agents** | [[paper]](https://arxiv.org/abs/2505.19549) | [code]

- [2025/05/26] **Task Memory Engine: Spatial Memory for Robust Multi-Step LLM Agents** | [[paper]](https://arxiv.org/abs/2505.19436) | [code]

- [2025/05/23] **Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic Access Control** | [[paper]](https://arxiv.org/abs/2505.18279) | [code]

- [2025/05/22] **Embodied Agents Meet Personalization: Exploring Memory Utilization for Personalized Assistance** | [[paper]](https://arxiv.org/abs/2505.16348) | [code]

- [2025/04/30] **LLM-Empowered Embodied Agent for Memory-Augmented Task Planning in Household Robotics** | [[paper]](https://arxiv.org/abs/2504.21716) | [code]

- [2025/04/28] **Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory** | [[paper]](https://arxiv.org/abs/2504.19413) | [code]

- [2025/04/11] **Task Memory Engine (TME): A Structured Memory Framework with Graph-Aware Extensions for Multi-Step LLM Agent Tasks** | [[paper]](https://arxiv.org/abs/2504.08525) | [code]

- [2025/03/27] **MemInsight: Autonomous Memory Augmentation for LLM Agents** | [[paper]](https://arxiv.org/abs/2503.21760) | [code]

- [2025/03/25] **MARS: Memory-Enhanced Agents with Reflective Self-improvement** | [[paper]](https://arxiv.org/abs/2503.19271) | [code]

- [2025/03/11] **In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents** | [[paper]](https://arxiv.org/abs/2503.08026) | [code]

- [2025/02/17] **A-MEM: Agentic Memory for LLM Agents** | [[paper]](https://arxiv.org/abs/2502.12110) | [code]

- [2025/02/08] **On Memory Construction and Retrieval for Personalized Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.05589) | [code]

- [2025/01/20] **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** | [[paper]](https://arxiv.org/abs/2501.13956) | [code]

- [2025/01/15] **Doc-Guided Sent2Sent++: A Sent2Sent++ Agent with Doc-Guided memory for Document-level Machine Translation** | [[paper]](https://arxiv.org/abs/2501.08523) | [code]

- [2024/12/17] **On the Structural Memory of LLM Agents** | [[paper]](https://arxiv.org/abs/2412.15266) | [code]

- [2024/12/17] **Memory-Augmented Agent Training for Business Document Understanding** | [[paper]](https://arxiv.org/abs/2412.15274) | [code]

- [2024/10/10] **DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory** | [[paper]](https://arxiv.org/abs/2410.08143) | [code]

- [2024/09/28] **Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs** | [[paper]](https://arxiv.org/abs/2409.19401) | [code]

- [2024/09/11] **Agent Workflow Memory** | [[paper]](https://arxiv.org/abs/2409.07429) | [code]

- [2024/09/01] **Self-evolving Agents with reflective and memory-augmented abilities** | [[paper]](https://arxiv.org/abs/2409.00872) | [code]

- [2024/08/18] **HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model** | [[paper]](https://arxiv.org/abs/2408.09559) | [code]

- [2024/08/07] **Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks** | [[paper]](https://arxiv.org/abs/2408.03615) | [code]

- [2024/05/29] **Toward Conversational Agents with Context and Time Sensitive Long-term Memory** | [[paper]](https://arxiv.org/abs/2406.00057) | [[code]](https://github.com/Zyphra/TemporalMemoryDataset)

- [2024/04/15] **Memory Sharing for Large Language Model based Agents** | [[paper]](https://arxiv.org/abs/2404.09982) | [[code]](https://github.com/GHupppp/MemorySharingLLM)

- [2024/02/19] **Compress to Impress: Unleashing the Potential of Compressive Memory in Real-World Long-Term Conversations** | [[paper]](https://arxiv.org/abs/2402.11975) | [code]

- [2024/02/07] **InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory** | [[paper]](https://arxiv.org/abs/2402.04617) | [code]

- [2024/02/06] **RAP: Retrieval-Augmented Planning with Contextual Memory for Multimodal LLM Agents** | [[paper]](https://arxiv.org/abs/2402.03610) | [code]

- [2024/01/05] **From LLM to Conversational Agent: A Memory Enhanced Architecture with Fine-Tuning of Large Language Models** | [[paper]](https://arxiv.org/abs/2401.02777) | [code]

- [2023/12/22] **Empowering Working Memory for Large Language Model Agents** | [[paper]](https://arxiv.org/abs/2312.17259) | [code]

- [2023/12/22] **Personalized Large Language Model Assistant with Evolving Conditional Memory** | [[paper]](https://arxiv.org/abs/2312.17257) | [code]

- [2023/11/10] **JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models** | [[paper]](https://arxiv.org/abs/2311.05997) | [[code]](https://github.com/CraftJarvis/JARVIS-1)

- [2023/06/06] **ChatDB: Augmenting LLMs with Databases as Their Symbolic Memory** | [[paper]](https://arxiv.org/abs/2306.03901) | [code]

- [2023/05/23] **RET-LLM: Towards a General Read-Write Memory for Large Language Models** | [[paper]](https://arxiv.org/abs/2305.14322) | [code]

- [2023/05/17] **MemoryBank: Enhancing Large Language Models with Long-Term Memory** | [[paper]](https://arxiv.org/abs/2305.10250) | [code]

- [2023/05/02] **The Role of Summarization in Generative Agents: A Preliminary Perspective** | [[paper]](https://arxiv.org/abs/2305.01253) | [code]

- [2023/05/01] **Learning to Reason and Memorize with Self-Notes** | [[paper]](https://arxiv.org/abs/2305.00833) | [code]

- [2023/04/26] **Enhancing Large Language Model with Self-Controlled Memory Framework** | [[paper]](https://arxiv.org/abs/2304.13343) | [code]

- [2023/04/21] **Emergent and Predictable Memorization in Large Language Models** | [[paper]](https://arxiv.org/abs/2304.11158) | [code]

#### Feedback&Reflection
- [2025/07/08] **Conditional Multi-Stage Failure Recovery for Embodied Agents** | [[paper]](https://arxiv.org/abs/2507.06016) | [code]

- [2025/06/10] **Reinforce LLM Reasoning through Multi-Agent Reflection** | [[paper]](https://arxiv.org/abs/2506.08379) | [code]

- [2025/06/04] **Debate, Reflect, and Distill: Multi-Agent Feedback with Tree-Structured Preference Optimization for Efficient Language Model Enhancement** | [[paper]](https://arxiv.org/abs/2506.03541) | [code]

- [2025/06/04] **Graph Counselor: Adaptive Graph Exploration via Multi-Agent Synergy to Enhance LLM Reasoning** | [[paper]](https://arxiv.org/abs/2506.03939) | [code]

- [2025/06/03] **Mitigating Manipulation and Enhancing Persuasion: A Reflective Multi-Agent Approach for Legal Argument Generation** | [[paper]](https://arxiv.org/abs/2506.02992) | [code]

- [2025/05/22] **Optimizing LLM-Based Multi-Agent System with Textual Feedback: A Case Study on Software Development** | [[paper]](https://arxiv.org/abs/2505.16086) | [code]

- [2025/05/21] **ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection** | [[paper]](https://arxiv.org/abs/2505.15182) | [code]

- [2025/05/21] **Aligning Dialogue Agents with Global Feedback via Large Language Model Reward Decomposition** | [[paper]](https://arxiv.org/abs/2505.15922) | [code]

- [2025/05/06] **FRAME: Feedback-Refined Agent Methodology for Enhancing Medical Research Insights** | [[paper]](https://arxiv.org/abs/2505.04649) | [code]

- [2025/04/26] **Stealing Creator&#39;s Workflow: A Creator-Inspired Agentic Framework with Iterative Feedback Loop for Improved Scientific Short-form Generation** | [[paper]](https://arxiv.org/abs/2504.18805) | [code]

- [2025/03/20] **The Lighthouse of Language: Enhancing LLM Agents via Critique-Guided Improvement** | [[paper]](https://arxiv.org/abs/2503.16024) | [code]

- [2025/03/11] **In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents** | [[paper]](https://arxiv.org/abs/2503.08026) | [code]

- [2025/03/04] **Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent** | [[paper]](https://arxiv.org/abs/2503.02519) | [code]

- [2025/03/03] **Improving Retrospective Language Agents via Joint Policy Gradient Optimization** | [[paper]](https://arxiv.org/abs/2503.01490) | [code]

- [2025/02/20] **STeCa: Step-level Trajectory Calibration for LLM Agent Learning** | [[paper]](https://arxiv.org/abs/2502.14276) | [[code]](https://github.com/WangHanLinHenry/STeCa)

- [2025/02/17] **Table-Critic: A Multi-Agent Framework for Collaborative Criticism and Refinement in Table Reasoning** | [[paper]](https://arxiv.org/abs/2502.11799) | [code]

- [2025/02/17] **A Study on Leveraging Search and Self-Feedback for Agent Reasoning** | [[paper]](https://arxiv.org/abs/2502.12094) | [code]

- [2025/02/03] **PlotGen: Multi-Agent LLM-based Scientific Data Visualization via Multimodal Feedback** | [[paper]](https://arxiv.org/abs/2502.00988) | [code]

- [2025/01/26] **Large Language Models as Theory of Mind Aware Generative Agents with Counterfactual Reflection** | [[paper]](https://arxiv.org/abs/2501.15355) | [code]

- [2025/01/23] **AgentRec: Agent Recommendation Using Sentence Embeddings Aligned to Human Feedback** | [[paper]](https://arxiv.org/abs/2501.13333) | [code]

- [2025/01/08] **InfiGUIAgent: A Multimodal Generalist GUI Agent with Native Reasoning and Reflection** | [[paper]](https://arxiv.org/abs/2501.04575) | [code]

- [2024/12/31] **Enhancing LLM Reasoning with Multi-Path Collaborative Reactive and Reflection agents** | [[paper]](https://arxiv.org/abs/2501.00430) | [code]

- [2024/12/22] **A Multi-AI Agent System for Autonomous Optimization of Agentic AI Solutions via Iterative Refinement and LLM-Driven Feedback Loops** | [[paper]](https://arxiv.org/abs/2412.17149) | [code]

- [2024/11/29] **Training Agents with Weakly Supervised Feedback from Large Language Models** | [[paper]](https://arxiv.org/abs/2411.19547) | [code]

- [2024/11/21] **Enhancing LLMs for Power System Simulations: A Feedback-driven Multi-agent Framework** | [[paper]](https://arxiv.org/abs/2411.16707) | [code]

- [2024/11/11] **Using Generative AI and Multi-Agents to Provide Automatic Feedback** | [[paper]](https://arxiv.org/abs/2411.07407) | [code]

- [2024/11/04] **Positive Experience Reflection for Agents in Interactive Text Environments** | [[paper]](https://arxiv.org/abs/2411.02223) | [code]

- [2024/10/29] **Enhancing Financial Question Answering with a Multi-Agent Reflection Framework** | [[paper]](https://arxiv.org/abs/2410.21741) | [code]

- [2024/10/28] **CRAT: A Multi-Agent Framework for Causality-Enhanced Reflective and Retrieval-Augmented Translation with Large Language Models** | [[paper]](https://arxiv.org/abs/2410.21067) | [code]

- [2024/10/25] **OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization** | [[paper]](https://arxiv.org/abs/2410.19609) | [code]

- [2024/10/23] **ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents** | [[paper]](https://arxiv.org/abs/2410.17657) | [code]

- [2024/10/20] **Training Language Models to Critique With Multi-agent Feedback** | [[paper]](https://arxiv.org/abs/2410.15287) | [code]

- [2024/10/16] **PRefLexOR: Preference-based Recursive Language Modeling for Exploratory Optimization of Reasoning and Agentic Thinking** | [[paper]](https://arxiv.org/abs/2410.12375) | [code]

- [2024/10/08] **DataEnvGym: Data Generation Agents in Teacher Environments with Student Feedback** | [[paper]](https://arxiv.org/abs/2410.06215) | [code]

- [2024/10/02] **ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning** | [[paper]](https://arxiv.org/abs/2410.02052) | [code]

- [2024/10/02] **RGD: Multi-LLM Based Agent Debugger via Refinement and Generation Guidance** | [[paper]](https://arxiv.org/abs/2410.01242) | [code]

- [2024/09/18] **MAgICoRe: Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning** | [[paper]](https://arxiv.org/abs/2409.12147) | [code]

- [2024/09/05] **E2CL: Exploration-based Error Correction Learning for Embodied Agents** | [[paper]](https://arxiv.org/abs/2409.03256) | [[code]](https://github.com/WangHanLinHenry/E2CL)

- [2024/09/01] **Self-evolving Agents with reflective and memory-augmented abilities** | [[paper]](https://arxiv.org/abs/2409.00872) | [code]

- [2024/08/30] **Tool-Assisted Agent on SQL Inspection and Refinement in Real-World Scenarios** | [[paper]](https://arxiv.org/abs/2408.16991) | [code]

- [2024/08/15] **MAG-SQL: Multi-Agent Generative Approach with Soft Schema Linking and Iterative Sub-SQL Refinement for Text-to-SQL** | [[paper]](https://arxiv.org/abs/2408.07930) | [code]

- [2024/07/25] **Recursive Introspection: Teaching Language Model Agents How to Self-Improve** | [[paper]](https://arxiv.org/abs/2407.18219) | [code]

- [2024/06/09] **A Review of Prominent Paradigms for LLM-Based Agents: Tool Use (Including RAG), Planning, and Feedback Learning** | [[paper]](https://arxiv.org/abs/2406.05804) | [code]

- [2024/06/05] **LLM-based Rewriting of Inappropriate Argumentation using Reinforcement Learning from Machine Feedback** | [[paper]](https://arxiv.org/abs/2406.03363) | [code]

- [2024/06/03] **Re-ReST: Reflection-Reinforced Self-Training for Language Agents** | [[paper]](https://arxiv.org/abs/2406.01495) | [[code]](https://github.com/PlusLabNLP/Re-ReST)

- [2024/03/18] **QueryAgent: A Reliable and Efficient Reasoning Framework with Environmental Feedback-based Self-Correction** | [[paper]](https://arxiv.org/abs/2403.11886) | [code]

- [2024/03/17] **Improving Dialogue Agents by Decomposing One Global Explicit Annotation with Local Implicit Multimodal Feedback** | [[paper]](https://arxiv.org/abs/2403.11330) | [code]

- [2024/03/08] **ChatASU: Evoking LLM&#39;s Reflexion to Truly Understand Aspect Sentiment in Dialogues** | [[paper]](https://arxiv.org/abs/2403.05326) | [code]

- [2024/03/04] **Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents** | [[paper]](https://arxiv.org/abs/2403.02502) | [code]

- [2024/02/27] **Agent-Pro: Learning to Evolve via Policy-Level Reflection and Optimization** | [[paper]](https://arxiv.org/abs/2402.17574) | [code]

- [2024/02/26] **SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection** | [[paper]](https://arxiv.org/abs/2402.16705) | [code]

- [2024/02/22] **Mirror: A Multiple-perspective Self-Reflection Method for Knowledge-rich Reasoning** | [[paper]](https://arxiv.org/abs/2402.14963) | [code]

- [2024/02/19] **A Critical Evaluation of AI Feedback for Aligning Large Language Models** | [[paper]](https://arxiv.org/abs/2402.12366) | [code]

- [2024/02/06] **AnyTool: Self-Reflective, Hierarchical Agents for Large-Scale API Calls** | [[paper]](https://arxiv.org/abs/2402.04253) | [[code]](https://github.com/dyabel/anytool)

- [2024/02/02] **StepCoder: Improve Code Generation with Reinforcement Learning from Compiler Feedback** | [[paper]](https://arxiv.org/abs/2402.01391) | [code]

- [2023/11/14] **The ART of LLM Refinement: Ask, Refine, and Trust** | [[paper]](https://arxiv.org/abs/2311.07961) | [code]

- [2023/10/31] **Learning From Mistakes Makes LLM Better Reasoner** | [[paper]](https://arxiv.org/abs/2310.20689) | [code]

- [2023/10/12] **A Zero-Shot Language Agent for Computer Control with Structured Reflection** | [[paper]](https://arxiv.org/abs/2310.08740) | [code]

- [2023/07/27] **PanGu-Coder2: Boosting Large Language Models for Code with Ranking Feedback** | [[paper]](https://arxiv.org/abs/2307.14936) | [code]

- [2023/05/22] **Making Language Models Better Tool Learners with Execution Feedback** | [[paper]](https://arxiv.org/abs/2305.13068) | [code]

- [2023/05/17] **Improving Language Model Negotiation with Self-Play and In-Context Learning from AI Feedback** | [[paper]](https://arxiv.org/abs/2305.10142) | [code]

- [2023/04/21] **Improving Grounded Language Understanding in a Collaborative Environment by Interacting with Agents Through Help Feedback** | [[paper]](https://arxiv.org/abs/2304.10750) | [code]

- [2023/04/11] **Teaching Large Language Models to Self-Debug** | [[paper]](https://arxiv.org/abs/2304.05128) | [code]

- [2023/03/30] **Self-Refine: Iterative Refinement with Self-Feedback** | [[paper]](https://arxiv.org/abs/2303.17651) | [code]

#### RAG
- [2025/07/09] **Multi-Agent Retrieval-Augmented Framework for Evidence-Based Counterspeech Against Health Misinformation** | [[paper]](https://arxiv.org/abs/2507.07307) | [code]

- [2025/07/04] **AI-VaxGuide: An Agentic RAG-Based LLM for Vaccination Decisions** | [[paper]](https://arxiv.org/abs/2507.03493) | [code]

- [2025/06/28] **Knowledge Augmented Finetuning Matters in both RAG and Agent Based Dialog Systems** | [[paper]](https://arxiv.org/abs/2506.22852) | [code]

- [2025/06/27] **ARAG: Agentic Retrieval Augmented Generation for Personalized Recommendation** | [[paper]](https://arxiv.org/abs/2506.21931) | [code]

- [2025/06/12] **CIIR@LiveRAG 2025: Optimizing Multi-Agent Retrieval Augmented Generation through Self-Training** | [[paper]](https://arxiv.org/abs/2506.10844) | [code]

- [2025/06/04] **Graph Counselor: Adaptive Graph Exploration via Multi-Agent Synergy to Enhance LLM Reasoning** | [[paper]](https://arxiv.org/abs/2506.03939) | [code]

- [2025/05/28] **Agent-UniRAG: A Trainable Open-Source LLM Agent Framework for Unified Retrieval-Augmented Generation Systems** | [[paper]](https://arxiv.org/abs/2505.22571) | [code]

- [2025/05/26] **MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning** | [[paper]](https://arxiv.org/abs/2505.20096) | [code]

- [2025/05/22] **O$^2$-Searcher: A Searching-based Agent Model for Open-Domain Open-Ended Question Answering** | [[paper]](https://arxiv.org/abs/2505.16582) | [code]

- [2025/05/22] **Personalizing Student-Agent Interactions Using Log-Contextualized Retrieval Augmented Generation (RAG)** | [[paper]](https://arxiv.org/abs/2505.17238) | [code]

- [2025/05/22] **Search Wisely: Mitigating Sub-optimal Agentic Searches By Reducing Uncertainty** | [[paper]](https://arxiv.org/abs/2505.17281) | [code]

- [2025/05/21] **InfoDeepSeek: Benchmarking Agentic Information Seeking for Retrieval-Augmented Generation** | [[paper]](https://arxiv.org/abs/2505.15872) | [code]

- [2025/05/13] **ALOHA: Empowering Multilingual Agent for University Orientation with Hierarchical Retrieval** | [[paper]](https://arxiv.org/abs/2505.08130) | [code]

- [2025/05/12] **Reinforced Internal-External Knowledge Synergistic Reasoning for Efficient Adaptive Search Agent** | [[paper]](https://arxiv.org/abs/2505.07596) | [code]

- [2025/04/30] **Talk Before You Retrieve: Agent-Led Discussions for Better RAG in Medical QA** | [[paper]](https://arxiv.org/abs/2504.21252) | [code]

- [2025/04/24] **A RAG-Based Multi-Agent LLM System for Natural Hazard Resilience and Adaptation** | [[paper]](https://arxiv.org/abs/2504.17200) | [code]

- [2025/04/15] **Towards Automated Safety Requirements Derivation Using Agent-based RAG** | [[paper]](https://arxiv.org/abs/2504.11243) | [code]

- [2025/04/13] **HM-RAG: Hierarchical Multi-Agent Multimodal Retrieval Augmented Generation** | [[paper]](https://arxiv.org/abs/2504.12330) | [code]

- [2025/04/11] **TP-RAG: Benchmarking Retrieval-Augmented Large Language Model Agents for Spatiotemporal-Aware Travel Planning** | [[paper]](https://arxiv.org/abs/2504.08694) | [code]

- [2025/04/10] **CollEX -- A Multimodal Agentic RAG System Enabling Interactive Exploration of Scientific Collections** | [[paper]](https://arxiv.org/abs/2504.07643) | [code]

- [2025/03/18] **Retrieval-Augmented Simulacra: Generative Agents for Up-to-date and Knowledge-Adaptive Simulations** | [[paper]](https://arxiv.org/abs/2503.14620) | [code]

- [2025/03/14] **RAG-KG-IL: A Multi-Agent Hybrid Framework for Reducing Hallucinations and Enhancing LLM Reasoning through RAG and Incremental Knowledge Graph Learning Integration** | [[paper]](https://arxiv.org/abs/2503.13514) | [code]

- [2025/03/01] **EXCLAIM: An Explainable Cross-Modal Agentic System for Misinformation Detection with Hierarchical Retrieval** | [[paper]](https://arxiv.org/abs/2504.06269) | [code]

- [2025/02/25] **ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents** | [[paper]](https://arxiv.org/abs/2502.18017) | [code]

- [2025/02/19] **RAG-Gym: Optimizing Reasoning and Search Agents with Process Supervision** | [[paper]](https://arxiv.org/abs/2502.13957) | [code]

- [2025/02/08] **On Memory Construction and Retrieval for Personalized Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.05589) | [code]

- [2025/02/06] **Enhancing Online Learning Efficiency Through Heterogeneous Resource Integration with a Multi-Agent RAG System** | [[paper]](https://arxiv.org/abs/2502.03948) | [code]

- [2025/01/25] **Improving Retrieval-Augmented Generation through Multi-Agent Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2501.15228) | [code]

- [2024/12/31] **MAIN-RAG: Multi-Agent Filtering Retrieval-Augmented Generation** | [[paper]](https://arxiv.org/abs/2501.00332) | [code]

- [2024/12/24] **GeAR: Graph-enhanced Agent for Retrieval-augmented Generation** | [[paper]](https://arxiv.org/abs/2412.18431) | [code]

- [2024/12/20] **Towards Interpretable Radiology Report Generation via Concept Bottlenecks using a Multi-Agentic RAG** | [[paper]](https://arxiv.org/abs/2412.16086) | [code]

- [2024/12/16] **BioRAGent: A Retrieval-Augmented Generation System for Showcasing Generative Query Expansion and Domain-Specific Search for Scientific Q&amp;A** | [[paper]](https://arxiv.org/abs/2412.12358) | [code]

- [2024/12/07] **SLA Management in Reconfigurable Multi-Agent RAG: A Systems Approach to Question Answering** | [[paper]](https://arxiv.org/abs/2412.06832) | [code]

- [2024/11/05] **Benchmarking Multimodal Retrieval Augmented Generation with Dynamic VQA Dataset and Self-adaptive Planning Agent** | [[paper]](https://arxiv.org/abs/2411.02937) | [code]

- [2024/10/28] **CRAT: A Multi-Agent Framework for Causality-Enhanced Reflective and Retrieval-Augmented Translation with Large Language Models** | [[paper]](https://arxiv.org/abs/2410.21067) | [code]

- [2024/10/18] **Toolshed: Scale Tool-Equipped Agents with Advanced RAG-Tool Fusion and Tool Knowledge Bases** | [[paper]](https://arxiv.org/abs/2410.14594) | [code]

- [2024/10/01] **Conversational Exploratory Search of Scholarly Publications Using Knowledge Graphs** | [[paper]](https://arxiv.org/abs/2410.00427) | [code]

- [2024/09/28] **Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs** | [[paper]](https://arxiv.org/abs/2409.19401) | [code]

- [2024/08/18] **Agentic Retrieval-Augmented Generation for Time Series Analysis** | [[paper]](https://arxiv.org/abs/2408.14484) | [code]

- [2024/08/05] **LLM Agents Improve Semantic Code Search** | [[paper]](https://arxiv.org/abs/2408.11058) | [code]

- [2024/08/03] **MALADE: Orchestration of LLM-powered Agents with Retrieval Augmented Generation for Pharmacovigilance** | [[paper]](https://arxiv.org/abs/2408.01869) | [code]

- [2024/07/20] **Golden-Retriever: High-Fidelity Agentic Retrieval Augmented Generation for Industrial Knowledge Base** | [[paper]](https://arxiv.org/abs/2408.00798) | [code]

- [2024/06/26] **Geode: A Zero-shot Geospatial Question-Answering Agent with Explicit Reasoning and Precise Spatio-Temporal Retrieval** | [[paper]](https://arxiv.org/abs/2407.11014) | [code]

- [2024/06/19] **StackRAG Agent: Improving Developer Answers with Retrieval-Augmented Generation** | [[paper]](https://arxiv.org/abs/2406.13840) | [code]

- [2024/06/09] **A Review of Prominent Paradigms for LLM-Based Agents: Tool Use (Including RAG), Planning, and Feedback Learning** | [[paper]](https://arxiv.org/abs/2406.05804) | [code]

- [2024/03/05] **AgentsCourt: Building Judicial Decision-Making Agents with Court Debate Simulation and Legal Knowledge Augmentation** | [[paper]](https://arxiv.org/abs/2403.02959) | [code]

- [2024/02/06] **RAP: Retrieval-Augmented Planning with Contextual Memory for Multimodal LLM Agents** | [[paper]](https://arxiv.org/abs/2402.03610) | [code]

- [2023/12/27] **Automating Knowledge Acquisition for Content-Centric Cognitive Agents Using LLMs** | [[paper]](https://arxiv.org/abs/2312.16378) | [code]

#### Search
- [2025/06/09] **CheMatAgent: Enhancing LLMs for Chemistry and Materials Science through Tree-Search Based Tool Learning** | [[paper]](https://arxiv.org/abs/2506.07551) | [code]

- [2025/06/06] **AgentSwift: Efficient LLM Agent Design via Value-guided Hierarchical Search** | [[paper]](https://arxiv.org/abs/2506.06017) | [code]

- [2025/05/26] **T^2Agent A Tool-augmented Multimodal Misinformation Detection Agent with Monte Carlo Tree Search** | [[paper]](https://arxiv.org/abs/2505.19768) | [code]

- [2025/05/12] **Structural Entropy Guided Agent for Detecting and Repairing Knowledge Deficiencies in LLMs** | [[paper]](https://arxiv.org/abs/2505.07184) | [code]

- [2025/04/10] **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** | [[paper]](https://arxiv.org/abs/2504.08066) | [code]

- [2025/04/04] **SynWorld: Virtual Scenario Synthesis for Agentic Action Knowledge Refinement** | [[paper]](https://arxiv.org/abs/2504.03561) | [code]

- [2025/03/18] **DARS: Dynamic Action Re-Sampling to Enhance Coding Agent Performance by Adaptive Tree Traversal** | [[paper]](https://arxiv.org/abs/2503.14269) | [code]

- [2025/02/20] **I-MCTS: Enhancing Agentic AutoML via Introspective Monte Carlo Tree Search** | [[paper]](https://arxiv.org/abs/2502.14693) | [code]

- [2025/02/18] **R2-KG: General-Purpose Dual-Agent Framework for Reliable Reasoning on Knowledge Graphs** | [[paper]](https://arxiv.org/abs/2502.12767) | [code]

- [2025/02/18] **Agentic Deep Graph Reasoning Yields Self-Organizing Knowledge Networks** | [[paper]](https://arxiv.org/abs/2502.13025) | [code]

- [2025/02/17] **A Study on Leveraging Search and Self-Feedback for Agent Reasoning** | [[paper]](https://arxiv.org/abs/2502.12094) | [code]

- [2025/02/05] **SymAgent: A Neural-Symbolic Self-Learning Agent Framework for Complex Reasoning over Knowledge Graphs** | [[paper]](https://arxiv.org/abs/2502.03283) | [code]

- [2025/02/02] **Efficient Multi-Agent System Training with Data Influence-Oriented Tree Search** | [[paper]](https://arxiv.org/abs/2502.00955) | [code]

- [2025/01/31] **KBQA-o1: Agentic Knowledge Base Question Answering with Monte Carlo Tree Search** | [[paper]](https://arxiv.org/abs/2501.18922) | [code]

- [2025/01/09] **Search-o1: Agentic Search-Enhanced Large Reasoning Models** | [[paper]](https://arxiv.org/abs/2501.05366) | [code]

- [2024/12/24] **A Novel Task-Driven Method with Evolvable Interactive Agents Using Event Trees for Enhanced Emergency Decision Support** | [[paper]](https://arxiv.org/abs/2501.06193) | [code]

- [2024/12/22] **Multi-Agent Sampling: Scaling Inference Compute for Data Synthesis with Tree Search-Based Agentic Collaboration** | [[paper]](https://arxiv.org/abs/2412.17061) | [code]

- [2024/12/05] **Agent AI with LangGraph: A Modular Framework for Enhancing Machine Translation Using Large Language Models** | [[paper]](https://arxiv.org/abs/2412.03801) | [code]

- [2024/11/07] **CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models** | [[paper]](https://arxiv.org/abs/2411.04329) | [code]

- [2024/10/29] **Synergizing LLM Agents and Knowledge Graph for Socioeconomic Prediction in LBSN** | [[paper]](https://arxiv.org/abs/2411.00028) | [code]

- [2024/10/25] **AGENT-CQ: Automatic Generation and Evaluation of Clarifying Questions for Conversational Search with LLMs** | [[paper]](https://arxiv.org/abs/2410.19692) | [code]

- [2024/10/22] **SELA: Tree-Search Enhanced LLM Agents for Automated Machine Learning** | [[paper]](https://arxiv.org/abs/2410.17238) | [code]

- [2024/10/13] **Expanding Search Space with Diverse Prompting Agents: An Efficient Sampling Approach for LLM Mathematical Reasoning** | [[paper]](https://arxiv.org/abs/2410.09780) | [code]

- [2024/10/13] **LLM-Based Multi-Agent Systems are Scalable Graph Generative Models** | [[paper]](https://arxiv.org/abs/2410.09824) | [code]

- [2024/10/02] **ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning** | [[paper]](https://arxiv.org/abs/2410.02052) | [code]

- [2024/09/09] **SciAgents: Automating scientific discovery through multi-agent intelligent graph reasoning** | [[paper]](https://arxiv.org/abs/2409.05556) | [code]

- [2024/07/01] **Tree Search for Language Model Agents** | [[paper]](https://arxiv.org/abs/2407.01476) | [code]

- [2024/06/17] **Input Conditioned Graph Generation for Language Agents** | [[paper]](https://arxiv.org/abs/2406.11555) | [[code]](https://github.com/lukasvierling/dynamicgptswarm)

- [2024/02/17] **KG-Agent: An Efficient Autonomous Agent Framework for Complex Reasoning over Knowledge Graph** | [[paper]](https://arxiv.org/abs/2402.11163) | [code]

- [2024/02/16] **When is Tree Search Useful for LLM Planning? It Depends on the Discriminator** | [[paper]](https://arxiv.org/abs/2402.10890) | [[code]](https://github.com/osu-nlp-group/llm-planning-eval)

- [2024/02/09] **CoSearchAgent: A Lightweight Collaborative Search Agent with Large Language Models** | [[paper]](https://arxiv.org/abs/2402.06360) | [code]

- [2023/05/17] **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** | [[paper]](https://arxiv.org/abs/2305.10601) | [code]

### Interaction
#### Role Playing
- [2025/06/28] **Agent-to-Agent Theory of Mind: Testing Interlocutor Awareness among Large Language Models** | [[paper]](https://arxiv.org/abs/2506.22957) | [code]

- [2025/06/24] **MAM: Modular Multi-Agent Framework for Multi-Modal Medical Diagnosis via Role-Specialized Collaboration** | [[paper]](https://arxiv.org/abs/2506.19835) | [code]

- [2025/06/20] **Language-Informed Synthesis of Rational Agent Models for Grounded Theory-of-Mind Reasoning On-The-Fly** | [[paper]](https://arxiv.org/abs/2506.16755) | [code]

- [2025/06/06] **PersonaAgent: When Large Language Model Agents Meet Personalization at Test Time** | [[paper]](https://arxiv.org/abs/2506.06254) | [code]

- [2025/06/02] **Thinking in Character: Advancing Role-Playing Agents with Role-Aware Reasoning** | [[paper]](https://arxiv.org/abs/2506.01748) | [code]

- [2025/05/30] **Context-Aware Sentiment Forecasting via LLM-based Multi-Perspective Role-Playing Agents** | [[paper]](https://arxiv.org/abs/2505.24331) | [code]

- [2025/05/29] **ChARM: Character-based Act-adaptive Reward Modeling for Advanced Role-Playing Language Agents** | [[paper]](https://arxiv.org/abs/2505.23923) | [code]

- [2025/05/26] **OmniCharacter: Towards Immersive Role-Playing Agents with Seamless Speech-Language Personality Interaction** | [[paper]](https://arxiv.org/abs/2505.20277) | [code]

- [2025/05/20] **Inter(sectional) Alia(s): Ambiguity in Voice Agent Identity via Intersectional Japanese Self-Referents** | [[paper]](https://arxiv.org/abs/2506.01998) | [code]

- [2025/04/29] **BrAIcht, a theatrical agent that speaks like Bertolt Brecht&#39;s characters** | [[paper]](https://arxiv.org/abs/2504.20552) | [code]

- [2025/04/25] **Exploring Personality-Aware Interactions in Salesperson Dialogue Agents** | [[paper]](https://arxiv.org/abs/2504.18058) | [code]

- [2025/04/13] **UXAgent: A System for Simulating Usability Testing of Web Design with LLM Agents** | [[paper]](https://arxiv.org/abs/2504.09407) | [code]

- [2025/04/03] **LLMs as Deceptive Agents: How Role-Based Prompting Induces Semantic Ambiguity in Puzzle Tasks** | [[paper]](https://arxiv.org/abs/2504.02254) | [code]

- [2025/03/14] **AIstorian lets AI be a historian: A KG-powered multi-agent system for accurate biography generation** | [[paper]](https://arxiv.org/abs/2503.11346) | [code]

- [2025/02/20] **InstructAgent: Building User Controllable Recommender via LLM Agent** | [[paper]](https://arxiv.org/abs/2502.14662) | [code]

- [2025/02/18] **SEFL: Harnessing Large Language Model Agents to Improve Educational Feedback Systems** | [[paper]](https://arxiv.org/abs/2502.12927) | [code]

- [2025/02/17] **Can LLM Agents Maintain a Persona in Discourse?** | [[paper]](https://arxiv.org/abs/2502.11843) | [code]

- [2025/02/17] **LM Agents for Coordinating Multi-User Information Gathering** | [[paper]](https://arxiv.org/abs/2502.12328) | [code]

- [2025/02/16] **SCALE: Towards Collaborative Content Analysis in Social Science with Large Language Model Agents and Human Intervention** | [[paper]](https://arxiv.org/abs/2502.10937) | [code]

- [2025/02/13] **Language Agents as Digital Representatives in Collective Decision-Making** | [[paper]](https://arxiv.org/abs/2502.09369) | [code]

- [2025/02/06] **PsyPlay: Personality-Infused Role-Playing Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.03821) | [code]

- [2025/02/03] **Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant** | [[paper]](https://arxiv.org/abs/2502.01390) | [code]

- [2025/01/23] **AgentRec: Agent Recommendation Using Sentence Embeddings Aligned to Human Feedback** | [[paper]](https://arxiv.org/abs/2501.13333) | [code]

- [2025/01/15] **Personality Modeling for Persuasion of Misinformation using AI Agent** | [[paper]](https://arxiv.org/abs/2501.08985) | [code]

- [2024/12/28] **BaiJia: A Large-Scale Role-Playing Agent Corpus of Chinese Historical Characters** | [[paper]](https://arxiv.org/abs/2412.20024) | [code]

- [2024/12/22] **Modular Conversational Agents for Surveys and Interviews** | [[paper]](https://arxiv.org/abs/2412.17049) | [code]

- [2024/12/11] **SweetieChat: A Strategy-Enhanced Role-playing Framework for Diverse Scenarios Handling Emotional Support Agent** | [[paper]](https://arxiv.org/abs/2412.08389) | [code]

- [2024/12/10] **My Words Imply Your Opinion: Reader Agent-Based Propagation Enhancement for Personalized Implicit Emotion Analysis** | [[paper]](https://arxiv.org/abs/2412.07367) | [code]

- [2024/11/21] **Towards Full Delegation: Designing Ideal Agentic Behaviors for Travel Planning** | [[paper]](https://arxiv.org/abs/2411.13904) | [code]

- [2024/11/19] **Probing the Capacity of Language Model Agents to Operationalize Disparate Experiential Context Despite Distraction** | [[paper]](https://arxiv.org/abs/2411.12828) | [code]

- [2024/11/12] **SHARP: Unlocking Interactive Hallucination via Stance Transfer in Role-Playing Agents** | [[paper]](https://arxiv.org/abs/2411.07965) | [code]

- [2024/11/04] **A Multi-Task Role-Playing Agent Capable of Imitating Character Linguistic Styles** | [[paper]](https://arxiv.org/abs/2411.02457) | [code]

- [2024/10/28] **Guide-LLM: An Embodied LLM Agent and Text-Based Topological Map for Robotic Guidance of People with Visual Impairments** | [[paper]](https://arxiv.org/abs/2410.20666) | [code]

- [2024/10/24] **Schema-Guided Culture-Aware Complex Event Simulation with Multi-Agent Role-Play** | [[paper]](https://arxiv.org/abs/2410.18935) | [code]

- [2024/09/23] **ERABAL: Enhancing Role-Playing Agents through Boundary-Aware Learning** | [[paper]](https://arxiv.org/abs/2409.14710) | [code]

- [2024/09/19] **FoodPuzzle: Developing Large Language Model Agents as Flavor Scientists** | [[paper]](https://arxiv.org/abs/2409.12832) | [code]

- [2024/09/12] **TravelAgent: An AI Assistant for Personalized Travel Planning** | [[paper]](https://arxiv.org/abs/2409.08069) | [code]

- [2024/09/11] **Using Generative Agents to Create Tip Sheets for Investigative Data Reporting** | [[paper]](https://arxiv.org/abs/2409.07286) | [code]

- [2024/08/28] **Interactive Agents: Simulating Counselor-Client Psychological Counseling via Role-Playing LLM-to-LLM Interactions** | [[paper]](https://arxiv.org/abs/2408.15787) | [code]

- [2024/08/21] **Drama Engine: A Framework for Narrative Agents** | [[paper]](https://arxiv.org/abs/2408.11574) | [code]

- [2024/06/24] **The Effects of Embodiment and Personality Expression on Learning in LLM-based Educational Agents** | [[paper]](https://arxiv.org/abs/2407.10993) | [code]

- [2024/06/17] **HoLLMwood: Unleashing the Creativity of Large Language Models in Screenwriting via Role Playing** | [[paper]](https://arxiv.org/abs/2406.11683) | [code]

- [2024/06/11] **Agent-SiMT: Agent-assisted Simultaneous Machine Translation with Large Language Models** | [[paper]](https://arxiv.org/abs/2406.06910) | [code]

- [2024/06/09] **Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions** | [[paper]](https://arxiv.org/abs/2406.05688) | [[code]](https://github.com/chengtan9907/reviewmt)

- [2024/05/28] **TimeChara: Evaluating Point-in-Time Character Hallucination of Role-Playing Large Language Models** | [[paper]](https://arxiv.org/abs/2405.18027) | [code]

- [2024/05/10] **LLM Discussion: Enhancing the Creativity of Large Language Models via Discussion Framework and Role-Play** | [[paper]](https://arxiv.org/abs/2405.06373) | [code]

- [2024/05/08] **LLMs with Personalities in Multi-issue Negotiation Games** | [[paper]](https://arxiv.org/abs/2405.05248) | [code]

- [2024/05/06] **Large Language Models (LLMs) as Agents for Augmented Democracy** | [[paper]](https://arxiv.org/abs/2405.03452) | [code]

- [2024/05/02] **GAIA: A General AI Assistant for Intelligent Accelerator Operations** | [[paper]](https://arxiv.org/abs/2405.01359) | [code]

- [2024/05/01] **&#34;Ask Me Anything&#34;: How Comcast Uses LLMs to Assist Agents in Real Time** | [[paper]](https://arxiv.org/abs/2405.00801) | [code]

- [2024/04/26] **Large Language Model Agent as a Mechanical Designer** | [[paper]](https://arxiv.org/abs/2404.17525) | [code]

- [2024/04/19] **Cooperative Sentiment Agents for Multimodal Sentiment Analysis** | [[paper]](https://arxiv.org/abs/2404.12642) | [[code]](https://github.com/smwanghhh/co-sa)

- [2024/03/31] **DiffAgent: Fast and Accurate Text-to-Image API Selection with Large Language Model** | [[paper]](https://arxiv.org/abs/2404.01342) | [[code]](https://github.com/OpenGVLab/DiffAgent)

- [2024/03/23] **EduAgent: Generative Student Agents in Learning** | [[paper]](https://arxiv.org/abs/2404.07963) | [code]

- [2024/03/19] **Characteristic AI Agents via Large Language Models** | [[paper]](https://arxiv.org/abs/2403.12368) | [code]

- [2024/03/15] **VideoAgent: Long-form Video Understanding with Large Language Model as Agent** | [[paper]](https://arxiv.org/abs/2403.10517) | [code]

- [2024/03/13] **Evaluating Large Language Models as Generative User Simulators for Conversational Recommendation** | [[paper]](https://arxiv.org/abs/2403.09738) | [code]

- [2024/02/29] **On the Decision-Making Abilities in Role-Playing using Large Language Models** | [[paper]](https://arxiv.org/abs/2402.18807) | [code]

- [2024/02/28] **Prospect Personalized Recommendation on Large Language Model-based Agent Platform** | [[paper]](https://arxiv.org/abs/2402.18240) | [code]

- [2024/02/26] **Language Agents as Optimizable Graphs** | [[paper]](https://arxiv.org/abs/2402.16823) | [[code]](https://github.com/metauto-ai/gptswarm)

- [2024/02/22] **Triad: A Framework Leveraging a Multi-Role LLM-based Agent to Solve Knowledge Base Question Answering** | [[paper]](https://arxiv.org/abs/2402.14320) | [code]

- [2024/02/22] **Large Language Models as Urban Residents: An LLM Agent Framework for Personal Mobility Generation** | [[paper]](https://arxiv.org/abs/2402.14744) | [code]

- [2024/02/21] **Neeko: Leveraging Dynamic LoRA for Efficient Multi-Character Role-Playing Agent** | [[paper]](https://arxiv.org/abs/2402.13717) | [code]

- [2024/02/19] **Stick to your Role! Stability of Personal Values Expressed in Large Language Models** | [[paper]](https://arxiv.org/abs/2402.14846) | [code]

- [2024/02/18] **Modelling Political Coalition Negotiations Using LLM-based Agents** | [[paper]](https://arxiv.org/abs/2402.11712) | [code]

- [2024/02/06] **Professional Agents -- Evolving Large Language Models into Autonomous Experts with Human-Level Competencies** | [[paper]](https://arxiv.org/abs/2402.03628) | [code]

- [2024/02/06] **Can Generative Agents Predict Emotion?** | [[paper]](https://arxiv.org/abs/2402.04232) | [code]

- [2024/02/05] **GUARD: Role-playing to Generate Natural-language Jailbreakings to Test Guideline Adherence of Large Language Models** | [[paper]](https://arxiv.org/abs/2402.03299) | [code]

- [2024/01/31] **LLMs Simulate Big Five Personality Traits: Further Evidence** | [[paper]](https://arxiv.org/abs/2402.01765) | [code]

- [2023/12/22] **Personalized Large Language Model Assistant with Evolving Conditional Memory** | [[paper]](https://arxiv.org/abs/2312.17257) | [code]

- [2023/12/21] **ChatGPT as a commenter to the news: can LLMs generate human-like opinions?** | [[paper]](https://arxiv.org/abs/2312.13961) | [code]

- [2023/12/20] **Machine Mindset: An MBTI Exploration of Large Language Models** | [[paper]](https://arxiv.org/abs/2312.12999) | [code]

- [2023/12/19] **Can ChatGPT be Your Personal Medical Assistant?** | [[paper]](https://arxiv.org/abs/2312.12006) | [code]

- [2023/10/13] **AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems** | [[paper]](https://arxiv.org/abs/2310.09233) | [code]

- [2023/10/01] **RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities of Large Language Models** | [[paper]](https://arxiv.org/abs/2310.00746) | [code]

- [2023/09/02] **ModelScope-Agent: Building Your Customizable Agent System with Open-source Large Language Models** | [[paper]](https://arxiv.org/abs/2309.00986) | [code]

- [2023/08/22] **Towards an On-device Agent for Text Rewriting** | [[paper]](https://arxiv.org/abs/2308.11807) | [code]

- [2023/08/10] **LLM As DBA** | [[paper]](https://arxiv.org/abs/2308.05481) | [code]

- [2023/08/03] **InterAct: Exploring the Potentials of ChatGPT as a Cooperative Agent** | [[paper]](https://arxiv.org/abs/2308.01552) | [code]

- [2023/07/11] **Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration** | [[paper]](https://arxiv.org/abs/2307.05300) | [code]

- [2023/07/05] **Building Cooperative Embodied Agents Modularly with Large Language Models** | [[paper]](https://arxiv.org/abs/2307.02485) | [code]

- [2023/05/25] **Role-Play with Large Language Models** | [[paper]](https://arxiv.org/abs/2305.16367) | [code]

- [2023/05/09] **TidyBot: Personalized Robot Assistance with Large Language Models** | [[paper]](https://arxiv.org/abs/2305.05658) | [code]

#### Conversation
- [2025/06/28] **Knowledge Augmented Finetuning Matters in both RAG and Agent Based Dialog Systems** | [[paper]](https://arxiv.org/abs/2506.22852) | [code]

- [2025/06/24] **Augmenting Multi-Agent Communication with State Delta Trajectory** | [[paper]](https://arxiv.org/abs/2506.19209) | [code]

- [2025/06/17] **From What to Respond to When to Respond: Timely Response Generation for Open-domain Dialogue Agents** | [[paper]](https://arxiv.org/abs/2506.14285) | [code]

- [2025/06/17] **Expectation Confirmation Preference Optimization for Multi-Turn Conversational Recommendation Agent** | [[paper]](https://arxiv.org/abs/2506.14302) | [code]

- [2025/06/13] **The Behavior Gap: Evaluating Zero-shot LLM Agents in Complex Task-Oriented Dialogs** | [[paper]](https://arxiv.org/abs/2506.12266) | [code]

- [2025/06/11] **Chat-of-Thought: Collaborative Multi-Agent System for Generating Domain Specific Information** | [[paper]](https://arxiv.org/abs/2506.10086) | [code]

- [2025/06/09] **$\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment** | [[paper]](https://arxiv.org/abs/2506.07982) | [code]

- [2025/06/04] **AI Agents for Conversational Patient Triage: Preliminary Simulation-Based Evaluation with Real-World EHR Data** | [[paper]](https://arxiv.org/abs/2506.04032) | [code]

- [2025/06/04] **CLAIM: An Intent-Driven Multi-Agent Framework for Analyzing Manipulation in Courtroom Dialogues** | [[paper]](https://arxiv.org/abs/2506.04131) | [code]

- [2025/05/29] **A Practical Approach for Building Production-Grade Conversational Agents with Workflow Graphs** | [[paper]](https://arxiv.org/abs/2505.23006) | [code]

- [2025/05/28] **ChatCFD: an End-to-End CFD Agent with Domain-specific Structured Thinking** | [[paper]](https://arxiv.org/abs/2506.02019) | [code]

- [2025/05/26] **Towards Multi-Granularity Memory Association and Selection for Long-Term Conversational Agents** | [[paper]](https://arxiv.org/abs/2505.19549) | [code]

- [2025/05/24] **Multi-Party Conversational Agents: A Survey** | [[paper]](https://arxiv.org/abs/2505.18845) | [code]

- [2025/05/21] **Aligning Dialogue Agents with Global Feedback via Large Language Model Reward Decomposition** | [[paper]](https://arxiv.org/abs/2505.15922) | [code]

- [2025/04/29] **BrAIcht, a theatrical agent that speaks like Bertolt Brecht&#39;s characters** | [[paper]](https://arxiv.org/abs/2504.20552) | [code]

- [2025/04/26] **MATCHA: Can Multi-Agent Collaboration Build a Trustworthy Conversational Recommender?** | [[paper]](https://arxiv.org/abs/2504.20094) | [code]

- [2025/04/21] **EducationQ: Evaluating LLMs&#39; Teaching Capabilities Through Multi-Agent Dialogue Framework** | [[paper]](https://arxiv.org/abs/2504.14928) | [code]

- [2025/04/20] **DialogueAgents: A Hybrid Agent-Based Speech Synthesis Framework for Multi-Party Dialogue** | [[paper]](https://arxiv.org/abs/2504.14482) | [code]

- [2025/04/12] **A Multi-view Discourse Framework for Integrating Semantic and Syntactic Features in Dialog Agents** | [[paper]](https://arxiv.org/abs/2504.09073) | [code]

- [2025/04/07] **Bridging Industrial Expertise and XR with LLM-Powered Conversational Agents** | [[paper]](https://arxiv.org/abs/2504.05527) | [code]

- [2025/04/07] **A Desideratum for Conversational Agents: Capabilities, Challenges, and Future Directions** | [[paper]](https://arxiv.org/abs/2504.16939) | [code]

- [2025/03/28] **Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey** | [[paper]](https://arxiv.org/abs/2503.22458) | [code]

- [2025/03/27] **EQ-Negotiator: An Emotion-Reasoning LLM Agent in Credit Dialogues** | [[paper]](https://arxiv.org/abs/2503.21080) | [code]

- [2025/03/26] **3MDBench: Medical Multimodal Multi-agent Dialogue Benchmark** | [[paper]](https://arxiv.org/abs/2504.13861) | [code]

- [2025/03/25] **CoMAC: Conversational Agent for Multi-Source Auxiliary Context with Sparse and Symmetric Latent Interactions** | [[paper]](https://arxiv.org/abs/2503.19274) | [code]

- [2025/03/25] **Substance over Style: Evaluating Proactive Conversational Coaching Agents** | [[paper]](https://arxiv.org/abs/2503.19328) | [code]

- [2025/03/18] **Personalized Attacks of Social Engineering in Multi-turn Conversations -- LLM Agents for Simulation and Detection** | [[paper]](https://arxiv.org/abs/2503.15552) | [code]

- [2025/03/11] **In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents** | [[paper]](https://arxiv.org/abs/2503.08026) | [code]

- [2025/03/05] **Cite Before You Speak: Enhancing Context-Response Grounding in E-commerce Conversational LLM-Agents** | [[paper]](https://arxiv.org/abs/2503.04830) | [code]

- [2025/02/24] **Turning Conversations into Workflows: A Framework to Extract and Evaluate Dialog Workflows for Service AI Agents** | [[paper]](https://arxiv.org/abs/2502.17321) | [code]

- [2025/02/20] **Enhancing Conversational Agents with Theory of Mind: Aligning Beliefs, Desires, and Intentions for Human-Like Interaction** | [[paper]](https://arxiv.org/abs/2502.14171) | [code]

- [2025/02/18] **One Size doesn&#39;t Fit All: A Personalized Conversational Tutoring Agent for Mathematics Instruction** | [[paper]](https://arxiv.org/abs/2502.12633) | [code]

- [2025/02/18] **Training Turn-by-Turn Verifiers for Dialogue Tutoring Agents: The Curious Case of LLMs as Your Coding Tutors** | [[paper]](https://arxiv.org/abs/2502.13311) | [code]

- [2025/02/18] **You need to MIMIC to get FAME: Solving Meeting Transcript Scarcity with a Multi-Agent Conversations** | [[paper]](https://arxiv.org/abs/2502.13001) | [code]

- [2025/02/17] **InfoQuest: Evaluating Multi-Turn Dialogue Agents for Open-Ended Conversations with Hidden Context** | [[paper]](https://arxiv.org/abs/2502.12257) | [code]

- [2025/02/13] **Reliable Conversational Agents under ASP Control that Understand Natural Language** | [[paper]](https://arxiv.org/abs/2502.09237) | [code]

- [2025/02/12] **Can a Single Model Master Both Multi-turn Conversations and Tool Use? CoALM: A Unified Conversational Agentic Language Model** | [[paper]](https://arxiv.org/abs/2502.08820) | [code]

- [2025/02/09] **MTPChat: A Multimodal Time-Aware Persona Dataset for Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.05887) | [code]

- [2025/02/09] **HamRaz: A Culture-Based Persian Conversation Dataset for Person-Centered Therapy Using LLM Agents** | [[paper]](https://arxiv.org/abs/2502.05982) | [code]

- [2025/02/08] **On Memory Construction and Retrieval for Personalized Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.05589) | [code]

- [2025/02/06] **PsyPlay: Personality-Infused Role-Playing Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.03821) | [code]

- [2025/01/24] **Unmasking Conversational Bias in AI Multiagent Systems** | [[paper]](https://arxiv.org/abs/2501.14844) | [code]

- [2025/01/23] **Communicating Activations Between Language Model Agents** | [[paper]](https://arxiv.org/abs/2501.14082) | [code]

- [2025/01/19] **IntellAgent: A Multi-Agent Framework for Evaluating Conversational AI Systems** | [[paper]](https://arxiv.org/abs/2501.11067) | [code]

- [2025/01/14] **Developing Enhanced Conversational Agents for Social Virtual Worlds** | [[paper]](https://arxiv.org/abs/2501.16341) | [code]

- [2025/01/03] **PSYCHE: A Multi-faceted Patient Simulation Framework for Evaluation of Psychiatric Assessment Conversational Agents** | [[paper]](https://arxiv.org/abs/2501.01594) | [code]

- [2024/12/30] **Exploring and Controlling Diversity in LLM-Agent Conversation** | [[paper]](https://arxiv.org/abs/2412.21102) | [code]

- [2024/12/24] **Extracting triples from dialogues for conversational social agents** | [[paper]](https://arxiv.org/abs/2412.18364) | [code]

- [2024/12/22] **Modular Conversational Agents for Surveys and Interviews** | [[paper]](https://arxiv.org/abs/2412.17049) | [code]

- [2024/12/21] **InfoTech Assistant : A Multimodal Conversational Agent for InfoTechnology Web Portal Queries** | [[paper]](https://arxiv.org/abs/2412.16412) | [code]

- [2024/12/13] **Script-Based Dialog Policy Planning for LLM-Powered Conversational Agents: A Basic Architecture for an &#34;AI Therapist&#34;** | [[paper]](https://arxiv.org/abs/2412.15242) | [code]

- [2024/12/06] **CALICO: Conversational Agent Localization via Synthetic Data Generation** | [[paper]](https://arxiv.org/abs/2412.05388) | [code]

- [2024/12/05] **Educational-Psychological Dialogue Robot Based on Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2412.03847) | [code]

- [2024/12/01] **Examining Identity Drift in Conversations of LLM Agents** | [[paper]](https://arxiv.org/abs/2412.00804) | [code]

- [2024/11/07] **Thanos: Enhancing Conversational Agents with Skill-of-Mind-Infused Large Language Model** | [[paper]](https://arxiv.org/abs/2411.04496) | [code]

- [2024/11/07] **Interactive Dialogue Agents via Reinforcement Learning on Hindsight Regenerations** | [[paper]](https://arxiv.org/abs/2411.05194) | [code]

- [2024/11/06] **MRJ-Agent: An Effective Jailbreak Agent for Multi-Round Dialogue** | [[paper]](https://arxiv.org/abs/2411.03814) | [code]

- [2024/11/01] **DARD: A Multi-Agent Approach for Task-Oriented Dialog Systems** | [[paper]](https://arxiv.org/abs/2411.00427) | [code]

- [2024/11/01] **ReSpAct: Harmonizing Reasoning, Speaking, and Acting Towards Building Large Language Model-Based Conversational AI Agents** | [[paper]](https://arxiv.org/abs/2411.00927) | [code]

- [2024/10/29] **MARCO: Multi-Agent Real-time Chat Orchestration** | [[paper]](https://arxiv.org/abs/2410.21784) | [code]

- [2024/10/25] **AGENT-CQ: Automatic Generation and Evaluation of Clarifying Questions for Conversational Search with LLMs** | [[paper]](https://arxiv.org/abs/2410.19692) | [code]

- [2024/10/18] **Coherence-Driven Multimodal Safety Dialogue with Active Learning for Embodied Agents** | [[paper]](https://arxiv.org/abs/2410.14141) | [code]

- [2024/10/15] **HR-Agent: A Task-Oriented Dialogue (TOD) LLM Agent Tailored for HR Applications** | [[paper]](https://arxiv.org/abs/2410.11239) | [code]

- [2024/10/10] **Rewriting Conversational Utterances with Instructed Large Language Models** | [[paper]](https://arxiv.org/abs/2410.07797) | [code]

- [2024/09/24] **Automated test generation to evaluate tool-augmented LLMs as conversational AI agents** | [[paper]](https://arxiv.org/abs/2409.15934) | [code]

- [2024/09/23] **Beyond Turn-Based Interfaces: Synchronous LLMs as Full-Duplex Dialogue Agents** | [[paper]](https://arxiv.org/abs/2409.15594) | [code]

- [2024/09/13] **AI-LieDar: Examine the Trade-off Between Utility and Truthfulness in LLM Agents** | [[paper]](https://arxiv.org/abs/2409.09013) | [code]

- [2024/09/06] **Sparse Rewards Can Self-Train Dialogue Agents** | [[paper]](https://arxiv.org/abs/2409.04617) | [code]

- [2024/09/02] **Co-Learning: Code Learning for Multi-Agent Reinforcement Collaborative Framework with Conversational Natural Language Interfaces** | [[paper]](https://arxiv.org/abs/2409.00985) | [code]

- [2024/08/27] **Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations** | [[paper]](https://arxiv.org/abs/2408.15232) | [code]

- [2024/08/22] **MDD-5k: A New Diagnostic Conversation Dataset for Mental Disorders Synthesized via Neuro-Symbolic LLM Agents** | [[paper]](https://arxiv.org/abs/2408.12142) | [code]

- [2024/08/13] **What should I wear to a party in a Greek taverna? Evaluation for Conversational Agents in the Fashion Domain** | [[paper]](https://arxiv.org/abs/2408.08907) | [code]

- [2024/08/06] **OpenOmni: A Collaborative Open Source Tool for Building Future-Ready Multimodal Conversational Agents** | [[paper]](https://arxiv.org/abs/2408.03047) | [code]

- [2024/08/03] **Self-Emotion Blended Dialogue Generation in Social Simulation Agents** | [[paper]](https://arxiv.org/abs/2408.01633) | [code]

- [2024/07/31] **Towards Achieving Human Parity on End-to-end Simultaneous Speech Translation via LLM Agent** | [[paper]](https://arxiv.org/abs/2407.21646) | [code]

- [2024/07/13] **Cohesive Conversations: Enhancing Authenticity in Multi-Agent Simulated Dialogues** | [[paper]](https://arxiv.org/abs/2407.09897) | [code]

- [2024/07/04] **Controllable Conversations: Planning-Based Dialogue Agent with Large Language Models** | [[paper]](https://arxiv.org/abs/2407.03884) | [code]

- [2024/07/01] **Empathic Grounding: Explorations using Multimodal Interaction and Large Language Models with Conversational Agents** | [[paper]](https://arxiv.org/abs/2407.01824) | [code]

- [2024/06/30] **CAMON: Cooperative Agents for Multi-Object Navigation with LLM-based Conversations** | [[paper]](https://arxiv.org/abs/2407.00632) | [code]

- [2024/06/09] **Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions** | [[paper]](https://arxiv.org/abs/2406.05688) | [[code]](https://github.com/chengtan9907/reviewmt)

- [2024/05/29] **Toward Conversational Agents with Context and Time Sensitive Long-term Memory** | [[paper]](https://arxiv.org/abs/2406.00057) | [[code]](https://github.com/Zyphra/TemporalMemoryDataset)

- [2024/05/16] **Speaker Verification in Agent-Generated Conversations** | [[paper]](https://arxiv.org/abs/2405.10150) | [code]

- [2024/04/19] **Towards Human-centered Proactive Conversational Agents** | [[paper]](https://arxiv.org/abs/2404.12670) | [code]

- [2024/04/10] **Apollonion: Profile-centric Dialog Agent** | [[paper]](https://arxiv.org/abs/2404.08692) | [code]

- [2024/03/17] **Improving Dialogue Agents by Decomposing One Global Explicit Annotation with Local Implicit Multimodal Feedback** | [[paper]](https://arxiv.org/abs/2403.11330) | [code]

- [2024/03/08] **ChatASU: Evoking LLM&#39;s Reflexion to Truly Understand Aspect Sentiment in Dialogues** | [[paper]](https://arxiv.org/abs/2403.05326) | [code]

- [2024/02/25] **Understanding Public Perceptions of AI Conversational Agents: A Cross-Cultural Analysis** | [[paper]](https://arxiv.org/abs/2402.16039) | [code]

- [2024/02/23] **On the Multi-turn Instruction Following for Conversational Web Agents** | [[paper]](https://arxiv.org/abs/2402.15057) | [code]

- [2024/02/20] **CHATATC: Large Language Model-Driven Conversational Agents for Supporting Strategic Air Traffic Flow Management** | [[paper]](https://arxiv.org/abs/2402.14850) | [code]

- [2024/01/29] **Assistive Large Language Model Agents for Socially-Aware Negotiation Dialogues** | [[paper]](https://arxiv.org/abs/2402.01737) | [code]

- [2024/01/10] **Bootstrapping LLM-based Task-Oriented Dialogue Agents via Self-Talk** | [[paper]](https://arxiv.org/abs/2401.05033) | [code]

- [2024/01/02] **CharacterEval: A Chinese Benchmark for Role-Playing Conversational Agent Evaluation** | [[paper]](https://arxiv.org/abs/2401.01275) | [code]

- [2023/12/21] **Team Flow at DRC2023: Building Common Ground and Text-based Turn-taking in a Travel Agent Spoken Dialogue System** | [[paper]](https://arxiv.org/abs/2312.13816) | [code]

- [2023/11/15] **ToolTalk: Evaluating Tool-Usage in a Conversational Setting** | [[paper]](https://arxiv.org/abs/2311.10775) | [code]

- [2023/10/01] **Adapting LLM Agents Through Communication** | [[paper]](https://arxiv.org/abs/2310.01444v2) | [code]

- [2023/06/28] **Inferring the Goals of Communicating Agents from Actions and Instructions** | [[paper]](https://arxiv.org/abs/2306.16207) | [code]

- [2023/04/26] **Multi-Party Chat: Conversational Agents in Group Settings with Humans and Models** | [[paper]](https://arxiv.org/abs/2304.13835) | [code]

- [2023/03/31] **CAMEL: Communicative Agents for &#34;Mind&#34; Exploration of Large Language Model Society** | [[paper]](https://arxiv.org/abs/2303.17760) | [[code]](https://github.com/camel-ai/camel)

#### Game Playing
- [2025/06/30] **SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2506.24119) | [code]

- [2025/06/05] **Time to Talk: LLM Agents for Asynchronous Group Communication in Mafia Games** | [[paper]](https://arxiv.org/abs/2506.05309) | [code]

- [2025/06/04] **TextAtari: 100K Frames Game Playing with Language Agents** | [[paper]](https://arxiv.org/abs/2506.04098) | [code]

- [2025/05/29] **The Automated but Risky Game: Modeling Agent-to-Agent Negotiations and Transactions in Consumer Markets** | [[paper]](https://arxiv.org/abs/2506.00073) | [code]

- [2025/05/28] **First Steps Towards Overhearing LLM Agents: A Case Study With Dungeons &amp; Dragons Gameplay** | [[paper]](https://arxiv.org/abs/2505.22809) | [code]

- [2025/05/25] **When Ethics and Payoffs Diverge: LLM Agents in Morally Charged Social Dilemmas** | [[paper]](https://arxiv.org/abs/2505.19212) | [code]

- [2025/05/23] **CoMet: Metaphor-Driven Covert Communication for Multi-Agent Language Games** | [[paper]](https://arxiv.org/abs/2505.18218) | [code]

- [2025/05/20] **BAR: A Backward Reasoning based Agent for Complex Minecraft Tasks** | [[paper]](https://arxiv.org/abs/2505.14079) | [code]

- [2025/04/23] **Monte Carlo Planning with Large Language Model for Text-Based Game Agents** | [[paper]](https://arxiv.org/abs/2504.16855) | [code]

- [2025/04/15] **TextArena** | [[paper]](https://arxiv.org/abs/2504.11442) | [code]

- [2025/04/09] **Persona Dynamics: Unveiling the Impact of Personality Traits on Agents in Text-Based Games** | [[paper]](https://arxiv.org/abs/2504.06868) | [code]

- [2025/03/08] **DSGBench: A Diverse Strategic Game Benchmark for Evaluating LLM-based Agents in Complex Decision-Making Environments** | [[paper]](https://arxiv.org/abs/2503.06047) | [code]

- [2025/03/06] **VQEL: Enabling Self-Developed Symbolic Language in Agents through Vector Quantization in Emergent Language Games** | [[paper]](https://arxiv.org/abs/2503.04940) | [code]

- [2025/03/06] **Factorio Learning Environment** | [[paper]](https://arxiv.org/abs/2503.09617) | [code]

- [2025/02/05] **Multimodal Transformer Models for Turn-taking Prediction: Effects on Conversational Dynamics of Human-Agent Interaction during Cooperative Gameplay** | [[paper]](https://arxiv.org/abs/2503.16432) | [code]

- [2025/02/01] **Who&#39;s the MVP? A Game-Theoretic Evaluation Benchmark for Modular Attribution in LLM Agents** | [[paper]](https://arxiv.org/abs/2502.00510) | [code]

- [2025/01/24] **Multi-agent KTO: Reinforcing Strategic Interactions of Large Language Model in Language Game** | [[paper]](https://arxiv.org/abs/2501.14225) | [code]

- [2024/12/06] **TeamCraft: A Benchmark for Multi-Modal Multi-Agent Systems in Minecraft** | [[paper]](https://arxiv.org/abs/2412.05255) | [code]

- [2024/11/08] **Game-theoretic LLM: Agent Workflow for Negotiation Games** | [[paper]](https://arxiv.org/abs/2411.05990) | [code]

- [2024/10/28] **Can Machines Think Like Humans? A Behavioral Evaluation of LLM-Agents in Dictator Games** | [[paper]](https://arxiv.org/abs/2410.21359) | [code]

- [2024/09/03] **An Implementation of Werewolf Agent That does not Truly Trust LLMs** | [[paper]](https://arxiv.org/abs/2409.01575) | [code]

- [2024/08/05] **Evaluating and Enhancing LLMs Agent based on Theory of Mind in Guandan: A Multi-Player Cooperative Game under Imperfect Information** | [[paper]](https://arxiv.org/abs/2408.02559) | [code]

- [2024/07/23] **AMONGAGENTS: Evaluating Large Language Models in the Interactive Text-Based Social Deduction Game** | [[paper]](https://arxiv.org/abs/2407.16521) | [code]

- [2024/07/17] **A LLM Benchmark based on the Minecraft Builder Dialog Agent Task** | [[paper]](https://arxiv.org/abs/2407.12734) | [code]

- [2024/06/27] **OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents** | [[paper]](https://arxiv.org/abs/2407.00114) | [code]

- [2024/06/07] **GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents** | [[paper]](https://arxiv.org/abs/2406.06613) | [[code]](https://github.com/Joshuaclymer/GameBench)

- [2024/06/05] **The Good, the Bad, and the Hulk-like GPT: Analyzing Emotional Decisions of Large Language Models in Cooperation and Bargaining Games** | [[paper]](https://arxiv.org/abs/2406.03299) | [code]

- [2024/05/24] **Hacc-Man: An Arcade Game for Jailbreaking LLMs** | [[paper]](https://arxiv.org/abs/2405.15902) | [code]

- [2024/05/23] **Human-Agent Cooperation in Games under Incomplete Information through Natural Language Communication** | [[paper]](https://arxiv.org/abs/2405.14173) | [code]

- [2024/05/08] **LLMs with Personalities in Multi-issue Negotiation Games** | [[paper]](https://arxiv.org/abs/2405.05248) | [code]

- [2024/04/30] **PANGeA: Procedural Artificial Narrative using Generative AI for Turn-Based Video Games** | [[paper]](https://arxiv.org/abs/2404.19721) | [code]

- [2024/04/03] **Learn to Disguise: Avoid Refusal Responses in LLM&#39;s Defense via a Multi-agent Attacker-Disguiser Game** | [[paper]](https://arxiv.org/abs/2404.02532) | [code]

- [2024/03/28] **MineLand: Simulating Large-Scale Multi-Agent Interactions with Limited Multimodal Senses and Physical Needs** | [[paper]](https://arxiv.org/abs/2403.19267) | [[code]](https://github.com/cocacola-lab/mineland)

- [2024/03/18] **How Far Are We on the Decision-Making of LLMs? Evaluating LLMs&#39; Gaming Ability in Multi-Agent Environments** | [[paper]](https://arxiv.org/abs/2403.11807) | [code]

- [2024/02/19] **PsychoGAT: A Novel Psychological Measurement Paradigm through Interactive Fiction Games with LLM Agents** | [[paper]](https://arxiv.org/abs/2402.12326) | [code]

- [2024/02/13] **Large Language Models as Minecraft Agents** | [[paper]](https://arxiv.org/abs/2402.08392) | [code]

- [2024/02/12] **Large Language Models as Agents in Two-Player Games** | [[paper]](https://arxiv.org/abs/2402.08078) | [code]

- [2024/02/04] **Enhance Reasoning for Large Language Models in the Game Werewolf** | [[paper]](https://arxiv.org/abs/2402.02330) | [code]

- [2024/02/02] **PokeLLMon: A Human-Parity Agent for Pokemon Battles with Large Language Models** | [[paper]](https://arxiv.org/abs/2402.01118) | [code]

- [2023/12/29] **Cooperation on the Fly: Exploring Language Agents for Ad Hoc Teamwork in the Avalon Game** | [[paper]](https://arxiv.org/abs/2312.17515) | [code]

- [2023/12/01] **Deciphering Digital Detectives: Understanding LLM Behaviors and Capabilities in Multi-Agent Mystery Games** | [[paper]](https://arxiv.org/abs/2312.00746) | [code]

- [2023/10/31] **Leveraging Word Guessing Games to Assess the Intelligence of Large Language Models** | [[paper]](https://arxiv.org/abs/2310.20499) | [code]

- [2023/09/29] **Suspicion-Agent: Playing Imperfect Information Games with Theory of Mind Aware GPT-4** | [[paper]](https://arxiv.org/abs/2309.17277) | [code]

- [2023/09/18] **MindAgent: Emergent Gaming Interaction** | [[paper]](https://arxiv.org/abs/2309.09971) | [[code]](https://mindagent.github.io/)

- [2023/09/10] **An Appraisal-Based Chain-Of-Emotion Architecture for Affective Language Model Game Agents** | [[paper]](https://arxiv.org/abs/2309.05076) | [code]

- [2023/09/09] **Exploring Large Language Models for Communication Games: An Empirical Study on Werewolf** | [[paper]](https://arxiv.org/abs/2309.04658) | [code]

- [2023/08/23] **Are ChatGPT and GPT-4 Good Poker Players? -- A Pre-Flop Analysis** | [[paper]](https://arxiv.org/abs/2308.12466) | [code]

- [2023/05/31] **Recursive Metropolis-Hastings Naming Game: Symbol Emergence in a Multi-agent System based on Probabilistic Generative Models** | [[paper]](https://arxiv.org/abs/2305.19761) | [code]

- [2023/05/26] **Playing repeated games with Large Language Models** | [[paper]](https://arxiv.org/abs/2305.16867) | [code]

- [2023/05/25] **Ghost in the Minecraft: Generally Capable Agents for Open-World Environments via Large Language Models with Text-based Knowledge and Memory** | [[paper]](https://arxiv.org/abs/2305.17144) | [code]

- [2023/05/08] **Knowledge-enhanced Agents for Interactive Text Games** | [[paper]](https://arxiv.org/abs/2305.05091) | [code]

- [2023/04/06] **Can Large Language Models Play Text Games Well? Current State-of-the-Art and Open Questions** | [[paper]](https://arxiv.org/abs/2304.02868) | [code]

#### Human-Agent Interaction
- [2025/06/11] **A Call for Collaborative Intelligence: Why Human-Agent Systems Should Precede AI Autonomy** | [[paper]](https://arxiv.org/abs/2506.09420) | [code]

- [2025/05/16] **Talk to Your Slides: Language-Driven Agents for Efficient Slide Editing** | [[paper]](https://arxiv.org/abs/2505.11604) | [code]

- [2025/03/26] **TAMA: A Human-AI Collaborative Thematic Analysis Framework Using Multi-Agent LLMs for Clinical Interviews** | [[paper]](https://arxiv.org/abs/2503.20666) | [code]

- [2025/02/17] **Leveraging Dual Process Theory in Language Agent Framework for Real-time Simultaneous Human-AI Collaboration** | [[paper]](https://arxiv.org/abs/2502.11882) | [code]

- [2025/02/05] **Multimodal Transformer Models for Turn-taking Prediction: Effects on Conversational Dynamics of Human-Agent Interaction during Cooperative Gameplay** | [[paper]](https://arxiv.org/abs/2503.16432) | [code]

- [2025/01/28] **CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation** | [[paper]](https://arxiv.org/abs/2501.16609) | [code]

- [2024/12/20] **Collaborative Gym: A Framework for Enabling and Evaluating Human-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2412.15701) | [code]

- [2024/06/28] **Designing and Evaluating Multi-Chatbot Interface for Human-AI Communication: Preliminary Findings from a Persuasion Task** | [[paper]](https://arxiv.org/abs/2406.19648) | [code]

- [2024/06/11] **Towards Human-AI Collaboration in Healthcare: Guided Deferral Systems with Large Language Models** | [[paper]](https://arxiv.org/abs/2406.07212) | [code]

- [2024/06/02] **Towards a copilot in BIM authoring tool using a large language model-based agent for intelligent human-machine interaction** | [[paper]](https://arxiv.org/abs/2406.16903) | [code]

- [2024/03/05] **ChatCite: LLM Agent with Human Workflow Guidance for Comparative Literature Summary** | [[paper]](https://arxiv.org/abs/2403.02574) | [code]

- [2024/02/20] **Large Language Model-based Human-Agent Collaboration for Complex Task Solving** | [[paper]](https://arxiv.org/abs/2402.12914) | [code]

- [2024/02/18] **Shaping Human-AI Collaboration: Varied Scaffolding Levels in Co-writing with Language Models** | [[paper]](https://arxiv.org/abs/2402.11723) | [code]

- [2024/02/17] **MONAL: Model Autophagy Analysis for Modeling Human-AI Interactions** | [[paper]](https://arxiv.org/abs/2402.11271) | [code]

- [2023/09/22] **Learning to Coordinate with Anyone** | [[paper]](https://arxiv.org/abs/2309.12633) | [code]

- [2023/07/31] **HAGRID: A Human-LLM Collaborative Dataset for Generative Information-Seeking with Attribution** | [[paper]](https://arxiv.org/abs/2307.16883) | [code]

- [2023/04/26] **Multi-Party Chat: Conversational Agents in Group Settings with Humans and Models** | [[paper]](https://arxiv.org/abs/2304.13835) | [code]

#### Tool Usage
- [2025/07/10] **PyVision: Agentic Vision with Dynamic Tooling** | [[paper]](https://arxiv.org/abs/2507.07998) | [code]

- [2025/07/09] **VisualTrap: A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation** | [[paper]](https://arxiv.org/abs/2507.06899) | [code]

- [2025/07/03] **WebSailor: Navigating Super-human Reasoning for Web Agent** | [[paper]](https://arxiv.org/abs/2507.02592) | [code]

- [2025/07/02] **OpenTable-R1: A Reinforcement Learning Augmented Tool Agent for Open-Domain Table Question Answering** | [[paper]](https://arxiv.org/abs/2507.03018) | [code]

- [2025/06/30] **LineRetriever: Planning-Aware Observation Reduction for Web Agents** | [[paper]](https://arxiv.org/abs/2507.00210) | [code]

- [2025/06/27] **More Vulnerable than You Think: On the Stability of Tool-Integrated LLM Agents** | [[paper]](https://arxiv.org/abs/2506.21967) | [code]

- [2025/06/24] **Doc2Agent: Scalable Generation of Tool-Using Agents from API Documentation** | [[paper]](https://arxiv.org/abs/2506.19998) | [code]

- [2025/06/24] **NaviAgent: Bilevel Planning on Tool Dependency Graphs for Function Calling** | [[paper]](https://arxiv.org/abs/2506.19500) | [code]

- [2025/06/18] **Understanding GUI Agent Localization Biases through Logit Sharpness** | [[paper]](https://arxiv.org/abs/2506.15425) | [code]

- [2025/06/18] **Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence** | [[paper]](https://arxiv.org/abs/2506.15677) | [code]

- [2025/06/17] **AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents** | [[paper]](https://arxiv.org/abs/2506.14205) | [code]

- [2025/06/12] **VideoDeepResearch: Long Video Understanding With Agentic Tool Using** | [[paper]](https://arxiv.org/abs/2506.10821) | [code]

- [2025/06/12] **Build the web for agents, not agents for the web** | [[paper]](https://arxiv.org/abs/2506.10953) | [code]

- [2025/06/10] **Atomic-to-Compositional Generalization for Mobile Agents with A New Benchmark and Scheduling System** | [[paper]](https://arxiv.org/abs/2506.08972) | [code]

- [2025/06/10] **GUIRoboTron-Speech: Towards Automated GUI Agents Based on Speech Instructions** | [[paper]](https://arxiv.org/abs/2506.11127) | [code]

- [2025/06/09] **CheMatAgent: Enhancing LLMs for Chemistry and Materials Science through Tree-Search Based Tool Learning** | [[paper]](https://arxiv.org/abs/2506.07551) | [code]

- [2025/06/04] **Go-Browse: Training Web Agents with Structured Exploration** | [[paper]](https://arxiv.org/abs/2506.03533) | [code]

- [2025/06/03] **GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents** | [[paper]](https://arxiv.org/abs/2506.03143) | [code]

- [2025/06/02] **AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning** | [[paper]](https://arxiv.org/abs/2506.01391) | [code]

- [2025/05/30] **MedOrch: Medical Diagnosis with Tool-Augmented Reasoning Agents for Flexible Extensibility** | [[paper]](https://arxiv.org/abs/2506.00235) | [code]

- [2025/05/28] **RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments** | [[paper]](https://arxiv.org/abs/2505.21936) | [code]

- [2025/05/28] **EvolveSearch: An Iterative Self-Evolving Search Agent** | [[paper]](https://arxiv.org/abs/2505.22501) | [code]

- [2025/05/28] **UI-Evol: Automatic Knowledge Evolving for Computer Use Agents** | [[paper]](https://arxiv.org/abs/2505.21964) | [code]

- [2025/05/28] **WebDancer: Towards Autonomous Information Seeking Agency** | [[paper]](https://arxiv.org/abs/2505.22648) | [[code]](https://github.com/Alibaba-NLP/WebAgent)

- [2025/05/27] **BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism** | [[paper]](https://arxiv.org/abs/2505.20660) | [code]

- [2025/05/27] **UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents** | [[paper]](https://arxiv.org/abs/2505.21496) | [code]

- [2025/05/27] **ChemHAS: Hierarchical Agent Stacking for Enhancing Chemistry Tools** | [[paper]](https://arxiv.org/abs/2505.21569) | [code]

- [2025/05/26] **T^2Agent A Tool-augmented Multimodal Misinformation Detection Agent with Monte Carlo Tree Search** | [[paper]](https://arxiv.org/abs/2505.19768) | [code]

- [2025/05/26] **WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback** | [[paper]](https://arxiv.org/abs/2505.20013) | [code]

- [2025/05/23] **Deep Video Discovery: Agentic Search with Tool Use for Long-form Video Understanding** | [[paper]](https://arxiv.org/abs/2505.18079) | [code]

- [2025/05/23] **ProgRM: Build Better GUI Agents with Progress Rewards** | [[paper]](https://arxiv.org/abs/2505.18121) | [code]

- [2025/05/23] **Gaming Tool Preferences in Agentic LLMs** | [[paper]](https://arxiv.org/abs/2505.18135) | [code]

- [2025/05/22] **WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2505.16421) | [code]

- [2025/05/22] **T1: A Tool-Oriented Conversational Dataset for Multi-Turn Agentic Planning** | [[paper]](https://arxiv.org/abs/2505.16986) | [code]

- [2025/05/21] **Web-Shepherd: Advancing PRMs for Reinforcing Web Agents** | [[paper]](https://arxiv.org/abs/2505.15277) | [code]

- [2025/05/21] **X-WebAgentBench: A Multilingual Interactive Web Benchmark for Evaluating Global Agentic System** | [[paper]](https://arxiv.org/abs/2505.15372) | [code]

- [2025/05/21] **GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents** | [[paper]](https://arxiv.org/abs/2505.15810) | [code]

- [2025/05/21] **AgentThink: A Unified Framework for Tool-Augmented Chain-of-Thought Reasoning in Vision-Language Models for Autonomous Driving** | [[paper]](https://arxiv.org/abs/2505.15298) | [code]

- [2025/05/20] **Mobile-Agent-V: A Video-Guided Approach for Effortless and Efficient Operational Knowledge Injection in Mobile Automation** | [[paper]](https://arxiv.org/abs/2505.13887) | [code]

- [2025/05/20] **Efficient Agent Training for Computer Use** | [[paper]](https://arxiv.org/abs/2505.13909) | [code]

- [2025/05/20] **s3: You Don&#39;t Need That Much Data to Train a Search Agent via RL** | [[paper]](https://arxiv.org/abs/2505.14146) | [code]

- [2025/05/19] **GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection in GUI Agents** | [[paper]](https://arxiv.org/abs/2505.12842) | [code]

- [2025/05/18] **Enhance Mobile Agents Thinking Process Via Iterative Preference Learning** | [[paper]](https://arxiv.org/abs/2505.12299) | [code]

- [2025/05/17] **Demystifying and Enhancing the Efficiency of Large Language Model Based Search Agents** | [[paper]](https://arxiv.org/abs/2505.12065) | [code]

- [2025/05/16] **EnvInjection: Environmental Prompt Injection Attack to Multi-modal Web Agents** | [[paper]](https://arxiv.org/abs/2505.11717) | [code]

- [2025/05/09] **ScaleMCP: Dynamic and Auto-Synchronizing Model Context Protocol Tools for LLM Agents** | [[paper]](https://arxiv.org/abs/2505.06416) | [code]

- [2025/04/28] **MICE for CATs: Model-Internal Confidence Estimation for Calibrating Agents with Tools** | [[paper]](https://arxiv.org/abs/2504.20168) | [code]

- [2025/04/27] **AndroidGen: Building an Android Language Agent under Data Scarcity** | [[paper]](https://arxiv.org/abs/2504.19298) | [code]

- [2025/04/24] **Toward a Human-Centered Evaluation Framework for Trustworthy LLM-Powered GUI Agents** | [[paper]](https://arxiv.org/abs/2504.17934) | [code]

- [2025/04/23] **WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model** | [[paper]](https://arxiv.org/abs/2504.21024) | [code]

- [2025/04/22] **Guiding VLM Agents with Process Rewards at Inference Time for GUI Navigation** | [[paper]](https://arxiv.org/abs/2504.16073) | [code]

- [2025/04/19] **InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners** | [[paper]](https://arxiv.org/abs/2504.14239) | [code]

- [2025/04/17] **WebLists: Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents** | [[paper]](https://arxiv.org/abs/2504.12682) | [code]

- [2025/04/16] **Enhancing Web Agents with Explicit Rollback Mechanisms** | [[paper]](https://arxiv.org/abs/2504.11788) | [code]

- [2025/04/15] **The Obvious Invisible Threat: LLM-Powered GUI Agents&#39; Vulnerability to Fine-Print Injections** | [[paper]](https://arxiv.org/abs/2504.11281) | [code]

- [2025/04/14] **Breaking the Data Barrier -- Building GUI Agents Through Task Generalization** | [[paper]](https://arxiv.org/abs/2504.10127) | [code]

- [2025/04/14] **GUI-R1 : A Generalist R1-Style Vision-Language Action Model For GUI Agents** | [[paper]](https://arxiv.org/abs/2504.10458) | [code]

- [2025/04/09] **Inducing Programmatic Skills for Agentic Tasks** | [[paper]](https://arxiv.org/abs/2504.06821) | [code]

- [2025/04/09] **SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills** | [[paper]](https://arxiv.org/abs/2504.07079) | [code]

- [2025/04/02] **An Illusion of Progress? Assessing the Current State of Web Agents** | [[paper]](https://arxiv.org/abs/2504.01382) | [code]

- [2025/04/01] **On the Robustness of Agentic Function Calling** | [[paper]](https://arxiv.org/abs/2504.00914) | [code]

- [2025/04/01] **Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents** | [[paper]](https://arxiv.org/abs/2504.00906) | [code]

- [2025/03/26] **Open Deep Search: Democratizing Search with Open-source Reasoning Agents** | [[paper]](https://arxiv.org/abs/2503.20201) | [code]

- [2025/03/24] **Safeguarding Mobile GUI Agent via Logic-based Action Verification** | [[paper]](https://arxiv.org/abs/2503.18492) | [code]

- [2025/03/18] **PLAY2PROMPT: Zero-shot Tool Instruction Optimization for LLM Agents via Tool Play** | [[paper]](https://arxiv.org/abs/2503.14432) | [code]

- [2025/03/14] **DeskVision: Large Scale Desktop Region Captioning for Advanced GUI Agents** | [[paper]](https://arxiv.org/abs/2503.11170) | [code]

- [2025/03/12] **Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents** | [[paper]](https://arxiv.org/abs/2503.10689) | [code]

- [2025/03/10] **BEARCUBS: A benchmark for computer-using web agents** | [[paper]](https://arxiv.org/abs/2503.07919) | [code]

- [2025/03/06] **Measuring temporal effects of agent knowledge by date-controlled tool use** | [[paper]](https://arxiv.org/abs/2503.04188) | [code]

- [2025/03/06] **SafeArena: Evaluating the Safety of Autonomous Web Agents** | [[paper]](https://arxiv.org/abs/2503.04957) | [code]

- [2025/03/04] **LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications** | [[paper]](https://arxiv.org/abs/2503.02950) | [code]

- [2025/03/01] **Smoothing Grounding and Reasoning for MLLM-Powered GUI Agents with Query-Oriented Pivot Tasks** | [[paper]](https://arxiv.org/abs/2503.00401) | [code]

- [2025/02/27] **Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis** | [[paper]](https://arxiv.org/abs/2502.20383) | [code]

- [2025/02/24] **MobileSteward: Integrating Multiple App-Oriented Agents with Self-Evolution to Automate Cross-App Instructions** | [[paper]](https://arxiv.org/abs/2502.16796) | [code]

- [2025/02/24] **Mobile-Agent-V: Learning Mobile Device Operation Through Video-Guided Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2502.17110) | [[code]](https://github.com/X-PLUG/MobileAgent)

- [2025/02/17] **LLM Agents Making Agent Tools** | [[paper]](https://arxiv.org/abs/2502.11705) | [code]

- [2025/02/17] **SMART: Self-Aware Agent for Tool Overuse Mitigation** | [[paper]](https://arxiv.org/abs/2502.11435) | [code]

- [2025/02/16] **OctoTools: An Agentic Framework with Extensible Tools for Complex Reasoning** | [[paper]](https://arxiv.org/abs/2502.11271) | [code]

- [2025/02/12] **Can a Single Model Master Both Multi-turn Conversations and Tool Use? CoALM: A Unified Conversational Agentic Language Model** | [[paper]](https://arxiv.org/abs/2502.08820) | [code]

- [2025/02/07] **Agentic Reasoning: Reasoning LLMs with Tools for the Deep Research** | [[paper]](https://arxiv.org/abs/2502.04644) | [code]

- [2025/02/06] **Division-of-Thoughts: Harnessing Hybrid Language Model Synergy for Efficient On-Device Agents** | [[paper]](https://arxiv.org/abs/2502.04392) | [code]

- [2025/02/05] **ReachAgent: Enhancing Mobile Agent via Page Reaching and Operation** | [[paper]](https://arxiv.org/abs/2502.02955) | [code]

- [2025/01/28] **CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation** | [[paper]](https://arxiv.org/abs/2501.16609) | [code]

- [2025/01/21] **UI-TARS: Pioneering Automated GUI Interaction with Native Agents** | [[paper]](https://arxiv.org/abs/2501.12326) | [code]

- [2025/01/20] **Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks** | [[paper]](https://arxiv.org/abs/2501.11733) | [code]

- [2025/01/20] **PlotEdit: Natural Language-Driven Accessible Chart Editing in PDFs via Multimodal LLM Agents** | [[paper]](https://arxiv.org/abs/2501.11233) | [code]

- [2025/01/08] **InfiGUIAgent: A Multimodal Generalist GUI Agent with Native Reasoning and Reflection** | [[paper]](https://arxiv.org/abs/2501.04575) | [code]

- [2025/01/08] **FinSphere: A Conversational Stock Analysis Agent Equipped with Quantitative Tools based on Real-Time Database** | [[paper]](https://arxiv.org/abs/2501.12399) | [code]

- [2025/01/07] **PPTAgent: Generating and Evaluating Presentations Beyond Text-to-Slides** | [[paper]](https://arxiv.org/abs/2501.03936) | [code]

- [2024/12/28] **Efficient Multi-Agent Collaboration with Tool Use for Online Planning in Complex Table Question Answering** | [[paper]](https://arxiv.org/abs/2412.20145) | [code]

- [2024/12/21] **InfoTech Assistant : A Multimodal Conversational Agent for InfoTechnology Web Portal Queries** | [[paper]](https://arxiv.org/abs/2412.16412) | [code]

- [2024/12/12] **AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials** | [[paper]](https://arxiv.org/abs/2412.09605) | [code]

- [2024/12/08] **Cooperative SQL Generation for Segmented Databases By Using Multi-functional LLM Agents** | [[paper]](https://arxiv.org/abs/2412.05850) | [code]

- [2024/12/05] **Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction** | [[paper]](https://arxiv.org/abs/2412.04454) | [code]

- [2024/11/26] **ShowUI: One Vision-Language-Action Model for GUI Visual Agent** | [[paper]](https://arxiv.org/abs/2411.17465) | [code]

- [2024/11/22] **ScribeAgent: Towards Specialized Web Agents Using Production-Scale Workflow Data** | [[paper]](https://arxiv.org/abs/2411.15004) | [code]

- [2024/11/20] **AdaptAgent: Adapting Multimodal Web Agents with Few-Shot Learning from Human Demonstrations** | [[paper]](https://arxiv.org/abs/2411.13451) | [code]

- [2024/11/15] **The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use** | [[paper]](https://arxiv.org/abs/2411.10323) | [code]

- [2024/11/04] **WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2411.02337) | [code]

- [2024/11/04] **Attacking Vision-Language Computer Agents via Pop-ups** | [[paper]](https://arxiv.org/abs/2411.02391) | [code]

- [2024/11/02] **Infant Agent: A Tool-Integrated, Logic-Driven Agent with Cost-Effective API Usage** | [[paper]](https://arxiv.org/abs/2411.01114) | [code]

- [2024/10/28] **AutoGLM: Autonomous Foundation Agents for GUIs** | [[paper]](https://arxiv.org/abs/2411.00820) | [code]

- [2024/10/25] **OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization** | [[paper]](https://arxiv.org/abs/2410.19609) | [code]

- [2024/10/24] **Infogent: An Agent-Based Framework for Web Information Aggregation** | [[paper]](https://arxiv.org/abs/2410.19054) | [code]

- [2024/10/23] **ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents** | [[paper]](https://arxiv.org/abs/2410.17657) | [code]

- [2024/10/22] **Large Language Models Empowered Personalized Web Agents** | [[paper]](https://arxiv.org/abs/2410.17236) | [code]

- [2024/10/21] **VipAct: Visual-Perception Enhancement via Specialized VLM Agent Collaboration and Tool-use** | [[paper]](https://arxiv.org/abs/2410.16400) | [code]

- [2024/10/21] **Beyond Browsing: API-Based Web Agents** | [[paper]](https://arxiv.org/abs/2410.16464) | [code]

- [2024/10/18] **Toolshed: Scale Tool-Equipped Agents with Advanced RAG-Tool Fusion and Tool Knowledge Bases** | [[paper]](https://arxiv.org/abs/2410.14594) | [code]

- [2024/10/17] **Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation** | [[paper]](https://arxiv.org/abs/2410.13232) | [code]

- [2024/10/17] **MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling** | [[paper]](https://arxiv.org/abs/2410.13610) | [code]

- [2024/10/17] **MobA: A Two-Level Agent System for Efficient Mobile Task Automation** | [[paper]](https://arxiv.org/abs/2410.13757) | [code]

- [2024/10/17] **AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents** | [[paper]](https://arxiv.org/abs/2410.13825) | [code]

- [2024/10/16] **Agent Skill Acquisition for Large Language Models via CycleQD** | [[paper]](https://arxiv.org/abs/2410.14735) | [code]

- [2024/10/10] **Agent S: An Open Agentic Framework that Uses Computers Like a Human** | [[paper]](https://arxiv.org/abs/2410.08164) | [code]

- [2024/10/07] **Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents** | [[paper]](https://arxiv.org/abs/2410.05243) | [code]

- [2024/10/03] **NNetNav: Unsupervised Learning of Browser Agents Through Environment Interaction in the Wild** | [[paper]](https://arxiv.org/abs/2410.02907) | [code]

- [2024/09/24] **Automated test generation to evaluate tool-augmented LLMs as conversational AI agents** | [[paper]](https://arxiv.org/abs/2409.15934) | [code]

- [2024/09/17] **EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage** | [[paper]](https://arxiv.org/abs/2409.11295) | [code]

- [2024/09/01] **TinyAgent: Function Calling at the Edge** | [[paper]](https://arxiv.org/abs/2409.00608) | [code]

- [2024/08/30] **Tool-Assisted Agent on SQL Inspection and Refinement in Real-World Scenarios** | [[paper]](https://arxiv.org/abs/2408.16991) | [code]

- [2024/08/15] **VerilogCoder: Autonomous Verilog Coding Agents with Graph-based Planning and Abstract Syntax Tree (AST)-based Waveform Tracing Tool** | [[paper]](https://arxiv.org/abs/2408.08927) | [code]

- [2024/08/05] **Caution for the Environment: Multimodal Agents are Susceptible to Environmental Distractions** | [[paper]](https://arxiv.org/abs/2408.02544) | [code]

- [2024/08/01] **OmniParser for Pure Vision Based GUI Agent** | [[paper]](https://arxiv.org/abs/2408.00203) | [code]

- [2024/07/26] **AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents** | [[paper]](https://arxiv.org/abs/2407.18901) | [[code]](https://github.com/stonybrooknlp/appworld)

- [2024/07/22] **AssistantBench: Can Web Agents Solve Realistic and Time-Consuming Tasks?** | [[paper]](https://arxiv.org/abs/2407.15711) | [code]

- [2024/07/11] **GTA: A Benchmark for General Tool Agents** | [[paper]](https://arxiv.org/abs/2407.08713) | [code]

- [2024/07/01] **Mobile-Bench: An Evaluation Benchmark for LLM-based Mobile Agents** | [[paper]](https://arxiv.org/abs/2407.00993) | [code]

- [2024/06/17] **GUICourse: From General Vision Language Models to Versatile GUI Agents** | [[paper]](https://arxiv.org/abs/2406.11317) | [[code]](https://github.com/yiye3/guicourse)

- [2024/06/16] **GUI-WORLD: A Dataset for GUI-oriented Multimodal LLM-based Agents** | [[paper]](https://arxiv.org/abs/2406.10819) | [code]

- [2024/06/06] **Tool-Planner: Task Planning with Clusters across Multiple Tools** | [[paper]](https://arxiv.org/abs/2406.03807) | [[code]](https://github.com/OceannTwT/Tool-Planner)

- [2024/06/03] **Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2406.01014) | [[code]](https://github.com/x-plug/mobileagent)

- [2024/06/02] **Towards a copilot in BIM authoring tool using a large language model-based agent for intelligent human-machine interaction** | [[paper]](https://arxiv.org/abs/2406.16903) | [code]

- [2024/05/30] **Large Language Models Can Self-Improve At Web Agent Tasks** | [[paper]](https://arxiv.org/abs/2405.20309) | [code]

- [2024/05/17] **Latent State Estimation Helps UI Agents to Reason** | [[paper]](https://arxiv.org/abs/2405.11120) | [code]

- [2024/05/06] **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering** | [[paper]](https://arxiv.org/abs/2405.15793) | [code]

- [2024/05/02] **CACTUS: Chemistry Agent Connecting Tool-Usage to Science** | [[paper]](https://arxiv.org/abs/2405.00972) | [[code]](https://github.com/pnnl/cactus)

- [2024/05/01] **Navigating WebAI: Training Agents to Complete Web Tasks with Large Language Models and Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2405.00516) | [code]

- [2024/04/23] **Evaluating Tool-Augmented Agents in Remote Sensing Platforms** | [[paper]](https://arxiv.org/abs/2405.00709) | [code]

- [2024/04/17] **The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey** | [[paper]](https://arxiv.org/abs/2404.11584) | [code]

- [2024/04/17] **Octopus v3: Technical Report for On-device Sub-billion Multimodal AI Agent** | [[paper]](https://arxiv.org/abs/2404.11459) | [code]

- [2024/04/16] **Grounded Language Agent for Product Search via Intelligent Web Interactions** | [[paper]](https://arxiv.org/abs/2404.10887) | [code]

- [2024/04/04] **AutoWebGLM: A Large Language Model-based Web Navigating Agent** | [[paper]](https://arxiv.org/abs/2404.03648) | [[code]](https://github.com/THUDM/AutoWebGLM)

- [2024/04/01] **Rapid Mobile App Development for Generative AI Agents on MIT App Inventor** | [[paper]](https://arxiv.org/abs/2405.01561) | [code]

- [2024/03/05] **InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents** | [[paper]](https://arxiv.org/abs/2403.02691) | [code]

- [2024/03/05] **Android in the Zoo: Chain-of-Action-Thought for GUI Agents** | [[paper]](https://arxiv.org/abs/2403.02713) | [code]

- [2024/02/27] **BASES: Large-scale Web Search User Simulation with Large Language Model based Agents** | [[paper]](https://arxiv.org/abs/2402.17505) | [code]

- [2024/02/26] **Look Before You Leap: Towards Decision-Aware and Generalizable Tool-Usage for Large Language Models** | [[paper]](https://arxiv.org/abs/2402.16696) | [code]

- [2024/02/23] **On the Multi-turn Instruction Following for Conversational Web Agents** | [[paper]](https://arxiv.org/abs/2402.15057) | [code]

- [2024/02/20] **AgentMD: Empowering Language Agents for Risk Prediction with Large-Scale Clinical Tool Learning** | [[paper]](https://arxiv.org/abs/2402.13225) | [code]

- [2024/02/18] **SciAgent: Tool-augmented Language Models for Scientific Reasoning** | [[paper]](https://arxiv.org/abs/2402.11451) | [code]

- [2024/02/16] **ToolSword: Unveiling Safety Issues of Large Language Models in Tool Learning Across Three Stages** | [[paper]](https://arxiv.org/abs/2402.10753) | [[code]](https://github.com/junjie-ye/toolsword)

- [2024/02/08] **UFO: A UI-Focused Agent for Windows OS Interaction** | [[paper]](https://arxiv.org/abs/2402.07939) | [code]

- [2024/02/06] **AnyTool: Self-Reflective, Hierarchical Agents for Large-Scale API Calls** | [[paper]](https://arxiv.org/abs/2402.04253) | [[code]](https://github.com/dyabel/anytool)

- [2024/01/11] **EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction** | [[paper]](https://arxiv.org/abs/2401.06201) | [code]

- [2024/01/03] **GPT-4V(ision) is a Generalist Web Agent, if Grounded** | [[paper]](https://arxiv.org/abs/2401.01614) | [code]

- [2023/12/21] **AppAgent: Multimodal Agents as Smartphone Users** | [[paper]](https://arxiv.org/abs/2312.13771) | [code]

- [2023/12/18] **CLOVA: A Closed-Loop Visual Assistant with Tool Usage and Update** | [[paper]](https://arxiv.org/abs/2312.10908) | [[code]](https://clova-tool.github.io/)

- [2023/12/14] **CogAgent: A Visual Language Model for GUI Agents** | [[paper]](https://arxiv.org/abs/2312.08914) | [code]

- [2023/11/19] **TPTU-v2: Boosting Task Planning and Tool Usage of Large Language Model-based Agents in Real-world Systems** | [[paper]](https://arxiv.org/abs/2311.11315) | [code]

- [2023/11/15] **ToolTalk: Evaluating Tool-Usage in a Conversational Setting** | [[paper]](https://arxiv.org/abs/2311.10775) | [code]

- [2023/11/10] **Smart Agent-Based Modeling: On the Use of Large Language Models in Computer Simulations** | [[paper]](https://arxiv.org/abs/2311.06330) | [code]

- [2023/10/12] **A Zero-Shot Language Agent for Computer Control with Structured Reflection** | [[paper]](https://arxiv.org/abs/2310.08740) | [code]

- [2023/08/07] **TPTU: Large Language Model-based AI Agents for Task Planning and Tool Usage** | [[paper]](https://arxiv.org/abs/2308.03427) | [code]

- [2023/06/09] **Mind2Web: Towards a Generalist Agent for the Web** | [[paper]](https://arxiv.org/abs/2306.06070) | [code]

- [2023/05/22] **Making Language Models Better Tool Learners with Execution Feedback** | [[paper]](https://arxiv.org/abs/2305.13068) | [code]

- [2023/05/19] **ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings** | [[paper]](https://arxiv.org/abs/2305.11554) | [code]

#### Simulation
- [2025/07/10] **Automating MD simulations for Proteins using Large language Models: NAMD-Agent** | [[paper]](https://arxiv.org/abs/2507.07887) | [code]

- [2025/07/01] **TransLaw: Benchmarking Large Language Models in Multi-Agent Simulation of the Collaborative Translation** | [[paper]](https://arxiv.org/abs/2507.00875) | [code]

- [2025/06/26] **CitySim: Modeling Urban Behaviors and City Dynamics with Large-Scale LLM-Driven Agent Simulation** | [[paper]](https://arxiv.org/abs/2506.21805) | [code]

- [2025/06/24] **LLM-Based Social Simulations Require a Boundary** | [[paper]](https://arxiv.org/abs/2506.19806) | [code]

- [2025/06/23] **TrajTok: Technical Report for 2025 Waymo Open Sim Agents Challenge** | [[paper]](https://arxiv.org/abs/2506.21618) | [code]

- [2025/06/16] **CAMS: A CityGPT-Powered Agentic Framework for Urban Human Mobility Simulation** | [[paper]](https://arxiv.org/abs/2506.13599) | [code]

- [2025/06/07] **Modeling Earth-Scale Human-Like Societies with One Billion Agents** | [[paper]](https://arxiv.org/abs/2506.12078) | [code]

- [2025/06/03] **MASTER: Enhancing Large Language Model via Multi-Agent Simulated Teaching** | [[paper]](https://arxiv.org/abs/2506.02689) | [code]

- [2025/06/02] **LAM SIMULATOR: Advancing Data Generation for Large Action Model Training via Online Exploration and Trajectory Feedback** | [[paper]](https://arxiv.org/abs/2506.02298) | [code]

- [2025/05/31] **Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents** | [[paper]](https://arxiv.org/abs/2506.00320) | [code]

- [2025/05/28] **Scalable, Symbiotic, AI and Non-AI Agent Based Parallel Discrete Event Simulations** | [[paper]](https://arxiv.org/abs/2505.23846) | [code]

- [2025/05/26] **Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents** | [[paper]](https://arxiv.org/abs/2505.19997) | [code]

- [2025/05/25] **When Ethics and Payoffs Diverge: LLM Agents in Morally Charged Social Dilemmas** | [[paper]](https://arxiv.org/abs/2505.19212) | [code]

- [2025/05/19] **Simulation Agent: A Framework for Integrating Simulation and Large Language Models for Enhanced Decision-Making** | [[paper]](https://arxiv.org/abs/2505.13761) | [code]

- [2025/05/11] **EcoLANG: Efficient and Effective Agent Communication Language Induction for Social Simulation** | [[paper]](https://arxiv.org/abs/2505.06904) | [code]

- [2025/04/20] **BookWorld: From Novels to Interactive Agent Societies for Creative Story Generation** | [[paper]](https://arxiv.org/abs/2504.14538) | [code]

- [2025/04/17] **SimUSER: Simulating User Behavior with Large Language Models for Recommender System Evaluation** | [[paper]](https://arxiv.org/abs/2504.12722) | [code]

- [2025/04/14] **SocioVerse: A World Model for Social Simulation Powered by LLM Agents and A Pool of 10 Million Real-World Users** | [[paper]](https://arxiv.org/abs/2504.10157) | [code]

- [2025/04/10] **MOSAIC: Modeling Social AI for Content Dissemination and Regulation in Multi-Agent Simulations** | [[paper]](https://arxiv.org/abs/2504.07830) | [code]

- [2025/04/04] **APIGen-MT: Agentic Pipeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay** | [[paper]](https://arxiv.org/abs/2504.03601) | [code]

- [2025/04/04] **Algorithmic Prompt Generation for Diverse Human-like Teaming and Communication with Large Language Models** | [[paper]](https://arxiv.org/abs/2504.03991) | [code]

- [2025/03/28] **Self-Evolving Multi-Agent Simulations for Realistic Clinical Interactions** | [[paper]](https://arxiv.org/abs/2503.22678) | [code]

- [2025/03/18] **Retrieval-Augmented Simulacra: Generative Agents for Up-to-date and Knowledge-Adaptive Simulations** | [[paper]](https://arxiv.org/abs/2503.14620) | [code]

- [2025/03/12] **Can A Society of Generative Agents Simulate Human Behavior and Inform Public Health Policy? A Case Study on Vaccine Hesitancy** | [[paper]](https://arxiv.org/abs/2503.09639) | [code]

- [2025/02/06] **Simulating the Emergence of Differential Case Marking with Communicating Neural-Network Agents** | [[paper]](https://arxiv.org/abs/2502.04038) | [code]

- [2025/02/03] **Eliciting Language Model Behaviors with Investigator Agents** | [[paper]](https://arxiv.org/abs/2502.01236) | [code]

- [2025/02/03] **TwinMarket: A Scalable Behavioral and Social Simulation for Financial Markets** | [[paper]](https://arxiv.org/abs/2502.01506) | [code]

- [2025/01/25] **Are Human Interactions Replicable by Generative Agents? A Case Study on Pronoun Usage in Hierarchical Interactions** | [[paper]](https://arxiv.org/abs/2501.15283) | [code]

- [2025/01/19] **Self-Explanation in Social AI Agents** | [[paper]](https://arxiv.org/abs/2501.13945) | [code]

- [2025/01/12] **LLMs Model Non-WEIRD Populations: Experiments with Synthetic Cultural Agents** | [[paper]](https://arxiv.org/abs/2501.06834) | [code]

- [2024/12/10] **Political Actor Agent: Simulating Legislative System for Roll Call Votes Prediction with Large Language Models** | [[paper]](https://arxiv.org/abs/2412.07144) | [code]

- [2024/11/18] **OASIS: Open Agent Social Interaction Simulations with One Million Agents** | [[paper]](https://arxiv.org/abs/2411.11581) | [code]

- [2024/10/28] **ElectionSim: Massive Population Election Simulation Powered by Large Language Model Driven Agents** | [[paper]](https://arxiv.org/abs/2410.20746) | [code]

- [2024/10/24] **Schema-Guided Culture-Aware Complex Event Simulation with Multi-Agent Role-Play** | [[paper]](https://arxiv.org/abs/2410.18935) | [code]

- [2024/10/18] **SRAP-Agent: Simulating and Optimizing Scarce Resource Allocation Policy with LLM-based Agent** | [[paper]](https://arxiv.org/abs/2410.14152) | [code]

- [2024/10/05] **Large Language Models can Achieve Social Balance** | [[paper]](https://arxiv.org/abs/2410.04054) | [code]

- [2024/09/25] **Plurals: A System for Guiding LLMs Via Simulated Social Ensembles** | [[paper]](https://arxiv.org/abs/2409.17213) | [code]

- [2024/09/14] **Synergistic Simulations: Multi-Agent Problem Solving with Large Language Models** | [[paper]](https://arxiv.org/abs/2409.13753) | [code]

- [2024/09/02] **Agentic Society: Merging skeleton from real world and texture from Large Language Model** | [[paper]](https://arxiv.org/abs/2409.10550) | [code]

- [2024/08/28] **Logic-Enhanced Language Model Agents for Trustworthy Social Simulations** | [[paper]](https://arxiv.org/abs/2408.16081) | [code]

- [2024/08/15] **AgentCourt: Simulating Court with Adversarial Evolvable Lawyer Agents** | [[paper]](https://arxiv.org/abs/2408.08089) | [code]

- [2024/08/03] **Self-Emotion Blended Dialogue Generation in Social Simulation Agents** | [[paper]](https://arxiv.org/abs/2408.01633) | [code]

- [2024/06/26] **Simulating The U.S. Senate: An LLM-Driven Agent Approach to Modeling Legislative Behavior and Bipartisanship** | [[paper]](https://arxiv.org/abs/2406.18702) | [code]

- [2024/06/20] **Artificial Leviathan: Exploring Social Evolution of LLM Agents Through the Lens of Hobbesian Social Contract Theory** | [[paper]](https://arxiv.org/abs/2406.14373) | [code]

- [2024/06/10] **Can Language Models Serve as Text-Based World Simulators?** | [[paper]](https://arxiv.org/abs/2406.06485) | [code]

- [2024/05/12] **Exploring the Potential of Conversational AI Support for Agent-Based Social Simulation Model Design** | [[paper]](https://arxiv.org/abs/2405.08032) | [code]

- [2024/04/23] **BattleAgent: Multi-modal Dynamic Emulation on Historical Battles to Complement Historical Analysis** | [[paper]](https://arxiv.org/abs/2404.15532) | [[code]](https://github.com/agiresearch/battleagent)

- [2024/03/20] **AgentGroupChat: An Interactive Group Chat Simulacra For Better Eliciting Emergent Behavior** | [[paper]](https://arxiv.org/abs/2403.13433) | [code]

- [2024/03/05] **AgentsCourt: Building Judicial Decision-Making Agents with Court Debate Simulation and Legal Knowledge Augmentation** | [[paper]](https://arxiv.org/abs/2403.02959) | [code]

- [2024/02/26] **Unveiling the Truth and Facilitating Change: Towards Agent-based Large-scale Social Movement Simulation** | [[paper]](https://arxiv.org/abs/2402.16333) | [code]

- [2024/02/20] **What if LLMs Have Different World Views: Simulating Alien Civilizations with LLM-based Agents** | [[paper]](https://arxiv.org/abs/2402.13184) | [code]

- [2024/02/07] **Can Large Language Model Agents Simulate Human Trust Behavior?** | [[paper]](https://arxiv.org/abs/2402.04559) | [code]

- [2024/01/08] **SpeechAgents: Human-Communication Simulation with Multi-Modal Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2401.03945) | [code]

- [2023/12/06] **LLM as OS, Agents as Apps: Envisioning AIOS, Agents and the AIOS-Agent Ecosystem** | [[paper]](https://arxiv.org/abs/2312.03815) | [code]

- [2023/11/28] **War and Peace (WarAgent): Large Language Model-based Multi-Agent Simulation of World Wars** | [[paper]](https://arxiv.org/abs/2311.17227) | [code]

- [2023/10/10] **MetaAgents: Simulating Interactions of Human Behaviors for LLM-based Task-oriented Coordination via Collaborative Generative Agents** | [[paper]](https://arxiv.org/abs/2310.06500) | [code]

- [2023/06/05] **User Behavior Simulation with Large Language Model based Agents** | [[paper]](https://arxiv.org/abs/2306.02552) | [code]

- [2023/05/26] **Training Socially Aligned Language Models on Simulated Social Interactions** | [[paper]](https://arxiv.org/abs/2305.16960) | [code]

- [2023/04/07] **Generative Agents: Interactive Simulacra of Human Behavior** | [[paper]](https://arxiv.org/abs/2304.03442) | [code]

### Application
#### Math
- [2025/05/21] **ModelingAgent: Bridging LLMs and Mathematical Modeling for Real-World Challenges** | [[paper]](https://arxiv.org/abs/2505.15068) | [code]

- [2025/03/23] **MathAgent: Leveraging a Mixture-of-Math-Agent Framework for Real-World Multimodal Mathematical Error Detection** | [[paper]](https://arxiv.org/abs/2503.18132) | [code]

- [2025/03/05] **MA-LoT: Multi-Agent Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving** | [[paper]](https://arxiv.org/abs/2503.03205) | [code]

- [2025/02/25] **LLM Knows Geometry Better than Algebra: Numerical Understanding of LLM-Based Agents in A Trading Arena** | [[paper]](https://arxiv.org/abs/2502.17967) | [code]

- [2025/02/18] **One Size doesn&#39;t Fit All: A Personalized Conversational Tutoring Agent for Mathematics Instruction** | [[paper]](https://arxiv.org/abs/2502.12633) | [code]

- [2025/02/04] **Automating Mathematical Proof Generation Using Large Language Model Agents and Knowledge Graphs** | [[paper]](https://arxiv.org/abs/2503.11657) | [code]

- [2024/10/29] **Flow-DPO: Improving LLM Mathematical Reasoning through Online Multi-Agent Learning** | [[paper]](https://arxiv.org/abs/2410.22304) | [code]

- [2024/10/13] **Expanding Search Space with Diverse Prompting Agents: An Efficient Sampling Approach for LLM Mathematical Reasoning** | [[paper]](https://arxiv.org/abs/2410.09780) | [code]

- [2024/08/03] **MathLearner: A Large Language Model Agent Framework for Learning to Solve Mathematical Problems** | [[paper]](https://arxiv.org/abs/2408.01779) | [code]

- [2024/04/10] **MathVC: An LLM-Simulated Multi-Character Virtual Classroom for Mathematics Education** | [[paper]](https://arxiv.org/abs/2404.06711) | [code]

- [2024/04/06] **MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems** | [[paper]](https://arxiv.org/abs/2404.04735) | [[code]](https://github.com/bin123apple/macm)

#### Chemistry
- [2025/05/27] **ChemHAS: Hierarchical Agent Stacking for Enhancing Chemistry Tools** | [[paper]](https://arxiv.org/abs/2505.21569) | [code]

- [2025/04/18] **System of Agentic AI for the Discovery of Metal-Organic Frameworks** | [[paper]](https://arxiv.org/abs/2504.14110) | [code]

- [2025/03/22] **Building Resource-Constrained Language Agents: A Korean Case Study on Chemical Toxicity Information** | [[paper]](https://arxiv.org/abs/2503.17753) | [code]

- [2025/01/23] **Hypothesis Generation for Materials Discovery and Design Using Goal-Driven and Constraint-Guided LLM Agents** | [[paper]](https://arxiv.org/abs/2501.13299) | [code]

- [2025/01/11] **ChemAgent: Self-updating Library in Large Language Models Improves Chemical Reasoning** | [[paper]](https://arxiv.org/abs/2501.06590) | [code]

- [2024/08/29] **HoneyComb: A Flexible LLM-Based Agent System for Materials Science** | [[paper]](https://arxiv.org/abs/2409.00135) | [code]

- [2024/06/26] **A Review of Large Language Models and Autonomous Agents in Chemistry** | [[paper]](https://arxiv.org/abs/2407.01603) | [code]

#### Biology
- [2025/04/28] **m-KAILIN: Knowledge-Driven Agentic Scientific Corpus Distillation Framework for Biomedical Large Language Models Training** | [[paper]](https://arxiv.org/abs/2504.19565) | [code]

- [2025/04/08] **SkillFlow: Efficient Skill and Code Transfer Through Communication in Adapting AI Agents** | [[paper]](https://arxiv.org/abs/2504.06188) | [code]

- [2025/04/07] **scAgent: Universal Single-Cell Annotation via a LLM Agent** | [[paper]](https://arxiv.org/abs/2504.04698) | [code]

- [2024/10/16] **PRefLexOR: Preference-based Recursive Language Modeling for Exploratory Optimization of Reasoning and Agentic Thinking** | [[paper]](https://arxiv.org/abs/2410.12375) | [code]

- [2024/06/29] **BioKGBench: A Knowledge Graph Checking Benchmark of AI Agent for Biomedical Science** | [[paper]](https://arxiv.org/abs/2407.00466) | [code]

- [2024/05/25] **GeneAgent: Self-verification Language Agent for Gene Set Knowledge Discovery using Domain Databases** | [[paper]](https://arxiv.org/abs/2405.16205) | [code]

- [2024/04/27] **CRISPR-GPT: An LLM Agent for Automated Design of Gene-Editing Experiments** | [[paper]](https://arxiv.org/abs/2404.18021) | [code]

- [2024/04/03] **Empowering Biomedical Discovery with AI Agents** | [[paper]](https://arxiv.org/abs/2404.02831) | [code]

- [2024/01/27] **ProtAgents: Protein discovery via large language model multi-agent collaborations combining physics and machine learning** | [[paper]](https://arxiv.org/abs/2402.04268) | [code]

#### Physics
- [2025/06/06] **Can Theoretical Physics Research Benefit from Language Agents?** | [[paper]](https://arxiv.org/abs/2506.06214) | [code]

- [2025/01/23] **Hypothesis Generation for Materials Discovery and Design Using Goal-Driven and Constraint-Guided LLM Agents** | [[paper]](https://arxiv.org/abs/2501.13299) | [code]

- [2024/12/09] **StarWhisper Telescope: Agent-Based Observation Assistant System to Approach AI Astrophysicist** | [[paper]](https://arxiv.org/abs/2412.06412) | [code]

- [2024/08/29] **HoneyComb: A Flexible LLM-Based Agent System for Materials Science** | [[paper]](https://arxiv.org/abs/2409.00135) | [code]

- [2024/01/27] **ProtAgents: Protein discovery via large language model multi-agent collaborations combining physics and machine learning** | [[paper]](https://arxiv.org/abs/2402.04268) | [code]

#### Geography
- [2024/12/23] **MineAgent: Towards Remote-Sensing Mineral Exploration with Multimodal Large Language Models** | [[paper]](https://arxiv.org/abs/2412.17339) | [code]

- [2024/07/13] **An Autonomous GIS Agent Framework for Geospatial Data Retrieval** | [[paper]](https://arxiv.org/abs/2407.21024) | [code]

#### Art
- [2025/01/22] **FilmAgent: A Multi-Agent Framework for End-to-End Film Automation in Virtual 3D Spaces** | [[paper]](https://arxiv.org/abs/2501.12909) | [code]

- [2024/10/02] **Agent-Driven Large Language Models for Mandarin Lyric Generation** | [[paper]](https://arxiv.org/abs/2410.01450) | [code]

- [2024/09/05] **LLM-based multi-agent poetry generation in non-cooperative environments** | [[paper]](https://arxiv.org/abs/2409.03659) | [code]

- [2024/08/13] **What should I wear to a party in a Greek taverna? Evaluation for Conversational Agents in the Fashion Domain** | [[paper]](https://arxiv.org/abs/2408.08907) | [code]

- [2024/07/01] **IBSEN: Director-Actor Agent Collaboration for Controllable and Interactive Drama Script Generation** | [[paper]](https://arxiv.org/abs/2407.01093) | [code]

- [2024/04/28] **ComposerX: Multi-Agent Symbolic Music Composition with LLMs** | [[paper]](https://arxiv.org/abs/2404.18081) | [[code]](https://github.com/lllindsey0615/composerx)

- [2024/03/12] **AesopAgent: Agent-driven Evolutionary System on Story-to-Video Production** | [[paper]](https://arxiv.org/abs/2403.07952) | [code]

- [2023/10/18] **MusicAgent: An AI Agent for Music Understanding and Generation with Large Language Models** | [[paper]](https://arxiv.org/abs/2310.11954) | [code]

#### Medicine
- [2025/07/10] **Toward Real-World Chinese Psychological Support Dialogues: CPsDD Dataset and a Co-Evolving Multi-Agent System** | [[paper]](https://arxiv.org/abs/2507.07509) | [code]

- [2025/07/03] **RLVER: Reinforcement Learning with Verifiable Emotion Rewards for Empathetic Agents** | [[paper]](https://arxiv.org/abs/2507.03112) | [code]

- [2025/07/01] **STELLA: Self-Evolving LLM Agent for Biomedical Research** | [[paper]](https://arxiv.org/abs/2507.02004) | [code]

- [2025/06/27] **Exploring Modularity of Agentic Systems for Drug Discovery** | [[paper]](https://arxiv.org/abs/2506.22189) | [code]

- [2025/06/26] **Large Language Model Agent for Modular Task Execution in Drug Discovery** | [[paper]](https://arxiv.org/abs/2507.02925) | [code]

- [2025/06/25] **An Agentic System for Rare Disease Diagnosis with Traceable Reasoning** | [[paper]](https://arxiv.org/abs/2506.20430) | [code]

- [2025/06/24] **MAM: Modular Multi-Agent Framework for Multi-Modal Medical Diagnosis via Role-Specialized Collaboration** | [[paper]](https://arxiv.org/abs/2506.19835) | [code]

- [2025/06/18] **From RAG to Agentic: Validating Islamic-Medicine Responses with LLM Agents** | [[paper]](https://arxiv.org/abs/2506.15911) | [code]

- [2025/06/17] **RadFabric: Agentic AI System with Reasoning Capability for Radiology** | [[paper]](https://arxiv.org/abs/2506.14142) | [code]

- [2025/06/16] **Language Agents for Hypothesis-driven Clinical Decision Making with Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2506.13474) | [code]

- [2025/06/13] **Large Language Model-Powered Conversational Agent Delivering Problem-Solving Therapy (PST) for Family Caregivers: Enhancing Empathy and Therapeutic Alliance Using In-Context Learning** | [[paper]](https://arxiv.org/abs/2506.11376) | [code]

- [2025/06/12] **Neural at ArchEHR-QA 2025: Agentic Prompt Optimization for Evidence-Grounded Clinical Question Answering** | [[paper]](https://arxiv.org/abs/2506.10751) | [code]

- [2025/06/11] **ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning** | [[paper]](https://arxiv.org/abs/2506.09513) | [code]

- [2025/06/04] **AI Agents for Conversational Patient Triage: Preliminary Simulation-Based Evaluation with Real-World EHR Data** | [[paper]](https://arxiv.org/abs/2506.04032) | [code]

- [2025/06/04] **MedAgentGym: Training LLM Agents for Code-Based Medical Reasoning at Scale** | [[paper]](https://arxiv.org/abs/2506.04405) | [code]

- [2025/05/31] **MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning** | [[paper]](https://arxiv.org/abs/2506.00555) | [code]

- [2025/05/30] **MedOrch: Medical Diagnosis with Tool-Augmented Reasoning Agents for Flexible Extensibility** | [[paper]](https://arxiv.org/abs/2506.00235) | [code]

- [2025/05/27] **Silence is Not Consensus: Disrupting Agreement Bias in Multi-Agent LLMs via Catfish Agent for Clinical Decision Making** | [[paper]](https://arxiv.org/abs/2505.21503) | [code]

- [2025/05/27] **BehaviorSFT: Behavioral Token Conditioning for Clinical Agents Across the Proactivity Spectrum** | [[paper]](https://arxiv.org/abs/2505.21757) | [code]

- [2025/05/24] **DDO: Dual-Decision Optimization via Multi-Agent Collaboration for LLM-Based Medical Consultation** | [[paper]](https://arxiv.org/abs/2505.18630) | [code]

- [2025/05/21] **A Risk Taxonomy for Evaluating AI-Powered Psychotherapy Agents** | [[paper]](https://arxiv.org/abs/2505.15108) | [code]

- [2025/05/18] **MedAgentBoard: Benchmarking Multi-Agent Collaboration with Conventional Methods for Diverse Medical Tasks** | [[paper]](https://arxiv.org/abs/2505.12371) | [code]

- [2025/05/06] **FRAME: Feedback-Refined Agent Methodology for Enhancing Medical Research Insights** | [[paper]](https://arxiv.org/abs/2505.04649) | [code]

- [2025/04/30] **Talk Before You Retrieve: Agent-Led Discussions for Better RAG in Medical QA** | [[paper]](https://arxiv.org/abs/2504.21252) | [code]

- [2025/04/28] **m-KAILIN: Knowledge-Driven Agentic Scientific Corpus Distillation Framework for Biomedical Large Language Models Training** | [[paper]](https://arxiv.org/abs/2504.19565) | [code]

- [2025/04/25] **MAGI: Multi-Agent Guided Interview for Psychiatric Assessment** | [[paper]](https://arxiv.org/abs/2504.18260) | [code]

- [2025/04/13] **EmoAgent: Assessing and Safeguarding Human-AI Interaction for Mental Health Safety** | [[paper]](https://arxiv.org/abs/2504.09689) | [code]

- [2025/04/08] **TxGemma: Efficient and Agentic LLMs for Therapeutics** | [[paper]](https://arxiv.org/abs/2504.06196) | [code]

- [2025/04/04] **YaleNLP @ PerAnsSumm 2025: Multi-Perspective Integration via Mixture-of-Agents for Enhanced Healthcare QA Summarization** | [[paper]](https://arxiv.org/abs/2504.03932) | [code]

- [2025/03/28] **Self-Evolving Multi-Agent Simulations for Realistic Clinical Interactions** | [[paper]](https://arxiv.org/abs/2503.22678) | [code]

- [2025/03/26] **TAMA: A Human-AI Collaborative Thematic Analysis Framework Using Multi-Agent LLMs for Clinical Interviews** | [[paper]](https://arxiv.org/abs/2503.20666) | [code]

- [2025/03/26] **3MDBench: Medical Multimodal Multi-agent Dialogue Benchmark** | [[paper]](https://arxiv.org/abs/2504.13861) | [code]

- [2025/03/21] **Autonomous Radiotherapy Treatment Planning Using DOLA: A Privacy-Preserving, LLM-Based Optimization Agent** | [[paper]](https://arxiv.org/abs/2503.17553) | [code]

- [2025/03/19] **When Pigs Get Sick: Multi-Agent AI for Swine Disease Detection** | [[paper]](https://arxiv.org/abs/2503.15204) | [code]

- [2025/03/19] **EmpathyAgent: Can Embodied Agents Conduct Empathetic Actions?** | [[paper]](https://arxiv.org/abs/2503.16545) | [code]

- [2025/03/17] **MAP: Evaluation and Multi-Agent Enhancement of Large Language Models for Inpatient Pathways** | [[paper]](https://arxiv.org/abs/2503.13205) | [code]

- [2025/03/10] **MedAgentsBench: Benchmarking Thinking Models and Agent Frameworks for Complex Medical Reasoning** | [[paper]](https://arxiv.org/abs/2503.07459) | [code]

- [2025/03/07] **GEMA-Score: Granular Explainable Multi-Agent Score for Radiology Report Evaluation** | [[paper]](https://arxiv.org/abs/2503.05347) | [code]

- [2025/03/07] **Multi Agent based Medical Assistant for Edge Devices** | [[paper]](https://arxiv.org/abs/2503.05397) | [code]

- [2025/02/27] **M^3Builder: A Multi-Agent System for Automated Machine Learning in Medical Imaging** | [[paper]](https://arxiv.org/abs/2502.20301) | [code]

- [2025/02/26] **MEDDxAgent: A Unified Modular Agent Framework for Explainable Automatic Differential Diagnosis** | [[paper]](https://arxiv.org/abs/2502.19175) | [code]

- [2025/02/25] **Scaffolding Empathy: Training Counselors with Simulated Patients and Utterance-level Performance Visualizations** | [[paper]](https://arxiv.org/abs/2502.18673) | [code]

- [2025/02/24] **Improving Interactive Diagnostic Ability of a Large Language Model Agent Through Clinical Experience Learning** | [[paper]](https://arxiv.org/abs/2503.16463) | [code]

- [2025/02/19] **LIDDIA: Language-based Intelligent Drug Discovery Agent** | [[paper]](https://arxiv.org/abs/2502.13959) | [code]

- [2025/02/18] **An LLM-Powered Agent for Physiological Data Analysis: A Case Study on PPG-based Heart Rate Estimation** | [[paper]](https://arxiv.org/abs/2502.12836) | [code]

- [2025/02/18] **Sleepless Nights, Sugary Days: Creating Synthetic Users with Health Conditions for Realistic Coaching Agent Interactions** | [[paper]](https://arxiv.org/abs/2502.13135) | [code]

- [2025/02/13] **PathFinder: A Multi-Modal Multi-Agent System for Medical Diagnostic Decision-Making Applied to Histopathology** | [[paper]](https://arxiv.org/abs/2502.08916) | [code]

- [2025/02/09] **HamRaz: A Culture-Based Persian Conversation Dataset for Person-Centered Therapy Using LLM Agents** | [[paper]](https://arxiv.org/abs/2502.05982) | [code]

- [2025/02/09] **The Application of MATEC (Multi-AI Agent Team Care) Framework in Sepsis Care** | [[paper]](https://arxiv.org/abs/2503.16433) | [code]

- [2025/02/05] **CAMI: A Counselor Agent Supporting Motivational Interviewing through State Inference and Topic Exploration** | [[paper]](https://arxiv.org/abs/2502.02807) | [code]

- [2025/02/02] **Agent-Based Uncertainty Awareness Improves Automated Radiology Report Labeling with an Open-Source Large Language Model** | [[paper]](https://arxiv.org/abs/2502.01691) | [code]

- [2025/01/27] **MADP: Multi-Agent Deductive Planning for Enhanced Cognitive-Behavioral Mental Health Question Answer** | [[paper]](https://arxiv.org/abs/2501.15826) | [code]

- [2025/01/16] **AutoCBT: An Autonomous Multi-agent Framework for Cognitive Behavioral Therapy in Psychological Counseling** | [[paper]](https://arxiv.org/abs/2501.09426) | [code]

- [2025/01/03] **PSYCHE: A Multi-faceted Patient Simulation Framework for Evaluation of Psychiatric Assessment Conversational Agents** | [[paper]](https://arxiv.org/abs/2501.01594) | [code]

- [2024/12/19] **PsyDraw: A Multi-Agent Multimodal System for Mental Health Screening in Left-Behind Children** | [[paper]](https://arxiv.org/abs/2412.14769) | [code]

- [2024/12/17] **RareAgents: Advancing Rare Disease Care through LLM-Empowered Multi-disciplinary Team** | [[paper]](https://arxiv.org/abs/2412.12475) | [code]

- [2024/12/16] **LLMs Can Simulate Standardized Patients via Agent Coevolution** | [[paper]](https://arxiv.org/abs/2412.11716) | [code]

- [2024/12/13] **Script-Based Dialog Policy Planning for LLM-Powered Conversational Agents: A Basic Architecture for an &#34;AI Therapist&#34;** | [[paper]](https://arxiv.org/abs/2412.15242) | [code]

- [2024/12/05] **Educational-Psychological Dialogue Robot Based on Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2412.03847) | [code]

- [2024/12/02] **Medchain: Bridging the Gap Between LLM Agents and Clinical Practice through Interactive Sequential Benchmarking** | [[paper]](https://arxiv.org/abs/2412.01605) | [code]

- [2024/11/21] **PIORS: Personalized Intelligent Outpatient Reception based on Large Language Model with Multi-Agents Medical Scenario Simulation** | [[paper]](https://arxiv.org/abs/2411.13902) | [code]

- [2024/11/16] **Towards Next-Generation Medical Agent: How o1 is Reshaping Decision-Making in Medical Scenarios** | [[paper]](https://arxiv.org/abs/2411.14461) | [code]

- [2024/11/03] **EcoAct: Economic Agent Determines When to Register What Action** | [[paper]](https://arxiv.org/abs/2411.01643) | [code]

- [2024/10/25] **$\texttt{PatentAgent}$: Intelligent Agent for Automated Pharmaceutical Patent Analysis** | [[paper]](https://arxiv.org/abs/2410.21312) | [code]

- [2024/10/23] **ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents** | [[paper]](https://arxiv.org/abs/2410.17657) | [code]

- [2024/10/17] **MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling** | [[paper]](https://arxiv.org/abs/2410.13610) | [code]

- [2024/10/16] **MedAide: Towards an Omni Medical Aide via Specialized LLM-based Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2410.12532) | [code]

- [2024/10/02] **Zodiac: A Cardiologist-Level LLM Framework for Multi-Agent Diagnostics** | [[paper]](https://arxiv.org/abs/2410.02026) | [code]

- [2024/08/28] **Interactive Agents: Simulating Counselor-Client Psychological Counseling via Role-Playing LLM-to-LLM Interactions** | [[paper]](https://arxiv.org/abs/2408.15787) | [code]

- [2024/08/23] **DrugAgent: Explainable Drug Repurposing Agent with Large Language Model-based Reasoning** | [[paper]](https://arxiv.org/abs/2408.13378) | [code]

- [2024/08/14] **Development of a Large Language Model-based Multi-Agent Clinical Decision Support System for Korean Triage and Acuity Scale (KTAS)-Based Triage and Treatment Planning in Emergency Departments** | [[paper]](https://arxiv.org/abs/2408.07531) | [code]

- [2024/07/18] **CoD, Towards an Interpretable Medical Agent using Chain of Diagnosis** | [[paper]](https://arxiv.org/abs/2407.13301) | [code]

- [2024/07/10] **Virtual Agents for Alcohol Use Counseling: Exploring LLM-Powered Motivational Interviewing** | [[paper]](https://arxiv.org/abs/2407.08095) | [code]

- [2024/07/03] **MentalAgora: A Gateway to Advanced Personalized Care in Mental Health through Multi-Agent Debating and Attribute Control** | [[paper]](https://arxiv.org/abs/2407.02736) | [code]

- [2024/07/02] **MMedAgent: Learning to Use Medical Tools with Multi-modal Agent** | [[paper]](https://arxiv.org/abs/2407.02483) | [code]

- [2024/04/23] **ClinicalAgent: Clinical Trial Multi-Agent System with Large Language Model-based Reasoning** | [[paper]](https://arxiv.org/abs/2404.14777) | [code]

- [2024/04/03] **Empowering Biomedical Discovery with AI Agents** | [[paper]](https://arxiv.org/abs/2404.02831) | [code]

- [2024/02/20] **Can Large Language Models be Used to Provide Psychological Counselling? An Analysis of GPT-4-Generated Responses Using Role-play Dialogues** | [[paper]](https://arxiv.org/abs/2402.12738) | [code]

- [2024/02/20] **AgentMD: Empowering Language Agents for Risk Prediction with Large-Scale Clinical Tool Learning** | [[paper]](https://arxiv.org/abs/2402.13225) | [code]

- [2024/02/15] **Knowledge-Infused LLM-Powered Conversational Health Agent: A Case Study for Diabetes Patients** | [[paper]](https://arxiv.org/abs/2402.10153) | [code]

- [2024/02/01] **Generation, Distillation and Evaluation of Motivational Interviewing-Style Reflections with a Foundational Language Model** | [[paper]](https://arxiv.org/abs/2402.01051) | [code]

- [2023/12/19] **Can ChatGPT be Your Personal Medical Assistant?** | [[paper]](https://arxiv.org/abs/2312.12006) | [code]

- [2023/10/03] **Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View** | [[paper]](https://arxiv.org/abs/2310.02124) | [code]

#### Finance
- [2025/07/08] **ECom-Bench: Can LLM Agent Resolve Real-World E-commerce Customer Support Issues?** | [[paper]](https://arxiv.org/abs/2507.05639) | [code]

- [2025/07/07] **MindFlow: Revolutionizing E-commerce Customer Support with Multimodal LLM Agents** | [[paper]](https://arxiv.org/abs/2507.05330) | [code]

- [2025/06/10] **Improved LLM Agents for Financial Document Question Answering** | [[paper]](https://arxiv.org/abs/2506.08726) | [code]

- [2025/06/09] **EconWebArena: Benchmarking Autonomous Agents on Economic Tasks in Realistic Web Environments** | [[paper]](https://arxiv.org/abs/2506.08136) | [code]

- [2025/05/20] **Hidden Ghost Hand: Unveiling Backdoor Vulnerabilities in MLLM-Powered Mobile GUI Agents** | [[paper]](https://arxiv.org/abs/2505.14418) | [code]

- [2025/04/08] **Are Generative AI Agents Effective Personalized Financial Advisors?** | [[paper]](https://arxiv.org/abs/2504.05862) | [code]

- [2025/04/07] **AI for Climate Finance: Agentic Retrieval and Multi-Step Reasoning for Early Warning System Investments** | [[paper]](https://arxiv.org/abs/2504.05104) | [code]

- [2025/03/27] **EQ-Negotiator: An Emotion-Reasoning LLM Agent in Credit Dialogues** | [[paper]](https://arxiv.org/abs/2503.21080) | [code]

- [2025/03/05] **Cite Before You Speak: Enhancing Context-Response Grounding in E-commerce Conversational LLM-Agents** | [[paper]](https://arxiv.org/abs/2503.04830) | [code]

- [2025/02/25] **LLM Knows Geometry Better than Algebra: Numerical Understanding of LLM-Based Agents in A Trading Arena** | [[paper]](https://arxiv.org/abs/2502.17967) | [code]

- [2025/02/08] **Agentic AI Systems Applied to tasks in Financial Services: Modeling and model risk management crews** | [[paper]](https://arxiv.org/abs/2502.05439) | [code]

- [2025/02/01] **MarketSenseAI 2.0: Enhancing Stock Analysis through LLM Agents** | [[paper]](https://arxiv.org/abs/2502.00415) | [code]

- [2025/01/08] **FinSphere: A Conversational Stock Analysis Agent Equipped with Quantitative Tools based on Real-Time Database** | [[paper]](https://arxiv.org/abs/2501.12399) | [code]

- [2024/12/27] **OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis** | [[paper]](https://arxiv.org/abs/2412.19723) | [code]

- [2024/12/19] **Beyond the Sum: Unlocking AI Agents Potential Through Market Forces** | [[paper]](https://arxiv.org/abs/2501.10388) | [code]

- [2024/11/07] **Enhancing Investment Analysis: Optimizing AI-Agent Collaboration in Financial Research** | [[paper]](https://arxiv.org/abs/2411.04788) | [code]

- [2024/10/29] **Enhancing Financial Question Answering with a Multi-Agent Reflection Framework** | [[paper]](https://arxiv.org/abs/2410.21741) | [code]

- [2024/09/19] **Strategic Collusion of LLM Agents: Market Division in Multi-Commodity Competitions** | [[paper]](https://arxiv.org/abs/2410.00031) | [code]

- [2024/07/18] **dzFinNlp at AraFinNLP: Improving Intent Detection in Financial Conversational Agents** | [[paper]](https://arxiv.org/abs/2407.13565) | [code]

- [2024/07/09] **FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making** | [[paper]](https://arxiv.org/abs/2407.06567) | [code]

- [2024/07/05] **Towards Automated Functional Equation Proving: A Benchmark Dataset and A Domain-Specific In-Context Agent** | [[paper]](https://arxiv.org/abs/2407.14521) | [code]

- [2024/05/07] **Enhancing the Efficiency and Accuracy of Underlying Asset Reviews in Structured Finance: The Application of Multi-agent Framework** | [[paper]](https://arxiv.org/abs/2405.04294) | [code]

#### Software Engineering
- [2025/06/13] **Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards** | [[paper]](https://arxiv.org/abs/2506.11425) | [code]

- [2025/06/04] **MedAgentGym: Training LLM Agents for Code-Based Medical Reasoning at Scale** | [[paper]](https://arxiv.org/abs/2506.04405) | [code]

- [2025/06/03] **Coding Agents with Multimodal Browsing are Generalist Problem Solvers** | [[paper]](https://arxiv.org/abs/2506.03011) | [code]

- [2025/05/28] **Co-Saving: Resource Aware Multi-Agent Collaboration for Software Development** | [[paper]](https://arxiv.org/abs/2505.21898) | [code]

- [2025/05/26] **Vibe Coding vs. Agentic Coding: Fundamentals and Practical Implications of Agentic AI** | [[paper]](https://arxiv.org/abs/2505.19443) | [code]

- [2025/05/26] **SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents** | [[paper]](https://arxiv.org/abs/2505.20411) | [code]

- [2025/05/24] **SEW: Self-Evolving Agentic Workflows for Automated Code Generation** | [[paper]](https://arxiv.org/abs/2505.18646) | [code]

- [2025/05/22] **Optimizing LLM-Based Multi-Agent System with Textual Feedback: A Case Study on Software Development** | [[paper]](https://arxiv.org/abs/2505.16086) | [code]

- [2025/05/19] **Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents** | [[paper]](https://arxiv.org/abs/2505.13652) | [code]

- [2025/05/13] **LibVulnWatch: A Deep Assessment Agent System and Leaderboard for Uncovering Hidden Vulnerabilities in Open-Source AI Libraries** | [[paper]](https://arxiv.org/abs/2505.08842) | [code]

- [2025/04/30] **SWE-smith: Scaling Data for Software Engineering Agents** | [[paper]](https://arxiv.org/abs/2504.21798) | [code]

- [2025/04/28] **ResearchCodeAgent: An LLM Multi-Agent System for Automated Codification of Research Methodologies** | [[paper]](https://arxiv.org/abs/2504.20117) | [code]

- [2025/04/18] **CodeVisionary: An Agent-based Framework for Evaluating Large Language Models in Code Generation** | [[paper]](https://arxiv.org/abs/2504.13472) | [code]

- [2025/04/09] **R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents** | [[paper]](https://arxiv.org/abs/2504.07164) | [code]

- [2025/03/27] **GateLens: A Reasoning-Enhanced LLM Agent for Automotive Software Release Analytics** | [[paper]](https://arxiv.org/abs/2503.21735) | [code]

- [2025/03/24] **Verbal Process Supervision Elicits Better Coding Agents** | [[paper]](https://arxiv.org/abs/2503.18494) | [code]

- [2025/03/18] **DARS: Dynamic Action Re-Sampling to Enhance Coding Agent Performance by Adaptive Tree Traversal** | [[paper]](https://arxiv.org/abs/2503.14269) | [code]

- [2025/03/12] **LocAgent: Graph-Guided LLM Agents for Code Localization** | [[paper]](https://arxiv.org/abs/2503.09089) | [code]

- [2025/03/10] **ProjectEval: A Benchmark for Programming Agents Automated Evaluation on Project-Level Code Generation** | [[paper]](https://arxiv.org/abs/2503.07010) | [code]

- [2025/02/19] **An LLM-based Agent for Reliable Docker Environment Configuration** | [[paper]](https://arxiv.org/abs/2502.13681) | [code]

- [2025/02/18] **Training Turn-by-Turn Verifiers for Dialogue Tutoring Agents: The Curious Case of LLMs as Your Coding Tutors** | [[paper]](https://arxiv.org/abs/2502.13311) | [code]

- [2025/02/18] **UXAgent: An LLM Agent-Based Usability Testing Framework for Web Design** | [[paper]](https://arxiv.org/abs/2502.12561) | [code]

- [2025/02/14] **The Ann Arbor Architecture for Agent-Oriented Programming** | [[paper]](https://arxiv.org/abs/2502.09903) | [[code]](https://github.com/aaalgo/postline_0.1)

- [2025/02/11] **Multi-Agent Collaboration for Multilingual Code Instruction Tuning** | [[paper]](https://arxiv.org/abs/2502.07487) | [code]

- [2025/02/10] **SyncMind: Measuring Agent Out-of-Sync Recovery in Collaborative Software Engineering** | [[paper]](https://arxiv.org/abs/2502.06994) | [code]

- [2025/02/08] **CODESIM: Multi-Agent Code Generation and Problem Solving through Simulation-Driven Planning and Debugging** | [[paper]](https://arxiv.org/abs/2502.05664) | [code]

- [2024/12/30] **Training Software Engineering Agents and Verifiers with SWE-Gym** | [[paper]](https://arxiv.org/abs/2412.21139) | [code]

- [2024/12/24] **Molly: Making Large Language Model Agents Solve Python Problem More Logically** | [[paper]](https://arxiv.org/abs/2412.18093) | [code]

- [2024/12/16] **Seeker: Towards Exception Safety Code Generation with Intermediate Language Agents Framework** | [[paper]](https://arxiv.org/abs/2412.11713) | [code]

- [2024/11/07] **CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models** | [[paper]](https://arxiv.org/abs/2411.04329) | [code]

- [2024/10/29] **SceneGenAgent: Precise Industrial Scene Generation with Coding Agent** | [[paper]](https://arxiv.org/abs/2410.21909) | [code]

- [2024/10/09] **DA-Code: Agent Data Science Code Generation Benchmark for Large Language Models** | [[paper]](https://arxiv.org/abs/2410.07331) | [code]

- [2024/10/09] **Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach** | [[paper]](https://arxiv.org/abs/2410.06949) | [code]

- [2024/09/02] **Co-Learning: Code Learning for Multi-Agent Reinforcement Collaborative Framework with Conversational Natural Language Interfaces** | [[paper]](https://arxiv.org/abs/2409.00985) | [code]

- [2024/08/19] **GoNoGo: An Efficient LLM-based Multi-Agent System for Streamlining Automotive Software Release Decision-Making** | [[paper]](https://arxiv.org/abs/2408.09785) | [code]

- [2024/08/13] **Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents** | [[paper]](https://arxiv.org/abs/2408.07060) | [code]

- [2024/08/05] **LLM Agents Improve Semantic Code Search** | [[paper]](https://arxiv.org/abs/2408.11058) | [code]

- [2024/07/26] **AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents** | [[paper]](https://arxiv.org/abs/2407.18901) | [[code]](https://github.com/stonybrooknlp/appworld)

- [2024/07/01] **Agentless: Demystifying LLM-based Software Engineering Agents** | [[paper]](https://arxiv.org/abs/2407.01489) | [code]

- [2024/06/13] **Multi-Agent Software Development through Cross-Team Collaboration** | [[paper]](https://arxiv.org/abs/2406.08979) | [[code]](https://github.com/openbmb/chatdev)

- [2024/05/06] **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering** | [[paper]](https://arxiv.org/abs/2405.15793) | [code]

- [2024/04/11] **Behavior Trees Enable Structured Programming of Language Model Agents** | [[paper]](https://arxiv.org/abs/2404.07439) | [[code]](https://github.com/RichardKelley/dendron)

- [2024/04/02] **Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization** | [[paper]](https://arxiv.org/abs/2404.02183) | [code]

- [2024/03/02] **SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code** | [[paper]](https://arxiv.org/abs/2403.01248) | [code]

- [2024/02/26] **RepoAgent: An LLM-Powered Open-Source Framework for Repository-level Code Documentation Generation** | [[paper]](https://arxiv.org/abs/2402.16667) | [code]

- [2024/02/19] **WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment** | [[paper]](https://arxiv.org/abs/2402.12275) | [code]

- [2024/02/02] **StepCoder: Improve Code Generation with Reinforcement Learning from Compiler Feedback** | [[paper]](https://arxiv.org/abs/2402.01391) | [code]

- [2024/02/01] **Executable Code Actions Elicit Better LLM Agents** | [[paper]](https://arxiv.org/abs/2402.01030) | [code]

- [2023/12/28] **Experiential Co-Learning of Software-Developing Agents** | [[paper]](https://arxiv.org/abs/2312.17025) | [code]

- [2023/12/20] **AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation** | [[paper]](https://arxiv.org/abs/2312.13010) | [code]

- [2023/07/27] **PanGu-Coder2: Boosting Large Language Models for Code with Ranking Feedback** | [[paper]](https://arxiv.org/abs/2307.14936) | [code]

- [2023/07/16] **ChatDev: Communicative Agents for Software Development** | [[paper]](https://arxiv.org/abs/2307.07924) | [code]

- [2023/04/15] **Self-collaboration Code Generation via ChatGPT** | [[paper]](https://arxiv.org/abs/2304.07590) | [code]

#### Research
- [2025/07/01] **STELLA: Self-Evolving LLM Agent for Biomedical Research** | [[paper]](https://arxiv.org/abs/2507.02004) | [code]

- [2025/06/27] **RExBench: Can coding agents autonomously implement AI research extensions?** | [[paper]](https://arxiv.org/abs/2506.22598) | [code]

- [2025/06/25] **Language Modeling by Language Models** | [[paper]](https://arxiv.org/abs/2506.20249) | [code]

- [2025/06/23] **From Web Search towards Agentic Deep Research: Incentivizing Search with Reasoning Agents** | [[paper]](https://arxiv.org/abs/2506.18959) | [code]

- [2025/06/12] **VideoDeepResearch: Long Video Understanding With Agentic Tool Using** | [[paper]](https://arxiv.org/abs/2506.10821) | [code]

- [2025/06/06] **Can Theoretical Physics Research Benefit from Language Agents?** | [[paper]](https://arxiv.org/abs/2506.06214) | [code]

- [2025/05/30] **Unifying Language Agent Algorithms with Graph-based Orchestration Engine for Reproducible Agent Research** | [[paper]](https://arxiv.org/abs/2505.24354) | [code]

- [2025/05/29] **Large Language Model-Based Agents for Automated Research Reproducibility: An Exploratory Study in Alzheimer&#39;s Disease** | [[paper]](https://arxiv.org/abs/2505.23852) | [code]

- [2025/05/26] **MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research** | [[paper]](https://arxiv.org/abs/2505.19955) | [code]

- [2025/05/22] **BioDSA-1K: Benchmarking Data Science Agents for Biomedical Research** | [[paper]](https://arxiv.org/abs/2505.16100) | [code]

- [2025/05/22] **NovelSeek: When Agent Becomes the Scientist -- Building Closed-Loop System from Hypothesis to Verification** | [[paper]](https://arxiv.org/abs/2505.16938) | [code]

- [2025/04/28] **ResearchCodeAgent: An LLM Multi-Agent System for Automated Codification of Research Methodologies** | [[paper]](https://arxiv.org/abs/2504.20117) | [code]

- [2025/04/21] **Completing A Systematic Review in Hours instead of Months with Interactive AI Agents** | [[paper]](https://arxiv.org/abs/2504.14822) | [code]

- [2025/04/10] **CollEX -- A Multimodal Agentic RAG System Enabling Interactive Exploration of Scientific Collections** | [[paper]](https://arxiv.org/abs/2504.07643) | [code]

- [2025/04/10] **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** | [[paper]](https://arxiv.org/abs/2504.08066) | [code]

- [2025/04/02] **Automated Survey Collection with LLM-based Conversational Agents** | [[paper]](https://arxiv.org/abs/2504.02891) | [code]

- [2025/03/23] **AgentRxiv: Towards Collaborative Autonomous Research** | [[paper]](https://arxiv.org/abs/2503.18102) | [code]

- [2025/03/12] **Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions** | [[paper]](https://arxiv.org/abs/2503.08979) | [code]

- [2025/03/11] **ReviewAgents: Bridging the Gap Between Human and AI-Generated Paper Reviews** | [[paper]](https://arxiv.org/abs/2503.08506) | [code]

- [2025/02/25] **LAG: LLM agents for Leaderboard Auto Generation on Demanding** | [[paper]](https://arxiv.org/abs/2502.18209) | [code]

- [2025/02/20] **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** | [[paper]](https://arxiv.org/abs/2502.14499) | [code]

- [2025/02/07] **Agentic Reasoning: Reasoning LLMs with Tools for the Deep Research** | [[paper]](https://arxiv.org/abs/2502.04644) | [code]

- [2025/01/08] **Agent Laboratory: Using LLM Agents as Research Assistants** | [[paper]](https://arxiv.org/abs/2501.04227) | [code]

- [2024/10/17] **Chain of Ideas: Revolutionizing Research Via Novel Idea Development with LLM Agents** | [[paper]](https://arxiv.org/abs/2410.13185) | [code]

- [2024/10/12] **Many Heads Are Better Than One: Improved Scientific Idea Generation by A LLM-Based Multi-Agent System** | [[paper]](https://arxiv.org/abs/2410.09403) | [code]

- [2024/10/07] **ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery** | [[paper]](https://arxiv.org/abs/2410.05080) | [code]

- [2024/10/07] **ImProver: Agent-Based Automated Proof Optimization** | [[paper]](https://arxiv.org/abs/2410.04753) | [code]

- [2024/09/23] **Towards a Realistic Long-Term Benchmark for Open-Web Research Agents** | [[paper]](https://arxiv.org/abs/2409.14913) | [code]

- [2024/09/17] **CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark** | [[paper]](https://arxiv.org/abs/2409.11363) | [code]

- [2024/09/12] **DSBench: How Far Are Data Science Agents to Becoming Data Science Experts?** | [[paper]](https://arxiv.org/abs/2409.07703) | [code]

- [2024/09/11] **SUPER: Evaluating Agents on Setting Up and Executing Tasks from Research Repositories** | [[paper]](https://arxiv.org/abs/2409.07440) | [code]

- [2024/09/10] **Language agents achieve superhuman synthesis of scientific knowledge** | [[paper]](https://arxiv.org/abs/2409.13740) | [code]

- [2024/09/09] **SciAgents: Automating scientific discovery through multi-agent intelligent graph reasoning** | [[paper]](https://arxiv.org/abs/2409.05556) | [code]

- [2024/08/26] **MLR-Copilot: Autonomous Machine Learning Research based on Large Language Models Agents** | [[paper]](https://arxiv.org/abs/2408.14033) | [code]

- [2024/08/20] **Automating Knowledge Discovery from Scientific Literature via LLMs: A Dual-Agent Approach with Progressive Ontology Prompting** | [[paper]](https://arxiv.org/abs/2409.00054) | [code]

- [2024/06/13] **ResearchArena: Benchmarking Large Language Models&#39; Ability to Collect and Organize Information as Research Agents** | [[paper]](https://arxiv.org/abs/2406.10291) | [code]

- [2024/05/02] **CACTUS: Chemistry Agent Connecting Tool-Usage to Science** | [[paper]](https://arxiv.org/abs/2405.00972) | [[code]](https://github.com/pnnl/cactus)

- [2024/04/09] **SurveyAgent: A Conversational System for Personalized and Efficient Research Survey** | [[paper]](https://arxiv.org/abs/2404.06364) | [code]

- [2024/02/28] **Data Interpreter: An LLM Agent For Data Science** | [[paper]](https://arxiv.org/abs/2402.18679) | [[code]](https://github.com/geekan/metagpt)

- [2024/02/18] **SciAgent: Tool-augmented Language Models for Scientific Reasoning** | [[paper]](https://arxiv.org/abs/2402.11451) | [code]

- [2024/02/06] **Prioritizing Safeguarding Over Autonomy: Risks of LLM Agents for Science** | [[paper]](https://arxiv.org/abs/2402.04247) | [code]

- [2024/01/08] **MARG: Multi-Agent Review Generation for Scientific Papers** | [[paper]](https://arxiv.org/abs/2401.04259) | [code]

### Automation
#### Workflow
- [2025/06/02] **Follow the Flow: Fine-grained Flowchart Attribution with Neurosymbolic Agents** | [[paper]](https://arxiv.org/abs/2506.01344) | [code]

- [2025/05/26] **ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows** | [[paper]](https://arxiv.org/abs/2505.19897) | [code]

- [2025/04/17] **MetaSynth: Meta-Prompting-Driven Agentic Scaffolds for Diverse Synthetic Data Generation** | [[paper]](https://arxiv.org/abs/2504.12563) | [code]

- [2025/02/24] **Turning Conversations into Workflows: A Framework to Extract and Evaluate Dialog Workflows for Service AI Agents** | [[paper]](https://arxiv.org/abs/2502.17321) | [code]

- [2025/02/11] **EvoFlow: Evolving Diverse Agentic Workflows On The Fly** | [[paper]](https://arxiv.org/abs/2502.07373) | [code]

- [2025/02/07] **nvAgent: Automated Data Visualization from Natural Language via Collaborative Agent Workflow** | [[paper]](https://arxiv.org/abs/2502.05036) | [code]

- [2025/02/06] **ScoreFlow: Mastering LLM Agent Workflows via Score-based Preference Optimization** | [[paper]](https://arxiv.org/abs/2502.04306) | [code]

- [2024/12/17] **An Agentic Approach to Automatic Creation of P&amp;ID Diagrams from Natural Language Descriptions** | [[paper]](https://arxiv.org/abs/2412.12898) | [code]

- [2024/12/15] **LAW: Legal Agentic Workflows for Custody and Fund Services Contracts** | [[paper]](https://arxiv.org/abs/2412.11063) | [code]

- [2024/11/22] **ScribeAgent: Towards Specialized Web Agents Using Production-Scale Workflow Data** | [[paper]](https://arxiv.org/abs/2411.15004) | [code]

- [2024/11/12] **BudgetMLAgent: A Cost-Effective LLM Multi-Agent system for Automating Machine Learning Tasks** | [[paper]](https://arxiv.org/abs/2411.07464) | [code]

- [2024/11/08] **Game-theoretic LLM: Agent Workflow for Negotiation Games** | [[paper]](https://arxiv.org/abs/2411.05990) | [code]

- [2024/10/24] **An LLM Agent for Automatic Geospatial Data Analysis** | [[paper]](https://arxiv.org/abs/2410.18792) | [code]

- [2024/10/17] **From Barriers to Tactics: A Behavioral Science-Informed Agentic Workflow for Personalized Nutrition Coaching** | [[paper]](https://arxiv.org/abs/2410.14041) | [code]

- [2024/10/17] **ControlAgent: Automating Control System Design via Novel Integration of LLM Agents and Domain Expertise** | [[paper]](https://arxiv.org/abs/2410.19811) | [code]

- [2024/10/16] **Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance** | [[paper]](https://arxiv.org/abs/2410.12361) | [code]

- [2024/10/14] **AFlow: Automating Agentic Workflow Generation** | [[paper]](https://arxiv.org/abs/2410.10762) | [code]

- [2024/10/10] **Benchmarking Agentic Workflow Generation** | [[paper]](https://arxiv.org/abs/2410.07869) | [code]

- [2024/10/03] **AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML** | [[paper]](https://arxiv.org/abs/2410.02958) | [code]

- [2024/09/11] **Agent Workflow Memory** | [[paper]](https://arxiv.org/abs/2409.07429) | [code]

- [2024/08/16] **The Fellowship of the LLMs: Multi-Agent Workflows for Synthetic Preference Optimization Dataset Generation** | [[paper]](https://arxiv.org/abs/2408.08688) | [code]

- [2024/07/15] **Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?** | [[paper]](https://arxiv.org/abs/2407.10956) | [code]

- [2024/07/03] **AgentInstruct: Toward Generative Teaching with Agentic Flows** | [[paper]](https://arxiv.org/abs/2407.03502) | [code]

- [2024/07/01] **AutoFlow: Automated Workflow Generation for Large Language Model Agents** | [[paper]](https://arxiv.org/abs/2407.12821) | [code]

- [2024/06/21] **Autonomous Agents for Collaborative Task under Information Asymmetry** | [[paper]](https://arxiv.org/abs/2406.14928) | [code]

- [2024/03/13] **AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents** | [[paper]](https://arxiv.org/abs/2403.08978) | [code]

- [2024/03/05] **ChatCite: LLM Agent with Human Workflow Guidance for Comparative Literature Summary** | [[paper]](https://arxiv.org/abs/2403.02574) | [code]

#### Automatic Evaluation
- [2025/06/26] **Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge** | [[paper]](https://arxiv.org/abs/2506.21506) | [code]

- [2025/06/23] **AI Agents-as-Judge: Automated Assessment of Accuracy, Consistency, Completeness and Clarity for Enterprise Documents** | [[paper]](https://arxiv.org/abs/2506.22485) | [code]

- [2025/06/08] **Manifesto from Dagstuhl Perspectives Workshop 24352 -- Conversational Agents: A Framework for Evaluation (CAFE)** | [[paper]](https://arxiv.org/abs/2506.11112) | [code]

- [2025/05/22] **HiMATE: A Hierarchical Multi-Agent Framework for Machine Translation Evaluation** | [[paper]](https://arxiv.org/abs/2505.16281) | [code]

- [2025/05/21] **UrduFactCheck: An Agentic Fact-Checking Framework for Urdu with Evidence Boosting and Benchmarking** | [[paper]](https://arxiv.org/abs/2505.15063) | [code]

- [2025/05/21] **AGENT-X: Adaptive Guideline-based Expert Network for Threshold-free AI-generated teXt detection** | [[paper]](https://arxiv.org/abs/2505.15261) | [code]

- [2025/05/20] **CAFES: A Collaborative Multi-Agent Framework for Multi-Granular Multimodal Essay Scoring** | [[paper]](https://arxiv.org/abs/2505.13965) | [code]

- [2025/05/18] **ESC-Judge: A Framework for Comparing Emotional Support Conversational Agents** | [[paper]](https://arxiv.org/abs/2505.12531) | [code]

- [2025/05/13] **TRAIL: Trace Reasoning and Agentic Issue Localization** | [[paper]](https://arxiv.org/abs/2505.08638) | [code]

- [2025/05/05] **AutoLibra: Agent Metric Induction from Open-Ended Feedback** | [[paper]](https://arxiv.org/abs/2505.02820) | [code]

- [2025/05/01] **Sentient Agent as a Judge: Evaluating Higher-Order Social Cognition in Large Language Models** | [[paper]](https://arxiv.org/abs/2505.02847) | [code]

- [2025/04/21] **EvalAgent: Discovering Implicit Evaluation Criteria from the Web** | [[paper]](https://arxiv.org/abs/2504.15219) | [code]

- [2025/04/09] **A Unified Agentic Framework for Evaluating Conditional Image Generation** | [[paper]](https://arxiv.org/abs/2504.07046) | [code]

- [2025/04/01] **VerifiAgent: a Unified Verification Agent in Language Model Reasoning** | [[paper]](https://arxiv.org/abs/2504.00406) | [code]

- [2025/04/01] **Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language generation applications** | [[paper]](https://arxiv.org/abs/2504.02867) | [code]

- [2025/03/07] **GEMA-Score: Granular Explainable Multi-Agent Score for Radiology Report Evaluation** | [[paper]](https://arxiv.org/abs/2503.05347) | [code]

- [2025/02/26] **Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems** | [[paper]](https://arxiv.org/abs/2502.19328) | [[code]](https://github.com/THU-KEG/Agentic-Reward-Modeling)

- [2025/02/25] **Debt Collection Negotiations with Large Language Models: An Evaluation System and Optimizing Decision Making with Multi-Agent** | [[paper]](https://arxiv.org/abs/2502.18228) | [code]

- [2025/02/25] **FACT-AUDIT: An Adaptive Multi-Agent Framework for Dynamic Fact-Checking Evaluation of Large Language Models** | [[paper]](https://arxiv.org/abs/2502.17924) | [code]

- [2025/02/14] **Automated Hypothesis Validation with Agentic Sequential Falsifications** | [[paper]](https://arxiv.org/abs/2502.09858) | [code]

- [2025/01/19] **IntellAgent: A Multi-Agent Framework for Evaluating Conversational AI Systems** | [[paper]](https://arxiv.org/abs/2501.11067) | [code]

- [2025/01/17] **Agent-as-Judge for Factual Summarization of Long Narratives** | [[paper]](https://arxiv.org/abs/2501.09993) | [code]

- [2025/01/03] **PSYCHE: A Multi-faceted Patient Simulation Framework for Evaluation of Psychiatric Assessment Conversational Agents** | [[paper]](https://arxiv.org/abs/2501.01594) | [code]

- [2024/12/28] **M-MAD: Multidimensional Multi-Agent Debate for Advanced Machine Translation Evaluation** | [[paper]](https://arxiv.org/abs/2412.20127) | [code]

- [2024/12/10] **Evaluation Agent: Efficient and Promptable Evaluation Framework for Visual Generative Models** | [[paper]](https://arxiv.org/abs/2412.09645) | [code]

- [2024/11/25] **SAGEval: The frontiers of Satisfactory Agent based NLG Evaluation for reference-free open-ended text** | [[paper]](https://arxiv.org/abs/2411.16077) | [code]

- [2024/11/15] **Large Language Models as User-Agents for Evaluating Task-Oriented-Dialogue Systems** | [[paper]](https://arxiv.org/abs/2411.09972) | [code]

- [2024/09/24] **Automated test generation to evaluate tool-augmented LLMs as conversational AI agents** | [[paper]](https://arxiv.org/abs/2409.15934) | [code]

- [2024/09/22] **The Ability of Large Language Models to Evaluate Constraint-satisfaction in Agent Responses to Open-ended Requests** | [[paper]](https://arxiv.org/abs/2409.14371) | [code]

- [2024/09/13] **Safeguarding Decentralized Social Media: LLM Agents for Automating Community Rule Compliance** | [[paper]](https://arxiv.org/abs/2409.08963) | [code]

- [2024/05/23] **ALI-Agent: Assessing LLMs&#39; Alignment with Human Values via Agent-based Evaluation** | [[paper]](https://arxiv.org/abs/2405.14125) | [code]

- [2024/03/28] **MATEval: A Multi-Agent Discussion Framework for Advancing Open-Ended Text Evaluation** | [[paper]](https://arxiv.org/abs/2403.19305) | [code]

- [2023/08/14] **ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate** | [[paper]](https://arxiv.org/abs/2308.07201) | [code]

### Training
#### Fine tuning
- [2025/07/10] **SAND: Boosting LLM Agents with Self-Taught Action Deliberation** | [[paper]](https://arxiv.org/abs/2507.07441) | [code]

- [2025/07/08] **Agentic-R1: Distilled Dual-Strategy Reasoning** | [[paper]](https://arxiv.org/abs/2507.05707) | [code]

- [2025/06/28] **Knowledge Augmented Finetuning Matters in both RAG and Agent Based Dialog Systems** | [[paper]](https://arxiv.org/abs/2506.22852) | [code]

- [2025/06/04] **Go-Browse: Training Web Agents with Structured Exploration** | [[paper]](https://arxiv.org/abs/2506.03533) | [code]

- [2025/06/02] **AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning** | [[paper]](https://arxiv.org/abs/2506.01391) | [code]

- [2025/05/31] **ARIA: Training Language Agents with Intention-Driven Reward Aggregation** | [[paper]](https://arxiv.org/abs/2506.00539) | [code]

- [2025/05/28] **LaMDAgent: An Autonomous Framework for Post-Training Pipeline Optimization via LLM Agents** | [[paper]](https://arxiv.org/abs/2505.21963) | [code]

- [2025/05/27] **BehaviorSFT: Behavioral Token Conditioning for Clinical Agents Across the Proactivity Spectrum** | [[paper]](https://arxiv.org/abs/2505.21757) | [code]

- [2025/05/26] **Frictional Agent Alignment Framework: Slow Down and Don&#39;t Break Things** | [[paper]](https://arxiv.org/abs/2505.19428) | [code]

- [2025/05/26] **Training LLM-Based Agents with Synthetic Self-Reflected Trajectories and Partial Masking** | [[paper]](https://arxiv.org/abs/2505.20023) | [code]

- [2025/05/26] **MaskSearch: A Universal Pre-Training Framework to Enhance Agentic Search Capability** | [[paper]](https://arxiv.org/abs/2505.20285) | [code]

- [2025/03/05] **MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2503.03686) | [code]

- [2025/03/05] **Enhancing Collective Intelligence in Large Language Models Through Emotional Integration** | [[paper]](https://arxiv.org/abs/2503.04849) | [code]

- [2025/03/04] **ATLaS: Agent Tuning via Learning Critical Steps** | [[paper]](https://arxiv.org/abs/2503.02197) | [code]

- [2025/02/24] **Training a Generally Curious Agent** | [[paper]](https://arxiv.org/abs/2502.17543) | [code]

- [2025/02/19] **UM_FHS at TREC 2024 PLABA: Exploration of Fine-tuning and AI agent approach for plain language adaptations of biomedical text** | [[paper]](https://arxiv.org/abs/2502.14144) | [code]

- [2025/02/18] **Training Turn-by-Turn Verifiers for Dialogue Tutoring Agents: The Curious Case of LLMs as Your Coding Tutors** | [[paper]](https://arxiv.org/abs/2502.13311) | [code]

- [2025/02/11] **Multi-Agent Collaboration for Multilingual Code Instruction Tuning** | [[paper]](https://arxiv.org/abs/2502.07487) | [code]

- [2025/02/10] **Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training** | [[paper]](https://arxiv.org/abs/2502.06589) | [code]

- [2025/01/10] **Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains** | [[paper]](https://arxiv.org/abs/2501.05707) | [code]

- [2025/01/03] **AgentRefine: Enhancing Agent Generalization through Refinement Tuning** | [[paper]](https://arxiv.org/abs/2501.01702) | [code]

- [2024/12/30] **Training Software Engineering Agents and Verifiers with SWE-Gym** | [[paper]](https://arxiv.org/abs/2412.21139) | [code]

- [2024/12/30] **Aviary: training language agents on challenging scientific tasks** | [[paper]](https://arxiv.org/abs/2412.21154) | [code]

- [2024/12/16] **Virtual Agent-Based Communication Skills Training to Facilitate Health Persuasion Among Peers** | [[paper]](https://arxiv.org/abs/2412.12061) | [code]

- [2024/11/29] **Training Agents with Weakly Supervised Feedback from Large Language Models** | [[paper]](https://arxiv.org/abs/2411.19547) | [code]

- [2024/11/21] **Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning** | [[paper]](https://arxiv.org/abs/2411.14497) | [code]

- [2024/10/20] **Training Language Models to Critique With Multi-agent Feedback** | [[paper]](https://arxiv.org/abs/2410.15287) | [code]

- [2024/10/16] **Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance** | [[paper]](https://arxiv.org/abs/2410.12361) | [code]

- [2024/10/10] **AgentBank: Towards Generalized LLM Agents via Fine-Tuning on 50000+ Interaction Trajectories** | [[paper]](https://arxiv.org/abs/2410.07706) | [code]

- [2024/07/25] **Recursive Introspection: Teaching Language Model Agents How to Self-Improve** | [[paper]](https://arxiv.org/abs/2407.18219) | [code]

- [2024/06/11] **CoEvol: Constructing Better Responses for Instruction Finetuning through Multi-Agent Cooperation** | [[paper]](https://arxiv.org/abs/2406.07054) | [[code]](https://github.com/lirenhao1997/coevol)

- [2024/04/05] **Social Skill Training with Large Language Models** | [[paper]](https://arxiv.org/abs/2404.04204) | [code]

- [2024/04/02] **CMAT: A Multi-Agent Collaboration Tuning Framework for Enhancing Small Language Models** | [[paper]](https://arxiv.org/abs/2404.01663) | [code]

- [2024/03/29] **Enhancing the General Agent Capabilities of Low-Parameter LLMs through Tuning and Multi-Branch Reasoning** | [[paper]](https://arxiv.org/abs/2403.19962) | [code]

- [2024/03/21] **ReAct Meets ActRe: When Language Agents Enjoy Training Data Autonomy** | [[paper]](https://arxiv.org/abs/2403.14589) | [code]

- [2024/03/19] **Agent-FLAN: Designing Data and Methods of Effective Agent Tuning for Large Language Models** | [[paper]](https://arxiv.org/abs/2403.12881) | [code]

- [2024/02/23] **AgentOhana: Design Unified Data and Training Pipeline for Effective Agent Learning** | [[paper]](https://arxiv.org/abs/2402.15506) | [code]

- [2024/02/21] **Neeko: Leveraging Dynamic LoRA for Efficient Multi-Character Role-Playing Agent** | [[paper]](https://arxiv.org/abs/2402.13717) | [code]

- [2024/02/18] **Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents** | [[paper]](https://arxiv.org/abs/2402.11651) | [code]

- [2024/01/10] **Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training** | [[paper]](https://arxiv.org/abs/2401.05566) | [code]

- [2024/01/05] **From LLM to Conversational Agent: A Memory Enhanced Architecture with Fine-Tuning of Large Language Models** | [[paper]](https://arxiv.org/abs/2401.02777) | [code]

- [2023/12/22] **Pangu-Agent: A Fine-Tunable Generalist Agent with Structured Reasoning** | [[paper]](https://arxiv.org/abs/2312.14878) | [code]

- [2023/11/28] **Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld** | [[paper]](https://arxiv.org/abs/2311.16714) | [code]

- [2023/10/19] **AgentTuning: Enabling Generalized Agent Abilities for LLMs** | [[paper]](https://arxiv.org/abs/2310.12823) | [code]

- [2023/10/09] **FireAct: Toward Language Agent Fine-tuning** | [[paper]](https://arxiv.org/abs/2310.05915) | [code]

- [2023/05/26] **Training Socially Aligned Language Models on Simulated Social Interactions** | [[paper]](https://arxiv.org/abs/2305.16960) | [code]

#### RL
- [2025/07/03] **MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent** | [[paper]](https://arxiv.org/abs/2507.02259) | [code]

- [2025/07/03] **RLVER: Reinforcement Learning with Verifiable Emotion Rewards for Empathetic Agents** | [[paper]](https://arxiv.org/abs/2507.03112) | [code]

- [2025/07/02] **OpenTable-R1: A Reinforcement Learning Augmented Tool Agent for Open-Domain Table Question Answering** | [[paper]](https://arxiv.org/abs/2507.03018) | [code]

- [2025/06/30] **L0: Reinforcement Learning to Become General Agents** | [[paper]](https://arxiv.org/abs/2506.23667) | [code]

- [2025/06/30] **Auto-TA: Towards Scalable Automated Thematic Analysis (TA) via Multi-Agent Large Language Models with Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2506.23998) | [code]

- [2025/06/30] **SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2506.24119) | [code]

- [2025/06/24] **KnowRL: Exploring Knowledgeable Reinforcement Learning for Factuality** | [[paper]](https://arxiv.org/abs/2506.19807) | [code]

- [2025/06/16] **Language Agents for Hypothesis-driven Clinical Decision Making with Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2506.13474) | [code]

- [2025/06/13] **Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards** | [[paper]](https://arxiv.org/abs/2506.11425) | [code]

- [2025/05/29] **ML-Agent: Reinforcing LLM Agents for Autonomous Machine Learning Engineering** | [[paper]](https://arxiv.org/abs/2505.23723) | [code]

- [2025/05/28] **WorkForceAgent-R1: Incentivizing Reasoning Capability in LLM-based Web Agents via Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2505.22942) | [code]

- [2025/05/28] **WebDancer: Towards Autonomous Information Seeking Agency** | [[paper]](https://arxiv.org/abs/2505.22648) | [[code]](https://github.com/Alibaba-NLP/WebAgent)

- [2025/05/27] **SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution** | [[paper]](https://arxiv.org/abs/2505.20732) | [[code]](https://github.com/WangHanLinHenry/SPA-RL-Agent)

- [2025/05/26] **DoctorAgent-RL: A Multi-Agent Collaborative Reinforcement Learning System for Multi-Turn Clinical Dialogue** | [[paper]](https://arxiv.org/abs/2505.19630) | [code]

- [2025/05/26] **REARANK: Reasoning Re-ranking Agent via Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2505.20046) | [code]

- [2025/05/22] **WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2505.16421) | [code]

- [2025/05/21] **An Empirical Study on Reinforcement Learning for Reasoning-Search Interleaved LLM Agents** | [[paper]](https://arxiv.org/abs/2505.15117) | [code]

- [2025/05/20] **Reinforcing Question Answering Agents with Minimalist Policy Gradient Optimization** | [[paper]](https://arxiv.org/abs/2505.17086) | [code]

- [2025/05/20] **s3: You Don&#39;t Need That Much Data to Train a Search Agent via RL** | [[paper]](https://arxiv.org/abs/2505.14146) | [code]

- [2025/05/17] **Retrospex: Language Agent Meets Offline Reinforcement Learning Critic** | [[paper]](https://arxiv.org/abs/2505.11807) | [code]

- [2025/05/06] **Divide, Optimize, Merge: Fine-Grained LLM Agent Optimization at Scale** | [[paper]](https://arxiv.org/abs/2505.03973) | [code]

- [2025/04/24] **RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2504.20073) | [code]

- [2025/04/20] **Meta-Thinking in LLMs via Multi-Agent Reinforcement Learning: A Survey** | [[paper]](https://arxiv.org/abs/2504.14520) | [code]

- [2025/04/04] **Learning Natural Language Constraints for Safe Reinforcement Learning of Language Agents** | [[paper]](https://arxiv.org/abs/2504.03185) | [code]

- [2025/03/16] **LLM-Mediated Guidance of MARL Systems** | [[paper]](https://arxiv.org/abs/2503.13553) | [code]

- [2025/03/12] **ReMA: Learning to Meta-think for LLMs with Multi-Agent Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2503.09501) | [code]

- [2025/03/03] **Improving Retrospective Language Agents via Joint Policy Gradient Optimization** | [[paper]](https://arxiv.org/abs/2503.01490) | [code]

- [2025/02/25] **AgentRM: Enhancing Agent Generalization with Reward Modeling** | [[paper]](https://arxiv.org/abs/2502.18407) | [code]

- [2025/02/09] **Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2502.06060) | [code]

- [2025/02/06] **Multi-Agent Reinforcement Learning with Focal Diversity Optimization** | [[paper]](https://arxiv.org/abs/2502.04492) | [code]

- [2025/01/25] **Improving Retrieval-Augmented Generation through Multi-Agent Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2501.15228) | [code]

- [2024/11/26] **LLM-Based Offline Learning for Embodied Agents via Consistency-Guided Reward Ensemble** | [[paper]](https://arxiv.org/abs/2411.17135) | [code]

- [2024/11/07] **Interactive Dialogue Agents via Reinforcement Learning on Hindsight Regenerations** | [[paper]](https://arxiv.org/abs/2411.05194) | [code]

- [2024/11/06] **From Novice to Expert: LLM Agent Policy Optimization via Step-wise Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2411.03817) | [code]

- [2024/11/04] **WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2411.02337) | [code]

- [2024/10/11] **Words as Beacons: Guiding RL Agents with High-Level Language Prompts** | [[paper]](https://arxiv.org/abs/2410.08632) | [code]

- [2024/10/10] **MACPO: Weak-to-Strong Alignment via Multi-Agent Contrastive Preference Optimization** | [[paper]](https://arxiv.org/abs/2410.07672) | [code]

- [2024/07/02] **Predicting vs. Acting: A Trade-off Between World Modeling &amp; Agent Modeling** | [[paper]](https://arxiv.org/abs/2407.02446) | [code]

- [2024/06/26] **Mental Modeling of Reinforcement Learning Agents by Language Models** | [[paper]](https://arxiv.org/abs/2406.18505) | [code]

- [2024/06/17] **Input Conditioned Graph Generation for Language Agents** | [[paper]](https://arxiv.org/abs/2406.11555) | [[code]](https://github.com/lukasvierling/dynamicgptswarm)

- [2024/06/05] **LLM-based Rewriting of Inappropriate Argumentation using Reinforcement Learning from Machine Feedback** | [[paper]](https://arxiv.org/abs/2406.03363) | [code]

- [2024/06/03] **Re-ReST: Reflection-Reinforced Self-Training for Language Agents** | [[paper]](https://arxiv.org/abs/2406.01495) | [[code]](https://github.com/PlusLabNLP/Re-ReST)

- [2024/05/30] **Safe Multi-agent Reinforcement Learning with Natural Language Constraints** | [[paper]](https://arxiv.org/abs/2405.20018) | [code]

- [2024/05/17] **LLM-based Multi-Agent Reinforcement Learning: Current and Future Directions** | [[paper]](https://arxiv.org/abs/2405.11106) | [code]

- [2024/05/16] **Fine-Tuning Large Vision-Language Models as Decision-Making Agents via Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2405.10292) | [code]

- [2024/05/01] **Navigating WebAI: Training Agents to Complete Web Tasks with Large Language Models and Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2405.00516) | [code]

- [2024/03/05] **Language Guided Exploration for RL Agents in Text Environments** | [[paper]](https://arxiv.org/abs/2403.03141) | [code]

- [2024/02/17] **Offline Training of Language Model Agents with Functions as Learnable Weights** | [[paper]](https://arxiv.org/abs/2402.11359) | [code]

- [2024/02/02] **StepCoder: Improve Code Generation with Reinforcement Learning from Compiler Feedback** | [[paper]](https://arxiv.org/abs/2402.01391) | [code]

- [2023/10/25] **MultiPrompter: Cooperative Prompt Optimization with Multi-Agent Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2310.16730) | [code]

- [2023/03/29] **Skill Reinforcement Learning and Planning for Open-World Long-Horizon Tasks** | [[paper]](https://arxiv.org/abs/2303.16563) | [code]

#### DPO
- [2025/06/17] **Expectation Confirmation Preference Optimization for Multi-Turn Conversational Recommendation Agent** | [[paper]](https://arxiv.org/abs/2506.14302) | [code]

- [2025/06/04] **Debate, Reflect, and Distill: Multi-Agent Feedback with Tree-Structured Preference Optimization for Efficient Language Model Enhancement** | [[paper]](https://arxiv.org/abs/2506.03541) | [code]

- [2025/06/02] **PGPO: Enhancing Agent Reasoning via Pseudocode-style Planning Guided Preference Optimization** | [[paper]](https://arxiv.org/abs/2506.01475) | [code]

- [2025/05/26] **MaskSearch: A Universal Pre-Training Framework to Enhance Agentic Search Capability** | [[paper]](https://arxiv.org/abs/2505.20285) | [code]

- [2025/05/04] **Adaptive Thinking via Mode Policy Optimization for Social Language Agents** | [[paper]](https://arxiv.org/abs/2505.02156) | [code]

- [2025/04/27] **Anyprefer: An Agentic Framework for Preference Data Synthesis** | [[paper]](https://arxiv.org/abs/2504.19276) | [code]

- [2025/02/26] **Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems** | [[paper]](https://arxiv.org/abs/2502.19328) | [[code]](https://github.com/THU-KEG/Agentic-Reward-Modeling)

- [2025/01/03] **SDPO: Segment-Level Direct Preference Optimization for Social Agents** | [[paper]](https://arxiv.org/abs/2501.01821) | [code]

- [2024/10/29] **Flow-DPO: Improving LLM Mathematical Reasoning through Online Multi-Agent Learning** | [[paper]](https://arxiv.org/abs/2410.22304) | [code]

- [2024/05/31] **Learning to Clarify: Multi-turn Conversations with Action-Based Contrastive Self-Training** | [[paper]](https://arxiv.org/abs/2406.00222) | [code]

### Scaling
#### Single-Agent Framework
- [2025/07/08] **Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving** | [[paper]](https://arxiv.org/abs/2507.06229) | [code]

- [2025/07/04] **GRAFT: A Graph-based Flow-aware Agentic Framework for Document-level Machine Translation** | [[paper]](https://arxiv.org/abs/2507.03311) | [code]

- [2025/06/29] **AURA: Agent for Understanding, Reasoning, and Automated Tool Use in Voice-Driven Tasks** | [[paper]](https://arxiv.org/abs/2506.23049) | [code]

- [2025/06/27] **A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis** | [[paper]](https://arxiv.org/abs/2507.02938) | [code]

- [2025/06/17] **VIDEE: Visual and Interactive Decomposition, Execution, and Evaluation of Text Analytics with Intelligent Agents** | [[paper]](https://arxiv.org/abs/2506.21582) | [code]

- [2025/06/17] **OAgents: An Empirical Study of Building Effective Agents** | [[paper]](https://arxiv.org/abs/2506.15741) | [code]

- [2025/06/16] **Leveraging In-Context Learning for Language Model Agents** | [[paper]](https://arxiv.org/abs/2506.13109) | [code]

- [2025/06/14] **Towards Building General Purpose Embedding Models for Industry 4.0 Agents** | [[paper]](https://arxiv.org/abs/2506.12607) | [code]

- [2025/06/12] **AutoMind: Adaptive Knowledgeable Agent for Automated Data Science** | [[paper]](https://arxiv.org/abs/2506.10974) | [code]

- [2025/06/03] **DIAMOND: An LLM-Driven Agent for Context-Aware Baseball Highlight Summarization** | [[paper]](https://arxiv.org/abs/2506.02351) | [code]

- [2025/06/03] **Comparative Analysis of AI Agent Architectures for Entity Relationship Classification** | [[paper]](https://arxiv.org/abs/2506.02426) | [code]

- [2025/06/02] **Self-Challenging Language Model Agents** | [[paper]](https://arxiv.org/abs/2506.01716) | [code]

- [2025/05/30] **NexusSum: Hierarchical LLM Agents for Long-Form Narrative Summarization** | [[paper]](https://arxiv.org/abs/2505.24575) | [code]

- [2025/05/21] **ViQAgent: Zero-Shot Video Question Answering via Agent with Open-Vocabulary Grounding Validation** | [[paper]](https://arxiv.org/abs/2505.15928) | [code]

- [2025/05/20] **ContextAgent: Context-Aware Proactive LLM Agents with Open-World Sensory Perceptions** | [[paper]](https://arxiv.org/abs/2505.14668) | [code]

- [2025/05/12] **Putting It All into Context: Simplifying Agents with LCLMs** | [[paper]](https://arxiv.org/abs/2505.08120) | [code]

- [2025/04/17] **Pandora: A Code-Driven Large Language Model Agent for Unified Reasoning Across Diverse Structured Knowledge** | [[paper]](https://arxiv.org/abs/2504.12734) | [code]

- [2025/04/11] **Toward Super Agent System with Hybrid AI Routers** | [[paper]](https://arxiv.org/abs/2504.10519) | [code]

- [2025/04/10] **AgentAda: Skill-Adaptive Data Analytics for Tailored Insight Discovery** | [[paper]](https://arxiv.org/abs/2504.07421) | [code]

- [2025/04/07] **DoCIA: An Online Document-Level Context Incorporation Agent for Speech Translation** | [[paper]](https://arxiv.org/abs/2504.05122) | [code]

- [2025/03/20] **Do Visual Imaginations Improve Vision-and-Language Navigation Agents?** | [[paper]](https://arxiv.org/abs/2503.16394) | [code]

- [2025/03/14] **Large Reasoning Models in Agent Scenarios: Exploring the Necessity of Reasoning Capabilities** | [[paper]](https://arxiv.org/abs/2503.11074) | [code]

- [2025/03/10] **DatawiseAgent: A Notebook-Centric LLM Agent Framework for Automated Data Science** | [[paper]](https://arxiv.org/abs/2503.07044) | [code]

- [2025/03/10] **ASTRA: A Negotiation Agent with Adaptive and Strategic Reasoning through Action in Dynamic Offer Optimization** | [[paper]](https://arxiv.org/abs/2503.07129) | [code]

- [2025/02/26] **TheoremExplainAgent: Towards Multimodal Explanations for LLM Theorem Understanding** | [[paper]](https://arxiv.org/abs/2502.19400) | [code]

- [2025/02/14] **Agentic Verification for Ambiguous Query Disambiguation** | [[paper]](https://arxiv.org/abs/2502.10352) | [code]

- [2025/02/12] **SPeCtrum: A Grounded Framework for Multidimensional Identity Representation in LLM-Based Agent** | [[paper]](https://arxiv.org/abs/2502.08599) | [code]

- [2025/02/09] **AutoAgent: A Fully-Automated and Zero-Code Framework for LLM Agents** | [[paper]](https://arxiv.org/abs/2502.05957) | [code]

- [2025/02/04] **Adaptive Self-improvement LLM Agentic System for ML Library Development** | [[paper]](https://arxiv.org/abs/2502.02534) | [code]

- [2025/01/31] **Enabling Autonomic Microservice Management through Self-Learning Agents** | [[paper]](https://arxiv.org/abs/2501.19056) | [code]

- [2024/12/28] **OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System** | [[paper]](https://arxiv.org/abs/2412.20005) | [code]

- [2024/12/21] **Self-guided Knowledgeable Network of Thoughts: Amplifying Reasoning with Large Language Models** | [[paper]](https://arxiv.org/abs/2412.16533) | [code]

- [2024/12/15] **AgentPS: Agentic Process Supervision for Multi-modal Content Quality Assurance through Multi-round QA** | [[paper]](https://arxiv.org/abs/2412.15251) | [code]

- [2024/12/11] **A Multimodal Social Agent** | [[paper]](https://arxiv.org/abs/2501.06189) | [code]

- [2024/12/11] **Federated In-Context LLM Agent Learning** | [[paper]](https://arxiv.org/abs/2412.08054) | [code]

- [2024/12/04] **How to Correctly do Semantic Backpropagation on Language-based Agentic Systems** | [[paper]](https://arxiv.org/abs/2412.03624) | [code]

- [2024/12/02] **SAUP: Situation Awareness Uncertainty Propagation on LLM Agent** | [[paper]](https://arxiv.org/abs/2412.01033) | [code]

- [2024/12/01] **Towards Adaptive Mechanism Activation in Language Agent** | [[paper]](https://arxiv.org/abs/2412.00722) | [code]

- [2024/11/20] **MindForge: Empowering Embodied Agents with Theory of Mind for Lifelong Collaborative Learning** | [[paper]](https://arxiv.org/abs/2411.12977) | [code]

- [2024/11/16] **IntentGPT: Few-shot Intent Discovery with Large Language Models** | [[paper]](https://arxiv.org/abs/2411.10670) | [code]

- [2024/11/04] **DynaSaur: Large Language Agents Beyond Predefined Actions** | [[paper]](https://arxiv.org/abs/2411.01747) | [code]

- [2024/11/04] **CRMArena: Understanding the Capacity of LLM Agents to Perform Professional CRM Tasks in Realistic Environments** | [[paper]](https://arxiv.org/abs/2411.02305) | [code]

- [2024/10/29] **ADAM: An Embodied Causal Agent in Open-World Environments** | [[paper]](https://arxiv.org/abs/2410.22194) | [code]

- [2024/10/27] **TrajAgent: An Agent Framework for Unified Trajectory Modelling** | [[paper]](https://arxiv.org/abs/2410.20445) | [code]

- [2024/10/22] **Adsorb-Agent: Autonomous Identification of Stable Adsorption Configurations via Large Language Model Agent** | [[paper]](https://arxiv.org/abs/2410.16658) | [code]

- [2024/10/11] **Encoding Agent Trajectories as Representations with Sequence Transformers** | [[paper]](https://arxiv.org/abs/2410.09204) | [code]

- [2024/10/10] **Agents Thinking Fast and Slow: A Talker-Reasoner Architecture** | [[paper]](https://arxiv.org/abs/2410.08328) | [code]

- [2024/10/08] **AgentSquare: Automatic LLM Agent Search in Modular Design Space** | [[paper]](https://arxiv.org/abs/2410.06153) | [[code]](https://github.com/tsinghua-fib-lab/AgentSquare)

- [2024/10/08] **Applying Refusal-Vector Ablation to Llama 3.1 70B Agents** | [[paper]](https://arxiv.org/abs/2410.10871) | [code]

- [2024/09/24] **MOSS: Enabling Code-Driven Evolution and Context Management for AI Agents** | [[paper]](https://arxiv.org/abs/2409.16120) | [code]

- [2024/09/19] **Textualized Agent-Style Reasoning for Complex Tasks by Multiple Round LLM Generation** | [[paper]](https://arxiv.org/abs/2409.12411) | [code]

- [2024/09/15] **Automatic Control With Human-Like Reasoning: Exploring Language Model Embodied Air Traffic Agents** | [[paper]](https://arxiv.org/abs/2409.09717) | [code]

- [2024/09/12] **Self-Supervised Inference of Agents in Trustless Environments** | [[paper]](https://arxiv.org/abs/2409.08386) | [code]

- [2024/09/05] **From MOOC to MAIC: Reshaping Online Teaching and Learning through LLM-driven Agents** | [[paper]](https://arxiv.org/abs/2409.03512) | [code]

- [2024/09/05] **Rx Strategist: Prescription Verification using LLM Agents System** | [[paper]](https://arxiv.org/abs/2409.03440) | [code]

- [2024/09/03] **AgentRE: An Agent-Based Framework for Navigating Complex Information Landscapes in Relation Extraction** | [[paper]](https://arxiv.org/abs/2409.01854) | [code]

- [2024/08/26] **AgentMove: A Large Language Model based Agentic Framework for Zero-shot Next Location Prediction** | [[paper]](https://arxiv.org/abs/2408.13986) | [code]

- [2024/08/19] **Anim-Director: A Large Multimodal Model Powered Agent for Controllable Animation Video Generation** | [[paper]](https://arxiv.org/abs/2408.09787) | [code]

- [2024/08/13] **Causal Agent based on Large Language Model** | [[paper]](https://arxiv.org/abs/2408.06849) | [code]

- [2024/08/02] **Coalitions of Large Language Models Increase the Robustness of AI Agents** | [[paper]](https://arxiv.org/abs/2408.01380) | [code]

- [2024/07/27] **AgentPeerTalk: Empowering Students through Agentic-AI-Driven Discernment of Bullying and Joking in Peer Interactions in Schools** | [[paper]](https://arxiv.org/abs/2408.01459) | [code]

- [2024/07/25] **Enhancing Agent Learning through World Dynamics Modeling** | [[paper]](https://arxiv.org/abs/2407.17695) | [code]

- [2024/07/25] **RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models** | [[paper]](https://arxiv.org/abs/2407.18035) | [code]

- [2024/07/16] **Preemptive Detection and Correction of Misaligned Actions in LLM Agents** | [[paper]](https://arxiv.org/abs/2407.11843) | [code]

- [2024/07/15] **Sibyl: Simple yet Effective Agent Framework for Complex Real-world Reasoning** | [[paper]](https://arxiv.org/abs/2407.10718) | [code]

- [2024/07/02] **Beyond Numeric Awards: In-Context Dueling Bandits with LLM Agents** | [[paper]](https://arxiv.org/abs/2407.01887) | [code]

- [2024/06/24] **OmAgent: A Multi-modal Agent Framework for Complex Video Understanding with Task Divide-and-Conquer** | [[paper]](https://arxiv.org/abs/2406.16620) | [code]

- [2024/06/07] **SelfGoal: Your Language Agents Already Know How to Achieve High-level Goals** | [[paper]](https://arxiv.org/abs/2406.04784) | [code]

- [2024/05/25] **AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning** | [[paper]](https://arxiv.org/abs/2405.16247) | [code]

- [2024/05/24] **Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models** | [[paper]](https://arxiv.org/abs/2405.15143) | [[code]](https://github.com/conglu1997/intelligent-go-explore)

- [2024/05/16] **Agent Design Pattern Catalogue: A Collection of Architectural Patterns for Foundation Model based Agents** | [[paper]](https://arxiv.org/abs/2405.10467) | [code]

- [2024/04/30] **Large Language Model Agent for Fake News Detection** | [[paper]](https://arxiv.org/abs/2405.01593) | [code]

- [2024/04/28] **Logic Agent: Enhancing Validity with Logic Rule Invocation** | [[paper]](https://arxiv.org/abs/2404.18130) | [code]

- [2024/04/13] **LLMSat: A Large Language Model-Based Goal-Oriented Agent for Autonomous Space Exploration** | [[paper]](https://arxiv.org/abs/2405.01392) | [code]

- [2024/04/01] **TraveLER: A Modular Multi-LMM Agent Framework for Video Question-Answering** | [[paper]](https://arxiv.org/abs/2404.01476) | [code]

- [2024/03/29] **ITCMA: A Generative Agent Based on a Computational Consciousness Structure** | [[paper]](https://arxiv.org/abs/2403.20097) | [code]

- [2024/02/25] **Bootstrapping Cognitive Agents with a Large Language Model** | [[paper]](https://arxiv.org/abs/2403.00810) | [code]

- [2024/02/24] **Empowering Large Language Model Agents through Action Learning** | [[paper]](https://arxiv.org/abs/2402.15809) | [[code]](https://github.com/zhao-ht/learnact)

- [2024/02/20] **Soft Self-Consistency Improves Language Model Agents** | [[paper]](https://arxiv.org/abs/2402.13212) | [code]

- [2024/02/04] **NavHint: Vision and Language Navigation Agent with a Hint Generator** | [[paper]](https://arxiv.org/abs/2402.02559) | [code]

- [2024/01/05] **AFSPP: Agent Framework for Shaping Preference and Personality with Large Language Models** | [[paper]](https://arxiv.org/abs/2401.02870) | [code]

- [2023/11/23] **Controlling Large Language Model-based Agents for Large-Scale Decision-Making: An Actor-Critic Approach** | [[paper]](https://arxiv.org/abs/2311.13884) | [code]

- [2023/11/02] **ProAgent: From Robotic Process Automation to Agentic Process Automation** | [[paper]](https://arxiv.org/abs/2311.10751) | [code]

- [2023/10/16] **CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization** | [[paper]](https://arxiv.org/abs/2310.10134) | [code]

- [2023/09/29] **Reason for Future, Act for Now: A Principled Framework for Autonomous LLM Agents with Provable Sample Efficiency** | [[paper]](https://arxiv.org/abs/2309.17382) | [code]

- [2023/09/14] **Agents: An Open-source Framework for Autonomous Language Agents** | [[paper]](https://arxiv.org/abs/2309.07870) | [code]

- [2023/09/08] **A Versatile Graph Learning Approach through LLM-based Agent** | [[paper]](https://arxiv.org/abs/2309.04565) | [code]

- [2023/09/05] **Cognitive Architectures for Language Agents** | [[paper]](https://arxiv.org/abs/2309.02427) | [code]

- [2023/05/27] **SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks** | [[paper]](https://arxiv.org/abs/2305.17390) | [code]

- [2023/05/25] **Voyager: An Open-Ended Embodied Agent with Large Language Models** | [[paper]](https://arxiv.org/abs/2305.16291) | [code]

#### Multi-Agent System
- [2025/07/09] **Pun Intended: Multi-Agent Translation of Wordplay with Contrastive Learning and Phonetic-Semantic Embeddings** | [[paper]](https://arxiv.org/abs/2507.06506) | [code]

- [2025/07/09] **MIND: A Multi-agent Framework for Zero-shot Harmful Meme Detection** | [[paper]](https://arxiv.org/abs/2507.06908) | [code]

- [2025/06/27] **GenEscape: Hierarchical Multi-Agent Generation of Escape Room Puzzles** | [[paper]](https://arxiv.org/abs/2506.21839) | [code]

- [2025/06/20] **SysTemp: A Multi-Agent System for Template-Based Generation of SysML v2** | [[paper]](https://arxiv.org/abs/2506.21608) | [code]

- [2025/06/19] **StoryWriter: A Multi-Agent Framework for Long Story Generation** | [[paper]](https://arxiv.org/abs/2506.16445) | [code]

- [2025/06/18] **AgentGroupChat-V2: Divide-and-Conquer Is What LLM-Based Multi-Agent System Need** | [[paper]](https://arxiv.org/abs/2506.15451) | [code]

- [2025/06/17] **MAS-LitEval : Multi-Agent System for Literary Translation Quality Assessment** | [[paper]](https://arxiv.org/abs/2506.14199) | [code]

- [2025/06/17] **Xolver: Multi-Agent Reasoning with Holistic Experience Learning Just Like an Olympiad Team** | [[paper]](https://arxiv.org/abs/2506.14234) | [code]

- [2025/06/13] **A Hybrid Multi-Agent Prompting Approach for Simplifying Complex Sentences** | [[paper]](https://arxiv.org/abs/2506.11681) | [code]

- [2025/06/13] **AutoGen Driven Multi Agent Framework for Iterative Crime Data Analysis and Prediction** | [[paper]](https://arxiv.org/abs/2506.11475) | [code]

- [2025/06/13] **Investigating the Potential of Large Language Model-Based Router Multi-Agent Architectures for Foundation Design Automation: A Task Classification and Expert Selection Study** | [[paper]](https://arxiv.org/abs/2506.13811) | [code]

- [2025/06/12] **A Multi-Agent Probabilistic Inference Framework Inspired by Kairanban-Style CoT System with IdoBata Conversation for Debiasing** | [[paper]](https://arxiv.org/abs/2506.21565) | [code]

- [2025/06/11] **Multi-Agent Language Models: Advancing Cooperation, Coordination, and Adaptation** | [[paper]](https://arxiv.org/abs/2506.09331) | [code]

- [2025/06/11] **ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning** | [[paper]](https://arxiv.org/abs/2506.09513) | [code]

- [2025/06/11] **Chat-of-Thought: Collaborative Multi-Agent System for Generating Domain Specific Information** | [[paper]](https://arxiv.org/abs/2506.10086) | [code]

- [2025/06/10] **CAF-I: A Collaborative Multi-Agent Framework for Enhanced Irony Detection with Large Language Models** | [[paper]](https://arxiv.org/abs/2506.08430) | [code]

- [2025/06/10] **Reinforce LLM Reasoning through Multi-Agent Reflection** | [[paper]](https://arxiv.org/abs/2506.08379) | [code]

- [2025/06/09] **From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reasoning via Bayesian Nash Equilibrium** | [[paper]](https://arxiv.org/abs/2506.08292) | [code]

- [2025/06/08] **Theorem-of-Thought: A Multi-Agent Framework for Abductive, Deductive, and Inductive Reasoning in Language Models** | [[paper]](https://arxiv.org/abs/2506.07106) | [code]

- [2025/06/06] **MAPLE: Multi-Agent Adaptive Planning with Long-Term Memory for Table Reasoning** | [[paper]](https://arxiv.org/abs/2506.05813) | [code]

- [2025/06/06] **Does It Run and Is That Enough? Revisiting Text-to-Chart Generation with a Multi-Agent Approach** | [[paper]](https://arxiv.org/abs/2506.06175) | [code]

- [2025/06/05] **Demonstrations of Integrity Attacks in Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2506.04572) | [code]

- [2025/06/04] **CLAIM: An Intent-Driven Multi-Agent Framework for Analyzing Manipulation in Courtroom Dialogues** | [[paper]](https://arxiv.org/abs/2506.04131) | [code]

- [2025/06/03] **MASTER: Enhancing Large Language Model via Multi-Agent Simulated Teaching** | [[paper]](https://arxiv.org/abs/2506.02689) | [code]

- [2025/06/03] **Adaptive Graph Pruning for Multi-Agent Communication** | [[paper]](https://arxiv.org/abs/2506.02951) | [code]

- [2025/06/03] **A Multi-Agent Framework for Mitigating Dialect Biases in Privacy Policy Question-Answering Systems** | [[paper]](https://arxiv.org/abs/2506.02998) | [code]

- [2025/06/03] **Mitigating Manipulation and Enhancing Persuasion: A Reflective Multi-Agent Approach for Legal Argument Generation** | [[paper]](https://arxiv.org/abs/2506.02992) | [code]

- [2025/06/03] **MAEBE: Multi-Agent Emergent Behavior Framework** | [[paper]](https://arxiv.org/abs/2506.03053) | [code]

- [2025/06/02] **STORM-BORN: A Challenging Mathematical Derivations Dataset Curated via a Human-in-the-Loop Multi-Agent Framework** | [[paper]](https://arxiv.org/abs/2506.01531) | [code]

- [2025/06/02] **An Empirical Study of Group Conformity in Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2506.01332) | [code]

- [2025/05/31] **Goal-Aware Identification and Rectification of Misinformation in Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2506.00509) | [code]

- [2025/05/31] **PAKTON: A Multi-Agent Framework for Question Answering in Long Legal Agreements** | [[paper]](https://arxiv.org/abs/2506.00608) | [code]

- [2025/05/30] **CREFT: Sequential Multi-Agent LLM for Character Relation Extraction** | [[paper]](https://arxiv.org/abs/2505.24553) | [code]

- [2025/05/30] **Multiple LLM Agents Debate for Equitable Cultural Alignment** | [[paper]](https://arxiv.org/abs/2505.24671) | [code]

- [2025/05/30] **An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring** | [[paper]](https://arxiv.org/abs/2505.24239) | [code]

- [2025/05/29] **Cross-Task Experiential Learning on LLM-based Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2505.23187) | [code]

- [2025/05/29] **OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation** | [[paper]](https://arxiv.org/abs/2505.23885) | [code]

- [2025/05/28] **Co-Saving: Resource Aware Multi-Agent Collaboration for Software Development** | [[paper]](https://arxiv.org/abs/2505.21898) | [code]

- [2025/05/28] **CoMaPOI: A Collaborative Multi-Agent Framework for Next POI Prediction Bridging the Gap Between Trajectory and Language** | [[paper]](https://arxiv.org/abs/2505.23837) | [code]

- [2025/05/28] **GETReason: Enhancing Image Context Extraction through Hierarchical Multi-Agent Reasoning** | [[paper]](https://arxiv.org/abs/2505.21863) | [code]

- [2025/05/27] **Long Context Scaling: Divide and Conquer via Multi-Agent Question-driven Collaboration** | [[paper]](https://arxiv.org/abs/2505.20625) | [code]

- [2025/05/27] **Rethinking Information Synthesis in Multimodal Question Answering A Multi-Agent Perspective** | [[paper]](https://arxiv.org/abs/2505.20816) | [code]

- [2025/05/27] **Scaling External Knowledge Input Beyond Context Windows of LLMs via Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2505.21471) | [code]

- [2025/05/26] **CoTGuard: Using Chain-of-Thought Triggering for Copyright Protection in Multi-Agent LLM Systems** | [[paper]](https://arxiv.org/abs/2505.19405) | [code]

- [2025/05/26] **Multi-Agent Collaboration via Evolving Orchestration** | [[paper]](https://arxiv.org/abs/2505.19591) | [code]

- [2025/05/26] **Select, Read, and Write: A Multi-Agent Framework of Full-Text-based Related Work Generation** | [[paper]](https://arxiv.org/abs/2505.19647) | [code]

- [2025/05/26] **Project Riley: Multimodal Multi-Agent LLM Collaboration with Emotional Reasoning and Voting** | [[paper]](https://arxiv.org/abs/2505.20521) | [code]

- [2025/05/25] **MetaMind: Modeling Human Social Thoughts with Metacognitive Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2505.18943) | [code]

- [2025/05/25] **GUARDIAN: Safeguarding LLM Multi-Agent Collaborations with Temporal Graph Modeling** | [[paper]](https://arxiv.org/abs/2505.19234) | [code]

- [2025/05/23] **ManuSearch: Democratizing Deep Search in Large Language Models with a Transparent and Open Multi-Agent Framework** | [[paper]](https://arxiv.org/abs/2505.18105) | [code]

- [2025/05/23] **PD$^3$: A Project Duplication Detection Framework via Adapted Multi-Agent Debate** | [[paper]](https://arxiv.org/abs/2505.17492) | [code]

- [2025/05/22] **EMULATE: A Multi-Agent Framework for Determining the Veracity of Atomic Claims by Emulating Human Actions** | [[paper]](https://arxiv.org/abs/2505.16576) | [code]

- [2025/05/22] **X-MAS: Towards Building Multi-Agent Systems with Heterogeneous LLMs** | [[paper]](https://arxiv.org/abs/2505.16997) | [code]

- [2025/05/21] **MAS-ZERO: Designing Multi-Agent Systems with Zero Supervision** | [[paper]](https://arxiv.org/abs/2505.14996) | [code]

- [2025/05/20] **MAATS: A Multi-Agent Automated Translation System Based on MQM Evaluation** | [[paper]](https://arxiv.org/abs/2505.14848) | [code]

- [2025/05/20] **MLZero: A Multi-Agent System for End-to-end Machine Learning Automation** | [[paper]](https://arxiv.org/abs/2505.13941) | [code]

- [2025/05/19] **AD-AGENT: A Multi-agent Framework for End-to-end Anomaly Detection** | [[paper]](https://arxiv.org/abs/2505.12594) | [code]

- [2025/05/18] **IP Leakage Attacks Targeting LLM-Based Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2505.12442) | [code]

- [2025/05/17] **BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering** | [[paper]](https://arxiv.org/abs/2505.11811) | [code]

- [2025/05/16] **Connecting the Dots: A Chain-of-Collaboration Prompting Framework for LLM Agents** | [[paper]](https://arxiv.org/abs/2505.10936) | [code]

- [2025/05/15] **Assessing Collective Reasoning in Multi-Agent LLMs via Hidden Profile Tasks** | [[paper]](https://arxiv.org/abs/2505.11556) | [code]

- [2025/05/12] **Towards Multi-Agent Reasoning Systems for Collaborative Expertise Delegation: An Exploratory Design Study** | [[paper]](https://arxiv.org/abs/2505.07313) | [code]

- [2025/05/06] **The Power of Stories: Narrative Priming Shapes How LLM Agents Collaborate and Compete** | [[paper]](https://arxiv.org/abs/2505.03961) | [code]

- [2025/04/30] **Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2505.00212) | [code]

- [2025/04/26] **MATCHA: Can Multi-Agent Collaboration Build a Trustworthy Conversational Recommender?** | [[paper]](https://arxiv.org/abs/2504.20094) | [code]

- [2025/04/24] **Collaborating Action by Action: A Multi-agent LLM Framework for Embodied Reasoning** | [[paper]](https://arxiv.org/abs/2504.17950) | [code]

- [2025/04/23] **Less is More: Enhancing Structured Multi-Agent Reasoning via Quality-Guided Distillation** | [[paper]](https://arxiv.org/abs/2504.16408) | [code]

- [2025/04/21] **EducationQ: Evaluating LLMs&#39; Teaching Capabilities Through Multi-Agent Dialogue Framework** | [[paper]](https://arxiv.org/abs/2504.14928) | [code]

- [2025/04/17] **Are AI agents the new machine translation frontier? Challenges and opportunities of single- and multi-agent systems for multilingual digital communication** | [[paper]](https://arxiv.org/abs/2504.12891) | [code]

- [2025/04/15] **X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents** | [[paper]](https://arxiv.org/abs/2504.13203) | [code]

- [2025/04/11] **Beyond Self-Reports: Multi-Observer Agents for Personality Assessment in Large Language Models** | [[paper]](https://arxiv.org/abs/2504.08399) | [code]

- [2025/04/11] **DocAgent: A Multi-Agent System for Automated Code Documentation Generation** | [[paper]](https://arxiv.org/abs/2504.08725) | [code]

- [2025/04/08] **FactGuard: Leveraging Multi-Agent Systems to Generate Answerable and Unanswerable Questions for Enhanced Long-Context LLM Extraction** | [[paper]](https://arxiv.org/abs/2504.05607) | [code]

- [2025/04/04] **YaleNLP @ PerAnsSumm 2025: Multi-Perspective Integration via Mixture-of-Agents for Enhanced Healthcare QA Summarization** | [[paper]](https://arxiv.org/abs/2504.03932) | [code]

- [2025/04/02] **Self-Resource Allocation in Multi-Agent LLM Systems** | [[paper]](https://arxiv.org/abs/2504.02051) | [code]

- [2025/04/02] **Achieving Unanimous Consensus in Decision Making Using Multi-Agents** | [[paper]](https://arxiv.org/abs/2504.02128) | [code]

- [2025/04/01] **When Persuasion Overrides Truth in Multi-Agent LLM Debates: Introducing a Confidence-Weighted Persuasion Override Rate (CW-POR)** | [[paper]](https://arxiv.org/abs/2504.00374) | [code]

- [2025/04/01] **AI Hiring with LLMs: A Context-Aware and Explainable Multi-Agent Framework for Resume Screening** | [[paper]](https://arxiv.org/abs/2504.02870) | [code]

- [2025/04/01] **AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2504.00587) | [code]

- [2025/03/31] **$\textit{Agents Under Siege}$: Breaking Pragmatic Multi-Agent LLM Systems with Optimized Prompt Attacks** | [[paper]](https://arxiv.org/abs/2504.00218) | [code]

- [2025/03/28] **WorkTeam: Constructing Workflows from Natural Language with Multi-Agents** | [[paper]](https://arxiv.org/abs/2503.22473) | [code]

- [2025/03/28] **Self-Evolving Multi-Agent Simulations for Realistic Clinical Interactions** | [[paper]](https://arxiv.org/abs/2503.22678) | [code]

- [2025/03/27] **Collab: Controlled Decoding using Mixture of Agents for LLM Alignment** | [[paper]](https://arxiv.org/abs/2503.21720) | [code]

- [2025/03/27] **Debate-Driven Multi-Agent LLMs for Phishing Email Detection** | [[paper]](https://arxiv.org/abs/2503.22038) | [code]

- [2025/03/26] **TAMA: A Human-AI Collaborative Thematic Analysis Framework Using Multi-Agent LLMs for Clinical Interviews** | [[paper]](https://arxiv.org/abs/2503.20666) | [code]

- [2025/03/26] **3MDBench: Medical Multimodal Multi-agent Dialogue Benchmark** | [[paper]](https://arxiv.org/abs/2504.13861) | [code]

- [2025/03/25] **Multi-agent Application System in Office Collaboration Scenarios** | [[paper]](https://arxiv.org/abs/2503.19584) | [code]

- [2025/03/24] **AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2503.18891) | [code]

- [2025/03/23] **MathAgent: Leveraging a Mixture-of-Math-Agent Framework for Real-World Multimodal Mathematical Error Detection** | [[paper]](https://arxiv.org/abs/2503.18132) | [code]

- [2025/03/21] **ConvoGen: Enhancing Conversational AI with Synthetic Data: A Multi-Agent Approach** | [[paper]](https://arxiv.org/abs/2503.17460) | [code]

- [2025/03/21] **MARS: A Multi-Agent Framework Incorporating Socratic Guidance for Automated Prompt Optimization** | [[paper]](https://arxiv.org/abs/2503.16874) | [code]

- [2025/03/19] **When Pigs Get Sick: Multi-Agent AI for Swine Disease Detection** | [[paper]](https://arxiv.org/abs/2503.15204) | [code]

- [2025/03/19] **MAMM-Refine: A Recipe for Improving Faithfulness in Generation with Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2503.15272) | [code]

- [2025/03/18] **Gricean Norms as a Basis for Effective Collaboration** | [[paper]](https://arxiv.org/abs/2503.14484) | [code]

- [2025/03/17] **Identifying Cooperative Personalities in Multi-agent Contexts through Personality Steering with Representation Engineering** | [[paper]](https://arxiv.org/abs/2503.12722) | [code]

- [2025/03/17] **MAP: Evaluation and Multi-Agent Enhancement of Large Language Models for Inpatient Pathways** | [[paper]](https://arxiv.org/abs/2503.13205) | [code]

- [2025/03/16] **LLM-Mediated Guidance of MARL Systems** | [[paper]](https://arxiv.org/abs/2503.13553) | [code]

- [2025/03/14] **AIstorian lets AI be a historian: A KG-powered multi-agent system for accurate biography generation** | [[paper]](https://arxiv.org/abs/2503.11346) | [code]

- [2025/03/14] **Prompt Injection Detection and Mitigation via AI Multi-Agent NLP Frameworks** | [[paper]](https://arxiv.org/abs/2503.11517) | [code]

- [2025/03/14] **RAG-KG-IL: A Multi-Agent Hybrid Framework for Reducing Hallucinations and Enhancing LLM Reasoning through RAG and Incremental Knowledge Graph Learning Integration** | [[paper]](https://arxiv.org/abs/2503.13514) | [code]

- [2025/03/13] **LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems** | [[paper]](https://arxiv.org/abs/2504.01963) | [code]

- [2025/03/12] **ReMA: Learning to Meta-think for LLMs with Multi-Agent Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2503.09501) | [code]

- [2025/03/07] **MM-StoryAgent: Immersive Narrated Storybook Video Generation with a Multi-Agent Paradigm across Text, Image and Audio** | [[paper]](https://arxiv.org/abs/2503.05242) | [code]

- [2025/03/07] **GEMA-Score: Granular Explainable Multi-Agent Score for Radiology Report Evaluation** | [[paper]](https://arxiv.org/abs/2503.05347) | [code]

- [2025/03/07] **Multi Agent based Medical Assistant for Edge Devices** | [[paper]](https://arxiv.org/abs/2503.05397) | [code]

- [2025/03/05] **MA-LoT: Multi-Agent Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving** | [[paper]](https://arxiv.org/abs/2503.03205) | [code]

- [2025/03/05] **MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2503.03686) | [code]

- [2025/03/05] **Multi-Agent Systems Powered by Large Language Models: Applications in Swarm Intelligence** | [[paper]](https://arxiv.org/abs/2503.03800) | [code]

- [2025/03/05] **Preserving Cultural Identity with Context-Aware Translation Through Multi-Agent AI Systems** | [[paper]](https://arxiv.org/abs/2503.04827) | [code]

- [2025/03/05] **Enhancing Collective Intelligence in Large Language Models Through Emotional Integration** | [[paper]](https://arxiv.org/abs/2503.04849) | [code]

- [2025/03/04] **BRIDGE: Bootstrapping Text to Control Time-Series Generation via Multi-Agent Iterative Optimization and Diffusion Modelling** | [[paper]](https://arxiv.org/abs/2503.02445) | [code]

- [2025/03/04] **Multi-Agent System for AI-Assisted Extraction of Narrative Arcs in TV Series** | [[paper]](https://arxiv.org/abs/2503.04817) | [code]

- [2025/03/01] **Structured Reasoning for Fairness: A Multi-Agent Approach to Bias Detection in Textual Data** | [[paper]](https://arxiv.org/abs/2503.00355) | [code]

- [2025/02/28] **PreMind: Multi-Agent Video Understanding for Advanced Indexing of Presentation-style Videos** | [[paper]](https://arxiv.org/abs/2503.00162) | [code]

- [2025/02/27] **M^3Builder: A Multi-Agent System for Automated Machine Learning in Medical Imaging** | [[paper]](https://arxiv.org/abs/2502.20301) | [code]

- [2025/02/26] **Stay Focused: Problem Drift in Multi-Agent Debate** | [[paper]](https://arxiv.org/abs/2502.19559) | [code]

- [2025/02/26] **Voting or Consensus? Decision-Making in Multi-Agent Debate** | [[paper]](https://arxiv.org/abs/2502.19130) | [code]

- [2025/02/25] **Enhancing Text Classification with a Novel Multi-Agent Collaboration Framework Leveraging BERT** | [[paper]](https://arxiv.org/abs/2502.18653) | [code]

- [2025/02/25] **A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition** | [[paper]](https://arxiv.org/abs/2502.18702) | [code]

- [2025/02/25] **Debt Collection Negotiations with Large Language Models: An Evaluation System and Optimizing Decision Making with Multi-Agent** | [[paper]](https://arxiv.org/abs/2502.18228) | [code]

- [2025/02/25] **FACT-AUDIT: An Adaptive Multi-Agent Framework for Dynamic Fact-Checking Evaluation of Large Language Models** | [[paper]](https://arxiv.org/abs/2502.17924) | [code]

- [2025/02/24] **MobileSteward: Integrating Multiple App-Oriented Agents with Self-Evolution to Automate Cross-App Instructions** | [[paper]](https://arxiv.org/abs/2502.16796) | [code]

- [2025/02/24] **Mobile-Agent-V: Learning Mobile Device Operation Through Video-Guided Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2502.17110) | [[code]](https://github.com/X-PLUG/MobileAgent)

- [2025/02/24] **METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling** | [[paper]](https://arxiv.org/abs/2502.17651) | [code]

- [2025/02/23] **The Hidden Strength of Disagreement: Unraveling the Consensus-Diversity Tradeoff in Adaptive Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2502.16565) | [[code]](https://github.com/wuzengqing001225/ConsensusDiversityTradeoffMAS)

- [2025/02/20] **Enhancing Language Multi-Agent Learning with Multi-Agent Credit Re-Assignment for Interactive Environment Generalization** | [[paper]](https://arxiv.org/abs/2502.14496) | [code]

- [2025/02/20] **CORBA: Contagious Recursive Blocking Attacks on Multi-Agent Systems Based on Large Language Models** | [[paper]](https://arxiv.org/abs/2502.14529) | [code]

- [2025/02/17] **Table-Critic: A Multi-Agent Framework for Collaborative Criticism and Refinement in Table Reasoning** | [[paper]](https://arxiv.org/abs/2502.11799) | [code]

- [2025/02/17] **HARBOR: Exploring Persona Dynamics in Multi-Agent Competition** | [[paper]](https://arxiv.org/abs/2502.12149) | [code]

- [2025/02/15] **Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation** | [[paper]](https://arxiv.org/abs/2502.10857) | [code]

- [2025/02/13] **PathFinder: A Multi-Modal Multi-Agent System for Medical Diagnostic Decision-Making Applied to Histopathology** | [[paper]](https://arxiv.org/abs/2502.08916) | [code]

- [2025/02/13] **Mind the Gaps: Logical English, Prolog, and Multi-agent Systems for Autonomous Vehicles** | [[paper]](https://arxiv.org/abs/2502.09216) | [code]

- [2025/02/12] **Faithful, Unfaithful or Ambiguous? Multi-Agent Debate with Initial Stance for Summary Evaluation** | [[paper]](https://arxiv.org/abs/2502.08514) | [code]

- [2025/02/12] **If Multi-Agent Debate is the Answer, What is the Question?** | [[paper]](https://arxiv.org/abs/2502.08788) | [code]

- [2025/02/11] **Don&#39;t Just Demo, Teach Me the Principles: A Principle-Based Multi-Agent Prompting Strategy for Text Classification** | [[paper]](https://arxiv.org/abs/2502.07165) | [code]

- [2025/02/11] **Multi-Agent Collaboration for Multilingual Code Instruction Tuning** | [[paper]](https://arxiv.org/abs/2502.07487) | [code]

- [2025/02/10] **KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment** | [[paper]](https://arxiv.org/abs/2502.06472) | [code]

- [2025/02/09] **Preventing Rogue Agents Improves Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2502.05986) | [code]

- [2025/02/09] **The Application of MATEC (Multi-AI Agent Team Care) Framework in Sepsis Care** | [[paper]](https://arxiv.org/abs/2503.16433) | [code]

- [2025/02/08] **CODESIM: Multi-Agent Code Generation and Problem Solving through Simulation-Driven Planning and Debugging** | [[paper]](https://arxiv.org/abs/2502.05664) | [code]

- [2025/02/08] **Multi-Agent Simulator Drives Language Models for Legal Intensive Interaction** | [[paper]](https://arxiv.org/abs/2502.06882) | [code]

- [2025/02/07] **S$^2$-MAD: Breaking the Token Barrier to Enhance Multi-Agent Debate Efficiency** | [[paper]](https://arxiv.org/abs/2502.04790) | [code]

- [2025/02/06] **Multi-Agent Reinforcement Learning with Focal Diversity Optimization** | [[paper]](https://arxiv.org/abs/2502.04492) | [code]

- [2025/02/06] **Enhancing Online Learning Efficiency Through Heterogeneous Resource Integration with a Multi-Agent RAG System** | [[paper]](https://arxiv.org/abs/2502.03948) | [code]

- [2025/02/06] **Multi-agent Architecture Search via Agentic Supernet** | [[paper]](https://arxiv.org/abs/2502.04180) | [code]

- [2025/02/04] **Position: Scaling LLM Agents Requires Asymptotic Analysis with LLM Primitives** | [[paper]](https://arxiv.org/abs/2502.04358) | [code]

- [2025/02/04] **Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies** | [[paper]](https://arxiv.org/abs/2502.02533) | [code]

- [2025/02/03] **PlotGen: Multi-Agent LLM-based Scientific Data Visualization via Multimodal Feedback** | [[paper]](https://arxiv.org/abs/2502.00988) | [code]

- [2025/02/03] **ChartCitor: Multi-Agent Framework for Fine-Grained Chart Visual Attribution** | [[paper]](https://arxiv.org/abs/2502.00989) | [code]

- [2025/02/02] **Rethinking Mixture-of-Agents: Is Mixing Different Large Language Models Beneficial?** | [[paper]](https://arxiv.org/abs/2502.00674) | [code]

- [2025/02/02] **Efficient Multi-Agent System Training with Data Influence-Oriented Tree Search** | [[paper]](https://arxiv.org/abs/2502.00955) | [code]

- [2025/01/29] **Layered Chain-of-Thought Prompting for Multi-Agent LLM Systems: A Comprehensive Approach to Explainable Large Language Models** | [[paper]](https://arxiv.org/abs/2501.18645) | [code]

- [2025/01/27] **MADP: Multi-Agent Deductive Planning for Enhanced Cognitive-Behavioral Mental Health Question Answer** | [[paper]](https://arxiv.org/abs/2501.15826) | [code]

- [2025/01/25] **Improving Retrieval-Augmented Generation through Multi-Agent Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2501.15228) | [code]

- [2025/01/24] **Multi-agent KTO: Reinforcing Strategic Interactions of Large Language Model in Language Game** | [[paper]](https://arxiv.org/abs/2501.14225) | [code]

- [2025/01/24] **Unmasking Conversational Bias in AI Multiagent Systems** | [[paper]](https://arxiv.org/abs/2501.14844) | [code]

- [2025/01/22] **FilmAgent: A Multi-Agent Framework for End-to-End Film Automation in Virtual 3D Spaces** | [[paper]](https://arxiv.org/abs/2501.12909) | [code]

- [2025/01/19] **IntellAgent: A Multi-Agent Framework for Evaluating Conversational AI Systems** | [[paper]](https://arxiv.org/abs/2501.11067) | [code]

- [2025/01/16] **AutoCBT: An Autonomous Multi-agent Framework for Cognitive Behavioral Therapy in Psychological Counseling** | [[paper]](https://arxiv.org/abs/2501.09426) | [code]

- [2025/01/14] **Talk to Right Specialists: Routing and Planning in Multi-agent System for Question Answering** | [[paper]](https://arxiv.org/abs/2501.07813) | [code]

- [2025/01/05] **LatteReview: A Multi-Agent Framework for Systematic Review Automation Using Large Language Models** | [[paper]](https://arxiv.org/abs/2501.05468) | [code]

- [2025/01/02] **Harnessing Multi-Agent LLMs for Complex Engineering Problem-Solving: A Framework for Senior Design Projects** | [[paper]](https://arxiv.org/abs/2501.01205) | [code]

- [2024/12/30] **Distributed Mixture-of-Agents for Edge Inference with Large Language Models** | [[paper]](https://arxiv.org/abs/2412.21200) | [code]

- [2024/12/28] **M-MAD: Multidimensional Multi-Agent Debate for Advanced Machine Translation Evaluation** | [[paper]](https://arxiv.org/abs/2412.20127) | [code]

- [2024/12/28] **Efficient Multi-Agent Collaboration with Tool Use for Online Planning in Complex Table Question Answering** | [[paper]](https://arxiv.org/abs/2412.20145) | [code]

- [2024/12/24] **Multi-Agents Based on Large Language Models for Knowledge-based Visual Question Answering** | [[paper]](https://arxiv.org/abs/2412.18351) | [code]

- [2024/12/22] **Multi-Agent Sampling: Scaling Inference Compute for Data Synthesis with Tree Search-Based Agentic Collaboration** | [[paper]](https://arxiv.org/abs/2412.17061) | [code]

- [2024/12/22] **A Multi-AI Agent System for Autonomous Optimization of Agentic AI Solutions via Iterative Refinement and LLM-Driven Feedback Loops** | [[paper]](https://arxiv.org/abs/2412.17149) | [code]

- [2024/12/20] **Mitigating Social Bias in Large Language Models: A Multi-Objective Approach within a Multi-Agent Framework** | [[paper]](https://arxiv.org/abs/2412.15504) | [code]

- [2024/12/19] **PsyDraw: A Multi-Agent Multimodal System for Mental Health Screening in Left-Behind Children** | [[paper]](https://arxiv.org/abs/2412.14769) | [code]

- [2024/12/18] **Gradual Vigilance and Interval Communication: Enhancing Value Alignment in Multi-Agent Debates** | [[paper]](https://arxiv.org/abs/2412.13471) | [code]

- [2024/12/15] **Cultural Palette: Pluralising Culture Alignment via Multi-agent Palette** | [[paper]](https://arxiv.org/abs/2412.11167) | [code]

- [2024/12/13] **AutoPatent: A Multi-Agent Framework for Automatic Patent Generation** | [[paper]](https://arxiv.org/abs/2412.09796) | [code]

- [2024/12/12] **DiverseAgentEntropy: Quantifying Black-Box LLM Uncertainty through Diverse Perspectives and Multi-Agent Interaction** | [[paper]](https://arxiv.org/abs/2412.09572) | [code]

- [2024/12/11] **NAT-NL2GQL: A Novel Multi-Agent Framework for Translating Natural Language to Graph Query Language** | [[paper]](https://arxiv.org/abs/2412.10434) | [code]

- [2024/12/10] **AutoPrep: Natural Language Question-Aware Data Preparation with a Multi-Agent Framework** | [[paper]](https://arxiv.org/abs/2412.10422) | [code]

- [2024/12/07] **SLA Management in Reconfigurable Multi-Agent RAG: A Systems Approach to Question Answering** | [[paper]](https://arxiv.org/abs/2412.06832) | [code]

- [2024/12/06] **Breaking Event Rumor Detection via Stance-Separated Multi-Agent Debate** | [[paper]](https://arxiv.org/abs/2412.04859) | [code]

- [2024/12/06] **Towards Effective GenAI Multi-Agent Collaboration: Design and Evaluation for Enterprise Applications** | [[paper]](https://arxiv.org/abs/2412.05449) | [code]

- [2024/12/06] **Enhancing LLMs for Impression Generation in Radiology Reports through a Multi-Agent System** | [[paper]](https://arxiv.org/abs/2412.06828) | [code]

- [2024/12/06] **TeamCraft: A Benchmark for Multi-Modal Multi-Agent Systems in Minecraft** | [[paper]](https://arxiv.org/abs/2412.05255) | [code]

- [2024/12/05] **Educational-Psychological Dialogue Robot Based on Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2412.03847) | [code]

- [2024/12/01] **Multi-Agent Collaboration in Incident Response with Large Language Models** | [[paper]](https://arxiv.org/abs/2412.00652) | [code]

- [2024/11/28] **MAG-V: A Multi-Agent Framework for Synthetic Data Generation and Verification** | [[paper]](https://arxiv.org/abs/2412.04494) | [code]

- [2024/11/21] **PIORS: Personalized Intelligent Outpatient Reception based on Large Language Model with Multi-Agents Medical Scenario Simulation** | [[paper]](https://arxiv.org/abs/2411.13902) | [code]

- [2024/11/21] **Enhancing LLMs for Power System Simulations: A Feedback-driven Multi-agent Framework** | [[paper]](https://arxiv.org/abs/2411.16707) | [code]

- [2024/11/18] **The Power of Many: Multi-Agent Multimodal Models for Cultural Image Captioning** | [[paper]](https://arxiv.org/abs/2411.11758) | [code]

- [2024/11/12] **BudgetMLAgent: A Cost-Effective LLM Multi-Agent system for Automating Machine Learning Tasks** | [[paper]](https://arxiv.org/abs/2411.07464) | [code]

- [2024/11/11] **Using Generative AI and Multi-Agents to Provide Automatic Feedback** | [[paper]](https://arxiv.org/abs/2411.07407) | [code]

- [2024/11/09] **Mixture of Knowledge Minigraph Agents for Literature Review Generation** | [[paper]](https://arxiv.org/abs/2411.06159) | [code]

- [2024/11/05] **SAUCE: Synchronous and Asynchronous User-Customizable Environment for Multi-Agent LLM Interaction** | [[paper]](https://arxiv.org/abs/2411.03397) | [code]

- [2024/11/05] **SMoA: Improving Multi-agent Large Language Models with Sparse Mixture-of-Agents** | [[paper]](https://arxiv.org/abs/2411.03284) | [code]

- [2024/11/01] **DARD: A Multi-Agent Approach for Task-Oriented Dialog Systems** | [[paper]](https://arxiv.org/abs/2411.00427) | [code]

- [2024/10/30] **ACC-Debate: An Actor-Critic Approach to Multi-Agent Debate** | [[paper]](https://arxiv.org/abs/2411.00053) | [code]

- [2024/10/29] **Flow-DPO: Improving LLM Mathematical Reasoning through Online Multi-Agent Learning** | [[paper]](https://arxiv.org/abs/2410.22304) | [code]

- [2024/10/29] **MARCO: Multi-Agent Real-time Chat Orchestration** | [[paper]](https://arxiv.org/abs/2410.21784) | [code]

- [2024/10/28] **CRAT: A Multi-Agent Framework for Causality-Enhanced Reflective and Retrieval-Augmented Translation with Large Language Models** | [[paper]](https://arxiv.org/abs/2410.21067) | [code]

- [2024/10/27] **AutoKaggle: A Multi-Agent Framework for Autonomous Data Science Competitions** | [[paper]](https://arxiv.org/abs/2410.20424) | [code]

- [2024/10/24] **Schema-Guided Culture-Aware Complex Event Simulation with Multi-Agent Role-Play** | [[paper]](https://arxiv.org/abs/2410.18935) | [code]

- [2024/10/23] **GraphTeam: Facilitating Large Language Model-based Graph Analysis via Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2410.18032) | [code]

- [2024/10/22] **Decoding Time Series with LLMs: A Multi-Agent Framework for Cross-Domain Annotation** | [[paper]](https://arxiv.org/abs/2410.17462) | [code]

- [2024/10/19] **An Electoral Approach to Diversify LLM-based Multi-Agent Collective Decision-Making** | [[paper]](https://arxiv.org/abs/2410.15168) | [code]

- [2024/10/18] **Synthesizing Post-Training Data for LLMs through Multi-Agent Simulation** | [[paper]](https://arxiv.org/abs/2410.14251) | [code]

- [2024/10/17] **AdaSwitch: Adaptive Switching between Small and Large Agents for Effective Cloud-Local Collaborative Learning** | [[paper]](https://arxiv.org/abs/2410.13181) | [code]

- [2024/10/16] **PRefLexOR: Preference-based Recursive Language Modeling for Exploratory Optimization of Reasoning and Agentic Thinking** | [[paper]](https://arxiv.org/abs/2410.12375) | [code]

- [2024/10/13] **LLM-Based Multi-Agent Systems are Scalable Graph Generative Models** | [[paper]](https://arxiv.org/abs/2410.09824) | [code]

- [2024/10/12] **Many Heads Are Better Than One: Improved Scientific Idea Generation by A LLM-Based Multi-Agent System** | [[paper]](https://arxiv.org/abs/2410.09403) | [code]

- [2024/10/11] **JAILJUDGE: A Comprehensive Jailbreak Judge Benchmark with Multi-Agent Enhanced Explanation Evaluation Framework** | [[paper]](https://arxiv.org/abs/2410.12855) | [code]

- [2024/10/11] **PEAR: A Robust and Flexible Automation Framework for Ptychography Enabled by Multiple Large Language Model Agents** | [[paper]](https://arxiv.org/abs/2410.09034) | [code]

- [2024/10/10] **AI-Press: A Multi-Agent News Generating and Feedback Simulation System Powered by Large Language Models** | [[paper]](https://arxiv.org/abs/2410.07561) | [code]

- [2024/10/10] **Multi-Agent Collaborative Data Selection for Efficient LLM Pretraining** | [[paper]](https://arxiv.org/abs/2410.08102) | [code]

- [2024/10/10] **Optima: Optimizing Effectiveness and Efficiency for LLM-Based Multi-Agent System** | [[paper]](https://arxiv.org/abs/2410.08115) | [code]

- [2024/10/10] **Prompt Engineering a Schizophrenia Chatbot: Utilizing a Multi-Agent Approach for Enhanced Compliance with Prompt Instructions** | [[paper]](https://arxiv.org/abs/2410.12848) | [code]

- [2024/10/10] **Diversity of Thought Elicits Stronger Reasoning Capabilities in Multi-Agent Debate Frameworks** | [[paper]](https://arxiv.org/abs/2410.12853) | [code]

- [2024/10/09] **Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach** | [[paper]](https://arxiv.org/abs/2410.06949) | [code]

- [2024/10/07] **Adversarial Multi-Agent Evaluation of Large Language Models through Iterative Debates** | [[paper]](https://arxiv.org/abs/2410.04663) | [code]

- [2024/10/06] **MindScope: Exploring cognitive biases in large language models through Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2410.04452) | [code]

- [2024/10/03] **Towards Implicit Bias Detection and Mitigation in Multi-Agent LLM Interactions** | [[paper]](https://arxiv.org/abs/2410.02584) | [code]

- [2024/10/03] **Agents&#39; Room: Narrative Generation through Multi-step Collaboration** | [[paper]](https://arxiv.org/abs/2410.02603) | [code]

- [2024/10/03] **Can Large Language Models Grasp Legal Theories? Enhance Legal Reasoning with Insights from Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2410.02507) | [code]

- [2024/10/03] **ColaCare: Enhancing Electronic Health Record Modeling through Large Language Model-Driven Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2410.02551) | [code]

- [2024/10/03] **AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML** | [[paper]](https://arxiv.org/abs/2410.02958) | [code]

- [2024/10/02] **RGD: Multi-LLM Based Agent Debugger via Refinement and Generation Guidance** | [[paper]](https://arxiv.org/abs/2410.01242) | [code]

- [2024/10/02] **Zodiac: A Cardiologist-Level LLM Framework for Multi-Agent Diagnostics** | [[paper]](https://arxiv.org/abs/2410.02026) | [code]

- [2024/09/21] **Towards Automated Patent Workflows: AI-Orchestrated Multi-Agent Framework for Intellectual Property Management and Analysis** | [[paper]](https://arxiv.org/abs/2409.19006) | [code]

- [2024/09/21] **GroupDebate: Enhancing the Efficiency of Multi-Agent Debate Using Group Discussion** | [[paper]](https://arxiv.org/abs/2409.14051) | [code]

- [2024/09/20] **Minstrel: Structural Prompt Generation with Multi-Agents Coordination for Non-AI Experts** | [[paper]](https://arxiv.org/abs/2409.13449) | [code]

- [2024/09/18] **MAgICoRe: Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning** | [[paper]](https://arxiv.org/abs/2409.12147) | [code]

- [2024/09/17] **The Art of Storytelling: Multi-Agent Generative AI for Dynamic Multimodal Narratives** | [[paper]](https://arxiv.org/abs/2409.11261) | [code]

- [2024/09/16] **Instigating Cooperation among LLM Agents Using Adaptive Information Modulation** | [[paper]](https://arxiv.org/abs/2409.10372) | [code]

- [2024/09/14] **Synergistic Simulations: Multi-Agent Problem Solving with Large Language Models** | [[paper]](https://arxiv.org/abs/2409.13753) | [code]

- [2024/09/12] **Knowledge Tagging with Large Language Model based Multi-Agent System** | [[paper]](https://arxiv.org/abs/2409.08406) | [code]

- [2024/09/11] **Propaganda to Hate: A Multimodal Analysis of Arabic Memes with Multi-Agent LLMs** | [[paper]](https://arxiv.org/abs/2409.07246) | [code]

- [2024/09/09] **SciAgents: Automating scientific discovery through multi-agent intelligent graph reasoning** | [[paper]](https://arxiv.org/abs/2409.05556) | [code]

- [2024/09/06] **Using Large Language Models to Generate Authentic Multi-agent Knowledge Work Datasets** | [[paper]](https://arxiv.org/abs/2409.04286) | [code]

- [2024/09/05] **xLAM: A Family of Large Action Models to Empower AI Agent Systems** | [[paper]](https://arxiv.org/abs/2409.03215) | [code]

- [2024/09/02] **Co-Learning: Code Learning for Multi-Agent Reinforcement Collaborative Framework with Conversational Natural Language Interfaces** | [[paper]](https://arxiv.org/abs/2409.00985) | [code]

- [2024/08/28] **BattleAgentBench: A Benchmark for Evaluating Cooperation and Competition Capabilities of Language Models in Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2408.15971) | [code]

- [2024/08/27] **AgentMonitor: A Plug-and-Play Framework for Predictive and Secure Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2408.14972) | [code]

- [2024/08/24] **Towards Human-Level Understanding of Complex Process Engineering Schematics: A Pedagogical, Introspective Multi-Agent Framework for Open-Domain Question Answering** | [[paper]](https://arxiv.org/abs/2409.00082) | [code]

- [2024/08/22] **MuMA-ToM: Multi-modal Multi-Agent Theory of Mind** | [[paper]](https://arxiv.org/abs/2408.12574) | [code]

- [2024/08/21] **DreamFactory: Pioneering Multi-Scene Long Video Generation with a Multi-Agent Framework** | [[paper]](https://arxiv.org/abs/2408.11788) | [code]

- [2024/08/16] **The Fellowship of the LLMs: Multi-Agent Workflows for Synthetic Preference Optimization Dataset Generation** | [[paper]](https://arxiv.org/abs/2408.08688) | [code]

- [2024/08/15] **MAG-SQL: Multi-Agent Generative Approach with Soft Schema Linking and Iterative Sub-SQL Refinement for Text-to-SQL** | [[paper]](https://arxiv.org/abs/2408.07930) | [code]

- [2024/08/15] **Text2BIM: Generating Building Models Using a Large Language Model-based Multi-Agent Framework** | [[paper]](https://arxiv.org/abs/2408.08054) | [code]

- [2024/08/14] **Development of a Large Language Model-based Multi-Agent Clinical Decision Support System for Korean Triage and Acuity Scale (KTAS)-Based Triage and Treatment Planning in Emergency Departments** | [[paper]](https://arxiv.org/abs/2408.07531) | [code]

- [2024/08/08] **Can LLMs Beat Humans in Debating? A Dynamic Multi-agent Framework for Competitive Debate** | [[paper]](https://arxiv.org/abs/2408.04472) | [code]

- [2024/08/05] **ReDel: A Toolkit for LLM-Powered Recursive Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2408.02248) | [code]

- [2024/08/05] **Evaluating and Enhancing LLMs Agent based on Theory of Mind in Guandan: A Multi-Player Cooperative Game under Imperfect Information** | [[paper]](https://arxiv.org/abs/2408.02559) | [code]

- [2024/07/23] **LawLuo: A Multi-Agent Collaborative Framework for Multi-Round Chinese Legal Consultation** | [[paper]](https://arxiv.org/abs/2407.16252) | [code]

- [2024/07/21] **Multi-Agent Causal Discovery Using Large Language Models** | [[paper]](https://arxiv.org/abs/2407.15073) | [code]

- [2024/07/19] **NeLLCom-X: A Comprehensive Neural-Agent Framework to Simulate Language Learning and Group Communication** | [[paper]](https://arxiv.org/abs/2407.13999) | [code]

- [2024/07/17] **Towards Collaborative Intelligence: Propagating Intentions and Reasoning for Multi-Agent Coordination with Large Language Models** | [[paper]](https://arxiv.org/abs/2407.12532) | [code]

- [2024/07/16] **InvAgent: A Large Language Model based Multi-Agent System for Inventory Management in Supply Chains** | [[paper]](https://arxiv.org/abs/2407.11384) | [code]

- [2024/07/13] **Synergistic Multi-Agent Framework with Trajectory Learning for Knowledge-Intensive Tasks** | [[paper]](https://arxiv.org/abs/2407.09893) | [code]

- [2024/07/13] **Cohesive Conversations: Enhancing Authenticity in Multi-Agent Simulated Dialogues** | [[paper]](https://arxiv.org/abs/2407.09897) | [code]

- [2024/07/10] **Flooding Spread of Manipulated Knowledge in LLM-Based Multi-Agent Communities** | [[paper]](https://arxiv.org/abs/2407.07791) | [code]

- [2024/07/09] **FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making** | [[paper]](https://arxiv.org/abs/2407.06567) | [code]

- [2024/07/09] **Internet of Agents: Weaving a Web of Heterogeneous Agents for Collaborative Intelligence** | [[paper]](https://arxiv.org/abs/2407.07061) | [code]

- [2024/07/04] **Solving Zebra Puzzles Using Constraint-Guided Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2407.03956) | [code]

- [2024/07/03] **MentalAgora: A Gateway to Advanced Personalized Care in Mental Health through Multi-Agent Debating and Attribute Control** | [[paper]](https://arxiv.org/abs/2407.02736) | [code]

- [2024/06/17] **Improving Multi-Agent Debate with Sparse Communication Topology** | [[paper]](https://arxiv.org/abs/2406.11776) | [code]

- [2024/06/13] **Multi-Agent Software Development through Cross-Team Collaboration** | [[paper]](https://arxiv.org/abs/2406.08979) | [[code]](https://github.com/openbmb/chatdev)

- [2024/06/11] **CoEvol: Constructing Better Responses for Instruction Finetuning through Multi-Agent Cooperation** | [[paper]](https://arxiv.org/abs/2406.07054) | [[code]](https://github.com/lirenhao1997/coevol)

- [2024/06/07] **Mixture-of-Agents Enhances Large Language Model Capabilities** | [[paper]](https://arxiv.org/abs/2406.04692) | [code]

- [2024/06/05] **Towards Detecting LLMs Hallucination via Markov Chain-based Multi-agent Debate Framework** | [[paper]](https://arxiv.org/abs/2406.03075) | [code]

- [2024/06/04] **Chain of Agents: Large Language Models Collaborating on Long-Context Tasks** | [[paper]](https://arxiv.org/abs/2406.02818) | [code]

- [2024/06/03] **Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2406.01014) | [[code]](https://github.com/x-plug/mobileagent)

- [2024/05/30] **Safe Multi-agent Reinforcement Learning with Natural Language Constraints** | [[paper]](https://arxiv.org/abs/2405.20018) | [code]

- [2024/05/23] **CityGPT: Towards Urban IoT Learning, Analysis and Interaction with Multi-Agent System** | [[paper]](https://arxiv.org/abs/2405.14691) | [code]

- [2024/05/20] **(Perhaps) Beyond Human Translation: Harnessing Multi-Agent Collaboration for Translating Ultra-Long Literary Texts** | [[paper]](https://arxiv.org/abs/2405.11804) | [code]

- [2024/05/10] **LLM Discussion: Enhancing the Creativity of Large Language Models via Discussion Framework and Role-Play** | [[paper]](https://arxiv.org/abs/2405.06373) | [code]

- [2024/05/07] **Enhancing the Efficiency and Accuracy of Underlying Asset Reviews in Structured Finance: The Application of Multi-agent Framework** | [[paper]](https://arxiv.org/abs/2405.04294) | [code]

- [2024/05/06] **Persona Inconstancy in Multi-Agent LLM Collaboration: Conformity, Confabulation, and Impersonation** | [[paper]](https://arxiv.org/abs/2405.03862) | [code]

- [2024/05/05] **Language Evolution for Evading Social Media Regulation via LLM-based Multi-agent Simulation** | [[paper]](https://arxiv.org/abs/2405.02858) | [code]

- [2024/04/25] **Cooperate or Collapse: Emergence of Sustainable Cooperation in a Society of LLM Agents** | [[paper]](https://arxiv.org/abs/2404.16698) | [code]

- [2024/04/23] **ClinicalAgent: Clinical Trial Multi-Agent System with Large Language Model-based Reasoning** | [[paper]](https://arxiv.org/abs/2404.14777) | [code]

- [2024/04/14] **Confidence Calibration and Rationalization for LLMs via Multi-Agent Deliberation** | [[paper]](https://arxiv.org/abs/2404.09127) | [code]

- [2024/04/12] **Leveraging Multi-AI Agents for Cross-Domain Knowledge Discovery** | [[paper]](https://arxiv.org/abs/2404.08511) | [code]

- [2024/04/09] **Foundation Models to the Rescue: Deadlock Resolution in Connected Multi-Robot Systems** | [[paper]](https://arxiv.org/abs/2404.06413) | [code]

- [2024/04/08] **360$^\circ$REA: Towards A Reusable Experience Accumulation with 360{\deg} Assessment for Multi-Agent System** | [[paper]](https://arxiv.org/abs/2404.05569) | [code]

- [2024/04/06] **MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems** | [[paper]](https://arxiv.org/abs/2404.04735) | [[code]](https://github.com/bin123apple/macm)

- [2024/04/02] **Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization** | [[paper]](https://arxiv.org/abs/2404.02183) | [code]

- [2024/04/02] **CMAT: A Multi-Agent Collaboration Tuning Framework for Enhancing Small Language Models** | [[paper]](https://arxiv.org/abs/2404.01663) | [code]

- [2024/03/26] **MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution** | [[paper]](https://arxiv.org/abs/2403.17927) | [code]

- [2024/03/22] **CACA Agent: Capability Collaboration based AI Agent** | [[paper]](https://arxiv.org/abs/2403.15137) | [code]

- [2024/03/21] **Multi-Agent VQA: Exploring Multi-Agent Foundation Models in Zero-Shot Visual Question Answering** | [[paper]](https://arxiv.org/abs/2403.14783) | [code]

- [2024/03/19] **Embodied LLM Agents Learn to Cooperate in Organized Teams** | [[paper]](https://arxiv.org/abs/2403.12482) | [code]

- [2024/03/12] **Transforming Competition into Collaboration: The Revolutionary Role of Multi-Agent Systems and Language Models in Modern Organizations** | [[paper]](https://arxiv.org/abs/2403.07769) | [code]

- [2024/03/02] **AutoDefense: Multi-Agent LLM Defense against Jailbreak Attacks** | [[paper]](https://arxiv.org/abs/2403.04783) | [code]

- [2024/02/28] **Rethinking the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key?** | [[paper]](https://arxiv.org/abs/2402.18272) | [code]

- [2024/02/26] **Chain-of-Discussion: A Multi-Model Framework for Complex Evidence-Based Question Answering** | [[paper]](https://arxiv.org/abs/2402.16313) | [code]

- [2024/02/26] **LLMArena: Assessing Capabilities of Large Language Models in Dynamic Multi-Agent Environments** | [[paper]](https://arxiv.org/abs/2402.16499) | [code]

- [2024/02/21] **LLM Based Multi-Agent Generation of Semi-structured Documents from Semantic Templates in the Public Administration Domain** | [[paper]](https://arxiv.org/abs/2402.14871) | [code]

- [2024/02/18] **Benchmark Self-Evolving: A Multi-Agent Framework for Dynamic LLM Evaluation** | [[paper]](https://arxiv.org/abs/2402.11443) | [[code]](https://github.com/nanshineloong/self-evolving-benchmark)

- [2024/02/18] **LongAgent: Scaling Language Models to 128k Context through Multi-Agent Collaboration** | [[paper]](https://arxiv.org/abs/2402.11550) | [code]

- [2024/02/15] **TDAG: A Multi-Agent Framework based on Dynamic Task Decomposition and Agent Generation** | [[paper]](https://arxiv.org/abs/2402.10178) | [code]

- [2024/02/03] **More Agents Is All You Need** | [[paper]](https://arxiv.org/abs/2402.05120) | [code]

- [2024/02/02] **Reasoning Capacity in Multi-Agent Systems: Limitations, Challenges and Human-Centered Solutions** | [[paper]](https://arxiv.org/abs/2402.01108) | [code]

- [2024/02/02] **A Multi-Agent Conversational Recommender System** | [[paper]](https://arxiv.org/abs/2402.01135) | [code]

- [2024/01/11] **Combating Adversarial Attacks with Multi-Agent Debate** | [[paper]](https://arxiv.org/abs/2401.05998) | [code]

- [2024/01/08] **MARG: Multi-Agent Review Generation for Scientific Papers** | [[paper]](https://arxiv.org/abs/2401.04259) | [code]

- [2024/01/08] **SpeechAgents: Human-Communication Simulation with Multi-Modal Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2401.03945) | [code]

- [2024/01/08] **Why Solving Multi-agent Path Finding with Large Language Model has not Succeeded Yet** | [[paper]](https://arxiv.org/abs/2401.03630) | [code]

- [2023/12/20] **AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation** | [[paper]](https://arxiv.org/abs/2312.13010) | [code]

- [2023/10/31] **Multi-Agent Consensus Seeking via Large Language Models** | [[paper]](https://arxiv.org/abs/2310.20151) | [code]

- [2023/10/25] **MultiPrompter: Cooperative Prompt Optimization with Multi-Agent Reinforcement Learning** | [[paper]](https://arxiv.org/abs/2310.16730) | [code]

- [2023/08/22] **ProAgent: Building Proactive Cooperative Agents with Large Language Models** | [[paper]](https://arxiv.org/abs/2308.11339) | [code]

- [2023/08/21] **AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors** | [[paper]](https://arxiv.org/abs/2308.10848) | [code]

- [2023/08/14] **ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate** | [[paper]](https://arxiv.org/abs/2308.07201) | [code]

- [2023/08/01] **MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework** | [[paper]](https://arxiv.org/abs/2308.00352) | [code]

- [2023/06/05] **Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents** | [[paper]](https://arxiv.org/abs/2306.03314) | [code]

- [2023/05/31] **Recursive Metropolis-Hastings Naming Game: Symbol Emergence in a Multi-agent System based on Probabilistic Generative Models** | [[paper]](https://arxiv.org/abs/2305.19761) | [code]

- [2023/05/30] **Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate** | [[paper]](https://arxiv.org/abs/2305.19118) | [code]

- [2023/04/26] **Multi-Party Chat: Conversational Agents in Group Settings with Humans and Models** | [[paper]](https://arxiv.org/abs/2304.13835) | [code]

- [2023/04/24] **ChatLLM Network: More brains, More intelligence** | [[paper]](https://arxiv.org/abs/2304.12998) | [code]

### Stability
#### Safety
- [2025/07/09] **VisualTrap: A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation** | [[paper]](https://arxiv.org/abs/2507.06899) | [code]

- [2025/07/04] **LTLCrit: A Temporal Logic-based LLM Critic for Safe and Efficient Embodied Agents** | [[paper]](https://arxiv.org/abs/2507.03293) | [code]

- [2025/07/01] **Enhancing LLM Agent Safety via Causal Influence Prompting** | [[paper]](https://arxiv.org/abs/2507.00979) | [code]

- [2025/07/01] **GAF-Guard: An Agentic Framework for Risk Management and Governance in Large Language Models** | [[paper]](https://arxiv.org/abs/2507.02986) | [code]

- [2025/06/25] **Model Editing as a Double-Edged Sword: Steering Agent Ethical Behavior Toward Beneficence or Harm** | [[paper]](https://arxiv.org/abs/2506.20606) | [code]

- [2025/06/11] **Effective Red-Teaming of Policy-Adherent Agents** | [[paper]](https://arxiv.org/abs/2506.09600) | [code]

- [2025/06/11] **Disclosure Audits for LLM Agents** | [[paper]](https://arxiv.org/abs/2506.10171) | [code]

- [2025/06/09] **SAFEFLOW: A Principled Protocol for Trustworthy and Transactional Autonomous Agent Systems** | [[paper]](https://arxiv.org/abs/2506.07564) | [code]

- [2025/06/04] **RedDebate: Safer Responses through Multi-Agent Red Teaming Debates** | [[paper]](https://arxiv.org/abs/2506.11083) | [code]

- [2025/06/01] **Simple Prompt Injection Attacks Can Leak Personal Data Observed by LLM Agents During Task Execution** | [[paper]](https://arxiv.org/abs/2506.01055) | [code]

- [2025/05/29] **AgentAlign: Navigating Safety Alignment in the Shift from Informative to Agentic Large Language Models** | [[paper]](https://arxiv.org/abs/2505.23020) | [code]

- [2025/05/28] **RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments** | [[paper]](https://arxiv.org/abs/2505.21936) | [code]

- [2025/05/26] **TrojanStego: Your Language Model Can Secretly Be A Steganographic Privacy Leaking Agent** | [[paper]](https://arxiv.org/abs/2505.20118) | [code]

- [2025/05/25] **GUARDIAN: Safeguarding LLM Multi-Agent Collaborations with Temporal Graph Modeling** | [[paper]](https://arxiv.org/abs/2505.19234) | [code]

- [2025/05/18] **IP Leakage Attacks Targeting LLM-Based Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2505.12442) | [code]

- [2025/05/16] **EnvInjection: Environmental Prompt Injection Attack to Multi-modal Web Agents** | [[paper]](https://arxiv.org/abs/2505.11717) | [code]

- [2025/04/24] **Assessing the Potential of Generative Agents in Crowdsourced Fact-Checking** | [[paper]](https://arxiv.org/abs/2504.19940) | [code]

- [2025/04/15] **Towards Automated Safety Requirements Derivation Using Agent-based RAG** | [[paper]](https://arxiv.org/abs/2504.11243) | [code]

- [2025/03/26] **sudo rm -rf agentic_security** | [[paper]](https://arxiv.org/abs/2503.20279) | [code]

- [2025/03/24] **AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents** | [[paper]](https://arxiv.org/abs/2503.18666) | [code]

- [2025/03/06] **SafeArena: Evaluating the Safety of Autonomous Web Agents** | [[paper]](https://arxiv.org/abs/2503.04957) | [code]

- [2025/02/20] **CORBA: Contagious Recursive Blocking Attacks on Multi-Agent Systems Based on Large Language Models** | [[paper]](https://arxiv.org/abs/2502.14529) | [code]

- [2025/02/18] **AEIA-MN: Evaluating the Robustness of Multimodal LLM-Powered Mobile Agents Against Active Environmental Injection Attacks** | [[paper]](https://arxiv.org/abs/2502.13053) | [code]

- [2025/02/17] **&#34;Nuclear Deployed!&#34;: Analyzing Catastrophic Risks in Decision-making of Autonomous LLM Agents** | [[paper]](https://arxiv.org/abs/2502.11355) | [code]

- [2025/02/01] **ALU: Agentic LLM Unlearning** | [[paper]](https://arxiv.org/abs/2502.00406) | [code]

- [2025/01/28] **Context is Key for Agent Security** | [[paper]](https://arxiv.org/abs/2501.17070) | [code]

- [2024/12/21] **The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents** | [[paper]](https://arxiv.org/abs/2412.16682) | [code]

- [2024/12/16] **Seeker: Towards Exception Safety Code Generation with Intermediate Language Agents Framework** | [[paper]](https://arxiv.org/abs/2412.11713) | [code]

- [2024/12/09] **The Fusion of Large Language Models and Formal Methods for Trustworthy AI Agents: A Roadmap** | [[paper]](https://arxiv.org/abs/2412.06512) | [code]

- [2024/11/08] **Towards Low-Resource Harmful Meme Detection with LMM Agents** | [[paper]](https://arxiv.org/abs/2411.05383) | [code]

- [2024/11/06] **MRJ-Agent: An Effective Jailbreak Agent for Multi-Round Dialogue** | [[paper]](https://arxiv.org/abs/2411.03814) | [code]

- [2024/11/04] **Attacking Vision-Language Computer Agents via Pop-ups** | [[paper]](https://arxiv.org/abs/2411.02391) | [code]

- [2024/10/22] **AdvWeb: Controllable Black-box Attacks on VLM-powered Web Agents** | [[paper]](https://arxiv.org/abs/2410.17401) | [code]

- [2024/10/18] **Coherence-Driven Multimodal Safety Dialogue with Active Learning for Embodied Agents** | [[paper]](https://arxiv.org/abs/2410.14141) | [code]

- [2024/10/11] **AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents** | [[paper]](https://arxiv.org/abs/2410.09024) | [code]

- [2024/10/09] **I Want to Break Free! Persuasion and Anti-Social Behavior of LLMs in Multi-Agent Settings with Social Hierarchy** | [[paper]](https://arxiv.org/abs/2410.07109) | [code]

- [2024/09/28] **SELP: Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models** | [[paper]](https://arxiv.org/abs/2409.19471) | [code]

- [2024/09/17] **EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage** | [[paper]](https://arxiv.org/abs/2409.11295) | [code]

- [2024/09/13] **AI-LieDar: Examine the Trade-off Between Utility and Truthfulness in LLM Agents** | [[paper]](https://arxiv.org/abs/2409.09013) | [code]

- [2024/08/20] **Athena: Safe Autonomous Agents with Verbal Contrastive Learning** | [[paper]](https://arxiv.org/abs/2408.11021) | [code]

- [2024/08/05] **Caution for the Environment: Multimodal Agents are Susceptible to Environmental Distractions** | [[paper]](https://arxiv.org/abs/2408.02544) | [code]

- [2024/07/23] **RedAgent: Red Teaming Large Language Models with Context-aware Autonomous Language Agent** | [[paper]](https://arxiv.org/abs/2407.16667) | [code]

- [2024/06/05] **BadAgent: Inserting and Activating Backdoor Attacks in LLM Agents** | [[paper]](https://arxiv.org/abs/2406.03007) | [[code]](https://github.com/dpamk/badagent)

- [2024/05/30] **Safe Multi-agent Reinforcement Learning with Natural Language Constraints** | [[paper]](https://arxiv.org/abs/2405.20018) | [code]

- [2024/05/24] **Hacc-Man: An Arcade Game for Jailbreaking LLMs** | [[paper]](https://arxiv.org/abs/2405.15902) | [code]

- [2024/03/02] **AutoDefense: Multi-Agent LLM Defense against Jailbreak Attacks** | [[paper]](https://arxiv.org/abs/2403.04783) | [code]

- [2024/02/17] **Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents** | [[paper]](https://arxiv.org/abs/2402.11208) | [code]

- [2024/02/16] **ToolSword: Unveiling Safety Issues of Large Language Models in Tool Learning Across Three Stages** | [[paper]](https://arxiv.org/abs/2402.10753) | [[code]](https://github.com/junjie-ye/toolsword)

- [2024/02/02] **TrustAgent: Towards Safe and Trustworthy LLM-based Agents** | [[paper]](https://arxiv.org/abs/2402.01586) | [code]

- [2024/01/11] **Combating Adversarial Attacks with Multi-Agent Debate** | [[paper]](https://arxiv.org/abs/2401.05998) | [code]

- [2023/11/17] **Testing Language Model Agents Safely in the Wild** | [[paper]](https://arxiv.org/abs/2311.10538) | [code]

#### Bias
- [2025/05/27] **Silence is Not Consensus: Disrupting Agreement Bias in Multi-Agent LLMs via Catfish Agent for Clinical Decision Making** | [[paper]](https://arxiv.org/abs/2505.21503) | [code]

- [2025/05/14] **Language Agents Mirror Human Causal Reasoning Biases. How Can We Help Them Think Like Scientists?** | [[paper]](https://arxiv.org/abs/2505.09614) | [code]

- [2025/04/10] **MALIBU Benchmark: Multi-Agent LLM Implicit Bias Uncovered** | [[paper]](https://arxiv.org/abs/2507.01019) | [code]

- [2025/03/27] **Bias-Aware Agent: Enhancing Fairness in AI-Driven Knowledge Retrieval** | [[paper]](https://arxiv.org/abs/2503.21237) | [code]

- [2025/03/01] **Structured Reasoning for Fairness: A Multi-Agent Approach to Bias Detection in Textual Data** | [[paper]](https://arxiv.org/abs/2503.00355) | [code]

- [2025/01/29] **Actions Speak Louder than Words: Agent Decisions Reveal Implicit Biases in Language Models** | [[paper]](https://arxiv.org/abs/2501.17420) | [code]

- [2025/01/24] **Unmasking Conversational Bias in AI Multiagent Systems** | [[paper]](https://arxiv.org/abs/2501.14844) | [code]

- [2024/12/20] **Mitigating Social Bias in Large Language Models: A Multi-Objective Approach within a Multi-Agent Framework** | [[paper]](https://arxiv.org/abs/2412.15504) | [code]

- [2024/11/12] **Mitigating Bias in Queer Representation within Large Language Models: A Collaborative Agent Approach** | [[paper]](https://arxiv.org/abs/2411.07656) | [code]

- [2024/10/06] **MindScope: Exploring cognitive biases in large language models through Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2410.04452) | [code]

- [2024/10/03] **Towards Implicit Bias Detection and Mitigation in Multi-Agent LLM Interactions** | [[paper]](https://arxiv.org/abs/2410.02584) | [code]

- [2024/05/23] **ALI-Agent: Assessing LLMs&#39; Alignment with Human Values via Agent-based Evaluation** | [[paper]](https://arxiv.org/abs/2405.14125) | [code]

- [2024/04/23] **Aligning LLM Agents by Learning Latent Preference from User Edits** | [[paper]](https://arxiv.org/abs/2404.15269) | [code]

- [2024/02/19] **Polarization of Autonomous Generative AI Agents Under Echo Chambers** | [[paper]](https://arxiv.org/abs/2402.12212) | [code]

- [2024/02/14] **Towards better Human-Agent Alignment: Assessing Task Utility in LLM-Powered Applications** | [[paper]](https://arxiv.org/abs/2402.09015) | [code]

- [2024/01/09] **Agent Alignment in Evolving Social Norms** | [[paper]](https://arxiv.org/abs/2401.04620) | [code]

#### Hallucination
- [2025/06/23] **A Comment On &#34;The Illusion of Thinking&#34;: Reframing the Reasoning Cliff as an Agentic Gap** | [[paper]](https://arxiv.org/abs/2506.18957) | [code]

- [2025/05/28] **Position: Uncertainty Quantification Needs Reassessment for Large-language Model Agents** | [[paper]](https://arxiv.org/abs/2505.22655) | [code]

- [2025/03/14] **Prompt Injection Detection and Mitigation via AI Multi-Agent NLP Frameworks** | [[paper]](https://arxiv.org/abs/2503.11517) | [code]

- [2025/03/14] **RAG-KG-IL: A Multi-Agent Hybrid Framework for Reducing Hallucinations and Enhancing LLM Reasoning through RAG and Incremental Knowledge Graph Learning Integration** | [[paper]](https://arxiv.org/abs/2503.13514) | [code]

- [2025/03/01] **EXCLAIM: An Explainable Cross-Modal Agentic System for Misinformation Detection with Hierarchical Retrieval** | [[paper]](https://arxiv.org/abs/2504.06269) | [code]

- [2025/02/26] **Winning Big with Small Models: Knowledge Distillation vs. Self-Training for Reducing Hallucination in QA Agents** | [[paper]](https://arxiv.org/abs/2502.19545) | [code]

- [2025/02/14] **Automated Hypothesis Validation with Agentic Sequential Falsifications** | [[paper]](https://arxiv.org/abs/2502.09858) | [code]

- [2025/02/04] **Position: Stop Acting Like Language Model Agents Are Normal Agents** | [[paper]](https://arxiv.org/abs/2502.10420) | [code]

- [2025/02/03] **SelfCheckAgent: Zero-Resource Hallucination Detection in Generative Large Language Models** | [[paper]](https://arxiv.org/abs/2502.01812) | [code]

- [2025/01/19] **Hallucination Mitigation using Agentic AI Natural Language-Based Frameworks** | [[paper]](https://arxiv.org/abs/2501.13946) | [code]

- [2024/11/25] **Enhancing Multi-Agent Consensus through Third-Party LLM Integration: Analyzing Uncertainty and Mitigating Hallucinations in Large Language Models** | [[paper]](https://arxiv.org/abs/2411.16189) | [code]

- [2024/11/12] **SHARP: Unlocking Interactive Hallucination via Stance Transfer in Role-Playing Agents** | [[paper]](https://arxiv.org/abs/2411.07965) | [code]

- [2024/07/08] **DebUnc: Mitigating Hallucinations in Large Language Model Agent Communication with Uncertainty Estimations** | [[paper]](https://arxiv.org/abs/2407.06426) | [code]

- [2024/06/29] **BioKGBench: A Knowledge Graph Checking Benchmark of AI Agent for Biomedical Science** | [[paper]](https://arxiv.org/abs/2407.00466) | [code]

- [2024/06/17] **Small Agent Can Also Rock! Empowering Small Language Models as Hallucination Detector** | [[paper]](https://arxiv.org/abs/2406.11277) | [code]

- [2024/06/05] **Towards Detecting LLMs Hallucination via Markov Chain-based Multi-agent Debate Framework** | [[paper]](https://arxiv.org/abs/2406.03075) | [code]

- [2024/05/28] **TimeChara: Evaluating Point-in-Time Character Hallucination of Role-Playing Large Language Models** | [[paper]](https://arxiv.org/abs/2405.18027) | [code]

- [2024/02/13] **Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast** | [[paper]](https://arxiv.org/abs/2402.08567) | [[code]](https://github.com/sail-sg/agent-smith)

### Infrastructure
#### Benchmark&Evaluation
- [2025/07/08] **ECom-Bench: Can LLM Agent Resolve Real-World E-commerce Customer Support Issues?** | [[paper]](https://arxiv.org/abs/2507.05639) | [code]

- [2025/07/07] **Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions** | [[paper]](https://arxiv.org/abs/2507.05257) | [code]

- [2025/07/04] **Recon, Answer, Verify: Agents in Search of Truth** | [[paper]](https://arxiv.org/abs/2507.03671) | [code]

- [2025/07/04] **STRUCTSENSE: A Task-Agnostic Agentic Framework for Structured Information Extraction with Human-In-The-Loop Evaluation and Benchmarking** | [[paper]](https://arxiv.org/abs/2507.03674) | [code]

- [2025/07/01] **TransLaw: Benchmarking Large Language Models in Multi-Agent Simulation of the Collaborative Translation** | [[paper]](https://arxiv.org/abs/2507.00875) | [code]

- [2025/06/27] **Don&#39;t Trust Generative Agents to Mimic Communication on Social Networks Unless You Benchmarked their Empirical Realism** | [[paper]](https://arxiv.org/abs/2506.21974) | [code]

- [2025/06/27] **RExBench: Can coding agents autonomously implement AI research extensions?** | [[paper]](https://arxiv.org/abs/2506.22598) | [code]

- [2025/06/26] **Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling across Perception, Planning, and Safety in Real-World Multimodal Agents** | [[paper]](https://arxiv.org/abs/2506.21252) | [code]

- [2025/06/25] **The Decrypto Benchmark for Multi-Agent Reasoning and Theory of Mind** | [[paper]](https://arxiv.org/abs/2506.20664) | [code]

- [2025/06/20] **MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents** | [[paper]](https://arxiv.org/abs/2506.21605) | [code]

- [2025/06/20] **Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems** | [[paper]](https://arxiv.org/abs/2506.17208) | [code]

- [2025/06/19] **IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks** | [[paper]](https://arxiv.org/abs/2506.16402) | [code]

- [2025/06/13] **DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents** | [[paper]](https://arxiv.org/abs/2506.11763) | [code]

- [2025/06/13] **The Behavior Gap: Evaluating Zero-shot LLM Agents in Complex Task-Oriented Dialogs** | [[paper]](https://arxiv.org/abs/2506.12266) | [code]

- [2025/06/11] **Bench to the Future: A Pastcasting Benchmark for Forecasting Agents** | [[paper]](https://arxiv.org/abs/2506.21558) | [code]

- [2025/06/10] **Atomic-to-Compositional Generalization for Mobile Agents with A New Benchmark and Scheduling System** | [[paper]](https://arxiv.org/abs/2506.08972) | [code]

- [2025/06/10] **UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench** | [[paper]](https://arxiv.org/abs/2506.09289) | [code]

- [2025/06/09] **EconWebArena: Benchmarking Autonomous Agents on Economic Tasks in Realistic Web Environments** | [[paper]](https://arxiv.org/abs/2506.08136) | [code]

- [2025/06/09] **HeuriGym: An Agentic Benchmark for LLM-Crafted Heuristics in Combinatorial Optimization** | [[paper]](https://arxiv.org/abs/2506.07972) | [code]

- [2025/06/09] **$\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment** | [[paper]](https://arxiv.org/abs/2506.07982) | [code]

- [2025/06/05] **Flex-TravelPlanner: A Benchmark for Flexible Planning with Language Agents** | [[paper]](https://arxiv.org/abs/2506.04649) | [code]

- [2025/06/04] **AgentMisalignment: Measuring the Propensity for Misaligned Behaviour in LLM-Based Agents** | [[paper]](https://arxiv.org/abs/2506.04018) | [code]

- [2025/06/02] **FormFactory: An Interactive Benchmarking Suite for Multimodal Form-Filling Agents** | [[paper]](https://arxiv.org/abs/2506.01520) | [code]

- [2025/06/02] **WebChoreArena: Evaluating Web Browsing Agents on Realistic Tedious Web Tasks** | [[paper]](https://arxiv.org/abs/2506.01952) | [code]

- [2025/05/31] **DefenderBench: A Toolkit for Evaluating Language Agents in Cybersecurity Environments** | [[paper]](https://arxiv.org/abs/2506.00739) | [code]

- [2025/05/30] **Draw ALL Your Imagine: A Holistic Benchmark and Agent Framework for Complex Instruction-based Image Generation** | [[paper]](https://arxiv.org/abs/2505.24787) | [code]

- [2025/05/30] **Agent-X: Evaluating Deep Multimodal Reasoning in Vision-Centric Agentic Tasks** | [[paper]](https://arxiv.org/abs/2505.24876) | [code]

- [2025/05/30] **Open CaptchaWorld: A Comprehensive Web-based Platform for Testing and Benchmarking Multimodal LLM Agents** | [[paper]](https://arxiv.org/abs/2505.24878) | [code]

- [2025/05/29] **GSO: Challenging Software Optimization Tasks for Evaluating SWE-Agents** | [[paper]](https://arxiv.org/abs/2505.23671) | [code]

- [2025/05/27] **AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs** | [[paper]](https://arxiv.org/abs/2505.21389) | [code]

- [2025/05/26] **ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows** | [[paper]](https://arxiv.org/abs/2505.19897) | [code]

- [2025/05/26] **MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research** | [[paper]](https://arxiv.org/abs/2505.19955) | [code]

- [2025/05/26] **On Path to Multimodal Historical Reasoning: HistBench and HistAgent** | [[paper]](https://arxiv.org/abs/2505.20246) | [code]

- [2025/05/24] **CRMArena-Pro: Holistic Assessment of LLM Agents Across Diverse Business Scenarios and Interactions** | [[paper]](https://arxiv.org/abs/2505.18878) | [code]

- [2025/05/22] **BioDSA-1K: Benchmarking Data Science Agents for Biomedical Research** | [[paper]](https://arxiv.org/abs/2505.16100) | [code]

- [2025/05/22] **From EduVisBench to EduVisAgent: A Benchmark and Multi-Agent Framework for Reasoning-Driven Pedagogical Visualization** | [[paper]](https://arxiv.org/abs/2505.16832) | [code]

- [2025/05/22] **AGENTIF: Benchmarking Instruction Following of Large Language Models in Agentic Scenarios** | [[paper]](https://arxiv.org/abs/2505.16944) | [code]

- [2025/05/21] **X-WebAgentBench: A Multilingual Interactive Web Benchmark for Evaluating Global Agentic System** | [[paper]](https://arxiv.org/abs/2505.15372) | [code]

- [2025/05/21] **BountyBench: Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems** | [[paper]](https://arxiv.org/abs/2505.15216) | [code]

- [2025/05/21] **InfoDeepSeek: Benchmarking Agentic Information Seeking for Retrieval-Augmented Generation** | [[paper]](https://arxiv.org/abs/2505.15872) | [code]

- [2025/05/21] **MAPS: A Multilingual Benchmark for Global Agent Performance and Security** | [[paper]](https://arxiv.org/abs/2505.15935) | [code]

- [2025/05/18] **MedAgentBoard: Benchmarking Multi-Agent Collaboration with Conventional Methods for Diverse Medical Tasks** | [[paper]](https://arxiv.org/abs/2505.12371) | [code]

- [2025/05/17] **Mobile-Bench-v2: A More Realistic and Comprehensive Benchmark for VLM-based Mobile Agents** | [[paper]](https://arxiv.org/abs/2505.11891) | [code]

- [2025/05/16] **GuideBench: Benchmarking Domain-Oriented Guideline Following for LLM Agents** | [[paper]](https://arxiv.org/abs/2505.11368) | [code]

- [2025/05/16] **REI-Bench: Can Embodied Agents Understand Vague Human Instructions in Task Planning?** | [[paper]](https://arxiv.org/abs/2505.10872) | [code]

- [2025/05/02] **PIPA: A Unified Evaluation Protocol for Diagnosing Interactive Planning Agents** | [[paper]](https://arxiv.org/abs/2505.01592) | [code]

- [2025/04/25] **Auto-SLURP: A Benchmark Dataset for Evaluating Multi-Agent Frameworks in Smart Personal Assistant** | [[paper]](https://arxiv.org/abs/2504.18373) | [code]

- [2025/04/24] **Toward a Human-Centered Evaluation Framework for Trustworthy LLM-Powered GUI Agents** | [[paper]](https://arxiv.org/abs/2504.17934) | [code]

- [2025/04/21] **PLANET: A Collection of Benchmarks for Evaluating LLMs&#39; Planning Capabilities** | [[paper]](https://arxiv.org/abs/2504.14773) | [code]

- [2025/04/16] **BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents** | [[paper]](https://arxiv.org/abs/2504.12516) | [code]

- [2025/04/15] **GraphicBench: A Planning Benchmark for Graphic Design with Language Agents** | [[paper]](https://arxiv.org/abs/2504.11571) | [code]

- [2025/04/13] **AgentA/B: Automated and Scalable Web A/BTesting with Interactive LLM Agents** | [[paper]](https://arxiv.org/abs/2504.09723) | [code]

- [2025/04/11] **TP-RAG: Benchmarking Retrieval-Augmented Large Language Model Agents for Spatiotemporal-Aware Travel Planning** | [[paper]](https://arxiv.org/abs/2504.08694) | [code]

- [2025/04/11] **AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories** | [[paper]](https://arxiv.org/abs/2504.08942) | [code]

- [2025/04/10] **MALIBU Benchmark: Multi-Agent LLM Implicit Bias Uncovered** | [[paper]](https://arxiv.org/abs/2507.01019) | [code]

- [2025/04/06] **CO-Bench: Benchmarking Language Model Agents in Algorithm Search for Combinatorial Optimization** | [[paper]](https://arxiv.org/abs/2504.04310) | [code]

- [2025/04/04] **How Social is It? A Benchmark for LLMs&#39; Capabilities in Multi-user Multi-turn Social Agent Tasks** | [[paper]](https://arxiv.org/abs/2505.04628) | [code]

- [2025/03/31] **SciReplicate-Bench: Benchmarking LLMs in Agent-driven Algorithmic Reproduction from Research Papers** | [[paper]](https://arxiv.org/abs/2504.00255) | [code]

- [2025/03/28] **Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey** | [[paper]](https://arxiv.org/abs/2503.22458) | [code]

- [2025/03/25] **Writing as a testbed for open ended agents** | [[paper]](https://arxiv.org/abs/2503.19711) | [code]

- [2025/03/24] **EconEvals: Benchmarks and Litmus Tests for LLM Agents in Unknown Environments** | [[paper]](https://arxiv.org/abs/2503.18825) | [code]

- [2025/03/20] **Survey on Evaluation of LLM-based Agents** | [[paper]](https://arxiv.org/abs/2503.16416) | [code]

- [2025/03/16] **VeriLA: A Human-Centered Evaluation Framework for Interpretable Verification of LLM Agent Failures** | [[paper]](https://arxiv.org/abs/2503.12651) | [code]

- [2025/03/11] **AgentOrca: A Dual-System Framework to Evaluate Language Agents on Operational Routine and Constraint Adherence** | [[paper]](https://arxiv.org/abs/2503.08669) | [code]

- [2025/03/10] **MedAgentsBench: Benchmarking Thinking Models and Agent Frameworks for Complex Medical Reasoning** | [[paper]](https://arxiv.org/abs/2503.07459) | [code]

- [2025/03/10] **ProjectEval: A Benchmark for Programming Agents Automated Evaluation on Project-Level Code Generation** | [[paper]](https://arxiv.org/abs/2503.07010) | [code]

- [2025/03/10] **RefactorBench: Evaluating Stateful Reasoning in Language Agents Through Code** | [[paper]](https://arxiv.org/abs/2503.07832) | [code]

- [2025/03/10] **BEARCUBS: A benchmark for computer-using web agents** | [[paper]](https://arxiv.org/abs/2503.07919) | [code]

- [2025/03/08] **DSGBench: A Diverse Strategic Game Benchmark for Evaluating LLM-based Agents in Complex Decision-Making Environments** | [[paper]](https://arxiv.org/abs/2503.06047) | [code]

- [2025/03/03] **MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents** | [[paper]](https://arxiv.org/abs/2503.01935) | [code]

- [2025/02/26] **TheoremExplainAgent: Towards Multimodal Explanations for LLM Theorem Understanding** | [[paper]](https://arxiv.org/abs/2502.19400) | [code]

- [2025/02/25] **RefuteBench 2.0 -- Agentic Benchmark for Dynamic Evaluation of LLM Responses to Refutation Instruction** | [[paper]](https://arxiv.org/abs/2502.18308) | [[code]](https://github.com/ElliottYan/RefuteBench-2.0)

- [2025/02/20] **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** | [[paper]](https://arxiv.org/abs/2502.14499) | [code]

- [2025/02/19] **DataSciBench: An LLM Agent Benchmark for Data Science** | [[paper]](https://arxiv.org/abs/2502.13897) | [code]

- [2025/02/13] **EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents** | [[paper]](https://arxiv.org/abs/2502.09560) | [code]

- [2025/02/07] **Evaluating Personality Traits in Large Language Models: Insights from Psychological Questionnaires** | [[paper]](https://arxiv.org/abs/2502.05248) | [code]

- [2025/02/06] **Robotouille: An Asynchronous Planning Benchmark for LLM Agents** | [[paper]](https://arxiv.org/abs/2502.05227) | [code]

- [2025/02/01] **Who&#39;s the MVP? A Game-Theoretic Evaluation Benchmark for Modular Attribution in LLM Agents** | [[paper]](https://arxiv.org/abs/2502.00510) | [code]

- [2025/01/21] **EmbodiedEval: Evaluate Multimodal LLMs as Embodied Agents** | [[paper]](https://arxiv.org/abs/2501.11858) | [code]

- [2024/12/23] **LegalAgentBench: Evaluating LLM Agents in Legal Domain** | [[paper]](https://arxiv.org/abs/2412.17259) | [code]

- [2024/12/19] **Agent-SafetyBench: Evaluating the Safety of LLM Agents** | [[paper]](https://arxiv.org/abs/2412.14470) | [code]

- [2024/12/18] **TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks** | [[paper]](https://arxiv.org/abs/2412.14161) | [code]

- [2024/12/18] **ChinaTravel: A Real-World Benchmark for Language Agents in Chinese Travel Planning** | [[paper]](https://arxiv.org/abs/2412.13682) | [code]

- [2024/12/06] **TeamCraft: A Benchmark for Multi-Modal Multi-Agent Systems in Minecraft** | [[paper]](https://arxiv.org/abs/2412.05255) | [code]

- [2024/12/02] **Medchain: Bridging the Gap Between LLM Agents and Clinical Practice through Interactive Sequential Benchmarking** | [[paper]](https://arxiv.org/abs/2412.01605) | [code]

- [2024/11/05] **Benchmarking Multimodal Retrieval Augmented Generation with Dynamic VQA Dataset and Self-adaptive Planning Agent** | [[paper]](https://arxiv.org/abs/2411.02937) | [code]

- [2024/10/28] **Can Machines Think Like Humans? A Behavioral Evaluation of LLM-Agents in Dictator Games** | [[paper]](https://arxiv.org/abs/2410.21359) | [code]

- [2024/10/25] **AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios** | [[paper]](https://arxiv.org/abs/2410.19346) | [code]

- [2024/10/25] **AGENT-CQ: Automatic Generation and Evaluation of Clarifying Questions for Conversational Search with LLMs** | [[paper]](https://arxiv.org/abs/2410.19692) | [code]

- [2024/10/23] **MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control** | [[paper]](https://arxiv.org/abs/2410.17520) | [code]

- [2024/10/16] **Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance** | [[paper]](https://arxiv.org/abs/2410.12361) | [code]

- [2024/10/15] **Revisiting Benchmark and Assessment: An Agent-based Exploratory Dynamic Evaluation Framework for LLMs** | [[paper]](https://arxiv.org/abs/2410.11507) | [code]

- [2024/10/11] **JAILJUDGE: A Comprehensive Jailbreak Judge Benchmark with Multi-Agent Enhanced Explanation Evaluation Framework** | [[paper]](https://arxiv.org/abs/2410.12855) | [code]

- [2024/10/11] **AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents** | [[paper]](https://arxiv.org/abs/2410.09024) | [code]

- [2024/10/10] **Benchmarking Agentic Workflow Generation** | [[paper]](https://arxiv.org/abs/2410.07869) | [code]

- [2024/10/09] **MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering** | [[paper]](https://arxiv.org/abs/2410.07095) | [code]

- [2024/10/09] **Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making** | [[paper]](https://arxiv.org/abs/2410.07166) | [code]

- [2024/10/09] **DA-Code: Agent Data Science Code Generation Benchmark for Large Language Models** | [[paper]](https://arxiv.org/abs/2410.07331) | [code]

- [2024/10/07] **Adversarial Multi-Agent Evaluation of Large Language Models through Iterative Debates** | [[paper]](https://arxiv.org/abs/2410.04663) | [code]

- [2024/10/07] **ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery** | [[paper]](https://arxiv.org/abs/2410.05080) | [code]

- [2024/09/23] **Towards a Realistic Long-Term Benchmark for Open-Web Research Agents** | [[paper]](https://arxiv.org/abs/2409.14913) | [code]

- [2024/09/17] **CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark** | [[paper]](https://arxiv.org/abs/2409.11363) | [code]

- [2024/09/12] **DSBench: How Far Are Data Science Agents to Becoming Data Science Experts?** | [[paper]](https://arxiv.org/abs/2409.07703) | [code]

- [2024/09/11] **SUPER: Evaluating Agents on Setting Up and Executing Tasks from Research Repositories** | [[paper]](https://arxiv.org/abs/2409.07440) | [code]

- [2024/09/02] **ComfyBench: Benchmarking LLM-based Agents in ComfyUI for Autonomously Designing Collaborative AI Systems** | [[paper]](https://arxiv.org/abs/2409.01392) | [code]

- [2024/08/28] **BattleAgentBench: A Benchmark for Evaluating Cooperation and Competition Capabilities of Language Models in Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2408.15971) | [code]

- [2024/08/19] **BLADE: Benchmarking Language Model Agents for Data-Driven Science** | [[paper]](https://arxiv.org/abs/2408.09667) | [code]

- [2024/08/13] **What should I wear to a party in a Greek taverna? Evaluation for Conversational Agents in the Fashion Domain** | [[paper]](https://arxiv.org/abs/2408.08907) | [code]

- [2024/08/12] **VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents** | [[paper]](https://arxiv.org/abs/2408.06327) | [code]

- [2024/07/26] **OfficeBench: Benchmarking Language Agents across Multiple Applications for Office Automation** | [[paper]](https://arxiv.org/abs/2407.19056) | [code]

- [2024/07/26] **AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents** | [[paper]](https://arxiv.org/abs/2407.18901) | [[code]](https://github.com/stonybrooknlp/appworld)

- [2024/07/25] **PersonaGym: Evaluating Persona Agents and LLMs** | [[paper]](https://arxiv.org/abs/2407.18416) | [code]

- [2024/07/23] **AMONGAGENTS: Evaluating Large Language Models in the Interactive Text-Based Social Deduction Game** | [[paper]](https://arxiv.org/abs/2407.16521) | [code]

- [2024/07/22] **AssistantBench: Can Web Agents Solve Realistic and Time-Consuming Tasks?** | [[paper]](https://arxiv.org/abs/2407.15711) | [code]

- [2024/07/12] **IDAT: A Multi-Modal Dataset and Toolkit for Building and Evaluating Interactive Task-Solving Agents** | [[paper]](https://arxiv.org/abs/2407.08898) | [code]

- [2024/07/11] **GTA: A Benchmark for General Tool Agents** | [[paper]](https://arxiv.org/abs/2407.08713) | [code]

- [2024/07/05] **Towards Automated Functional Equation Proving: A Benchmark Dataset and A Domain-Specific In-Context Agent** | [[paper]](https://arxiv.org/abs/2407.14521) | [code]

- [2024/07/01] **MIRAI: Evaluating LLM Agents for Event Forecasting** | [[paper]](https://arxiv.org/abs/2407.01231) | [code]

- [2024/07/01] **ProductAgent: Benchmarking Conversational Product Search Agent with Asking Clarification Questions** | [[paper]](https://arxiv.org/abs/2407.00942) | [code]

- [2024/07/01] **Mobile-Bench: An Evaluation Benchmark for LLM-based Mobile Agents** | [[paper]](https://arxiv.org/abs/2407.00993) | [code]

- [2024/06/28] **Designing and Evaluating Multi-Chatbot Interface for Human-AI Communication: Preliminary Findings from a Persuasion Task** | [[paper]](https://arxiv.org/abs/2406.19648) | [code]

- [2024/06/13] **ResearchArena: Benchmarking Large Language Models&#39; Ability to Collect and Organize Information as Research Agents** | [[paper]](https://arxiv.org/abs/2406.10291) | [code]

- [2024/06/13] **StreamBench: Towards Benchmarking Continuous Improvement of Language Agents** | [[paper]](https://arxiv.org/abs/2406.08747) | [code]

- [2024/06/07] **WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild** | [[paper]](https://arxiv.org/abs/2406.04770) | [[code]](https://github.com/allenai/wildbench)

- [2024/06/07] **GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents** | [[paper]](https://arxiv.org/abs/2406.06613) | [[code]](https://github.com/Joshuaclymer/GameBench)

- [2024/05/28] **TimeChara: Evaluating Point-in-Time Character Hallucination of Role-Playing Large Language Models** | [[paper]](https://arxiv.org/abs/2405.18027) | [code]

- [2024/05/23] **AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents** | [[paper]](https://arxiv.org/abs/2405.14573) | [code]

- [2024/05/13] **AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments** | [[paper]](https://arxiv.org/abs/2405.07960) | [code]

- [2024/05/01] **WorkBench: a Benchmark Dataset for Agents in a Realistic Workplace Setting** | [[paper]](https://arxiv.org/abs/2405.00823) | [[code]](https://github.com/olly-styles/workbench)

- [2024/04/23] **Evaluating Tool-Augmented Agents in Remote Sensing Platforms** | [[paper]](https://arxiv.org/abs/2405.00709) | [code]

- [2024/04/22] **How Well Can LLMs Echo Us? Evaluating AI Chatbots&#39; Role-Play Ability with ECHO** | [[paper]](https://arxiv.org/abs/2404.13957) | [code]

- [2024/04/15] **MMInA: Benchmarking Multihop Multimodal Internet Agents** | [[paper]](https://arxiv.org/abs/2404.09992) | [[code]](https://github.com/shulin16/mmina)

- [2024/04/11] **OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments** | [[paper]](https://arxiv.org/abs/2404.07972) | [code]

- [2024/04/09] **AgentQuest: A Modular Benchmark Framework to Measure Progress and Improve LLM Agents** | [[paper]](https://arxiv.org/abs/2404.06411) | [code]

- [2024/04/05] **GroundCocoa: A Benchmark for Evaluating Compositional &amp; Conditional Reasoning in Language Models** | [[paper]](https://arxiv.org/abs/2404.04237) | [code]

- [2024/03/29] **DataAgent: Evaluating Large Language Models&#39; Ability to Answer Zero-Shot, Natural Language Queries** | [[paper]](https://arxiv.org/abs/2404.00188) | [code]

- [2024/03/26] **Sharing the Cost of Success: A Game for Evaluating and Learning Collaborative Multi-Agent Instruction Giving and Following Policies** | [[paper]](https://arxiv.org/abs/2403.17497) | [[code]](https://github.com/clp-research/cost-sharing-reference-game)

- [2024/03/20] **SocialBench: Sociality Evaluation of Role-Playing Conversational Agents** | [[paper]](https://arxiv.org/abs/2403.13679) | [code]

- [2024/03/18] **How Far Are We on the Decision-Making of LLMs? Evaluating LLMs&#39; Gaming Ability in Multi-Agent Environments** | [[paper]](https://arxiv.org/abs/2403.11807) | [code]

- [2024/03/18] **Tur[k]ingBench: A Challenge Benchmark for Web Agents** | [[paper]](https://arxiv.org/abs/2403.11905) | [code]

- [2024/03/13] **Evaluating Large Language Models as Generative User Simulators for Conversational Recommendation** | [[paper]](https://arxiv.org/abs/2403.09738) | [code]

- [2024/03/05] **InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents** | [[paper]](https://arxiv.org/abs/2403.02691) | [code]

- [2024/02/27] **Evaluating Very Long-Term Conversational Memory of LLM Agents** | [[paper]](https://arxiv.org/abs/2402.17753) | [code]

- [2024/02/27] **Benchmarking Data Science Agents** | [[paper]](https://arxiv.org/abs/2402.17168) | [code]

- [2024/02/19] **A Critical Evaluation of AI Feedback for Aligning Large Language Models** | [[paper]](https://arxiv.org/abs/2402.12366) | [code]

- [2024/02/18] **Benchmark Self-Evolving: A Multi-Agent Framework for Dynamic LLM Evaluation** | [[paper]](https://arxiv.org/abs/2402.11443) | [[code]](https://github.com/nanshineloong/self-evolving-benchmark)

- [2024/02/18] **MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization** | [[paper]](https://arxiv.org/abs/2402.11453) | [code]

- [2024/02/05] **LLM Agents in Interaction: Measuring Personality Consistency and Linguistic Alignment in Interacting Populations of Large Language Models** | [[paper]](https://arxiv.org/abs/2402.02896) | [code]

- [2024/02/02] **TravelPlanner: A Benchmark for Real-World Planning with Language Agents** | [[paper]](https://arxiv.org/abs/2402.01622) | [[code]](https://github.com/OSU-NLP-Group/TravelPlanner)

- [2024/01/02] **CharacterEval: A Chinese Benchmark for Role-Playing Conversational Agent Evaluation** | [[paper]](https://arxiv.org/abs/2401.01275) | [code]

- [2023/12/28] **How Far Are LLMs from Believable AI? A Benchmark for Evaluating the Believability of Human Behavior Simulation** | [[paper]](https://arxiv.org/abs/2312.17115) | [code]

- [2023/12/26] **RoleEval: A Bilingual Role Evaluation Benchmark for Large Language Models** | [[paper]](https://arxiv.org/abs/2312.16132) | [code]

- [2023/11/16] **ML-Bench: Evaluating Large Language Models and Agents for Machine Learning Tasks on Repository-Level Code** | [[paper]](https://arxiv.org/abs/2311.09835) | [code]

- [2023/11/15] **ToolTalk: Evaluating Tool-Usage in a Conversational Setting** | [[paper]](https://arxiv.org/abs/2311.10775) | [code]

- [2023/10/24] **FANToM: A Benchmark for Stress-testing Machine Theory of Mind in Interactions** | [[paper]](https://arxiv.org/abs/2310.15421) | [code]

- [2023/10/09] **Put Your Money Where Your Mouth Is: Evaluating Strategic Planning and Execution of LLM Agents in an Auction Arena** | [[paper]](https://arxiv.org/abs/2310.05746) | [code]

- [2023/10/02] **SmartPlay: A Benchmark for LLMs as Intelligent Agents** | [[paper]](https://arxiv.org/abs/2310.01557) | [code]

- [2023/10/01] **RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities of Large Language Models** | [[paper]](https://arxiv.org/abs/2310.00746) | [code]

- [2023/08/11] **BOLAA: Benchmarking and Orchestrating LLM-augmented Autonomous Agents** | [[paper]](https://arxiv.org/abs/2308.05960) | [code]

- [2023/08/07] **AgentBench: Evaluating LLMs as Agents** | [[paper]](https://arxiv.org/abs/2308.03688) | [code]

- [2023/04/27] **ChatLog: Carefully Evaluating the Evolution of ChatGPT Across Time** | [[paper]](https://arxiv.org/abs/2304.14106) | [code]

#### Environment&Platform
- [2025/05/30] **Open CaptchaWorld: A Comprehensive Web-based Platform for Testing and Benchmarking Multimodal LLM Agents** | [[paper]](https://arxiv.org/abs/2505.24878) | [code]

- [2025/05/22] **Beyond Static Testbeds: An Interaction-Centric Agent Simulation Platform for Dynamic Recommender Systems** | [[paper]](https://arxiv.org/abs/2505.16429) | [code]

- [2025/05/22] **MASLab: A Unified and Comprehensive Codebase for LLM-based Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2505.16988) | [code]

- [2025/04/15] **TextArena** | [[paper]](https://arxiv.org/abs/2504.11442) | [code]

- [2025/03/14] **Cerebrum (AIOS SDK): A Platform for Agent Development, Deployment, Distribution, and Discovery** | [[paper]](https://arxiv.org/abs/2503.11444) | [code]

- [2025/03/06] **Factorio Learning Environment** | [[paper]](https://arxiv.org/abs/2503.09617) | [code]

- [2025/03/05] **Unified Mind Model: Reimagining Autonomous Agents in the LLM Era** | [[paper]](https://arxiv.org/abs/2503.03459) | [code]

- [2025/03/04] **LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications** | [[paper]](https://arxiv.org/abs/2503.02950) | [code]

- [2025/02/14] **The Ann Arbor Architecture for Agent-Oriented Programming** | [[paper]](https://arxiv.org/abs/2502.09903) | [[code]](https://github.com/aaalgo/postline_0.1)

- [2024/12/30] **Training Software Engineering Agents and Verifiers with SWE-Gym** | [[paper]](https://arxiv.org/abs/2412.21139) | [code]

- [2024/11/05] **SAUCE: Synchronous and Asynchronous User-Customizable Environment for Multi-Agent LLM Interaction** | [[paper]](https://arxiv.org/abs/2411.03397) | [code]

- [2024/08/09] **AutoGen Studio: A No-Code Developer Tool for Building and Debugging Multi-Agent Systems** | [[paper]](https://arxiv.org/abs/2408.15247) | [code]

- [2024/08/06] **OpenOmni: A Collaborative Open Source Tool for Building Future-Ready Multimodal Conversational Agents** | [[paper]](https://arxiv.org/abs/2408.03047) | [code]

- [2024/07/23] **OpenHands: An Open Platform for AI Software Developers as Generalist Agents** | [[paper]](https://arxiv.org/abs/2407.16741) | [code]

- [2024/07/14] **AutoGRAMS: Autonomous Graphical Agent Modeling Software** | [[paper]](https://arxiv.org/abs/2407.10049) | [code]

- [2024/07/12] **IDAT: A Multi-Modal Dataset and Toolkit for Building and Evaluating Interactive Task-Solving Agents** | [[paper]](https://arxiv.org/abs/2407.08898) | [code]

- [2024/07/08] **Coding Reliable LLM-based Integrated Task and Knowledge Agents with GenieWorksheets** | [[paper]](https://arxiv.org/abs/2407.05674) | [code]

- [2024/06/06] **AgentGym: Evolving Large Language Model-based Agents across Diverse Environments** | [[paper]](https://arxiv.org/abs/2406.04151) | [[code]](https://github.com/woooodyy/agentgym)

- [2024/05/23] **AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents** | [[paper]](https://arxiv.org/abs/2405.14573) | [code]

- [2024/02/27] **OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web** | [[paper]](https://arxiv.org/abs/2402.17553) | [code]

- [2023/03/14] **CB2: Collaborative Natural Language Interaction Research Platform** | [[paper]](https://arxiv.org/abs/2303.08127) | [code]

#### Dataset
- [2025/07/10] **Toward Real-World Chinese Psychological Support Dialogues: CPsDD Dataset and a Co-Evolving Multi-Agent System** | [[paper]](https://arxiv.org/abs/2507.07509) | [code]

- [2025/06/26] **AgentStealth: Reinforcing Large Language Model for Anonymizing User-generated Text** | [[paper]](https://arxiv.org/abs/2506.22508) | [code]

- [2025/06/25] **MAGPIE: A dataset for Multi-AGent contextual PrIvacy Evaluation** | [[paper]](https://arxiv.org/abs/2506.20737) | [code]

- [2025/06/11] **ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning** | [[paper]](https://arxiv.org/abs/2506.09513) | [code]

- [2025/06/02] **STORM-BORN: A Challenging Mathematical Derivations Dataset Curated via a Human-in-the-Loop Multi-Agent Framework** | [[paper]](https://arxiv.org/abs/2506.01531) | [code]

- [2025/05/27] **Towards Safety Reasoning in LLMs: AI-agentic Deliberation for Policy-embedded CoT Data Creation** | [[paper]](https://arxiv.org/abs/2505.21784) | [code]

- [2025/05/19] **Scalable Video-to-Dataset Generation for Cross-Platform Mobile Agents** | [[paper]](https://arxiv.org/abs/2505.12632) | [code]

- [2025/02/09] **MTPChat: A Multimodal Time-Aware Persona Dataset for Conversational Agents** | [[paper]](https://arxiv.org/abs/2502.05887) | [code]

- [2025/02/09] **HamRaz: A Culture-Based Persian Conversation Dataset for Person-Centered Therapy Using LLM Agents** | [[paper]](https://arxiv.org/abs/2502.05982) | [code]

- [2025/01/23] **Hypothesis Generation for Materials Discovery and Design Using Goal-Driven and Constraint-Guided LLM Agents** | [[paper]](https://arxiv.org/abs/2501.13299) | [code]

- [2025/01/14] **Agent-Centric Projection of Prompting Techniques and Implications for Synthetic Training Data for Large Language Models** | [[paper]](https://arxiv.org/abs/2501.07815) | [code]

- [2024/12/30] **Plancraft: an evaluation dataset for planning with LLM agents** | [[paper]](https://arxiv.org/abs/2412.21033) | [code]

- [2024/12/28] **BaiJia: A Large-Scale Role-Playing Agent Corpus of Chinese Historical Characters** | [[paper]](https://arxiv.org/abs/2412.20024) | [code]

- [2024/12/24] **Explainable Multi-Modal Data Exploration in Natural Language via LLM Agent** | [[paper]](https://arxiv.org/abs/2412.18428) | [code]

- [2024/12/06] **CALICO: Conversational Agent Localization via Synthetic Data Generation** | [[paper]](https://arxiv.org/abs/2412.05388) | [code]

- [2024/11/28] **MAG-V: A Multi-Agent Framework for Synthetic Data Generation and Verification** | [[paper]](https://arxiv.org/abs/2412.04494) | [code]

- [2024/11/21] **Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning** | [[paper]](https://arxiv.org/abs/2411.14497) | [code]

- [2024/10/18] **Synthesizing Post-Training Data for LLMs through Multi-Agent Simulation** | [[paper]](https://arxiv.org/abs/2410.14251) | [code]

- [2024/10/10] **AgentBank: Towards Generalized LLM Agents via Fine-Tuning on 50000+ Interaction Trajectories** | [[paper]](https://arxiv.org/abs/2410.07706) | [code]

- [2024/09/06] **Using Large Language Models to Generate Authentic Multi-agent Knowledge Work Datasets** | [[paper]](https://arxiv.org/abs/2409.04286) | [code]

- [2024/08/22] **MDD-5k: A New Diagnostic Conversation Dataset for Mental Disorders Synthesized via Neuro-Symbolic LLM Agents** | [[paper]](https://arxiv.org/abs/2408.12142) | [code]

- [2024/08/16] **The Fellowship of the LLMs: Multi-Agent Workflows for Synthetic Preference Optimization Dataset Generation** | [[paper]](https://arxiv.org/abs/2408.08688) | [code]

- [2024/07/12] **IDAT: A Multi-Modal Dataset and Toolkit for Building and Evaluating Interactive Task-Solving Agents** | [[paper]](https://arxiv.org/abs/2407.08898) | [code]

- [2024/06/16] **GUI-WORLD: A Dataset for GUI-oriented Multimodal LLM-based Agents** | [[paper]](https://arxiv.org/abs/2406.10819) | [code]

- [2024/03/19] **Agent-FLAN: Designing Data and Methods of Effective Agent Tuning for Large Language Models** | [[paper]](https://arxiv.org/abs/2403.12881) | [code]

- [2024/02/27] **OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web** | [[paper]](https://arxiv.org/abs/2402.17553) | [code]

- [2023/07/31] **HAGRID: A Human-LLM Collaborative Dataset for Generative Information-Seeking with Attribution** | [[paper]](https://arxiv.org/abs/2307.16883) | [code]

### Others
- [2025/07/04] **Agent-Based Detection and Resolution of Incompleteness and Ambiguity in Interactions with Large Language Models** | [[paper]](https://arxiv.org/abs/2507.03726) | [code]

- [2025/07/02] **Data Agent: A Holistic Architecture for Orchestrating Data+AI Ecosystems** | [[paper]](https://arxiv.org/abs/2507.01599) | [code]

- [2025/06/30] **LLM Agents Are the Antidote to Walled Gardens** | [[paper]](https://arxiv.org/abs/2506.23978) | [code]

- [2025/06/20] **UProp: Investigating the Uncertainty Propagation of LLMs in Multi-Step Agentic Decision-Making** | [[paper]](https://arxiv.org/abs/2506.17419) | [code]

- [2025/06/10] **TACTIC: Translation Agents with Cognitive-Theoretic Interactive Collaboration** | [[paper]](https://arxiv.org/abs/2506.08403) | [code]

- [2025/06/06] **Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce** | [[paper]](https://arxiv.org/abs/2506.06576) | [code]

- [2025/06/02] **Enhancing Interpretable Image Classification Through LLM Agents and Conditional Concept Bottleneck Models** | [[paper]](https://arxiv.org/abs/2506.01334) | [code]

- [2025/05/23] **Distilling LLM Agent into Small Models with Retrieval and Code Tools** | [[paper]](https://arxiv.org/abs/2505.17612) | [code]

- [2025/05/23] **Runaway is Ashamed, But Helpful: On the Early-Exit Behavior of Large Language Model-based Agents in Embodied Environments** | [[paper]](https://arxiv.org/abs/2505.17616) | [code]

- [2025/05/23] **The Real Barrier to LLM Agent Usability is Agentic ROI** | [[paper]](https://arxiv.org/abs/2505.17767) | [code]

- [2025/05/20] **Structured Agent Distillation for Large Language Model** | [[paper]](https://arxiv.org/abs/2505.13820) | [code]

- [2025/05/20] **Agent Context Protocols Enhance Collective Inference** | [[paper]](https://arxiv.org/abs/2505.14569) | [code]

- [2025/05/15] **Learning Virtual Machine Scheduling in Cloud Computing through Language Agents** | [[paper]](https://arxiv.org/abs/2505.10117) | [code]

- [2025/05/04] **Interpretable Emergent Language Using Inter-Agent Transformers** | [[paper]](https://arxiv.org/abs/2505.02215) | [code]

- [2025/05/02] **VTS-LLM: Domain-Adaptive LLM Agent for Enhancing Awareness in Vessel Traffic Services through Natural Language** | [[paper]](https://arxiv.org/abs/2505.00989) | [code]

- [2025/05/01] **Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks** | [[paper]](https://arxiv.org/abs/2505.00234) | [code]

- [2025/04/23] **OptimAI: Optimization from Natural Language Using LLM-Powered AI Agents** | [[paper]](https://arxiv.org/abs/2504.16918) | [code]

- [2025/04/04] **Agentic Knowledgeable Self-awareness** | [[paper]](https://arxiv.org/abs/2504.03553) | [code]

- [2025/04/04] **Inherent and emergent liability issues in LLM-based agentic systems: a principal-agent perspective** | [[paper]](https://arxiv.org/abs/2504.03255) | [code]

- [2025/04/02] **Review, Refine, Repeat: Understanding Iterative Decoding of AI Agents with Dynamic Evaluation and Selection** | [[paper]](https://arxiv.org/abs/2504.01931) | [code]

- [2025/03/14] **GNNs as Predictors of Agentic Workflow Performances** | [[paper]](https://arxiv.org/abs/2503.11301) | [code]

- [2025/03/14] **CoLLMLight: Cooperative Large Language Model Agents for Network-Wide Traffic Signal Control** | [[paper]](https://arxiv.org/abs/2503.11739) | [code]

- [2025/03/14] **Agent-Enhanced Large Language Models for Researching Political Institutions** | [[paper]](https://arxiv.org/abs/2503.13524) | [code]

- [2025/03/14] **LLM Agents for Education: Advances and Applications** | [[paper]](https://arxiv.org/abs/2503.11733) | [code]

- [2025/02/20] **Optimizing Model Selection for Compound AI Systems** | [[paper]](https://arxiv.org/abs/2502.14815) | [code]

- [2024/12/03] **Large Multimodal Agents for Accurate Phishing Detection with Enhanced Token Optimization and Cost Reduction** | [[paper]](https://arxiv.org/abs/2412.02301) | [code]

- [2024/03/18] **EnvGen: Generating and Adapting Environments via LLMs for Training Embodied Agents** | [[paper]](https://arxiv.org/abs/2403.12014) | [code]

---
## :star: Star History

[![Star History Chart](https://api.star-history.com/svg?repos=AGI-Edgerunners/LLM-Agents-Papers&type=Date)](https://star-history.com/#AGI-Edgerunners/LLM-Agents-Papers&Date)
