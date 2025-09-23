<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "63f595a56e534d0b164e313e360afab5",
  "translation_date": "2025-09-22T22:35:32+00:00",
  "source_file": "Module08/README.md",
  "language_code": "tl"
}
-->
# Module 08: Hands on With Microsoft Foundry Local - Kumpletong Toolkit para sa Developer

## Pangkalahatang-ideya

Ang Microsoft Foundry Local ay kumakatawan sa susunod na henerasyon ng edge AI development, nagbibigay sa mga developer ng makapangyarihang mga tool upang bumuo, mag-deploy, at mag-scale ng mga AI application nang lokal habang pinapanatili ang seamless integration sa Azure AI Foundry. Ang module na ito ay nagbibigay ng komprehensibong coverage ng Foundry Local mula sa pag-install hanggang sa advanced na pag-develop ng agent.

**Mga Pangunahing Teknolohiya:**
- Microsoft Foundry Local CLI at SDK
- Azure AI Foundry integration
- On-device model inference
- Lokal na model caching at optimization
- Arkitektura ng mga agent

## Mga Layunin sa Pag-aaral ng Module

Sa pagtatapos ng module na ito, ikaw ay:

- **Mag-master ng Foundry Local Setup**: Mag-install, mag-configure, at mag-optimize ng Foundry Local para sa Windows 11 development
- **Mag-deploy ng Iba't Ibang Modelo**: Magpatakbo ng phi, qwen, deepseek, at GPT-OSS-20B models nang lokal gamit ang mga CLI command
- **Bumuo ng Production Solutions**: Lumikha ng mga AI application gamit ang advanced prompt engineering at data integration
- **Gamitin ang Open-Source Ecosystem**: Mag-integrate ng Hugging Face models at mga kontribusyon mula sa komunidad
- **Ihambing ang AI Architectures**: Unawain ang trade-offs ng LLMs vs SLMs at mga deployment strategy
- **Mag-develop ng AI Agents**: Bumuo ng mga intelligent agents gamit ang Foundry Local's architecture at grounding capabilities
- **Mag-implement ng Models bilang Tools**: Lumikha ng modular, customizable AI solutions para sa mga enterprise application

## Estruktura ng Session

### [1: Pagsisimula sa Foundry Local](./01.FoundryLocalSetup.md)
**Pokusan**: Pag-install, CLI setup, model caching, at hardware acceleration

**Ano ang Matututunan Mo:**
- Kumpletong pag-install ng Foundry Local sa Windows 11
- CLI configuration at command structure
- Mga estratehiya sa model caching para sa optimal na performance
- Hardware acceleration setup at optimization
- Hands-on deployment ng phi, qwen, deepseek, at GPT-OSS-20B models

**Tagal**: 2-3 oras  
**Mga Kinakailangan**: Windows 11, pangunahing kaalaman sa command line

---

### [2: Bumuo ng AI Solutions gamit ang Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Pokusan**: Advanced prompt engineering, data integration, at actionable tasks

**Ano ang Matututunan Mo:**
- Mga advanced na teknik sa prompt engineering
- Mga pattern at best practices sa data integration
- Pagbuo ng actionable AI tasks gamit ang Foundry Local
- Seamless workflows sa Azure AI Foundry integration
- Optimization ng performance at monitoring

**Tagal**: 2-3 oras  
**Mga Kinakailangan**: Pagkumpleto ng Session 1, Azure account (opsyonal)

---

### [3: Open-Source Models Foundry Local](./03.OpenSourceModels.md)
**Pokusan**: Hugging Face integration, model selection strategies, at mga kontribusyon mula sa komunidad

**Ano ang Matututunan Mo:**
- Hugging Face model integration gamit ang Foundry Local
- Mga estratehiya sa Bring-your-own-model (BYOM) at implementasyon
- Mga insight mula sa Model Mondays series at kontribusyon ng komunidad
- Custom model deployment at optimization
- Mga pamantayan sa evaluation at pagpili ng community models

**Tagal**: 2-3 oras  
**Mga Kinakailangan**: Pagkumpleto ng Session 1-2, Hugging Face account

---

### [4: Tuklasin ang Cutting-Edge Models - LLMs, SLMs, at On-Device Inference](./04.CuttingEdgeModels.md)
**Pokusan**: Paghahambing ng mga modelo, EdgeAI gamit ang Phi at ONNX Runtime, advanced na demos

**Ano ang Matututunan Mo:**
- Komprehensibong paghahambing ng LLMs vs SLMs at mga use cases
- Mga trade-offs sa lokal vs cloud inference at mga decision frameworks
- EdgeAI implementasyon gamit ang Phi at ONNX Runtime
- Pag-develop at pag-deploy ng Chainlit RAG Chat App
- Mga teknik sa WebGPU inference optimization
- AI PC SDK integration at capabilities

**Tagal**: 3-4 oras  
**Mga Kinakailangan**: Pagkumpleto ng Session 1-3, kaalaman sa inference concepts

---

### [5: Bumuo ng AI-Powered Agents nang Mabilis gamit ang Foundry Local](./05.AIPoweredAgents.md)
**Pokusan**: Mabilisang pag-develop ng GenAI app, system prompts, grounding, at agent architectures

**Ano ang Matututunan Mo:**
- Foundry Local agent architecture at mga design patterns
- Teknik sa system prompt engineering para sa agent behavior
- Mga grounding techniques para sa maaasahang sagot ng agent
- Mga workflows sa mabilisang pag-develop ng GenAI application
- Agent orchestration at multi-agent systems
- Mga estratehiya sa production deployment para sa AI agents

**Tagal**: 3-4 oras  
**Mga Kinakailangan**: Pagkumpleto ng Session 1-4, pangunahing kaalaman sa AI agents

---

### [6: Foundry Local - Models bilang Tools](./06.ModelsAsTools.md)
**Pokusan**: Modular AI solutions, on-device deployment, at enterprise scaling

**Ano ang Matututunan Mo:**
- Paggamit ng AI models bilang modular, customizable tools
- On-device deployment nang walang cloud dependency
- Low-latency, cost-efficient, at privacy-preserving inference
- SDK, API, at CLI integration patterns
- Model customization para sa partikular na use cases
- Mga estratehiya sa scaling mula lokal hanggang Azure AI Foundry
- Enterprise-ready AI application architectures

**Tagal**: 3-4 oras  
**Mga Kinakailangan**: Lahat ng naunang sessions, karanasan sa enterprise development ay makakatulong

## Mga Kinakailangan

### Mga Kinakailangan sa Sistema
- **Operating System**: Windows 11 (22H2 o mas bago)
- **Memory**: 16GB RAM (32GB inirerekomenda para sa mas malalaking modelo)
- **Storage**: 50GB na libreng espasyo para sa model caching
- **Hardware**: NPU-enabled device inirerekomenda (Copilot+ PC), GPU opsyonal
- **Network**: High-speed internet para sa initial model downloads

### Development Environment
- Visual Studio Code na may AI Toolkit extension
- Python 3.10+ at pip
- Git para sa version control
- PowerShell o Command Prompt
- Azure CLI (opsyonal para sa cloud integration)

### Kaalaman na Kinakailangan
- Pangunahing kaalaman sa AI/ML concepts
- Pamilyaridad sa command line
- Mga pangunahing kaalaman sa Python programming
- REST API concepts
- Pangunahing kaalaman sa prompting at model inference

## Timeline ng Module

**Kabuuang Tinatayang Oras**: 15-20 oras

| Session | Pokusan | Oras | Complexity |
|---------|---------|------|------------|
|  1 | Setup & Basics | 2-3 oras | Beginner |
|  2 | AI Solutions | 2-3 oras | Intermediate |
|  3 | Open Source | 2-3 oras | Intermediate |
|  4 | Advanced Models | 3-4 oras | Advanced |
|  5 | AI Agents | 3-4 oras | Advanced |
|  6 | Enterprise Tools | 3-4 oras | Expert |

## Mga Pangunahing Resources

### Pangunahing Dokumentasyon
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Azure AI Foundry Local Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)
- [Model Mondays Series](https://aka.ms/model-mondays)

### Mga Resources ng Komunidad
- [Foundry Local Community Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Foundry Samples](https://github.com/Azure-Samples/ai-foundry)
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence)

## Mga Resulta ng Pag-aaral

Sa pagtatapos ng module na ito, ikaw ay magiging handa upang:

### Teknikal na Mastery
- **Mag-deploy at Mag-manage**: Foundry Local installations sa development at production environments
- **Mag-integrate ng Models**: Gumamit ng iba't ibang model families mula sa Microsoft, Hugging Face, at mga source ng komunidad
- **Bumuo ng Applications**: Lumikha ng production-ready AI applications na may advanced features at optimizations
- **Mag-develop ng Agents**: Mag-implement ng sophisticated AI agents na may grounding, reasoning, at tool integration

### Strategic Understanding
- **Mga Desisyon sa Arkitektura**: Gumawa ng mga informed na desisyon sa pagitan ng lokal vs cloud deployment
- **Optimization ng Performance**: Mag-optimize ng inference performance sa iba't ibang hardware configurations
- **Enterprise Scaling**: Magdisenyo ng mga application na maaaring mag-scale mula sa lokal na prototypes hanggang sa enterprise deployments
- **Privacy at Security**: Mag-implement ng privacy-preserving AI solutions gamit ang lokal na inference

### Innovation Capabilities
- **Mabilisang Prototyping**: Mabilis na bumuo at mag-test ng AI application concepts
- **Integration ng Komunidad**: Gamitin ang open-source models at mag-ambag sa ecosystem
- **Advanced Patterns**: Mag-implement ng cutting-edge AI patterns kabilang ang RAG, agents, at tool integration
- **Future-Ready Development**: Bumuo ng mga application na handa para sa mga umuusbong na AI technologies at patterns

## Pagsisimula

1. **Ihanda ang Iyong Environment**: Siguraduhing may Windows 11 na may inirerekomendang hardware specifications
2. **I-install ang Mga Kinakailangan**: I-set up ang development tools at dependencies
3. **Simulan sa Session 1**: Magsimula sa pag-install ng Foundry Local at basic setup
4. **Magpatuloy nang Sunod-sunod**: Kumpletuhin ang mga session sa tamang pagkakasunod-sunod para sa optimal na pag-aaral
5. **Magpraktis nang Patuloy**: I-apply ang mga konsepto sa pamamagitan ng hands-on exercises at projects

## Mga Sukatan ng Tagumpay

Subaybayan ang iyong progreso sa module:

- [ ] Matagumpay na ma-install at ma-configure ang Foundry Local
- [ ] Mag-deploy at magpatakbo ng hindi bababa sa 4 na iba't ibang model families
- [ ] Bumuo ng kumpletong AI solution na may data integration
- [ ] Mag-integrate ng hindi bababa sa 2 open-source models
- [ ] Lumikha ng functional na RAG chat application
- [ ] Mag-develop at mag-deploy ng AI agent
- [ ] Mag-implement ng models-as-tools architecture

## Mabilisang Pagsisimula para sa Mga Sample

### 1) Environment setup (Windows cmd.exe)
```cmd
cd Module08
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Magpatakbo ng lokal na modelo (bagong terminal)
```cmd
foundry model list
foundry model run phi-4-mini
```

### 3) Patakbuhin ang Chainlit demo (Session 4)
```cmd
cd Module08
.\.venv\Scripts\activate
chainlit run samples\04\app.py -w
```

### 4) Patakbuhin ang multi-agent coordinator (Session 5)
```cmd
cd Module08
.\.venv\Scripts\activate
python -m samples.05.agents.coordinator
```

Kung makakaranas ng connection errors, i-validate ang Foundry Local:
```cmd
curl http://localhost:8000/v1/models
```

### Router configuration (Session 6)
Ang router ay nagsasagawa ng mabilisang health check at sumusuporta sa env-based config:
```cmd
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-distill-qwen-7b
set CODE_MODEL=qwen2.5-7b-instruct
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"}}
python samples\06\router.py "Pick the best model for code refactoring"
```

Ang module na ito ay kumakatawan sa cutting edge ng edge AI development, pinagsasama ang enterprise-grade tools ng Microsoft sa flexibility at innovation ng open-source ecosystem. Sa pag-master ng Foundry Local, ikaw ay magiging nasa unahan ng AI application development.

Para sa Azure OpenAI (Session 2), tingnan ang sample README para sa mga kinakailangang environment variables at API version settings.

## Pangkalahatang-ideya ng Mga Sample

- `samples/01`: Mabilisang REST chat sa Foundry Local (`chat_quickstart.py`).
- `samples/02`: OpenAI SDK integration (`sdk_quickstart.py`).
- `samples/03`: Model discovery + quick bench (`list_and_bench.cmd`).
- `samples/04`: Chainlit RAG demo (`app.py`).
- `samples/05`: Multi-agent orchestration (`python -m samples.05.agents.coordinator`).
- `samples/06`: Models-as-Tools router (`python samples\06\router.py`).

---

